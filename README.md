# Website Homie — Nội thất Quảng Trị

Website "mặt tiền" giới thiệu Homie: khoe **mẫu mã** công trình thật, chia sẻ **kiến thức & xu hướng**
nội thất, và **thu số điện thoại/Zalo** của khách quan tâm (phễu đầu nguồn).

Tách riêng khỏi app quản lý sản xuất (`HOMIE-QUAN-LY-SAN-XUAT`) cho an toàn — web public không đụng dữ liệu nội bộ.

## Cấu trúc
- `app.py` — toàn bộ route + 3 bảng dữ liệu: `Project` (mẫu mã), `Article` (bài viết), `Lead` (khách để lại SĐT).
- `seed.py` — nạp 6 mẫu + 3 bài viết mẫu.
- `templates/` — giao diện (Bootstrap 5, tông gỗ ấm). `macros.html` = thẻ mẫu/bài dùng chung.
- `static/css/style.css` — màu thương hiệu.
- `static/uploads/` — nơi để ảnh thật của mẫu mã/bài viết.
- `data/homie_web.db` — SQLite (tự tạo).

## Chạy ở máy
```bash
python -m venv .venv
.\.venv\Scripts\python.exe -m pip install -r requirements.txt
.\.venv\Scripts\python.exe -m flask --app app seed     # nạp dữ liệu mẫu (chỉ chạy lần đầu)
.\.venv\Scripts\python.exe app.py                       # mở http://127.0.0.1:5001
```

## Các trang
| Đường dẫn | Nội dung |
|---|---|
| `/` | Trang chủ: hero + lợi thế + mẫu nổi bật + bài viết + form lấy SĐT |
| `/mau-ma` | Thư viện mẫu mã, lọc theo loại & chất liệu |
| `/mau-ma/<id>` | Chi tiết 1 mẫu |
| `/kien-thuc` | Danh sách bài kiến thức/xu hướng |
| `/kien-thuc/<slug>` | Chi tiết bài |
| `/gioi-thieu`, `/lien-he` | Giới thiệu, liên hệ |
| `/quan-tri/khach` | **(Chủ)** Xem khách để lại SĐT — đăng nhập bằng mật khẩu |

## Mật khẩu quản trị & thông tin liên hệ
Sửa nhanh trong `app.py` (biến `SITE` và `ADMIN_PASSWORD`) hoặc đặt biến môi trường:
`HOMIE_ZALO`, `HOMIE_HOTLINE`, `HOMIE_FB`, `HOMIE_DIACHI`, `HOMIE_ADMIN_PASS`, `SECRET_KEY`.
Mặc định mật khẩu quản trị: `homie123` — **nhớ đổi trước khi đưa lên mạng**.

## Thêm mẫu / bài mới (nhờ Claude làm)
Hiện chưa có trang tự đăng. Khi cần thêm mẫu mã hoặc bài viết, bà chủ chỉ cần:
1. Bỏ ảnh vào `static/uploads/` (vd `tu-bep-chi-lan.jpg`).
2. Nhắn Claude: "thêm mẫu/bài này..." kèm tiêu đề, mô tả, tên file ảnh.

## Đưa lên mạng (Render — miễn phí)
1. Đẩy thư mục này lên GitHub.
2. Trên render.com → New → Blueprint → trỏ vào repo (đã có `render.yaml`).
3. Đặt `HOMIE_ADMIN_PASS` (mật khẩu chủ) trong phần Environment.
> Lưu ý: gói free của Render dùng ổ đĩa tạm — danh sách khách (Lead) có thể mất khi service ngủ/khởi động lại.
> Nếu muốn giữ chắc chắn, gắn thêm Disk (như app quản lý sản xuất) hoặc đổi sang DB Postgres. Nhắn Claude khi cần.
