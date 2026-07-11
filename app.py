"""
Homie Website - Trang giới thiệu, thư viện mẫu mã & kiến thức nội thất
Mục tiêu: kéo khách mới để lại SĐT/Zalo (phễu đầu nguồn).
Stack: Flask + SQLite + Jinja2 + Bootstrap 5 (giống app quản lý sản xuất).
"""
import os
import re
import uuid
from datetime import datetime
from functools import wraps

from flask import (
    Flask, render_template, request, redirect, url_for,
    flash, session, abort, jsonify, send_file
)
from flask_sqlalchemy import SQLAlchemy
from werkzeug.utils import secure_filename
from sqlalchemy import func

BASE_DIR = os.path.abspath(os.path.dirname(__file__))
DATA_DIR = os.path.join(BASE_DIR, "data")
UPLOAD_DIR = os.path.join(BASE_DIR, "static", "uploads")
BOOK_DIR = os.path.join(BASE_DIR, "book")
BOOK_FILE = os.path.join(BOOK_DIR, "lam-nha-lan-dau.html")  # sách tặng (lead magnet)
os.makedirs(DATA_DIR, exist_ok=True)
os.makedirs(UPLOAD_DIR, exist_ok=True)

app = Flask(__name__)
app.config["SECRET_KEY"] = os.environ.get("SECRET_KEY", "homie-doi-mat-khau-nay")

# ---- Kết nối database: ưu tiên Postgres bền vững (Neon/Supabase) qua DATABASE_URL ----
# Nếu có DATABASE_URL -> dùng Postgres (dữ liệu KHÔNG mất khi deploy lại).
# Nếu không -> dùng SQLite local để chạy máy anh (data/homie_web.db).
_db_url = os.environ.get("DATABASE_URL", "").strip()
if _db_url:
    # SQLAlchemy cần scheme "postgresql://" (Neon/Render hay đưa "postgres://")
    if _db_url.startswith("postgres://"):
        _db_url = _db_url.replace("postgres://", "postgresql://", 1)
    # Ép SSL cho các nhà cung cấp free (Neon/Supabase) nếu chưa khai báo
    if _db_url.startswith("postgresql://") and "sslmode=" not in _db_url:
        _db_url += ("&" if "?" in _db_url else "?") + "sslmode=require"
    app.config["SQLALCHEMY_DATABASE_URI"] = _db_url
    # Giữ kết nối ổn định khi Neon "ngủ" rồi thức dậy
    app.config["SQLALCHEMY_ENGINE_OPTIONS"] = {"pool_pre_ping": True, "pool_recycle": 300}
else:
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///" + os.path.join(DATA_DIR, "homie_web.db")
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config["UPLOAD_FOLDER"] = UPLOAD_DIR
app.config["MAX_CONTENT_LENGTH"] = 64 * 1024 * 1024  # 64MB / lần gửi (đủ cho nhiều ảnh cùng lúc)

# Thông tin liên hệ Homie - bà chủ sửa ở đây hoặc qua biến môi trường
SITE = {
    "ten": "Homie - Nội Thất & Xây Nhà",
    "slogan": "Trao trọn yên tâm cho ngôi nhà của bạn",
    "khu_vuc": "Quảng Trị",
    "zalo": os.environ.get("HOMIE_ZALO", "0902866717"),
    "hotline": os.environ.get("HOMIE_HOTLINE", "0902 866 717"),
    "facebook": os.environ.get("HOMIE_FB", "https://facebook.com/"),
    "dia_chi": os.environ.get("HOMIE_DIACHI", "TP. Đông Hà, Quảng Trị"),
}

# Mật khẩu xem danh sách khách để lại SĐT (trang quản trị nhẹ)
ADMIN_PASSWORD = os.environ.get("HOMIE_ADMIN_PASS", "homie123")

db = SQLAlchemy(app)


