import os
import json
import time
import uuid
import zlib
import sqlite3
import zipfile

def create_minna_bai_3_apkg(output_path):
    temp_db_path = output_path + ".tmp.db"
    if os.path.exists(temp_db_path):
        os.remove(temp_db_path)

    conn = sqlite3.connect(temp_db_path)
    cur = conn.cursor()

    cur.execute("""
    CREATE TABLE col (
        id              integer primary key,
        crt             integer not null,
        mod             integer not null,
        scm             integer not null,
        ver             integer not null,
        dty             integer not null,
        usn             integer not null,
        ls              integer not null,
        conf            text not null,
        models          text not null,
        decks           text not null,
        dconf           text not null,
        tags            text not null
    );
    """)

    cur.execute("""
    CREATE TABLE notes (
        id              integer primary key,
        guid            text not null,
        mid             integer not null,
        mod             integer not null,
        usn             integer not null,
        tags            text not null,
        flds            text not null,
        sfld            text not null,
        csum            integer not null,
        flags           integer not null,
        data            text not null
    );
    """)

    cur.execute("""
    CREATE TABLE cards (
        id              integer primary key,
        nid             integer not null,
        did             integer not null,
        ord             integer not null,
        mod             integer not null,
        usn             integer not null,
        type            integer not null,
        queue           integer not null,
        due             integer not null,
        ivl             integer not null,
        factor          integer not null,
        reps            integer not null,
        lapses          integer not null,
        left            integer not null,
        odue            integer not null,
        odid            integer not null,
        flags           integer not null,
        data            text not null
    );
    """)

    cur.execute("CREATE TABLE revlog (id integer primary key, cid integer not null, usn integer not null, ease integer not null, ivl integer not null, lastIvl integer not null, factor integer not null, time integer not null, type integer not null);")
    cur.execute("CREATE TABLE graves (usn integer not null, oid integer not null, type integer not null);")

    now = int(time.time())
    deck_id = 1718000003000
    model_id = 1718000003001

    deck_name = "Minna no Nihongo N5 - Bài 3"

    decks = {
        "1": {"id": 1, "mod": now, "name": "Default", "usn": 0, "desc": "", "collapsed": False},
        str(deck_id): {
            "id": deck_id,
            "mod": now,
            "name": deck_name,
            "usn": -1,
            "desc": "Từ vựng Minna no Nihongo N5 - Bài 3 đầy đủ Kanji, Hiragana, Romaji, Hán Việt và giải nghĩa chi tiết.",
            "collapsed": False
        }
    }

    # Full Anki NoteField schema including "sticky", "rtl", "font", "size", etc.
    def make_field(name, ord_idx):
        return {
            "name": name,
            "ord": ord_idx,
            "sticky": False,
            "rtl": False,
            "font": "Arial",
            "size": 20,
            "description": "",
            "plainText": False,
            "collapsed": False,
            "excludeFromSearch": False,
            "id": None,
            "tag": None,
            "preventDeletion": False
        }

    flds = [
        make_field("Expression", 0),
        make_field("Reading", 1),
        make_field("Romaji", 2),
        make_field("HanViet", 3),
        make_field("Meaning", 4),
        make_field("Note", 5),
        make_field("Lesson", 6)
    ]

    tmpls = [
        {
            "name": "Card 1",
            "ord": 0,
            "qfmt": "<div style='font-size:0.85rem; color:#94a3b8; margin-bottom:8px;'>{{Lesson}}</div><div style='font-size:2.2rem; font-weight:700;'>{{Expression}}</div>",
            "afmt": "<div style='font-size:0.85rem; color:#94a3b8; margin-bottom:6px;'>{{Lesson}}</div><div style='font-size:2rem; font-weight:700;'>{{Expression}}</div>{{#Reading}}<div style='color:#60a5fa; font-size:1.15rem; margin-top:4px;'>{{Reading}}</div>{{/Reading}}{{#Romaji}}<div style='color:#a78bfa; font-size:0.95rem;'>{{Romaji}}</div>{{/Romaji}}<hr style='margin:14px 0; border:none; border-top:1px dashed rgba(255,255,255,0.2);'>{{#HanViet}}<div style='color:#38bdf8; font-size:0.9rem; margin-bottom:4px;'>Hán Việt: <strong>{{HanViet}}</strong></div>{{/HanViet}}<div style='font-size:1.3rem; font-weight:600; color:#f8fafc; margin-bottom:6px;'>{{Meaning}}</div>{{#Note}}<div style='font-size:0.88rem; color:#cbd5e1; background:rgba(255,255,255,0.06); padding:8px 12px; border-radius:10px; margin-top:8px;'>{{Note}}</div>{{/Note}}",
            "bqfmt": "",
            "bafmt": "",
            "did": None,
            "bfont": "",
            "bsize": 0,
            "id": None
        }
    ]

    model = {
        str(model_id): {
            "id": model_id,
            "name": "Minna Japanese Model",
            "type": 0,
            "mod": now,
            "usn": -1,
            "sortf": 0,
            "did": deck_id,
            "tmpls": tmpls,
            "flds": flds,
            "css": ".card { font-family: -apple-system, sans-serif; text-align: center; color: white; background-color: #1e293b; }",
            "latexPre": "\\documentclass[12pt]{article}\n\\special{papersize=3in,5in}\n\\usepackage[utf8]{inputenc}\n\\usepackage{amssymb,amsmath}\n\\pagestyle{empty}\n\\setlength{\\parindent}{0in}\n\\begin{document}\n",
            "latexPost": "\\end{document}",
            "latexsvg": False,
            "req": [[0, "all", [0]]],
            "tags": [],
            "vers": []
        }
    }

    dconf = {
        "1": {
            "id": 1,
            "mod": now,
            "name": "Default",
            "usn": 0,
            "maxTaken": 60,
            "autoplay": True,
            "timer": 0,
            "replayq": True,
            "new": {"bury": False, "delays": [1.0, 10.0], "initialFactor": 2500, "ints": [1, 4, 0], "order": 1, "perDay": 20},
            "lapse": {"delays": [10.0], "leechAction": 1, "leechFails": 8, "minInt": 1, "mult": 0.0},
            "rev": {"bury": False, "ease4": 1.3, "ivlFct": 1.0, "maxIvl": 36500, "perDay": 200}
        }
    }

    conf = {
        "activeDecks": [1],
        "curDeck": 1,
        "newSpread": 0,
        "collapseTime": 1200,
        "timeLim": 0,
        "estTimes": True,
        "dueCounts": True,
        "curModel": None,
        "nextPos": 1
    }

    cur.execute("""
    INSERT INTO col VALUES (
        1, ?, ?, ?, 11, 0, 0, 0,
        ?, ?, ?, ?, '{}'
    )
    """, (now, now, now, json.dumps(conf), json.dumps(model), json.dumps(decks), json.dumps(dconf)))

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

    card_id_base = now * 1000
    for idx, (expr, reading, romaji, hanviet, meaning, note, lesson) in enumerate(vocab_list):
        note_id = card_id_base + (idx * 2)
        card_id = card_id_base + (idx * 2) + 1
        note_guid = str(uuid.uuid4())[:10]

        fields_str = "\x1f".join([expr, reading, romaji, hanviet, meaning, note, lesson])
        csum = zlib.crc32(expr.encode('utf-8')) & 0xffffffff

        cur.execute("""
        INSERT INTO notes VALUES (?, ?, ?, ?, -1, '', ?, ?, ?, 0, '')
        """, (note_id, note_guid, model_id, now, fields_str, expr, csum))

        cur.execute("""
        INSERT INTO cards VALUES (
            ?, ?, ?, 0, ?, -1, 0, 0, ?, 0, 2500, 0, 0, 0, 0, 0, 0, ''
        )
        """, (card_id, note_id, deck_id, now, idx + 1))

    conn.commit()
    conn.close()

    if os.path.exists(output_path):
        os.remove(output_path)

    with zipfile.ZipFile(output_path, 'w', zipfile.ZIP_DEFLATED) as z:
        z.write(temp_db_path, 'collection.anki2')
        z.writestr('media', '{}')

    os.remove(temp_db_path)
    print(f"Created {output_path} with full Anki schema successfully!")

if __name__ == "__main__":
    out = r"C:\Users\nghie\.gemini\antigravity\scratch\anki-web-ios\Minna_no_Nihongo_Bai_3.apkg"
    create_minna_bai_3_apkg(out)
