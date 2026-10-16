"""Build the Vol42 calendar-notes (六曜・選日) divination reference master pack."""

from __future__ import annotations

from build_divination_expansion import build_pack
from build_divination_traditions import named


CALENDAR_NOTES_SECTIONS = [
    ("Foundations", "基礎", [
        ("calendar_notes", "暦注", "Calendar Notes", "暦日に吉凶・行事・禁忌などの注記を付ける日本の民間暦の伝統"),
        ("rokuyo", "六曜", "Rokuyo", "旧暦の月日から六種の日を循環させて割り当てる暦注"),
        ("senjitsu", "選日", "Selected Days", "干支・節月・旧暦などの組合せから特定の日を選び出す暦注群"),
        ("lunisolar_calendar", "旧暦", "Lunisolar Calendar", "朔を月初とし節気で閏月を調整する太陰太陽暦"),
        ("sexagenary_day", "日干支", "Sexagenary Day", "十干十二支の六十日周期で各日に割り当てる干支"),
        ("solar_term_month", "節月", "Solar-Term Month", "二十四節気の節入りで区切る月の単位"),
        ("almanac_registers", "上段・中段・下段", "Almanac Registers", "暦本で暦注を記載位置により三段に分ける慣行"),
        ("popular_almanac", "民間暦", "Popular Almanac", "官暦とは別に民間で作られ暦注を伝えてきた暦本"),
        ("method_declaration", "方式宣言", "Method Declaration", "採用した暦・変換表・選日規則・流派を明示すること"),
        ("calculation_trace", "暦注算出追跡", "Calendar-Note Calculation Trace", "対象日から旧暦・干支・節月を経て暦注を得る経路を保存すること"),
    ]),
    ("Six Days", "六曜", named([
        ("sensho", "先勝", "Sensho"), ("tomobiki", "友引", "Tomobiki"),
        ("senbu", "先負", "Senbu"), ("butsumetsu", "仏滅", "Butsumetsu"),
        ("taian", "大安", "Taian"), ("shakko", "赤口", "Shakko"),
    ], "六曜の{name}に割り当てられる時間帯や吉凶の言い伝え")),
    ("Rokuyo Rules", "六曜の規則", [
        ("rokuyo_formula", "六曜算出式", "Rokuyo Formula", "旧暦の月と日の和を六で割った余りから六曜を求める規則"),
        ("month_start_rokuyo", "月初六曜", "Month-Start Rokuyo", "旧暦の各月朔日に固定される六曜の配当"),
        ("rokuyo_sequence", "六曜循環", "Rokuyo Sequence", "先勝から赤口までを日ごとに順に巡らせる配列"),
        ("new_moon_reset", "朔日切替", "New-Moon Reset", "旧暦の月が替わると六曜の循環が途中で切り替わること"),
        ("leap_month_rokuyo", "閏月六曜", "Leap-Month Rokuyo", "閏月を前月と同じ月番号として扱う六曜の規則"),
        ("rokuyo_time_slots", "六曜時間帯", "Rokuyo Time Slots", "午前・正午・午後などで吉凶が分かれるとする言い伝え"),
        ("rokuyo_origin", "小六壬起源説", "Xiao Liu Ren Origin", "中国の時刻占いである小六壬を六曜の源流とみる説"),
        ("rokuyo_name_variants", "六曜名称異同", "Rokuyo Name Variants", "六曜の名称・読み・順序に見られる時代や地域の違い"),
    ]),
    ("Auspicious Selected Days", "吉日系選日", named([
        ("ichiryu_manbai", "一粒万倍日", "Ichiryu Manbai Day"), ("tensha", "天赦日", "Tensha Day"),
        ("tora_no_hi", "寅の日", "Day of the Tiger"), ("mi_no_hi", "巳の日", "Day of the Snake"),
        ("tsuchinoto_mi", "己巳の日", "Tsuchinoto-Mi Day"), ("kinoe_ne", "甲子の日", "Kinoe-Ne Day"),
        ("tenon", "天恩日", "Ten'on Day"), ("boso", "母倉日", "Boso Day"),
        ("daimyo", "大明日", "Daimyo Day"), ("kamiyoshi", "神吉日", "Kamiyoshi Day"),
        ("gettoku", "月徳日", "Gettoku Day"), ("kishuku", "鬼宿日", "Kishuku Day"),
    ], "吉日とされる選日の{name}に割り当てられる算出規則と言い伝え")),
    ("Caution Selected Days", "注意日系選日", named([
        ("fujoju", "不成就日", "Fujoju Day"), ("sanrinbo", "三隣亡", "Sanrinbo Day"),
        ("jippogure", "十方暮", "Jippogure Period"), ("happen", "八専", "Happen Period"),
        ("tenichi_tenjo", "天一天上", "Ten'ichi Tenjo Period"), ("jushi", "受死日", "Jushi Day"),
        ("jisshi", "十死日", "Jisshi Day"), ("kiko", "帰忌日", "Kiko Day"),
        ("chiimi", "血忌日", "Chiimi Day"), ("oumou", "往亡日", "Oumou Day"),
        ("juu", "重日", "Juu Day"), ("fuku", "復日", "Fuku Day"),
    ], "注意日とされる選日の{name}に割り当てられる算出規則と言い伝え")),
    ("Twelve Directives", "十二直", named([
        ("tatsu", "建", "Tatsu"), ("nozoku", "除", "Nozoku"),
        ("mitsu", "満", "Mitsu"), ("tairu", "平", "Tairu"),
        ("sadan", "定", "Sadan"), ("toru", "執", "Toru"),
        ("yaburu", "破", "Yaburu"), ("ayabu", "危", "Ayabu"),
        ("naru", "成", "Naru"), ("osamu", "納", "Osamu"),
        ("hiraku", "開", "Hiraku"), ("tozu", "閉", "Tozu"),
    ], "中段の十二直の{name}に割り当てられる伝統的分類")),
    ("Seasonal Days", "雑節", named([
        ("setsubun", "節分", "Setsubun"), ("higan", "彼岸", "Higan"),
        ("shanichi", "社日", "Shanichi"), ("hachiju_hachiya", "八十八夜", "Hachiju-Hachiya"),
        ("nyubai", "入梅", "Nyubai"), ("hangesho", "半夏生", "Hangesho"),
        ("doyo", "土用", "Doyo"), ("nihyaku_toka", "二百十日", "Nihyaku-Toka"),
        ("nihyaku_hatsuka", "二百二十日", "Nihyaku-Hatsuka"),
    ], "雑節の{name}に割り当てられる季節の目安と暦上の扱い")),
    ("Calculation and Tables", "計算と暦表", [
        ("lunar_conversion_table", "旧暦変換表", "Lunar Conversion Table", "新暦日付を旧暦の年月日と閏月へ対応させる表"),
        ("new_moon_calculation", "朔計算", "New-Moon Calculation", "天文計算で朔の日時を求め旧暦の月初を定めること"),
        ("solar_term_calculation", "節気計算", "Solar-Term Calculation", "太陽黄経から二十四節気の日時を求めること"),
        ("sexagenary_table", "干支暦表", "Sexagenary Table", "各日の日干支を連続して割り当てる表"),
        ("day_boundary", "日界", "Day Boundary", "一日の切替時刻を明示すること"),
        ("reference_time", "基準時刻", "Reference Time", "日本標準時など朔や節気の判定に用いる時刻基準"),
        ("table_range", "暦表対象期間", "Table Range", "変換表が有効な期間と範囲外の扱いを明示すること"),
        ("almanac_source", "暦表出典", "Almanac Source", "変換表や選日規則の出典を記録すること"),
        ("table_version", "暦表版管理", "Table Version", "暦表・規則表の版を結果とともに保持すること"),
        ("cross_check", "暦照合", "Cross-Check", "算出結果を公刊の暦と照合して検証すること"),
        ("calculation_reproducibility", "計算再現性", "Calculation Reproducibility", "同じ入力と規則から同じ暦注を再生成できること"),
    ]),
    ("Culture and History", "文化と歴史", [
        ("edo_almanac", "江戸期暦注", "Edo-Period Almanac Notes", "江戸時代の暦本に多様な暦注が記載された歴史"),
        ("meiji_reform", "明治改暦", "Meiji Calendar Reform", "太陽暦への改暦と官暦から暦注が除かれた経緯"),
        ("postwar_spread", "戦後の六曜普及", "Postwar Spread of Rokuyo", "戦後のカレンダーや手帳で六曜が広く印刷されるようになった経緯"),
        ("wedding_custom", "婚礼日取り慣習", "Wedding-Date Custom", "大安などを婚礼の日取りに参照してきた慣習"),
        ("funeral_custom", "友引葬儀慣習", "Tomobiki Funeral Custom", "友引に葬儀を避ける慣習と火葬場休業の例"),
        ("construction_custom", "建築慣習", "Construction Custom", "上棟などの日取りに暦注を参照してきた慣習"),
        ("business_custom", "開業慣習", "Business-Opening Custom", "開業・財布の新調などに吉日を参照する慣習"),
        ("regional_variation", "地域差", "Regional Variation", "暦注の重視度や解釈が地域によって異なること"),
        ("superstition_critique", "迷信批判", "Superstition Critique", "六曜などを根拠のない迷信として扱う行政・人権啓発の立場"),
        ("modern_entertainment", "現代の娯楽的利用", "Modern Entertainment Use", "暦注を話題や遊びとして気軽に楽しむ現代的な使われ方"),
    ]),
    ("Safety and Limits", "安全と限界", [
        ("tradition_label", "伝承表示", "Tradition Label", "暦注が民間の伝承であり事実の予測ではないことを表示すること"),
        ("no_fatalism", "宿命論回避", "Avoid Fatalism", "仏滅や注意日を不可避の災いとして表示しないこと"),
        ("no_disaster_prediction", "災害予測禁止", "No Disaster Prediction", "暦注から事故や災害を予測しないこと"),
        ("no_ceremony_pressure", "日取り強要禁止", "No Ceremony Pressure", "冠婚葬祭や行事の日取りを暦注で強制・誘導しないこと"),
        ("no_financial_decision", "金融判断禁止", "No Financial Decision", "投資・契約・購入の判断に暦注を使用しないこと"),
        ("no_health_claim", "健康判断禁止", "No Health Claim", "血忌日などを医療・受診の判断に用いないこと"),
        ("anti_discrimination", "差別助長防止", "Anti-Discrimination", "暦注を理由に人や行事を排除・差別する表現をしないこと"),
        ("gentle_framing", "穏当な表現", "Gentle Framing", "注意日を伝える場合も不安を煽らず軽い話題として扱うこと"),
        ("user_opt_out", "本人選択", "User Opt-Out", "暦注の表示有無と表示範囲を本人が選べるようにすること"),
        ("high_impact_exclusion", "高影響利用禁止", "High-Impact Exclusion", "雇用・教育・保険・信用等に利用しないこと"),
    ]),
]