# ----------------------------- MODELS -----------------------------
class Project(db.Model):
    """Mẫu mã / công trình thật để khoe trong thư viện."""
    __tablename__ = "project"
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200), nullable=False)
    category = db.Column(db.String(60))      # tu-bep, tu-ao, giuong, phong-khach...
    material = db.Column(db.String(60))       # nhua-rong, go-cong-nghiep
    segment = db.Column(db.String(60))        # nhom-a, nhom-b
    location = db.Column(db.String(120))      # Đông Hà, Triệu Phong...
    image = db.Column(db.String(255))         # tên file trong static/uploads (hoặc rỗng -> placeholder)
    summary = db.Column(db.String(300))
    description = db.Column(db.Text)
    featured = db.Column(db.Boolean, default=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)


class ProjectImage(db.Model):
    """Ảnh phụ của 1 dự án — cho phép 1 dự án có nhiều hình (thư viện ảnh)."""
    __tablename__ = "project_image"
    id = db.Column(db.Integer, primary_key=True)
    project_id = db.Column(db.Integer, db.ForeignKey("project.id"), nullable=False)
    filename = db.Column(db.String(255), nullable=False)  # tên file trong static/uploads
    sort_order = db.Column(db.Integer, default=0)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    project = db.relationship("Project", backref=db.backref(
        "images", cascade="all, delete-orphan",
        order_by="ProjectImage.sort_order, ProjectImage.id",
    ))


class Article(db.Model):
    """Bài kiến thức / xu hướng."""
    __tablename__ = "article"
    id = db.Column(db.Integer, primary_key=True)
    slug = db.Column(db.String(200), unique=True, nullable=False)
    title = db.Column(db.String(220), nullable=False)
    category = db.Column(db.String(60))       # kien-thuc, xu-huong, kinh-nghiem
    cover = db.Column(db.String(255))
    excerpt = db.Column(db.String(400))
    body = db.Column(db.Text)                 # HTML đơn giản
    featured = db.Column(db.Boolean, default=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)


class Lead(db.Model):
    """Khách để lại thông tin -> đầu mối bán hàng."""
    __tablename__ = "lead"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120))
    phone = db.Column(db.String(40), nullable=False)
    need = db.Column(db.String(120))          # nhu cầu: tủ bếp, trọn gói...
    budget = db.Column(db.String(60))
    message = db.Column(db.Text)
    source = db.Column(db.String(60))         # trang nào gửi
    created_at = db.Column(db.DateTime, default=datetime.utcnow)


# ----------------------------- BÁO LEAD VỀ ĐIỆN THOẠI -----------------------------
# Khi có khách để lại SĐT -> bắn tin về Telegram của chủ (miễn phí, tức thì),
# kèm sẵn link Zalo tới đúng khách để bấm 1 phát mở chat Zalo.
# Bật bằng biến môi trường trên Render: TELEGRAM_BOT_TOKEN + TELEGRAM_CHAT_ID
import urllib.parse
import urllib.request

TELEGRAM_BOT_TOKEN = os.environ.get("TELEGRAM_BOT_TOKEN", "")
TELEGRAM_CHAT_ID = os.environ.get("TELEGRAM_CHAT_ID", "")


def normalize_phone(raw):
    """Chuẩn hóa & kiểm tra SĐT di động Việt Nam.
    Trả về số 10 chữ số hợp lệ (VD 0902866717) hoặc None nếu sai/bậy."""
    if not raw:
        return None
    digits = re.sub(r"\D", "", raw)          # bỏ mọi ký tự không phải số
    if digits.startswith("84") and len(digits) == 11:   # +84... -> 0...
        digits = "0" + digits[2:]
    elif len(digits) == 9 and digits[0] in "35789":      # thiếu số 0 đầu
        digits = "0" + digits
    # Đầu số di động VN hợp lệ: 03, 05, 07, 08, 09 + đủ 10 số
    if re.fullmatch(r"0[35789]\d{8}", digits):
        return digits
    return None


