# -*- coding: utf-8 -*-
"""Nạp dữ liệu dự án THẬT cho website Homie — ảnh từ D:\HINH ANH\THI CONG\CHUNG TRON GOI"""


def run_seed(db, Project, Article, force_articles=False):
    already = Project.query.first() or Article.query.first()
    if already and not force_articles:
        return  # Đã có dữ liệu, bỏ qua (trừ khi cố tình làm mới bài viết)

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

    if not already:
        for p in projects:
            db.session.add(Project(**p))

    articles = [
        dict(slug="nhua-rong-hay-go-cong-nghiep",
             title="Nhựa hay gỗ công nghiệp: cuộc chiến thật sự nằm ở mép cạnh, không phải bề mặt",
             category="kien-thuc",
             cover="tc_chii-nga_01.jpg",
             excerpt="Người ta hay cãi nhau nhựa với gỗ cái nào bền hơn. Nhưng nước không tấn công vào giữa tấm ván — nó tìm đúng chỗ yếu nhất để ngấm. Hiểu chỗ đó, bạn sẽ chọn đúng mà không tốn thêm một đồng.",
             body="""
<p>Gần như nhà nào cũng dừng lại rất lâu ở câu hỏi này: làm nhựa hay làm gỗ công nghiệp. Và gần
như ai tư vấn cũng trả lời theo kiểu so bề mặt — gỗ vân đẹp hơn, nhựa nhẹ hơn, gỗ sang hơn, nhựa
rẻ hơn. Nghe thì xuôi tai, nhưng đó không phải chỗ quyết định chiếc tủ của bạn sống được mấy năm.</p>

<p>Muốn chọn đúng, phải hiểu một điều: <b>hư hỏng của đồ gỗ công nghiệp gần như không bao giờ bắt
đầu từ giữa tấm ván</b>. Nó bắt đầu từ mép.</p>

<h3>Cốt gỗ là bột gỗ ép keo — và bột gỗ thì hút nước</h3>
<p>Một tấm MDF, dù là loại lõi xanh chống ẩm, bản chất vẫn là sợi gỗ nghiền nhỏ ép lại với keo. Bề
mặt được phủ một lớp melamine hoặc laminate kín nước, nên đổ nước lên mặt tủ lau khô là xong,
không sao cả. Vấn đề là bốn cái mép. Ở mép cắt, cái lõi bột gỗ đó lộ ra, và người thợ phải dán một
dải cạnh (nẹp chỉ) để bịt lại. Nếu dải cạnh này dán hở, bong keo, hoặc thợ bỏ qua cái cạnh khuất
phía trong vì "ai nhìn thấy đâu" — thì đó chính là cái miệng để hơi ẩm và nước chui vào.</p>

<p>Khi nước ngấm được vào lõi, sợi gỗ nở ra. Và đây là điểm cốt tử: <b>gỗ đã trương nở thì không co
lại như cũ</b>. Chân tủ phồng lên, cạnh sùi ra, cửa xệ xuống không đóng khít nữa. Không có cách sửa,
chỉ có thay. Đây là lý do những chiếc tủ bếp hỏng đầu tiên luôn là khoang dưới bồn rửa và khoang
sát nền — nơi hơi nước quẩn quanh cả ngày.</p>

<h3>Nhựa không thắng vì "tốt hơn", nó thắng vì không có gì để nước phá</h3>
<p>Tấm nhựa (thường là PVC dạng foam, hay gọi picomat) không có sợi gỗ bên trong. Không có sợi gỗ
thì không có gì để trương nở. Bạn có ngâm nó, nó cũng chỉ ướt rồi khô, hình dạng không đổi. Đổi lại,
nhựa mềm hơn gỗ, bắt vít không "ăn" chắc bằng, và bề mặt vân không thật và ấm bằng gỗ khi sờ tay.</p>

<p>Vậy nên cách chọn khôn ngoan không phải chọn một loại cho cả nhà, mà là <b>đặt đúng vật liệu vào
đúng chỗ nó phải chịu đựng</b>. Chỗ nào tiếp xúc nước trực tiếp và thường xuyên — thùng tủ bếp,
đặc biệt khoang dưới chậu rửa, tủ dưới lavabo phòng tắm, chân tủ kịch sàn — để nhựa. Chỗ khô ráo mà
mắt nhìn vào mỗi ngày và tay chạm mỗi ngày — cánh tủ, kệ tivi, tủ áo, giường — để gỗ công nghiệp
cho được cái vân, cái ấm, cái chắc tay.</p>

<p>Một căn bếp làm đúng thường là thùng nhựa, cánh gỗ. Nhìn ngoài y hệt tủ gỗ nguyên khối, nhưng
cái phần âm thầm hứng nước suốt mười năm thì không bao giờ phồng. Người không biết sẽ tưởng hai
bên báo giá chênh nhau là do ăn bớt. Thật ra chênh nhau là ở chỗ có ai chịu nghĩ đến bốn cái mép hay
không.</p>
""",
             featured=True),

        dict(slug="kinh-nghiem-chong-non-am-mien-trung",
             title="Vì sao đồ gỗ ở miền Trung hỏng nhanh hơn nơi khác — và nó hỏng từ đâu",
             category="kinh-nghiem",
             cover="tc_kiem-anh_01.jpg",
             excerpt="Không phải cứ mưa nhiều là đồ mau hỏng. Thứ âm thầm giết đồ gỗ là những ngày nồm — khi tường 'đổ mồ hôi' và hơi ẩm len vào những khe bạn không bao giờ nhìn thấy.",
             body="""
<p>Người sống ở Quảng Trị đều quen cảnh này: mấy ngày trời nồm, sàn nhà nhớp nháp, tường rịn nước,
lau mãi không khô. Nhiều người nghĩ mùa mưa bão mới là lúc hại nhà. Thật ra bão thổi qua rồi thôi,
còn cái làm hỏng đồ đạc từ từ, năm này qua năm khác, lại là những ngày nồm lặng lẽ đó.</p>

<h3>Ẩm không tấn công từ ngoài vào, nó ngưng tụ từ trong khe</h3>
<p>Khi không khí ẩm gần như bão hòa gặp bề mặt mát hơn — mặt sau tủ áp vào tường, đáy tủ sát nền
gạch — hơi nước trong không khí ngưng lại thành giọt li ti ngay tại đó. Cái mặt tủ bạn nhìn thấy thì
khô, nhưng cái lưng tủ và chân tủ khuất phía trong thì ẩm ướt âm ỉ suốt mấy ngày. Đây là lý do một
chiếc tủ có thể mục ruỗng từ phía sau trong khi mặt trước vẫn còn như mới.</p>

<p>Hiểu được cơ chế này thì cách phòng cũng rõ ra, và nó không nằm ở chuyện "mua đồ xịn hơn":</p>

<p><b>Đừng cho tủ áp lì vào tường và kịch xuống nền.</b> Một khe hở dù chỉ một hai phân sau lưng tủ và
dưới chân tủ đủ để không khí lùa qua, không cho hơi nước đọng lại một chỗ. Tủ kê chân cao vài phân
bền hơn hẳn tủ ốp sát sàn, dù nhìn tủ kịch sàn có vẻ "kín đáo sạch sẽ" hơn.</p>

<p><b>Cạnh phải được dán kín cả những cạnh khuất.</b> Như đã nói, ẩm tìm đúng chỗ lõi gỗ hở ra để chui
vào. Cái cạnh phía trong, phía dưới, phía sau — chỗ khách không nhìn tới — lại chính là chỗ ẩm tấn công
đầu tiên. Thợ làm kỹ là thợ dán kín cả những cạnh chẳng ai soi.</p>

<p><b>Phụ kiện kim loại phải là loại không gỉ.</b> Bản lề, ray trượt bằng thép rẻ tiền gặp không khí ẩm là
chớm gỉ, rồi kẹt, rồi kêu. Chi tiết này nhỏ nhưng là thứ bạn chạm tay vào mỗi ngày, và hỏng nó thì
khó chịu hơn nhiều so với một vết xước trên mặt tủ.</p>

<p>Cuối cùng, có một sự thật ít người nói: cùng một tấm ván, cùng một bộ phụ kiện, thợ này làm bền
mười năm, thợ kia hai năm đã lung lay. Phần lớn tuổi thọ của đồ gỗ nằm ở tay người ráp nó, ở chỗ họ
có chịu bịt kín từng cái khe, chừa từng cái khe thở hay không — chứ không chỉ ở cái tem vật liệu dán
bên ngoài.</p>
""",
             featured=True),

        dict(slug="tai-sao-chon-homie",
             title="Vì sao báo giá rẻ hơn lại thành đắt hơn — đọc một bảng báo giá nội thất cho đúng",
             category="kinh-nghiem",
             cover="tc_tinh_01.jpg",
             excerpt="Hai bảng báo giá cùng một căn nhà chênh nhau vài chục triệu. Chỗ chênh đó không phải lãi của người ta ăn dày hơn — nó thường nằm ở những dòng bị cố tình bỏ trống.",
             body="""
<p>Cảnh này lặp lại với hầu hết gia chủ: xin ba bốn nơi báo giá cho cùng một căn nhà, cầm về so, thấy
chênh nhau vài chục triệu, rồi phân vân. Bên rẻ thì sợ làm ẩu, bên đắt thì tiếc tiền. Và cái bẫy lớn nhất
là mặc định rằng cùng một hạng mục thì bên nào rẻ hơn là bên đó tử tế hơn, ít ăn lãi hơn.</p>

<p>Thực tế thường ngược lại. Chênh lệch trong một bảng báo giá nội thất phần lớn không nằm ở phần
lãi, mà nằm ở <b>những thứ được ghi ra và những thứ được lặng lẽ bỏ đi</b>.</p>

<h3>Cùng chữ "tủ bếp" nhưng bên trong là hai thứ khác nhau</h3>
<p>Một dòng ghi "tủ bếp — X triệu/mét dài" nghe thì giống nhau, nhưng nó có thể là thùng nhựa hoặc
thùng gỗ thường; cạnh dán chỉ mỏng hay chỉ dày; bản lề ray là hàng phổ thông hay loại giảm chấn có
thương hiệu; mặt đá là loại nào, dày bao nhiêu. Mỗi lựa chọn thấp xuống một bậc là bảng giá nhẹ đi
một chút. Cộng lại thành vài chục triệu. Người báo giá rẻ không nói dối — họ chỉ chọn giúp bạn phương
án rẻ nhất ở mọi dòng, rồi để bạn tự phát hiện ra khi đã ở vào nhà.</p>

<h3>Ba câu hỏi làm lộ ra sự thật của một bảng báo giá</h3>
<p><b>Thứ nhất, hỏi bảng bóc tách chi tiết (BOQ).</b> Một đơn vị làm thật sẽ đưa được bảng liệt kê từng
hạng mục: thùng vật liệu gì, cánh vật liệu gì, phụ kiện hãng nào, mặt đá loại nào, số lượng bao nhiêu.
Ai chỉ đưa một con số tổng tròn trịa mà ngại tách chi tiết, thường là vì tách ra sẽ lộ chỗ đã rút.</p>

<p><b>Thứ hai, hỏi cái gì không nằm trong giá này.</b> Đây là câu khiến "phát sinh" hết đường xuất hiện.
Điện nước đấu nối, tháo dỡ đồ cũ, vận chuyển lên tầng, xử lý tường ẩm... món nào không ghi trong hợp
đồng thì sau này đều là tiền thêm. Biết trước thì không bị bất ngờ giữa chừng, lúc đã lỡ dở không quay
lại được.</p>

<p><b>Thứ ba, xin xem công trình thật đã bàn giao vài năm.</b> Ảnh render lúc nào cũng đẹp. Nhưng một
căn bếp đã dùng ba năm mà cánh vẫn khít, chân tủ chưa phồng, bản lề chưa xệ — đó mới là bằng chứng
về cách người ta làm phần khuất, phần bạn không kiểm tra được lúc nhận nhà.</p>

<p>Chọn nhà thầu, xét cho cùng, là chọn người sẽ thay bạn quyết định hàng trăm chi tiết nhỏ mà bạn
không có mặt để giám sát. Một bảng báo giá dám ghi rõ mọi dòng là một lời cam kết rằng những chi tiết
đó sẽ được làm đúng như đã ghi. Đọc báo giá theo cách này, bạn sẽ thôi hỏi "bên nào rẻ nhất" và bắt đầu
hỏi "bên nào ghi rõ nhất".</p>
""",
             featured=True),

        dict(slug="6-phong-cach-noi-that-pho-bien",
             title="Chọn phong cách nội thất: đừng bắt đầu từ cái tên, hãy bắt đầu từ ánh sáng nhà bạn",
             category="kien-thuc",
             cover="tc_duong_01.jpg",
             excerpt="Cùng một bộ nội thất Japandi, đặt trong căn hướng Nam đầy nắng thì ấm áp, đặt trong căn thiếu sáng lại thành xám lạnh. Phong cách không quyết định căn nhà — điều kiện thật của căn nhà mới quyết định phong cách nào hợp.",
             body="""
<p>Người chuẩn bị làm nhà hay hỏi "nên làm phong cách gì" như thể đó là câu hỏi về gu thẩm mỹ. Rồi
lên mạng lưu về một bộ ảnh Indochine sang trọng, hay một căn Scandinavian trắng sáng, đưa cho thợ và
nói "em muốn như thế này". Vài tháng sau ở vào nhà, cảm giác không giống trong ảnh, mà không hiểu vì
sao. Lý do gần như luôn là một: <b>bức ảnh đó được chụp trong một căn nhà có điều kiện ánh sáng và
diện tích khác hẳn nhà bạn.</b></p>

<h3>Phong cách là hệ quả của ánh sáng và diện tích, không phải nguyên nhân</h3>
<p>Một phong cách nhiều gỗ trầm và màu tối như Indochine hay Luxury cần rất nhiều ánh sáng để "đỡ"
lại, nếu không cả phòng sẽ nặng và tối. Nó hợp với nhà rộng, trần cao, cửa lớn đón nắng. Đặt cùng bảng
màu ấy vào một căn nhà ống hẹp, thiếu sáng, bạn sẽ có một không gian bí và u ám dù từng món đồ đều
đẹp.</p>

<p>Ngược lại, những phong cách gỗ sáng — Scandinavian, Japandi — sinh ra chính là để cứu những căn
thiếu nắng. Màu sáng phản xạ ánh sáng đi khắp phòng, làm căn nhà nhỏ nở ra và sáng lên. Đây là lý do
chúng hợp với chung cư và nhà phố hơn hẳn. Không phải vì chúng "hiện đại hơn", mà vì chúng ăn khớp
với điều kiện thật của phần lớn nhà Việt.</p>

<h3>Cách chọn ngược lại: đi từ nhà bạn ra, không đi từ ảnh vào</h3>
<p>Trước khi nghĩ đến tên phong cách, hãy đứng giữa căn phòng vào buổi trưa và nhìn xem nắng vào
tới đâu, sáng hay tối, rộng hay hẹp, trần cao hay thấp. Một căn nhiều nắng, trần cao thì gần như phong
cách nào cũng "gánh" được, tha hồ chọn theo gu. Một căn thiếu sáng thì nên tránh màu trầm và đồ nặng
khối, ưu tiên gỗ sáng, màu nhạt, đồ chân thoáng để nhường lại ánh sáng cho không gian.</p>

<p>Còn về cảm giác bạn muốn — thư thái, ấm cúng hay sang trọng — thì có một mẹo đơn giản hơn mọi
thuật ngữ: đừng gửi cho người thiết kế những cái tên phong cách, hãy gửi vài bức ảnh nhà thật mà bạn
thấy "được", rồi nói rõ bạn thích điều gì trong đó. Từ vài bức ảnh và điều kiện thật của căn nhà, một
người có nghề sẽ dịch ra được bảng màu và bố cục hợp với bạn — thứ mà một cái nhãn phong cách chung
chung không bao giờ nói hết được.</p>
""",
             featured=True),

        dict(slug="kich-thuoc-chuan-noi-that",
             title="Vài centimet sai lệch và mười năm mỏi lưng: những con số làm nên căn bếp dễ chịu",
             category="kien-thuc",
             cover="bep_01.jpg",
             excerpt="Một chiếc tủ bếp đẹp mà cao sai năm phân sẽ hành hạ cái lưng bạn mỗi bữa cơm, suốt nhiều năm. Đây là lý do đằng sau những con số chuẩn — và câu hỏi mà người làm giỏi luôn hỏi trước khi cắt tấm ván đầu tiên.",
             body="""
<p>Có một kiểu hối tiếc rất lặng lẽ khi làm nhà: mọi thứ đều đẹp, khách tới ai cũng khen, mà người ở
trong nhà thì ngày nào cũng thấy hơi bất tiện một chút. Đứng rửa bát lâu là mỏi lưng. Với tay lên tủ bếp
trên phải kiễng chân. Mở cánh tủ đập vào góc bàn. Những cái "hơi hơi" đó cộng lại qua mười năm là rất
nhiều khó chịu, và gần như tất cả đều đến từ vài centimet đặt sai.</p>

<h3>Tại sao mặt bàn bếp cao sai năm phân lại hại lưng đến thế</h3>
<p>Khi bạn thái, rửa, nhào bột, hai tay làm việc ở mặt bàn còn cột sống thì phải giữ nguyên tư thế đó
hàng chục phút mỗi ngày. Mặt bàn quá thấp buộc bạn cúi khom; quá cao buộc bạn so vai rụt cổ. Cơ thể
chịu được vài phút, nhưng ngày nào cũng lặp thì thành đau lưng, đau vai mạn tính. Con số thường dùng
là mặt bàn bếp cao khoảng <b>80–90cm</b>, nhưng con số đúng phải tính theo người: lấy chiều cao người
nấu chính chia đôi rồi cộng thêm chừng 5–10cm. Người cao 1m50 và người cao 1m70 mà dùng chung
một chiều cao bàn thì kiểu gì cũng có một người khổ.</p>

<p>Cũng vì vậy mà khu rửa nên nhỉnh cao hơn khu bếp nấu một chút — vì khi rửa tay bạn hạ thấp hơn,
nâng bồn lên đỡ phải cúi. Còn tủ bếp trên thì treo cách mặt bàn khoảng <b>70–75cm</b> và sâu chừng
<b>30–35cm</b>: đủ để kê đồ và thao tác bên dưới mà không cụng đầu, không che khuất tầm với.</p>

<h3>Những con số nên nhớ, và một câu hỏi quan trọng hơn mọi con số</h3>
<p>Vài mốc để bạn hình dung: tủ áo thường cao <b>200–220cm</b>, sâu <b>60cm</b> mới treo được vai áo mà
không chạm cửa; thanh treo áo dài cần khoảng 90cm chiều cao, treo đầm dài cần tới 150–165cm. Giường
mặt nệm cao <b>45–50cm</b> là vừa tầm ngồi dậy; lối đi quanh giường chừa tối thiểu 60cm để không phải
lách. Bàn ăn tính mỗi người khoảng 60cm chiều ngang, nên bàn bốn người rơi vào tầm 1m2–1m4.</p>

<p>Nhưng con số nào cũng chỉ là điểm khởi đầu. Điều quan trọng hơn tất cả là câu hỏi mà nhiều nơi
quên hỏi: <b>ai là người dùng chính, cao bao nhiêu, thuận tay nào, có ai lớn tuổi hay trẻ nhỏ trong nhà
không.</b> Một căn bếp làm cho người vợ cao 1m55 phải khác một căn làm cho người chồng cao 1m75.
Đồ nội thất tốt không phải là đồ theo đúng số chuẩn trong sách, mà là đồ được chỉnh lệch đi vài phân
cho vừa đúng cái người sẽ sống với nó mỗi ngày.</p>
""",
             featured=False),

        dict(slug="anh-sang-3-lop-cho-ngoi-nha",
             title="Vì sao nhà đẹp trên bản vẽ mà ở vào lại thấy lạnh: câu chuyện của ánh sáng",
             category="kien-thuc",
             cover="tc_anh-tam_01.jpg",
             excerpt="Bạn đầu tư cả trăm triệu cho nội thất, rồi lắp mấy chục bóng downlight trắng cho 'sáng sủa'. Buổi tối ngồi vào, căn phòng sáng trưng mà không ấm — vì ánh sáng đã làm phẳng hết mọi chiều sâu bạn bỏ tiền ra tạo.",
             body="""
<p>Có một nghịch lý nhiều người gặp: bỏ rất nhiều tiền và tâm sức chọn từng món đồ, từng màu sơn,
từng đường vân gỗ, để rồi buổi tối bật đèn lên ngồi vào lại thấy căn phòng "sao đó", không giống cảm
giác trong bản vẽ 3D. Đồ vẫn là đồ đó, màu vẫn màu đó. Thứ khác đi là ánh sáng. Và ánh sáng, chứ
không phải đồ đạc, mới là thứ quyết định một căn phòng ấm hay lạnh.</p>

<h3>Một nguồn sáng phẳng sẽ xóa hết chiều sâu</h3>
<p>Cách làm phổ biến nhất — và cũng gây tiếc nuối nhất — là rải đều trần nhà một loạt đèn downlight
trắng rồi bật hết lên cho "sáng sủa". Vấn đề là khi mọi thứ được chiếu sáng đều như nhau từ trên xuống,
căn phòng mất hết bóng đổ, mà bóng đổ mới là thứ tạo ra chiều sâu. Kết quả là một không gian sáng
đều tăm tắp như phòng khám: nhìn rõ mọi thứ nhưng không có điểm dừng cho mắt, không có góc ấm để
ngồi. Ánh trắng lạnh 6500K càng đẩy cảm giác đó đi xa hơn, biến phòng khách thành nơi ta muốn làm
việc chứ không muốn nghỉ ngơi.</p>

<h3>Ba lớp ánh sáng, như cách một căn phòng thật vận hành</h3>
<p>Cách làm cho không gian sống lại là chia ánh sáng thành nhiều lớp, mỗi lớp một việc. Lớp nền phủ
đều cả phòng ở mức vừa phải, đủ để đi lại và sinh hoạt. Lớp làm việc rọi thẳng vào chỗ tay bạn cần —
dải đèn dưới tủ bếp trên soi xuống mặt thớt (vì đèn trần luôn bị chính người đứng nấu che bóng), đèn
soi gương, đèn đầu giường để đọc. Và lớp điểm nhấn — hắt trần, hắt kệ, rọi một bức tranh — không để
nhìn cho rõ mà để tạo những mảng sáng tối, cho căn phòng có chiều sâu và có nơi để mắt nghỉ.</p>

<p>Chọn màu ánh sáng cũng quan trọng ngang chọn vị trí. Phòng khách, phòng ngủ, bàn ăn nên dùng
ánh vàng ấm hoặc trung tính khoảng <b>3000–4000K</b> — đó là sắc sáng khiến da người hồng hào, gỗ ấm
lên, bữa cơm ngon mắt. Ánh trắng lạnh chỉ nên để dành cho chỗ cần soi kỹ như bàn làm việc, gương
trang điểm, tủ áo.</p>

<p>Và nếu làm được một việc thôi để nâng hẳn chất lượng sống, thì đó là lắp bộ điều chỉnh độ sáng
(dimmer) cho phòng khách và phòng ngủ. Cùng một bộ đèn, ban ngày vặn sáng để sinh hoạt, tối ăn cơm
hạ xuống cho ấm, khuya dịu hẳn còn một mảng sáng nhỏ để dễ ngủ. Một căn phòng có thể "đổi tâm
trạng" theo giờ như thế mới thật sự là nơi để sống, chứ không chỉ để nhìn.</p>
""",
             featured=False),

        dict(slug="5-hang-muc-nen-dau-tu",
             title="Tiền nên dồn vào chỗ khó sửa, tiết kiệm ở chỗ dễ thay — một cách chia ngân sách ít ai chỉ",
             category="kinh-nghiem",
             cover="tc_kiem-anh_01.jpg",
             excerpt="Ngân sách làm nhà lúc nào cũng thiếu, nên ai cũng phải cắt chỗ này bù chỗ kia. Vấn đề là hầu hết người ta cắt nhầm chỗ: tiết kiệm ở những thứ sau này phải đục tường ra mới sửa được.",
             body="""
<p>Không mấy ai làm nhà mà ngân sách dư dả. Đến một lúc, bảng dự toán vượt túi tiền, và bạn buộc phải
ngồi xuống gạch bớt. Đây là khoảnh khắc quyết định căn nhà mười năm tới dễ chịu hay đầy ấm ức — bởi
vì phần lớn người ta cắt sai chỗ. Họ cắt vào thứ đập vào mắt để giữ lại thứ dễ thấy, trong khi nguyên tắc
đúng thì ngược lại: <b>dồn tiền vào nơi sau này khó sửa, và mạnh dạn tiết kiệm ở nơi lúc nào thay cũng
được.</b></p>

<h3>Thước đo không phải đắt hay rẻ, mà là "sửa lại tốn bao nhiêu đau khổ"</h3>
<p>Một bộ rèm, một cái đèn trang trí, một tấm thảm, mấy món decor — nếu chán hoặc mua hụt tiền, năm
sau đổi cái khác, tháo ra lắp vào trong một buổi chiều, không ảnh hưởng gì đến phần còn lại của nhà. Đây
chính là chỗ nên tiết kiệm, mua vừa phải trước, nâng cấp dần sau.</p>

<p>Ngược lại, có những hạng mục mà làm rồi thì gần như dính chặt vào căn nhà. Muốn sửa phải đục,
phải tháo, phải dọn đồ đi ở tạm, tốn gấp nhiều lần số tiền đáng ra bỏ thêm lúc đầu — và phiền gấp trăm
lần. Đó là những chỗ đáng đầu tư ngay từ đầu:</p>

<p><b>Chống thấm phòng tắm và ban công.</b> Đây là hạng mục vô hình, nằm dưới lớp gạch, nên rất dễ bị
cắt để tiết kiệm. Nhưng khi nó hỏng, nước thấm xuống trần nhà dưới, loang tường, bong sơn — và để sửa
thì phải đục toàn bộ nền gạch lên làm lại. Vài triệu tiết kiệm lúc đầu đổi lấy vài chục triệu và cả tháng
xáo trộn về sau.</p>

<p><b>Hệ điện và vị trí đèn.</b> Dây điện đã đi âm trong tường, ổ cắm và đèn đã định vị, thì đổi một cái ổ
cắm sang chỗ khác cũng phải cắt tường. Nghĩ kỹ ngay từ đầu chỗ nào cần ổ, chỗ nào cần đèn, rẻ hơn
nhiều so với đục lại.</p>

<p><b>Phần khuất của bếp và tủ.</b> Cái thùng tủ hứng nước, bộ bản lề ray đóng mở mỗi ngày, mặt đá chịu
dao thớt — những thứ này hỏng là phải tháo cả mảng ra thay. Trong khi cái cánh tủ đẹp bên ngoài thì
lúc nào sơn lại, dán lại cũng được.</p>

<p><b>Sàn nhà.</b> Thứ cả nhà giẫm lên mỗi ngày, và thay nó nghĩa là khiêng hết đồ đạc ra ngoài. Làm tốt
một lần để yên tâm nhiều năm.</p>

<p>Có một điều nên cộng thêm vào danh sách này, đặc biệt với nhà có trẻ nhỏ hoặc người nhạy cảm: ưu
tiên sơn và keo có chỉ số phát thải thấp (thường ghi VOC thấp, có chứng chỉ xanh). Cái này không nhìn
thấy, không khoe được, nhưng là thứ cả nhà hít thở mỗi ngày trong nhiều năm — đúng kiểu đầu tư
"khó thấy mà đáng".</p>
""",
             featured=False),

        dict(slug="thi-cong-tron-goi-va-boq",
             title="Hai chữ 'trọn gói' và cái bẫy phát sinh: hiểu cho đúng để không ức giữa chừng",
             category="kinh-nghiem",
             cover="tc_chii-nga_01.jpg",
             excerpt="'Trọn gói' nghe như đã gồm tất cả, nên khi giữa chừng bị báo thêm tiền, gia chủ thấy như bị lừa. Thật ra phần lớn phát sinh không đến từ nhà thầu gian, mà từ một hiểu lầm ngay từ ngày ký.",
             body="""
<p>Ít có cảm giác nào khó chịu bằng chuyện đang làm nhà dở dang thì bị báo phát sinh. Tiền đã chuyển
gần hết, đồ đã tháo, không còn đường lùi, mà giờ nghe "cái này chưa có trong giá, anh chị bù thêm". Lúc
đó gia chủ nào cũng thấy như bị gài. Nhưng nếu bình tĩnh nhìn lại, phần lớn những cú phát sinh ấy không
sinh ra từ lòng tham của người thi công, mà từ hai chữ "trọn gói" bị mỗi bên hiểu một kiểu ngay từ ngày
đặt bút ký.</p>

<h3>"Trọn gói" không có nghĩa là "gồm mọi thứ trên đời"</h3>
<p>Với gia chủ, trọn gói dễ được hiểu là: đưa một cục tiền, xong, khỏi lo gì thêm. Với người làm nghề,
trọn gói có một nghĩa hẹp hơn nhiều: gồm trọn <b>đúng những hạng mục đã được liệt kê trong hợp đồng
và bảng bóc tách khối lượng</b> — thường gọi là BOQ. Cái gì có trong bảng đó thì đã nằm trong giá. Cái gì
không có trong bảng đó thì không, dù bạn tưởng đương nhiên nó phải có.</p>

<p>Chính khoảng cách giữa hai cách hiểu này là nơi phát sinh chui vào. Tháo dỡ và chở bỏ đồ cũ, đấu nối
lại điện nước, xử lý một mảng tường bị ẩm mốc lộ ra khi tháo tủ, nâng hạ đồ lên tầng cao không thang
máy — những việc này nếu không được ghi vào bảng thì đều là phần ngoài. Không phải vì ai gian, mà vì
nó thật sự chưa từng được tính vào con số ban đầu.</p>

<h3>Cách để không bao giờ bị bất ngờ về tiền</h3>
<p>Cái bảng BOQ chi tiết, vì vậy, không phải là thủ tục giấy tờ rườm rà — nó chính là tấm khiên bảo vệ
bạn. Càng liệt kê rõ từng món, từng vật liệu, từng số lượng, thì càng ít khoảng trống cho phát sinh xuất
hiện. Trước khi ký, nên hỏi thẳng một câu rất đáng giá: <b>"Những gì không nằm trong bảng này thì là
phát sinh, đúng không? Vậy có việc gì anh dự là sẽ cần mà chưa ghi vào đây không?"</b> Một người làm
đàng hoàng sẽ ngồi rà cùng bạn và chỉ ra trước, thay vì để dành đó rồi báo sau.</p>

<p>Và khi giữa chừng thật sự cần thay đổi — bạn đổi ý muốn dùng vật liệu tốt hơn, hay muốn thêm một
món — thì cách làm sạch sẽ là hai bên ký một phụ lục ghi rõ thêm gì, thêm bao nhiêu tiền, ngay tại thời
điểm đó, chứ không phải gộp hết vào cuối rồi tính một cục. Phát sinh không xấu; phát sinh không được
thống nhất trước mới xấu.</p>

<p>Nói cho cùng, giá trị thật của một đơn vị làm trọn gói không nằm ở chỗ họ hứa "bao trọn không thêm
đồng nào" — lời hứa đó thường là dấu hiệu của một bảng giá mập mờ. Nó nằm ở chỗ họ dám ghi rõ ranh
giới ngay từ đầu: đây là những gì tôi làm, đây là những gì chưa gồm. Sự minh bạch hơi mất lòng lúc ký
lại chính là thứ giữ cho hai bên còn nhìn mặt nhau vui vẻ vào ngày bàn giao.</p>
""",
             featured=False),
    ]

    if force_articles:
        # Làm mới nội dung 8 bài viết theo slug — KHÔNG đụng dự án, KHÔNG đụng bài tự thêm
        for a in articles:
            existing = Article.query.filter_by(slug=a["slug"]).first()
            if existing:
                for k, v in a.items():
                    setattr(existing, k, v)
            else:
                db.session.add(Article(**a))
    else:
        for a in articles:
            db.session.add(Article(**a))

    db.session.commit()
    print(f"Seed OK: {len(projects)} du an that, {len(articles)} bai viet"
          f"{' (force refresh)' if force_articles else ''}.")
