"""
Homie Website - Trang giới thiệu, thư viện mẫu mã & kiến thức nội thất
Mục tiêu: kéo khách mới để lại SĐT/Zalo (phễu đầu nguồn).
Stack: Flask + SQLite + Jinja2 + Bootstrap 5 (giống app quản lý sản xuất).
"""
import os
from datetime import datetime
from functools import wraps

from flask import (
    Flask, render_template, request, redirect, url_for,
    flash, session, abort, jsonify
)
from flask_sqlalchemy import SQLAlchemy
from werkzeug.utils import secure_filename
from sqlalchemy import func

BASE_DIR = os.path.abspath(os.path.dirname(__file__))
DATA_DIR = os.path.join(BASE_DIR, "data")
UPLOAD_DIR = os.path.join(BASE_DIR, "static", "uploads")
os.makedirs(DATA_DIR, exist_ok=True)
os.makedirs(UPLOAD_DIR, exist_ok=True)

app = Flask(__name__)
app.config["SECRET_KEY"] = os.environ.get("SECRET_KEY", "homie-doi-mat-khau-nay")
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///" + os.path.join(DATA_DIR, "homie_web.db")
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config["UPLOAD_FOLDER"] = UPLOAD_DIR
app.config["MAX_CONTENT_LENGTH"] = 16 * 1024 * 1024  # 16MB / ảnh

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


# ----------------------------- HELPERS -----------------------------
CATEGORIES = [
    ("tu-bep", "Tủ bếp"),
    ("tu-ao", "Tủ áo"),
    ("giuong", "Giường ngủ"),
    ("phong-khach", "Phòng khách"),
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


# Đăng ký các bảng tra cứu tĩnh làm Jinja global để macro (import không kèm
# context) vẫn truy cập được.
app.jinja_env.globals.update(
    SITE=SITE, CATEGORIES=CATEGORIES, MATERIALS=MATERIALS,
    CAT_MAP=CAT_MAP, MAT_MAP=MAT_MAP, ART_CAT=ART_CAT,
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
    phone = (request.form.get("phone") or "").strip()
    if not phone:
        flash("Bà chủ vui lòng để lại số điện thoại/Zalo để Homie liên hệ nhé.", "warning")
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
    flash("Cảm ơn bạn! Homie đã nhận thông tin và sẽ liên hệ tư vấn miễn phí trong thời gian sớm nhất.", "success")
    return redirect(url_for("thanks"))


@app.route("/cam-on")
def thanks():
    return render_template("thanks.html")


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


# ---------- helpers upload ----------
ALLOWED_EXT = {"jpg", "jpeg", "png", "webp"}

def allowed_file(filename):
    return "." in filename and filename.rsplit(".", 1)[1].lower() in ALLOWED_EXT

def save_upload(file_field):
    """Lưu file upload, trả về tên file hoặc None."""
    f = request.files.get(file_field)
    if f and f.filename and allowed_file(f.filename):
        ext = f.filename.rsplit(".", 1)[1].lower()
        fname = f"{file_field}_{datetime.utcnow().strftime('%Y%m%d%H%M%S%f')}.{ext}"
        f.save(os.path.join(app.config["UPLOAD_FOLDER"], fname))
        return fname
    return None


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
        flash("Đã thêm dự án thành công.", "success")
        return redirect(url_for("admin_projects"))
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
        db.session.commit()
        flash("Đã cập nhật dự án.", "success")
        return redirect(url_for("admin_projects"))
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