def notify_new_lead(lead):
    """Gửi thông báo lead mới về Telegram chủ (không chặn luồng nếu lỗi)."""
    if not (TELEGRAM_BOT_TOKEN and TELEGRAM_CHAT_ID):
        return
    phone_digits = "".join(ch for ch in (lead.phone or "") if ch.isdigit())
    lines = [
        "🔔 <b>LEAD MỚI — Homie Website</b>",
        f"👤 {lead.name or '(không tên)'}",
        f"📞 <b>{lead.phone}</b>",
    ]
    if lead.need:
        lines.append(f"🎯 {lead.need}")
    if lead.budget:
        lines.append(f"💰 {lead.budget}")
    if lead.message:
        lines.append(f"📝 {lead.message}")
    lines.append(f"🌐 Nguồn: {lead.source or 'web'}")
    lines.append(f"🕐 {lead.created_at.strftime('%d/%m/%Y %H:%M')}")
    if phone_digits:
        lines.append(f'👉 <a href="https://zalo.me/{phone_digits}">Mở Zalo nhắn khách ngay</a>')
    text = "\n".join(lines)
    try:
        data = urllib.parse.urlencode({
            "chat_id": TELEGRAM_CHAT_ID,
            "text": text,
            "parse_mode": "HTML",
            "disable_web_page_preview": "true",
        }).encode()
        url = f"https://api.telegram.org/bot{TELEGRAM_BOT_TOKEN}/sendMessage"
        urllib.request.urlopen(urllib.request.Request(url, data=data), timeout=8)
    except Exception as e:
        print(f"[notify_new_lead] warning: {e}")


# ----------------------------- HELPERS -----------------------------
CATEGORIES = [
    ("tu-bep", "Tủ bếp"),
    ("tu-ao", "Tủ áo"),
    ("phong-khach", "Phòng khách"),
    ("phong-tho", "Phòng thờ"),
    ("giuong", "Giường ngủ"),
    ("phong-tre", "Phòng trẻ em"),
    ("tron-goi", "Trọn gói cả nhà"),
]
MATERIALS = [
    ("nhua-rong", "Nhựa rỗng (chống ẩm)"),
    ("go-cong-nghiep", "Gỗ công nghiệp An Cường"),
]

CAT_MAP = dict(CATEGORIES)
MAT_MAP = dict(MATERIALS)
ART_CAT = {"kien-thuc": "Kiến thức", "xu-huong": "Xu hướng", "kinh-nghiem": "Kinh nghiệm"}

# Sách tặng đầu phễu (lead magnet) — khách để lại SĐT/Zalo để nhận
BOOK = {
    "ten": "Làm Nhà Lần Đầu",
    "phu_de": "Cẩm nang tránh sai lầm khi làm nội thất — Thắng Nội Thất",
    "source": "sach-lam-nha-lan-dau",   # nhãn nguồn lead
    "diem": [
        "Nhựa rỗng hay gỗ công nghiệp — chọn sao cho đúng nhà & túi tiền",
        "Bí quyết chống nồm ẩm miền Trung để đồ bền hàng chục năm",
        "Kích thước chuẩn tủ bếp, tủ áo, giường... (cheat-sheet)",
        "5 hạng mục nên đầu tư vì 'khó sửa về sau'",
        "Cách đọc báo giá để không bị phát sinh giữa chừng",
    ],
}

