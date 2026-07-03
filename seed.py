# -*- coding: utf-8 -*-
"""Nạp dữ liệu dự án THẬT cho website Homie — ảnh từ D:\HINH ANH\THI CONG\CHUNG TRON GOI"""


def run_seed(db, Project, Article):
    if Project.query.first() or Article.query.first():
        return  # Đã có dữ liệu, bỏ qua

    projects = [
        # ---- TRỌN GÓI — dự án thật ----
        dict(title="Nội thất trọn gói — Chị Trang",
             category="tron-goi", material="nhua-rong", segment="nhom-a",
             location="Quảng Trị",
             image="tc_12-chi-trang_01.jpg",
             summary="Hoàn thiện nội thất trọn gói cho gia đình chị Trang — từ tủ bếp đến phòng ngủ.",
             description="Dự án nội thất trọn gói — Homie đồng hành từ khảo sát, thiết kế 3D đến thi công "
                         "lắp đặt và bàn giao. Chất liệu nhựa rỗng chống nồm ẩm, phụ kiện ray giảm chấn.",
             featured=True),

        dict(title="Nội thất trọn gói — A Hải Đông Hà",
             category="tron-goi", material="nhua-rong", segment="nhom-a",
             location="TP. Đông Hà",
             image="tc_a-hai-dong-ha_01.jpg",
             summary="Tủ bếp + phòng ngủ đồng bộ phong cách hiện đại cho gia đình A Hải.",
             description="Dự án thi công trọn gói tại Đông Hà. Hệ tủ bếp nhựa rỗng chữ L, phòng ngủ "
                         "gỗ công nghiệp tone trung tính. Bàn giao đúng hẹn, dọn nhà vào ở ngay.",
             featured=True),

        dict(title="Nội thất trọn gói — A Hiếu Hải Lăng",
             category="tron-goi", material="go-cong-nghiep", segment="nhom-b",
             location="Hải Lăng",
             image="tc_a-hieu-hai-lang_01.jpg",
             summary="Hoàn thiện nội thất toàn bộ nhà 2 tầng tại Hải Lăng — gỗ công nghiệp An Cường.",
             description="Dự án nhà 2 tầng tại Hải Lăng. Gỗ công nghiệp An Cường phủ Melamine vân gỗ "
                         "sang trọng cho toàn bộ không gian bếp, phòng khách, 3 phòng ngủ.",
             featured=True),

        dict(title="Nội thất trọn gói — Anh Sang",
             category="tron-goi", material="nhua-rong", segment="nhom-a",
             location="Quảng Trị",
             image="tc_anh-sang_01.jpg",
             summary="Hệ nội thất đầy đủ phòng bếp + phòng ngủ, nhựa rỗng chống ẩm.",
             description="Anh Sang chọn giải pháp nhựa rỗng cho toàn bộ nội thất — bền, chống nồm ẩm "
                         "miền Trung, phù hợp ngân sách. Thiết kế tối giản, dễ dọn dẹp.",
             featured=False),

        dict(title="Nội thất trọn gói — Anh Tâm",
             category="tron-goi", material="go-cong-nghiep", segment="nhom-b",
             location="Quảng Trị",
             image="tc_anh-tam_01.jpg",
             summary="Nội thất phong cách hiện đại ấm cúng — gỗ công nghiệp tone nâu vân gỗ.",
             description="Dự án anh Tâm — phong cách hiện đại ấm cúng. Gỗ công nghiệp An Cường tone "
                         "nâu ấm, kết hợp ánh sáng LED hắt tạo không gian ấm áp cho cả gia đình.",
             featured=False),

        dict(title="Nội thất trọn gói — Anh Vinh Gio Linh",
             category="tron-goi", material="nhua-rong", segment="nhom-a",
             location="Gio Linh",
             image="tc_anh-vinh-gio-ling_01.jpg",
             summary="Hoàn thiện nội thất nhà phố tại Gio Linh — tủ bếp + phòng ngủ đồng bộ.",
             description="Dự án tại Gio Linh — nhà phố 1 tầng hoàn thiện trọn gói. Tủ bếp nhựa rỗng "
                         "chữ L, phòng ngủ nhựa rỗng tone trắng kem gọn gàng, hiện đại.",
             featured=True),

        dict(title="Nội thất trọn gói — Chị Nga",
             category="tron-goi", material="go-cong-nghiep", segment="nhom-b",
             location="Quảng Trị",
             image="tc_chii-nga_01.jpg",
             summary="Dự án lớn đầy đủ phòng — bếp, phòng khách, 3 phòng ngủ đồng bộ phong cách.",
             description="Chị Nga đầu tư nội thất bài bản cho căn nhà mới. Gỗ công nghiệp An Cường "
                         "đồng màu xuyên suốt — tạo cảm giác sang trọng, thống nhất toàn nhà.",
             featured=True),

        dict(title="Nội thất trọn gói — Chị Ngọc Lan",
             category="tron-goi", material="nhua-rong", segment="nhom-a",
             location="Quảng Trị",
             image="tc_chi-ngoc-lan_01.jpg",
             summary="Nội thất nhà ống phố — tủ bếp nhựa rỗng + phòng ngủ gọn đẹp.",
             description="Nhà ống phố chật cần tận dụng không gian tối đa. Homie thiết kế tủ bếp "
                         "chữ I âm trần, phòng ngủ tủ áo kịch trần — dụng hết từng cm².",
             featured=False),

        dict(title="Nội thất trọn gói — Cửa Việt",
             category="tron-goi", material="nhua-rong", segment="nhom-a",
             location="Cửa Việt",
             image="tc_cua-viet_01.jpg",
             summary="Nội thất nhà ở khu vực ven biển Cửa Việt — đặc biệt chú trọng chống ẩm muối.",
             description="Khu vực ven biển Cửa Việt độ ẩm muối rất cao — nhựa rỗng là giải pháp tối ưu. "
                         "Phụ kiện inox 304 chống gỉ toàn bộ. Bảo hành 5 năm.",
             featured=True),

        dict(title="Nội thất trọn gói — Chị Yến",
             category="tron-goi", material="nhua-rong", segment="nhom-a",
             location="Quảng Trị",
             image="tc_chi-yen_01.jpg",
             summary="Bộ nội thất ấm cúng cho gia đình nhỏ — đủ tiện nghi, hợp ngân sách.",
             description="Gia đình chị Yến — ngân sách vừa phải nhưng vẫn muốn đầy đủ tiện nghi. "
                         "Nhựa rỗng giúp tối ưu chi phí mà không giảm độ bền. Giao nhà đúng hẹn.",
             featured=False),

        dict(title="Nội thất trọn gói — Anh Dương",
             category="tron-goi", material="go-cong-nghiep", segment="nhom-b",
             location="Quảng Trị",
             image="tc_duong_01.jpg",
             summary="Phong cách hiện đại minimalist — gỗ An Cường tone xám lạnh, line sạch.",
             description="Anh Dương yêu thích phong cách minimalist — đường nét thẳng, màu xám lạnh "
                         "phủ gỗ An Cường, không chi tiết thừa. Nội thất như trong tạp chí.",
             featured=False),

        dict(title="Nội thất trọn gói — Anh Hoàng Chợ Cạn",
             category="tron-goi", material="nhua-rong", segment="nhom-a",
             location="Quảng Trị",
             image="tc_hoang-cho-can_01.jpg",
             summary="Nhà mới hoàn thiện nội thất từ A-Z — bếp, phòng ngủ, phòng khách.",
             description="Anh Hoàng làm nội thất trọn gói toàn bộ nhà mới từ A-Z. Phân bổ ngân sách "
                         "hợp lý: nhựa rỗng cho khu ẩm, gỗ cho phòng ngủ — tối ưu cả bền lẫn đẹp.",
             featured=False),

        dict(title="Nội thất trọn gói — Kiệm Anh",
             category="tron-goi", material="go-cong-nghiep", segment="nhom-b",
             location="Quảng Trị",
             image="tc_kiem-anh_01.jpg",
             summary="Nội thất sang trọng đồng bộ — gỗ An Cường phủ Melamine vân gỗ óc chó.",
             description="Dự án đầu tư bài bản — gỗ công nghiệp An Cường vân óc chó xuyên suốt toàn nhà. "
                         "Phụ kiện Hafele nhập khẩu, ray giảm chấn êm ái.",
             featured=True),

        dict(title="Nội thất trọn gói — Anh Sáng",
             category="tron-goi", material="nhua-rong", segment="nhom-a",
             location="Quảng Trị",
             image="tc_sang_01.jpg",
             summary="Hoàn thiện nội thất nhà phố, đồng bộ tone màu trắng — sáng sủa, hiện đại.",
             description="Tone trắng kem xuyên suốt — tạo cảm giác sáng rộng cho nhà phố. "
                         "Nhựa rỗng cánh acrylic bóng dễ lau, bền đẹp qua năm tháng.",
             featured=False),

        dict(title="Nội thất trọn gói — Anh Tĩnh",
             category="tron-goi", material="go-cong-nghiep", segment="nhom-b",
             location="Quảng Trị",
             image="tc_tinh_01.jpg",
             summary="Dự án lớn — nội thất toàn bộ căn nhà 2 tầng, phong cách hiện đại ấm cúng.",
             description="Anh Tĩnh đầu tư nội thất toàn bộ 2 tầng. Tầng 1: bếp + phòng khách. "
                         "Tầng 2: 3 phòng ngủ đồng bộ. Gỗ An Cường phủ Melamine vân gỗ sáng.",
             featured=True),

        dict(title="Nội thất trọn gói — Chị Vy Ái Tử",
             category="tron-goi", material="nhua-rong", segment="nhom-a",
             location="Ái Tử, Triệu Phong",
             image="tc_vy-ai-tu_01.jpg",
             summary="Nhà mới tại Ái Tử — tủ bếp + phòng ngủ + kệ phòng khách hoàn chỉnh.",
             description="Chị Vy tại Ái Tử — nhà mới hoàn thiện trọn gói. Nhựa rỗng cho bếp "
                         "chống nồm ẩm sông Thạch Hãn, gỗ cho phòng ngủ ấm cúng.",
             featured=False),

        dict(title="Nội thất trọn gói — Chị Yến Khe Sanh",
             category="tron-goi", material="go-cong-nghiep", segment="nhom-b",
             location="Khe Sanh, Hướng Hóa",
             image="tc_yen-khe-sanh_01.jpg",
             summary="Nội thất nhà vùng cao Khe Sanh — chú trọng độ bền, chắc chắn qua thời tiết.",
             description="Dự án tại Khe Sanh — vùng khí hậu mát mẻ đặc thù. Gỗ công nghiệp An Cường "
                         "bền đẹp, phù hợp với khí hậu miền núi Hướng Hóa.",
             featured=False),

        dict(title="Nội thất trọn gói — A Trung Đông Văn Lưu",
             category="tron-goi", material="nhua-rong", segment="nhom-a",
             location="Quảng Trị",
             image="tc_a-trung-dvl_01.jpg",
             summary="Hoàn thiện nội thất nhà ở — bếp chữ L + 2 phòng ngủ đồng bộ.",
             description="A Trung chọn nhựa rỗng cho toàn bộ công trình — dễ vệ sinh, bền bỉ, "
                         "hợp khí hậu miền Trung. Bàn giao đúng tiến độ cam kết.",
             featured=False),

        dict(title="Nội thất trọn gói — Anh Dũng",
             category="tron-goi", material="go-cong-nghiep", segment="nhom-b",
             location="Quảng Trị",
             image="tc_anh-dung_01.jpg",
             summary="Nội thất căn nhà mới — tone nâu ấm gỗ An Cường, hiện đại sang trọng.",
             description="Anh Dũng hoàn thiện căn nhà mới với nội thất gỗ công nghiệp An Cường "
                         "tone nâu ấm. Đồng bộ từ phòng bếp, phòng khách đến 2 phòng ngủ.",
             featured=True),
    ]

    for p in projects:
        db.session.add(Project(**p))

    articles = [
        dict(slug="nhua-rong-hay-go-cong-nghiep",
             title="Nhựa rỗng hay gỗ công nghiệp? Chọn sao cho đúng nhà bạn",
             category="kien-thuc",
             cover="tc_chii-nga_01.jpg",
             excerpt="Hai chất liệu phổ biến nhất hiện nay, mỗi loại hợp một kiểu nhà và túi tiền. "
                     "Đây là cách Homie tư vấn khách chọn cho chuẩn.",
             body="""
<p>Khi làm nội thất, câu hỏi đầu tiên gần như nhà nào cũng hỏi: <b>"Nên làm nhựa hay gỗ?"</b>.
Không có loại nào tốt hơn tuyệt đối — chỉ có loại <i>hợp với nhà bạn</i> hơn.</p>
<h3>1. Nhựa rỗng (Picomat) — vua chống ẩm</h3>
<ul>
<li><b>Ưu điểm:</b> không thấm nước, không cong vênh, không mối mọt — cực hợp khí hậu nồm ẩm miền Trung. Nhẹ, dễ lau chùi, giá hợp lý.</li>
<li><b>Hợp với:</b> tủ bếp, tủ khu vực ẩm (gần nhà tắm), gia đình trẻ muốn bền - đẹp - tiết kiệm (phân khúc 50–150tr).</li>
</ul>
<h3>2. Gỗ công nghiệp An Cường — vân gỗ sang trọng</h3>
<ul>
<li><b>Ưu điểm:</b> bề mặt vân gỗ đẹp như thật, nhiều màu cao cấp, cảm giác chắc chắn, sang trọng.</li>
<li><b>Lưu ý:</b> nên chọn lõi xanh chống ẩm cho khu vực dễ ẩm; thi công chuẩn để bền lâu.</li>
<li><b>Hợp với:</b> phòng khách, phòng ngủ, nhà coi trọng thẩm mỹ - đẳng cấp (phân khúc 150–500tr).</li>
</ul>
<p><b>Lời khuyên của Homie:</b> nhiều nhà làm <i>kết hợp</i> — nhựa rỗng cho bếp và khu ẩm, gỗ công nghiệp
cho phòng khách phòng ngủ. Vừa bền vừa đẹp vừa hợp ngân sách.</p>
""",
             featured=True),

        dict(slug="kinh-nghiem-chong-non-am-mien-trung",
             title="Làm nội thất ở miền Trung: 5 điều phải nhớ để khỏi cong vênh, mối mọt",
             category="kinh-nghiem",
             cover="tc_kiem-anh_01.jpg",
             excerpt="Khí hậu nồm ẩm là kẻ thù số 1 của đồ gỗ. Đây là 5 nguyên tắc giúp nội thất nhà bạn bền hàng chục năm.",
             body="""
<p>Ở Quảng Trị nói riêng và miền Trung nói chung, độ ẩm cao và mùa nồm là nguyên nhân số 1 khiến
đồ nội thất nhanh hỏng. Sau nhiều công trình thực tế, Homie đúc kết 5 điều:</p>
<ol>
<li><b>Chọn chất liệu chống ẩm cho khu vực ướt:</b> bếp, tủ gần nhà tắm nên ưu tiên nhựa rỗng hoặc gỗ lõi xanh.</li>
<li><b>Chừa khe thoát ẩm:</b> tủ kịch sàn dễ hút ẩm chân tủ — nên kê chân hoặc chừa khe.</li>
<li><b>Phụ kiện inox/hợp kim:</b> bản lề, ray trượt nên dùng loại chống gỉ, đừng ham rẻ.</li>
<li><b>Dán cạnh kỹ:</b> cạnh không dán kín là nơi nước ngấm vào làm phồng cốt gỗ.</li>
<li><b>Thi công đúng kỹ thuật:</b> 70% độ bền nằm ở tay nghề thi công, không chỉ ở vật liệu.</li>
</ol>
<p>Homie là đơn vị <b>địa phương</b> — hiểu rõ khí hậu Quảng Trị và đã làm hàng trăm công trình thật ở đây.</p>
""",
             featured=True),

        dict(slug="tai-sao-chon-homie",
             title="Tại sao chọn Homie? 5 điều khách hàng Quảng Trị thường nói sau khi dọn nhà",
             category="kinh-nghiem",
             cover="tc_tinh_01.jpg",
             excerpt="Sau hàng trăm công trình, điều khách hay nhắc nhất không phải là đẹp hay rẻ — mà là đúng hẹn và không phát sinh.",
             body="""
<p>Chúng tôi hỏi khách sau khi bàn giao: <b>"Anh/chị thích điều gì nhất ở Homie?"</b>. Đây là 5 câu trả lời hay nhất:</p>
<ol>
<li><b>"Đúng hẹn"</b> — cam kết ngày bàn giao, làm đúng ngày đó.</li>
<li><b>"Không phát sinh"</b> — báo giá bao nhiêu, làm đúng bấy nhiêu. Không thêm phí lặt vặt sau.</li>
<li><b>"Có người chịu trách nhiệm"</b> — gặp sự cố, gọi là Homie ra ngay.</li>
<li><b>"Biết nghe"</b> — anh Thắng lắng nghe, hiểu mình muốn gì, không áp đặt.</li>
<li><b>"Giá hợp lý, không bị chặt"</b> — bảng giá minh bạch, dân Quảng Trị hiểu Quảng Trị.</li>
</ol>
<p>Đó là lý do Homie tồn tại — không phải để làm đẹp nhất, mà để làm <b>đúng nhất</b> cho từng gia đình.</p>
""",
             featured=True),
    ]

    for a in articles:
        db.session.add(Article(**a))

    db.session.commit()
    print(f"Seed OK: {len(projects)} du an that, {len(articles)} bai viet.")
