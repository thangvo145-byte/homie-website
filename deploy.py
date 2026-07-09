#!/usr/bin/env python3
"""Đẩy nhanh: commit + push + (tùy chọn) kích Render deploy ngay.

Dùng:
    python deploy.py "nội dung commit"

- Tự add tất cả thay đổi, commit, push lên master.
- Nếu có file .deploy_hook (URL Deploy Hook lấy từ Render), sẽ gọi luôn để
  ép Render build ngay, khỏi phải vào dashboard bấm tay.
  (Lấy URL: Render > service homie-website > Settings > Deploy Hook > Copy,
   dán vào file .deploy_hook cùng thư mục này — chỉ 1 dòng URL.)
"""
import os
import subprocess
import sys
import urllib.request

BASE = os.path.abspath(os.path.dirname(__file__))


def run(cmd):
    print("»", " ".join(cmd))
    return subprocess.run(cmd, cwd=BASE).returncode


def main():
    msg = sys.argv[1] if len(sys.argv) > 1 else "cập nhật nội dung"
    run(["git", "add", "-A"])
    # commit có thể "nothing to commit" -> bỏ qua lỗi
    subprocess.run(["git", "commit", "-m", msg], cwd=BASE)
    if run(["git", "push", "origin", "master"]) != 0:
        print("!! Push lỗi — kiểm tra mạng/GitHub."); return

    hook_file = os.path.join(BASE, ".deploy_hook")
    if os.path.exists(hook_file):
        url = open(hook_file, encoding="utf-8").read().strip()
        if url.startswith("http"):
            try:
                with urllib.request.urlopen(url, timeout=20) as r:
                    print("Đã kích Render deploy:", r.status)
            except Exception as e:
                print("!! Gọi deploy hook lỗi:", e)
    else:
        print("(Chưa có .deploy_hook — Render sẽ tự deploy nếu Auto-Deploy = Yes.)")


if __name__ == "__main__":
    main()