# Phong cách nội thất phổ biến (rút từ kho tri thức Homie — note 34)
STYLES = [
    dict(key="hien-dai", ten="Hiện đại / Tối giản", icon="🛋️",
         mo_ta="Trung tính, khối thanh thoát, nhiều khoảng trống. Bán chạy nhất, hợp mọi diện tích.",
         mau="Trắng · xám · be, điểm nhấn tối"),
    dict(key="scandinavian", ten="Scandinavian (Bắc Âu)", icon="🌿",
         mo_ta="Gỗ sáng + trắng + xanh nhạt, tận dụng ánh sáng tự nhiên. Hợp nhà có trẻ, chung cư.",
         mau="Gỗ sáng · trắng · xanh nhạt"),
    dict(key="japandi", ten="Japandi (Nhật × Bắc Âu)", icon="🍵",
         mo_ta="Gỗ sáng chủ đạo, sofa/bàn thấp, luôn ngăn nắp, cây xanh điểm xuyết. Tĩnh và ấm.",
         mau="Gỗ sáng · xám/be · xanh nhạt"),
    dict(key="indochine", ten="Indochine (Đông Dương)", icon="🪟",
         mo_ta="Hoài cổ sang trọng: gỗ nâu trầm + gạch bông + mây tre, hoa văn tinh tế.",
         mau="Nâu trầm · trắng ngà · vàng nghệ"),
    dict(key="wabi-sabi", ten="Wabi Sabi", icon="🪵",
         mo_ta="Bình dị, không hoàn hảo, tông trầm tự nhiên, ít decor. Vẻ đẹp mộc của chất liệu.",
         mau="Tông đất · trầm tự nhiên"),
    dict(key="luxury", ten="Luxury / Sang trọng", icon="✨",
         mo_ta="Gỗ tối óc chó, đá vân, ánh sáng nhiều lớp, phụ kiện cao cấp. Đẳng cấp có chiều sâu.",
         mau="Óc chó · đen · ánh kim"),
]


# Đăng ký các bảng tra cứu tĩnh làm Jinja global để macro (import không kèm
# context) vẫn truy cập được.
app.jinja_env.globals.update(
    SITE=SITE, CATEGORIES=CATEGORIES, MATERIALS=MATERIALS,
    CAT_MAP=CAT_MAP, MAT_MAP=MAT_MAP, ART_CAT=ART_CAT,
    BOOK=BOOK, STYLES=STYLES,
)


@app.context_processor
def inject_globals():
    return dict(now=datetime.utcnow())


def admin_required(f):
    @wraps(f)
    def wrap(*a, **kw):
        if not session.get("is_admin"):
            return redirect(url_for("admin_login", next=request.path))
        return f(*a, **kw)
    return wrap


# ----------------------------- PUBLIC ROUTES -----------------------------
@app.route("/")
def index():
    featured_projects = Project.query.filter_by(featured=True).order_by(Project.created_at.desc()).limit(6).all()
    if not featured_projects:
        featured_projects = Project.query.order_by(Project.created_at.desc()).limit(6).all()
    featured_articles = Article.query.order_by(Article.created_at.desc()).limit(3).all()
    return render_template("index.html", projects=featured_projects, articles=featured_articles)


@app.route("/mau-ma")
def gallery():
    cat = request.args.get("cat", "")
    mat = request.args.get("mat", "")
    q = Project.query
    if cat:
        q = q.filter_by(category=cat)
    if mat:
        q = q.filter_by(material=mat)
    projects = q.order_by(Project.created_at.desc()).all()
    return render_template("gallery.html", projects=projects, cat=cat, mat=mat)


@app.route("/mau-ma/<int:pid>")
def project_detail(pid):
    project = Project.query.get_or_404(pid)
    related = Project.query.filter(Project.category == project.category, Project.id != pid).limit(3).all()
    return render_template("project_detail.html", project=project, related=related)


@app.route("/kien-thuc")
def blog():
    cat = request.args.get("cat", "")
    q = Article.query
    if cat:
        q = q.filter_by(category=cat)
    articles = q.order_by(Article.created_at.desc()).all()
    return render_template("blog.html", articles=articles, cat=cat)


@app.route("/kien-thuc/<slug>")
def article_detail(slug):
    article = Article.query.filter_by(slug=slug).first_or_404()
    related = Article.query.filter(Article.id != article.id).order_by(Article.created_at.desc()).limit(3).all()
    return render_template("article.html", article=article, related=related)


@app.route("/gioi-thieu")
def about():
    return render_template("about.html")


@app.route("/lien-he")
def contact():
    return render_template("contact.html")


