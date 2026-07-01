# -*- coding: utf-8 -*-
"""Xóa DB cũ và nạp lại dữ liệu mẫu với ảnh thật.
Chạy: py -3 reset_and_seed.py  (sau khi đã tắt server Flask)
"""
import os, sys

db_path = os.path.join(os.path.dirname(__file__), "data", "homie_web.db")
if os.path.exists(db_path):
    os.remove(db_path)
    print(f"Đã xóa: {db_path}")
else:
    print("DB chưa tồn tại, tạo mới.")

# Import app để tạo bảng và seed
sys.path.insert(0, os.path.dirname(__file__))
from app import app, db, Project, Article
from seed import run_seed

with app.app_context():
    db.create_all()
    run_seed(db, Project, Article)

print("Xong! Khởi động server: py -3 app.py")
