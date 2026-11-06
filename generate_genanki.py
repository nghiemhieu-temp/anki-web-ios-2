import genanki

def build_deck():
    output_path = r"C:\Users\nghie\.gemini\antigravity\scratch\anki-web-ios\Minna_no_Nihongo_Bai_3.apkg"

    # Define Model
    minna_model = genanki.Model(
        1607392319,
        'Minna Japanese Model',
        fields=[
            {'name': 'Expression'},
            {'name': 'Reading'},
            {'name': 'Romaji'},
            {'name': 'HanViet'},
            {'name': 'Meaning'},
            {'name': 'Note'},
            {'name': 'Lesson'},
        ],
        templates=[
            {
                'name': 'Card 1',
                'qfmt': "<div style='font-size:0.85rem; color:#94a3b8; margin-bottom:8px;'>{{Lesson}}</div><div style='font-size:2.2rem; font-weight:700;'>{{Expression}}</div>",
                'afmt': "<div style='font-size:0.85rem; color:#94a3b8; margin-bottom:6px;'>{{Lesson}}</div><div style='font-size:2rem; font-weight:700;'>{{Expression}}</div>{{#Reading}}<div style='color:#60a5fa; font-size:1.15rem; margin-top:4px;'>{{Reading}}</div>{{/Reading}}{{#Romaji}}<div style='color:#a78bfa; font-size:0.95rem;'>{{Romaji}}</div>{{/Romaji}}<hr style='margin:14px 0; border:none; border-top:1px dashed rgba(255,255,255,0.2);'>{{#HanViet}}<div style='color:#38bdf8; font-size:0.9rem; margin-bottom:4px;'>Hán Việt: <strong>{{HanViet}}</strong></div>{{/HanViet}}<div style='font-size:1.3rem; font-weight:600; color:#f8fafc; margin-bottom:6px;'>{{Meaning}}</div>{{#Note}}<div style='font-size:0.88rem; color:#cbd5e1; background:rgba(255,255,255,0.06); padding:8px 12px; border-radius:10px; margin-top:8px;'>{{Note}}</div>{{/Note}}",
            },
        ],
        css=".card { font-family: -apple-system, sans-serif; text-align: center; color: white; background-color: #1e293b; }"
    )

    # Define Deck
    minna_deck = genanki.Deck(
        2059392110,
        'Minna no Nihongo N5 - Bài 3'
    )

    # 41 Vocabularies of Lesson 3
    vocab_list = [
        ("ここ", "", "koko", "", "Chỗ này, ở đây", "💡 Đại từ chỉ nơi chốn ở gần người nói", "Minna no Nihongo N5 - Bài 3"),
        ("そこ", "", "soko", "", "Chỗ đó, ở đó", "💡 Đại từ chỉ nơi chốn ở gần người nghe", "Minna no Nihongo N5 - Bài 3"),
        ("あそこ", "", "asoko", "", "Chỗ kia, ở kia", "💡 Đại từ chỉ nơi chốn ở xa cả hai người", "Minna no Nihongo N5 - Bài 3"),
        ("どこ", "", "doko", "", "Ở đâu, chỗ nào", "💡 Từ để hỏi nơi chốn", "Minna no Nihongo N5 - Bài 3"),
        ("こちら", "", "kochira", "", "Phía này, đằng này, nơi này", "💡 Cách nói lịch sự của ここ", "Minna no Nihongo N5 - Bài 3"),
        ("そちら", "", "sochira", "", "Phía đó, đằng đó, nơi đó", "💡 Cách nói lịch sự của そこ", "Minna no Nihongo N5 - Bài 3"),
        ("あちら", "", "achira", "", "Phía kia, đằng kia, nơi kia", "💡 Cách nói lịch sự của あそこ", "Minna no Nihongo N5 - Bài 3"),
        ("どちら", "", "dochira", "", "Phía nào, đằng nào, ở đâu", "💡 Cách nói lịch sự của どこ", "Minna no Nihongo N5 - Bài 3"),
        ("教室", "きょうしつ", "kyoushitsu", "GIÁO THẤT", "Phòng học, lớp học", "💡 Giáo (dạy) + Thất (phòng)", "Minna no Nihongo N5 - Bài 3"),
        ("食堂", "しょくどう", "shokudou", "THỰC ĐƯỜNG", "Nhà ăn, căng tin", "💡 Thực (ăn) + Đường (nhà lớn)", "Minna no Nihongo N5 - Bài 3"),
        ("事務所", "じむしょ", "jimusho", "SỰ VỤ SỞ", "Văn phòng", "💡 Nơi làm việc, giải quyết sự vụ", "Minna no Nihongo N5 - Bài 3"),
        ("会議室", "かいぎしつ", "kaigishitsu", "HỘI NGHỊ THẤT", "Phòng họp", "💡 Hội nghị (họp) + Thất (phòng)", "Minna no Nihongo N5 - Bài 3"),
        ("受付", "うけつけ", "uketsuke", "THỤ PHÓ", "Quầy tiếp tân, bàn tiếp khách", "💡 Nơi tiếp nhận khách và thư từ", "Minna no Nihongo N5 - Bài 3"),
        ("ロビー", "", "robii", "", "Hành lang, tiền sảnh (Lobby)", "💡 Từ mượn tiếng Anh Lobby", "Minna no Nihongo N5 - Bài 3"),
        ("部屋", "へや", "heya", "BỘ ỐC", "Căn phòng", "💡 Ốc (nhà, phòng)", "Minna no Nihongo N5 - Bài 3"),
        ("トイレ", "", "toire", "", "Nhà vệ sinh (Toilet)", "💡 Ngoài ra còn dùng お手洗い (otearai)", "Minna no Nihongo N5 - Bài 3"),
        ("お手洗い", "おてあらい", "otearai", "THỦ TẨY", "Nhà vệ sinh, phòng vệ sinh", "💡 Cách nói lịch sự, nghĩa đen là nơi rửa tay", "Minna no Nihongo N5 - Bài 3"),
        ("階段", "かいだん", "kaidan", "GIAI ĐOẠN", "Cầu thang bộ", "💡 Giai (bậc) + Đoạn (đoạn)", "Minna no Nihongo N5 - Bài 3"),
        ("エレベーター", "", "erebeetaa", "", "Thang máy (Elevator)", "💡 Thang máy thẳng đứng", "Minna no Nihongo N5 - Bài 3"),
        ("エスカレーター", "", "esukareetaa", "", "Thang cuốn (Escalator)", "💡 Thang cuốn di chuyển liên tục", "Minna no Nihongo N5 - Bài 3"),
        ("お国", "おくに", "okuni", "QUỐC", "Đất nước, quốc gia (của bạn)", "💡 Thêm tiền tố お để thể hiện sự lịch sự", "Minna no Nihongo N5 - Bài 3"),
        ("会社", "かいしゃ", "kaisha", "HỘI XÃ", "Công ty", "💡 Phân biệt với 社員 (nhân viên công ty)", "Minna no Nihongo N5 - Bài 3"),
        ("うち", "", "uchi", "", "Nhà (của mình)", "💡 Ngoài ra còn có 家 (いえ)", "Minna no Nihongo N5 - Bài 3"),
        ("電話", "でんわ", "denwa", "ĐIỆN THOẠI", "Điện thoại, cuộc gọi", "💡 Điện (tia điện) + Thoại (nói chuyện)", "Minna no Nihongo N5 - Bài 3"),
        ("靴", "くつ", "kutsu", "NGOA", "Giày", "💡 Đồ mang ở chân", "Minna no Nihongo N5 - Bài 3"),
        ("ネクタイ", "", "nekutai", "", "Cà vạt (Necktie)", "💡 Từ mượn tiếng Anh", "Minna no Nihongo N5 - Bài 3"),
        ("ワイン", "", "wain", "", "Rượu vang (Wine)", "💡 Rượu vang nho", "Minna no Nihongo N5 - Bài 3"),
        ("たばこ", "", "tabako", "", "Thuốc lá", "💡 Hút thuốc: たばこをすいます", "Minna no Nihongo N5 - Bài 3"),
        ("売り場", "うりば", "uriba", "MẠI TRƯỜNG", "Quầy bán hàng", "💡 Mại (bán) + Trường (nơi chốn)", "Minna no Nihongo N5 - Bài 3"),
        ("地下", "ちか", "chika", "ĐỊA HẠ", "Dưới hầm, tầng hầm", "💡 Địa (đất) + Hạ (dưới)", "Minna no Nihongo N5 - Bài 3"),
        ("〜階", "〜かい / 〜がい", "~kai / ~gai", "GIAI", "Tầng ~", "💡 Đếm tầng lầu (ví dụ: 1階 = いっかい, 3階 = さんがい)", "Minna no Nihongo N5 - Bài 3"),
        ("〜円", "〜えん", "~en", "VIÊN", "Đồng Yên (tiền Nhật)", "💡 Đơn vị tiền tệ Nhật Bản", "Minna no Nihongo N5 - Bài 3"),
        ("いくら", "", "ikura", "", "Bao nhiêu tiền?", "💡 Từ để hỏi giá tiền: これは いくらですか", "Minna no Nihongo N5 - Bài 3"),
        ("百", "ひゃく", "hyaku", "BÁCH", "Một trăm (100)", "💡 300 = さんびゃく, 600 = ろっぴゃく, 800 = はっぴゃく", "Minna no Nihongo N5 - Bài 3"),
        ("千", "せん", "sen", "THIÊN", "Một nghìn (1.000)", "💡 3000 = さんぜん, 8000 = はっせん", "Minna no Nihongo N5 - Bài 3"),
        ("万", "まん", "man", "VẠN", "Mười nghìn (10.000)", "💡 Đơn vị đếm 4 số 0 của Nhật (1万 = 10.000)", "Minna no Nihongo N5 - Bài 3"),
        ("すみません", "", "sumimasen", "", "Xin lỗi / Cho tôi hỏi...", "💡 Dùng khi nhờ vả, gọi phục vụ hoặc xin lỗi", "Minna no Nihongo N5 - Bài 3"),
        ("〜でございます", "", "~de gozaimasu", "", "Là ~ (thể lịch sự của です)", "💡 Thường dùng bởi nhân viên bán hàng, tiếp tân", "Minna no Nihongo N5 - Bài 3"),
        ("見せてください", "みせてください", "misete kudasai", "KIẾN", "Xin cho tôi xem [~]", "💡 [Tên vật] を みせてください", "Minna no Nihongo N5 - Bài 3"),
        ("じゃ", "", "ja", "", "Vậy thì, thế thì...", "💡 Dùng khi đưa ra quyết định hoặc chuyển ý", "Minna no Nihongo N5 - Bài 3"),
        ("ください", "", "kudasai", "", "Xin cho tôi [~], lấy cho tôi [~]", "💡 これを ください (Cho tôi lấy cái này)", "Minna no Nihongo N5 - Bài 3")
    ]

    for expr, reading, romaji, hanviet, meaning, note, lesson in vocab_list:
        note = genanki.Note(
            model=minna_model,
            fields=[expr, reading, romaji, hanviet, meaning, note, lesson]
        )
        minna_deck.add_note(note)

    package = genanki.Package(minna_deck)
    package.write_to_file(output_path)
    print("Successfully built .apkg using genanki!")

if __name__ == "__main__":
    build_deck()