@app.route("/lead", methods=["POST"])
def submit_lead():
    is_magnet = bool(request.form.get("magnet"))
    phone = normalize_phone(request.form.get("phone"))
    if not phone:
        flash("Số điện thoại chưa đúng. Bạn nhập lại số di động (VD: 0902 866 717) để Homie gửi sách/liên hệ nhé.", "warning")
        # Giữ đúng ngữ cảnh: phễu sách quay lại trang sách, còn lại quay về nơi vừa gửi
        if is_magnet:
            return redirect(url_for("nhan_sach"))
        return redirect(request.referrer or url_for("index"))
    lead = Lead(
        name=(request.form.get("name") or "").strip(),
        phone=phone,
        need=(request.form.get("need") or "").strip(),
        budget=(request.form.get("budget") or "").strip(),
        message=(request.form.get("message") or "").strip(),
        source=(request.form.get("source") or "web").strip(),
    )
    db.session.add(lead)
    db.session.commit()
    notify_new_lead(lead)      # bắn tin về Telegram chủ (nếu đã bật env)
    # Nếu là phễu "nhận sách": mở khóa quyền đọc sách + đưa sang trang đọc
    if is_magnet:
        session["book_unlocked"] = True
        flash("Cảm ơn bạn! Sách đã sẵn sàng — Homie cũng sẽ nhắn Zalo tư vấn thêm cho bạn.", "success")
        return redirect(url_for("doc_sach"))
    flash("Cảm ơn bạn! Homie đã nhận thông tin và sẽ liên hệ tư vấn miễn phí trong thời gian sớm nhất.", "success")
    return redirect(url_for("thanks"))


@app.route("/cam-on")
def thanks():
    return render_template("thanks.html")


# ----------------------------- PHỄU: NHẬN SÁCH (lead magnet) -----------------------------
@app.route("/nhan-sach")
def nhan_sach():
    """Trang giới thiệu sách tặng — khách để lại SĐT/Zalo để nhận."""
    return render_template("sach.html")


@app.route("/doc-sach")
def doc_sach():
    """Trang đọc sách — chỉ mở sau khi khách đã để lại thông tin."""
    if not session.get("book_unlocked"):
        flash("Bạn vui lòng để lại số điện thoại/Zalo để nhận sách nhé.", "warning")
        return redirect(url_for("nhan_sach"))
    return render_template("doc_sach.html")


@app.route("/sach-file")
def sach_file():
    """Trả file sách (đã kiểm soát quyền qua session)."""
    if not session.get("book_unlocked"):
        return redirect(url_for("nhan_sach"))
    if not os.path.exists(BOOK_FILE):
        abort(404)
    return send_file(BOOK_FILE)


@app.route("/tai-sach")
def tai_sach():
    """Tải sách về máy (đã kiểm soát quyền qua session)."""
    if not session.get("book_unlocked"):
        return redirect(url_for("nhan_sach"))
    if not os.path.exists(BOOK_FILE):
        abort(404)
    return send_file(BOOK_FILE, as_attachment=True,
                     download_name="Lam-Nha-Lan-Dau-Thang-Noi-That.html")


@app.route("/phong-cach")
def phong_cach():
    """Trang giới thiệu các phong cách nội thất Homie tư vấn."""
    return render_template("phong_cach.html")


@app.errorhandler(413)
def too_large(e):
    """Ảnh gửi lên quá nặng — báo nhẹ nhàng, quay lại trang trước thay vì màn lỗi trơ."""
    flash("Ảnh tải lên quá nặng (tổng vượt 64MB). Bạn giảm bớt số ảnh hoặc chụp nhẹ hơn rồi lưu lại nhé.", "warning")
    return redirect(request.referrer or url_for("admin_projects")), 413


# ----------------------------- ADMIN (nhẹ) -----------------------------
@app.route("/quan-tri/dang-nhap", methods=["GET", "POST"])
def admin_login():
    if request.method == "POST":
        if request.form.get("password") == ADMIN_PASSWORD:
            session["is_admin"] = True
            return redirect(request.args.get("next") or url_for("admin_dashboard"))
        flash("Sai mật khẩu.", "danger")
    return render_template("admin_login.html")


@app.route("/quan-tri/dang-xuat")
def admin_logout():
    session.pop("is_admin", None)
    return redirect(url_for("index"))


