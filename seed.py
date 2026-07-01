# -*- coding: utf-8 -*-
"""Nạp dữ liệu mẫu cho website Homie — dùng ảnh thật đã copy vào static/uploads."""


def run_seed(db, Project, Article):
    if Project.query.first() or Article.query.first():
        print("Đã có dữ liệu, bỏ qua seed. (Xóa data/homie_web.db nếu muốn nạp lại)")
        return

    projects = [
        # ---- TỦ BẾP ----
        dict(title="Tủ bếp chữ L nhựa rỗng — nhà chị Hương, Đông Hà",
             category="tu-bep", material="nhua-rong", segment="nhom-a",
             location="TP. Đông Hà",
             image="bep_01.jpg",
             summary="Tủ bếp nhựa rỗng chống nồm ẩm, cánh phủ acrylic bóng, tay nắm âm hiện đại.",
             description="Căn bếp chữ L tối ưu cho nhà ống. Chất liệu nhựa rỗng Picomat lõi đặc — "
                         "không cong vênh, không mối mọt, lau chùi dễ, rất hợp khí hậu nồm ẩm miền Trung. "
                         "Cánh phủ acrylic bóng gương chống bám dầu mỡ. Bàn đá thạch anh chống xước.",
             featured=True),
        dict(title="Tủ bếp chữ I gỗ công nghiệp — nhà anh Tuấn, Triệu Phong",
             category="tu-bep", material="go-cong-nghiep", segment="nhom-b",
             location="Triệu Phong",
             image="bep_02.jpg",
             summary="Tủ bếp gỗ An Cường vân sáng, tủ bếp trên kết hợp kính cường lực, sang trọng.",
             description="Thiết kế tủ bếp chữ I tối giản hiện đại. Gỗ công nghiệp An Cường phủ Melamine "
                         "vân sáng, tủ trên kết hợp cánh kính cường lực. Hệ thống phụ kiện ray giảm chấn Hafele.",
             featured=True),
        dict(title="Tủ bếp chữ U nhựa rỗng — căn hộ 75m², Đông Hà",
             category="tu-bep", material="nhua-rong", segment="nhom-a",
             location="TP. Đông Hà",
             image="bep_03.jpg",
             summary="Giải pháp bếp chữ U tối ưu diện tích cho căn hộ, màu xanh nhạt tươi mát.",
             description="Bếp chữ U cho căn hộ 75m² — tận dụng tối đa không gian góc bếp. "
                         "Màu xanh bạc hà phủ acrylic làm sáng không gian. Nhựa rỗng Picomat không lo mối ẩm.",
             featured=False),
        dict(title="Tủ bếp nhựa rỗng + đảo bếp — nhà chị Mai, Gio Linh",
             category="tu-bep", material="nhua-rong", segment="nhom-a",
             location="Gio Linh",
             image="bep_04.jpg",
             summary="Bếp mở kết hợp đảo bếp đa năng, phong cách hiện đại tối giản.",
             description="Không gian bếp mở kết hợp đảo bếp — xu hướng phổ biến cho nhà rộng. "
                         "Đảo bếp đa năng vừa làm quầy bar vừa là bàn ăn phụ. Nhựa rỗng bền đẹp lâu dài.",
             featured=False),
        dict(title="Tủ bếp gỗ An Cường vân óc chó — biệt thự Cam Lộ",
             category="tu-bep", material="go-cong-nghiep", segment="nhom-b",
             location="Cam Lộ",
             image="bep_05.jpg",
             summary="Hệ tủ bếp cao cấp vân óc chó, đá marble, phong cách luxury ấm cúng.",
             description="Dự án biệt thự — hệ tủ bếp gỗ An Cường phủ Melamine vân óc chó sang trọng. "
                         "Mặt đá marble tự nhiên, bồn rửa inox undermount. Phụ kiện Blum cao cấp.",
             featured=True),
        dict(title="Tủ bếp nhựa rỗng màu trắng kem — nhà phố Đông Hà",
             category="tu-bep", material="nhua-rong", segment="nhom-a",
             location="TP. Đông Hà",
             image="bep_06.jpg",
             summary="Bếp trắng kem sạch sẽ, sáng bóng — lựa chọn kinh điển không bao giờ lỗi mốt.",
             description="Tủ bếp nhựa rỗng màu trắng kem acrylic bóng — phong cách tối giản hiện đại. "
                         "Thiết kế tủ trên kiểu hộp giúp không gian gọn gàng, dễ vệ sinh.",
             featured=False),

        # ---- PHÒNG NGỦ MASTER ----
        dict(title="Phòng ngủ master gỗ óc chó — nhà anh Hùng, Đông Hà",
             category="giuong", material="go-cong-nghiep", segment="nhom-b",
             location="TP. Đông Hà",
             image="ngu_01.jpg",
             summary="Bộ phòng ngủ master đồng bộ vân óc chó — giường, táp, tủ áo, bàn phấn.",
             description="Trọn bộ phòng ngủ master: giường phản king-size, 2 táp đầu giường, tủ áo kịch trần "
                         "cánh lùa, bàn trang điểm gương lớn. Gỗ An Cường vân óc chó ấm áp sang trọng.",
             featured=True),
        dict(title="Phòng ngủ nhựa rỗng tone be — nhà chị Linh, Triệu Phong",
             category="giuong", material="nhua-rong", segment="nhom-a",
             location="Triệu Phong",
             image="ngu_02.jpg",
             summary="Phòng ngủ nhựa rỗng tone be kem nhẹ nhàng, tối ưu chi phí, chống ẩm tốt.",
             description="Giải pháp phòng ngủ tiết kiệm bằng nhựa rỗng — bền đẹp, không lo nồm ẩm. "
                         "Tone màu be kem tạo cảm giác ấm áp, thư giãn. Phù hợp ngân sách 50-100tr.",
             featured=True),
        dict(title="Phòng ngủ Japandi gỗ tự nhiên — nhà anh Thành, Cam Lộ",
             category="giuong", material="go-cong-nghiep", segment="nhom-b",
             location="Cam Lộ",
             image="ngu_03.jpg",
             summary="Phong cách Japandi ấm cúng, gỗ tự nhiên, ánh sáng vàng ấm — thư giãn tuyệt đối.",
             description="Phong cách Japandi kết hợp tinh tế Nhật Bản và Scandinavia — ít đồ nội thất nhưng "
                         "mỗi món đều có chức năng và thẩm mỹ. Tông màu gỗ ấm, vải mềm, ánh sáng vàng.",
             featured=False),

        # ---- PHÒNG NGỦ CƠ BẢN ----
        dict(title="Phòng ngủ cơ bản nhựa rỗng — nhà chị Phương, Gio Linh",
             category="giuong", material="nhua-rong", segment="nhom-a",
             location="Gio Linh",
             image="ngu-cb_01.jpg",
             summary="Combo phòng ngủ tiết kiệm: giường + tủ đầu giường + tủ áo, dưới 50tr.",
             description="Giải pháp phòng ngủ kinh tế nhưng đầy đủ tiện nghi. Nhựa rỗng bền đẹp, "
                         "không lo mối ẩm. Thiết kế gọn gàng phù hợp phòng nhỏ 10-15m².",
             featured=False),

        # ---- PHÒNG TRẺ EM ----
        dict(title="Phòng bé trai — tủ + bàn học liền khối, Đông Hà",
             category="phong-tre", material="nhua-rong", segment="nhom-a",
             location="TP. Đông Hà",
             image="ngu-tre_01.jpg",
             summary="Combo tủ quần áo + bàn học + kệ sách cho bé, an toàn, màu sắc vui tươi.",
             description="Thiết kế combo thông minh cho phòng bé: tủ quần áo, bàn học, kệ sách liền khối "
                         "tiết kiệm diện tích. Nhựa rỗng an toàn, không mùi, cạnh bo tròn chống va đập.",
             featured=True),
        dict(title="Phòng bé gái — giường tầng + bàn học, Triệu Phong",
             category="phong-tre", material="nhua-rong", segment="nhom-a",
             location="Triệu Phong",
             image="ngu-tre_02.jpg",
             summary="Giường tầng tiết kiệm diện tích + bàn học riêng cho bé gái, màu hồng pastel.",
             description="Giường tầng cho 2 bé — tiết kiệm tối đa diện tích phòng. Màu hồng pastel "
                         "vui tươi. Cầu thang có hộc kéo lưu trữ. Nhựa rỗng an toàn, không formaldehyde.",
             featured=False),

        # ---- TỦ ÁO ----
        dict(title="Tủ áo cánh lùa gỗ An Cường — phòng ngủ master",
             category="tu-ao", material="go-cong-nghiep", segment="nhom-b",
             location="Triệu Phong",
             image="tho_01.jpg",
             summary="Tủ áo kịch trần cánh lùa vân gỗ óc chó, tiết kiệm diện tích, sang trọng.",
             description="Tủ áo gỗ công nghiệp An Cường phủ Melamine vân óc chó, thiết kế kịch trần "
                         "tận dụng tối đa không gian lưu trữ. Cánh lùa ray giảm chấn êm, khoang đồ chia "
                         "khoa học cho cả vợ chồng.",
             featured=True),
        dict(title="Hệ tủ áo cánh mở nhựa rỗng — nhà chị Ngân, Đông Hà",
             category="tu-ao", material="nhua-rong", segment="nhom-a",
             location="TP. Đông Hà",
             image="tho_02.jpg",
             summary="Tủ áo nhựa rỗng cánh mở rộng 3m, khoang chia khoa học, chống ẩm tốt.",
             description="Hệ tủ áo nhựa rỗng rộng 3m — khoang treo dài, khoang gấp, ngăn kéo đủ đầy. "
                         "Cánh mở bản lề giảm chấn. Nhựa rỗng không lo cong vênh dù thời tiết nồm ẩm.",
             featured=True),
        dict(title="Kệ tivi + vách trang trí phòng khách — Gio Linh",
             category="phong-khach", material="nhua-rong", segment="nhom-a",
             location="Gio Linh",
             image="tho_03.jpg",
             summary="Kệ tivi treo kết hợp vách lam sóng, gọn gàng, hiện đại.",
             description="Phòng khách nhỏ được làm sang nhờ kệ tivi treo nhựa rỗng kết hợp vách lam sóng "
                         "ốp nền. Đèn hắt LED tạo chiều sâu. Giải pháp tối ưu chi phí cho gia đình trẻ.",
             featured=True),

        # ---- THIẾT KẾ 3D ----
        dict(title="Bản vẽ 3D tủ bếp chữ L — nhà chị Thảo, Đông Hà",
             category="thiet-ke-3d", material="nhua-rong", segment="nhom-a",
             location="TP. Đông Hà",
             image="thiet-ke-3d_01.jpg",
             summary="Bản vẽ 3D photoreal trước thi công — xem trước 100% trước khi chốt hợp đồng.",
             description="Homie dựng 3D theo đúng số đo thực tế căn bếp. Khách xem và yêu cầu chỉnh sửa "
                         "thoải mái trước khi chốt — không mất thêm phí. Render photoreal như ảnh thật.",
             featured=True),
        dict(title="Bản vẽ 3D phòng ngủ master — nhà anh Cường, Cam Lộ",
             category="thiet-ke-3d", material="go-cong-nghiep", segment="nhom-b",
             location="Cam Lộ",
             image="thiet-ke-3d_02.jpg",
             summary="Render 3D phòng ngủ master phong cách luxury — phối màu, vật liệu rõ ràng.",
             description="Bản vẽ 3D phòng ngủ master thể hiện đầy đủ màu sắc, vật liệu, bố cục. "
                         "Giúp gia chủ tự tin chốt thiết kế trước khi thi công.",
             featured=False),

        # ---- TRỌN GÓI ----
        dict(title="Nội thất trọn gói căn nhà 2 tầng — anh Tài, Cam Lộ",
             category="tron-goi", material="go-cong-nghiep", segment="nhom-b",
             location="Cam Lộ",
             image="ngu_04.jpg",
             summary="Trọn gói từ bếp, phòng khách tới 3 phòng ngủ, đồng bộ phong cách hiện đại.",
             description="Dự án trọn gói: Homie đồng hành từ bản vẽ 3D tới thi công lắp đặt. Đồng bộ "
                         "phong cách hiện đại ấm cúng cho toàn bộ căn nhà 2 tầng, bàn giao đúng hẹn dọn nhà.",
             featured=True),
    ]

    for p in projects:
        db.session.add(Project(**p))

    articles = [
        dict(slug="nhua-rong-hay-go-cong-nghiep",
             title="Nhựa rỗng hay gỗ công nghiệp? Chọn sao cho đúng nhà bạn",
             category="kien-thuc",
             cover="bep_02.jpg",
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
             cover="tho_01.jpg",
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
        dict(slug="xu-huong-noi-that-2026",
             title="Xu hướng nội thất 2026: tối giản ấm cúng & vật liệu thân thiện",
             category="xu-huong",
             cover="ngu_01.jpg",
             excerpt="Năm 2026 lên ngôi phong cách tối giản nhưng ấm, tông màu gỗ tự nhiên kết hợp xanh - kem. Cùng Homie điểm qua.",
             body="""
<p>Nội thất 2026 không còn chạy theo cầu kỳ. Xu hướng nổi bật:</p>
<ul>
<li><b>Tối giản ấm cúng (Japandi):</b> ít chi tiết, nhiều gỗ tự nhiên, cảm giác thư giãn.</li>
<li><b>Bảng màu 60-30-10:</b> 60% màu nền trung tính, 30% màu gỗ/kem, 10% màu nhấn (xanh rêu, terracotta).</li>
<li><b>Ánh sáng 3 lớp:</b> đèn trần + đèn hắt + đèn điểm tạo chiều sâu, ấm áp.</li>
<li><b>Vật liệu thân thiện, chống ẩm:</b> ưu tiên bền - dễ vệ sinh thay vì chỉ đẹp bề mặt.</li>
</ul>
<p>Bạn đang xây hoặc sửa nhà và muốn đi theo xu hướng này? Để Homie tư vấn phối màu - chọn vật liệu miễn phí.</p>
""",
             featured=True),
    ]

    for a in articles:
        db.session.add(Article(**a))

    db.session.commit()
    print(f"Đã nạp: {len(projects)} dự án, {len(articles)} bài viết.")