CALENDAR_NOTES_CONFIG = {
    "prefix": "KOY",
    "knowledge_type": "calendar_notes",
    "category": "Calendar Notes",
    "category_tag": "CAT:暦注",
    "label": "暦注",
    "tradition": "日本の暦注・六曜・選日",
    "source_type": "対象日・旧暦・日干支・節月",
    "required_inputs": ["対象日", "使用暦", "旧暦変換表", "干支暦表", "節月規則", "流派"],
    "calculation_basis": "対象日を旧暦・日干支・節月へ変換し六曜・選日・十二直等の規則表に当てはめる",
    "provenance": "中国の暦注・小六壬等に由来し江戸期以降の日本の民間暦で広まった六曜・選日の諸伝承",
    "related": ["文化的象徴", "生活習慣", "解釈不確実性"],
    "observable_data": ["対象日", "採用した暦・変換表・流派", "暦表の対象期間と欠測", "規則表で得られた暦注"],
    "signal_candidates": ["対象日と規則から再現可能な暦注を得る", "暦注を娯楽・話題の候補として示し行動の指示や予測へ短絡させない"],
    "device_level": "日付のみを入力とし出生情報を必要としない。高影響判断・診断・能力評価には利用しない",
    "modifiers": ["流派", "地域と時代", "暦と時間規則", "暦表の範囲", "解釈目的"],
    "trait_links": ["意思決定", "価値観", "生活習慣"],
    "output_dir": "vol42_calendar_notes/calendar_notes_001_100",
    "index_filename": "calendar_notes_001_100_index.yml",
    "master_filename": "vol42_calendar_notes_001_100.json",
}


def main():
    build_pack(CALENDAR_NOTES_CONFIG, CALENDAR_NOTES_SECTIONS)


if __name__ == "__main__":
    main()