# ---------- dashboard ----------
@app.route("/quan-tri/")
@app.route("/quan-tri")
@admin_required
def admin_dashboard():
    n_projects = Project.query.count()
    n_articles = Article.query.count()
    n_leads = Lead.query.count()
    recent_leads = Lead.query.order_by(Lead.created_at.desc()).limit(5).all()
    return render_template("admin_dashboard.html",
                           n_projects=n_projects, n_articles=n_articles,
                           n_leads=n_leads, recent_leads=recent_leads)


@app.route("/quan-tri/khach")
@admin_required
def admin_leads():
    leads = Lead.query.order_by(Lead.created_at.desc()).all()
    return render_template("admin_leads.html", leads=leads)


@app.route("/quan-tri/trang-thai")
def admin_status():
    """Chẩn đoán nhanh cấu hình (mở bằng ?pw=<mật khẩu admin>).
    Không lộ token/giá trị bí mật, chỉ báo BẬT/TẮT + gửi thử Telegram nếu ?test=1."""
    if request.args.get("pw", "") != ADMIN_PASSWORD:
        return "Sai hoặc thiếu mật khẩu. Dùng: /quan-tri/trang-thai?pw=MAT_KHAU", 403
    uri = app.config.get("SQLALCHEMY_DATABASE_URI", "")
    db_kind = "Postgres (bền vững)" if uri.startswith("postgresql") else "SQLite (mất khi deploy!)"
    lines = [
        "== TRẠNG THÁI HOMIE WEBSITE ==",
        f"Database: {db_kind}",
        f"Số lead đang lưu: {Lead.query.count()}",
        f"TELEGRAM_BOT_TOKEN: {'ĐÃ SET' if TELEGRAM_BOT_TOKEN else 'CHƯA SET !!'}",
        f"TELEGRAM_CHAT_ID:   {'ĐÃ SET' if TELEGRAM_CHAT_ID else 'CHƯA SET !!'}",
    ]
    if request.args.get("test") == "1":
        if TELEGRAM_BOT_TOKEN and TELEGRAM_CHAT_ID:
            try:
                data = urllib.parse.urlencode({
                    "chat_id": TELEGRAM_CHAT_ID,
                    "text": "✅ Test từ server Homie: thông báo lead đang chạy tốt!",
                }).encode()
                u = f"https://api.telegram.org/bot{TELEGRAM_BOT_TOKEN}/sendMessage"
                r = urllib.request.urlopen(urllib.request.Request(u, data=data), timeout=8)
                lines.append(f"Gửi thử Telegram: OK (HTTP {r.status}) — kiểm tra điện thoại")
            except Exception as e:
                lines.append(f"Gửi thử Telegram: LỖI -> {e}")
        else:
            lines.append("Gửi thử Telegram: bỏ qua (chưa set biến)")
    return "<pre>" + "\n".join(lines) + "</pre>"


# ---------- helpers upload ----------
ALLOWED_EXT = {"jpg", "jpeg", "png", "webp"}

def allowed_file(filename):
    return "." in filename and filename.rsplit(".", 1)[1].lower() in ALLOWED_EXT

def _store_filestorage(f, prefix):
    """Lưu 1 FileStorage vào thư mục uploads, trả về tên file (hoặc None)."""
    if f and f.filename and allowed_file(f.filename):
        ext = f.filename.rsplit(".", 1)[1].lower()
        # Hậu tố ngẫu nhiên để tránh trùng tên khi lưu nhiều ảnh trong cùng micro-giây
        fname = f"{prefix}_{datetime.utcnow().strftime('%Y%m%d%H%M%S')}_{uuid.uuid4().hex[:8]}.{ext}"
        f.save(os.path.join(app.config["UPLOAD_FOLDER"], fname))
        return fname
    return None

def _remove_upload_file(fname):
    """Xóa file ảnh khỏi thư mục uploads (bỏ qua nếu không có)."""
    if not fname:
        return
    try:
        os.remove(os.path.join(app.config["UPLOAD_FOLDER"], fname))
    except OSError:
        pass

def save_upload(file_field):
    """Lưu 1 file upload theo tên field, trả về tên file hoặc None."""
    return _store_filestorage(request.files.get(file_field), file_field)

def save_project_images(project, file_field="images"):
    """Lưu NHIỀU ảnh cùng lúc cho 1 dự án. Trả về số ảnh đã thêm.
    Nếu dự án chưa có ảnh đại diện thì lấy ảnh đầu tiên làm ảnh đại diện."""
    files = request.files.getlist(file_field)
    start = (max((im.sort_order for im in project.images), default=0) + 1)
    added = 0
    for f in files:
        fname = _store_filestorage(f, "img")
        if not fname:
            continue
        db.session.add(ProjectImage(project_id=project.id, filename=fname,
                                    sort_order=start + added))
        if not project.image:      # chưa có ảnh đại diện -> dùng ảnh đầu
            project.image = fname
        added += 1
    return added


# ---------- CRUD dự án ----------
@app.route("/quan-tri/du-an")
@admin_required
def admin_projects():
    projects = Project.query.order_by(Project.created_at.desc()).all()
    return render_template("admin_projects.html", projects=projects)


@app.route("/quan-tri/du-an/them", methods=["GET", "POST"])
@admin_required
def admin_project_add():
    if request.method == "POST":
        image = save_upload("image")
        p = Project(
            title=request.form.get("title", "").strip(),
            category=request.form.get("category", ""),
            material=request.form.get("material", ""),
            segment=request.form.get("segment", ""),
            location=request.form.get("location", "").strip(),
            summary=request.form.get("summary", "").strip(),
            description=request.form.get("description", "").strip(),
            image=image,
            featured=bool(request.form.get("featured")),
        )
        db.session.add(p)
        db.session.commit()
        n = save_project_images(p)      # thêm nhiều ảnh (nếu có)
        db.session.commit()
        extra = f" kèm {n} ảnh" if n else ""
        flash(f"Đã thêm dự án thành công{extra}.", "success")
        return redirect(url_for("admin_project_edit", pid=p.id))
    return render_template("admin_project_form.html", project=None,
                           action=url_for("admin_project_add"), title="Thêm dự án")


@app.route("/quan-tri/du-an/<int:pid>/sua", methods=["GET", "POST"])
@admin_required
def admin_project_edit(pid):
    p = Project.query.get_or_404(pid)
    if request.method == "POST":
        p.title = request.form.get("title", "").strip()
        p.category = request.form.get("category", "")
        p.material = request.form.get("material", "")
        p.segment = request.form.get("segment", "")
        p.location = request.form.get("location", "").strip()
        p.summary = request.form.get("summary", "").strip()
        p.description = request.form.get("description", "").strip()
        p.featured = bool(request.form.get("featured"))
        new_img = save_upload("image")
        if new_img:
            p.image = new_img
        # Xóa các ảnh phụ được tick chọn xóa
        del_ids = request.form.getlist("delete_image")
        if del_ids:
            for im in list(p.images):
                if str(im.id) in del_ids:
                    _remove_upload_file(im.filename)
                    if p.image == im.filename:
                        p.image = None
                    db.session.delete(im)
        # Thêm ảnh mới (nhiều ảnh cùng lúc)
        n = save_project_images(p)
        db.session.commit()
        flash(f"Đã cập nhật dự án{(' + ' + str(n) + ' ảnh mới') if n else ''}.", "success")
        return redirect(url_for("admin_project_edit", pid=pid))
    return render_template("admin_project_form.html", project=p,
                           action=url_for("admin_project_edit", pid=pid), title="Sửa dự án")


@app.route("/quan-tri/du-an/<int:pid>/xoa", methods=["POST"])
@admin_required
def admin_project_delete(pid):
    p = Project.query.get_or_404(pid)
    db.session.delete(p)
    db.session.commit()
    flash("Đã xóa dự án.", "info")
    return redirect(url_for("admin_projects"))


# ---------- CRUD bài viết ----------
@app.route("/quan-tri/bai-viet")
@admin_required
def admin_articles():
    articles = Article.query.order_by(Article.created_at.desc()).all()
    return render_template("admin_articles.html", articles=articles)


@app.route("/quan-tri/bai-viet/lam-moi", methods=["POST"])
@admin_required
def admin_articles_refresh():
    """Ghi đè nội dung 8 bài viết mẫu bằng bản viết sâu mới nhất (theo slug).
    KHÔNG xóa dự án, KHÔNG đụng bài viết tự thêm."""
    try:
        from seed import run_seed
        run_seed(db, Project, Article, force_articles=True)
        flash("Đã làm mới nội dung 8 bài viết kiến thức (bản viết sâu).", "success")
    except Exception as e:
        db.session.rollback()
        flash(f"Không làm mới được: {e}", "danger")
    return redirect(url_for("admin_articles"))


@app.route("/quan-tri/bai-viet/them", methods=["GET", "POST"])
@admin_required
def admin_article_add():
    if request.method == "POST":
        cover = save_upload("cover")
        slug = request.form.get("slug", "").strip()
        if not slug:
            import re, unicodedata
            raw = request.form.get("title", "")
            slug = unicodedata.normalize("NFKD", raw).encode("ascii", "ignore").decode()
            slug = re.sub(r"[^a-z0-9]+", "-", slug.lower()).strip("-")
        a = Article(
            slug=slug,
            title=request.form.get("title", "").strip(),
            category=request.form.get("category", "kien-thuc"),
            excerpt=request.form.get("excerpt", "").strip(),
            body=request.form.get("body", ""),
            cover=cover,
            featured=bool(request.form.get("featured")),
        )
        db.session.add(a)
        db.session.commit()
        flash("Đã thêm bài viết.", "success")
        return redirect(url_for("admin_articles"))
    return render_template("admin_article_form.html", article=None,
                           action=url_for("admin_article_add"), title="Thêm bài viết")


@app.route("/quan-tri/bai-viet/<int:aid>/sua", methods=["GET", "POST"])
@admin_required
def admin_article_edit(aid):
    a = Article.query.get_or_404(aid)
    if request.method == "POST":
        a.title = request.form.get("title", "").strip()
        a.category = request.form.get("category", "kien-thuc")
        a.excerpt = request.form.get("excerpt", "").strip()
        a.body = request.form.get("body", "")
        a.featured = bool(request.form.get("featured"))
        new_cover = save_upload("cover")
        if new_cover:
            a.cover = new_cover
        db.session.commit()
        flash("Đã cập nhật bài viết.", "success")
        return redirect(url_for("admin_articles"))
    return render_template("admin_article_form.html", article=a,
                           action=url_for("admin_article_edit", aid=aid), title="Sửa bài viết")


@app.route("/quan-tri/bai-viet/<int:aid>/xoa", methods=["POST"])
@admin_required
def admin_article_delete(aid):
    a = Article.query.get_or_404(aid)
    db.session.delete(a)
    db.session.commit()
    flash("Đã xóa bài viết.", "info")
    return redirect(url_for("admin_articles"))


@app.cli.command("seed")
def seed_cmd():
    """flask --app app seed  -> nạp dữ liệu mẫu."""
    from seed import run_seed
    run_seed(db, Project, Article)
    print("Đã nạp dữ liệu mẫu.")


@app.cli.command("refresh-articles")
def refresh_articles_cmd():
    """flask --app app refresh-articles -> ghi đè 8 bài viết bằng bản viết sâu."""
    from seed import run_seed
    run_seed(db, Project, Article, force_articles=True)
    print("Đã làm mới bài viết.")


with app.app_context():
    db.create_all()
    # Auto-seed: nếu DB trống thì nạp dữ liệu (chạy mỗi lần Render deploy lại)
    try:
        from seed import run_seed
        run_seed(db, Project, Article)
    except Exception as e:
        print(f"Seed warning: {e}")


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5001))
    app.run(host="0.0.0.0", port=port, debug=True)
