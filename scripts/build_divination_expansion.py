"""Build detailed Vol32-Vol34 divination reference master packs."""

from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
MASTER_ROOT = ROOT / "data" / "master_packs"


def entries(names, focus_template):
    return [
        (slug, name_ja, name_en, focus_template.format(name=name_ja))
        for slug, name_ja, name_en in names
    ]


WESTERN_SECTIONS = [
    ("Foundations", "基礎", [
        ("natal_astrology", "出生占星術", "Natal Astrology", "出生時点の天体配置を象徴体系として読む西洋占星術の領域"),
        ("tropical_zodiac", "トロピカル黄道", "Tropical Zodiac", "春分点を基準として黄道を十二等分する方式"),
        ("sidereal_zodiac", "サイデリアル黄道", "Sidereal Zodiac", "恒星基準の基点を用いて黄道を区分する方式"),
        ("ecliptic_longitude", "黄経", "Ecliptic Longitude", "黄道上の位置を角度で表す座標"),
        ("zodiac_sign", "サイン", "Zodiac Sign", "黄道を十二の30度区画として扱う分類"),
        ("planetary_function", "惑星機能", "Planetary Function", "天体ごとに割り当てられた伝統的象徴機能"),
        ("house_domain", "ハウス領域", "House Domain", "出生地点と時刻から区分される生活領域"),
        ("aspect_relation", "アスペクト関係", "Aspect Relation", "天体間の角距離を象徴的関係として扱うこと"),
        ("chart_context", "出生図文脈", "Chart Context", "単一配置を出生図全体の関係の中で読む原則"),
        ("school_declaration", "流派宣言", "School Declaration", "黄道・ハウス・許容度・支配星体系を明示すること"),
    ]),
    ("Zodiac Signs", "十二宮", entries([
        ("aries", "牡羊座", "Aries"), ("taurus", "牡牛座", "Taurus"),
        ("gemini", "双子座", "Gemini"), ("cancer", "蟹座", "Cancer"),
        ("leo", "獅子座", "Leo"), ("virgo", "乙女座", "Virgo"),
        ("libra", "天秤座", "Libra"), ("scorpio", "蠍座", "Scorpio"),
        ("sagittarius", "射手座", "Sagittarius"), ("capricorn", "山羊座", "Capricorn"),
        ("aquarius", "水瓶座", "Aquarius"), ("pisces", "魚座", "Pisces"),
    ], "{name}に対応づけられるエレメント・三区分・支配星・象徴テーマの組")),
    ("Planets", "天体", entries([
        ("sun", "太陽", "Sun"), ("moon", "月", "Moon"),
        ("mercury", "水星", "Mercury"), ("venus", "金星", "Venus"),
        ("mars", "火星", "Mars"), ("jupiter", "木星", "Jupiter"),
        ("saturn", "土星", "Saturn"), ("uranus", "天王星", "Uranus"),
        ("neptune", "海王星", "Neptune"), ("pluto", "冥王星", "Pluto"),
    ], "出生図で{name}に割り当てる伝統的または近現代的な象徴機能")),
    ("Houses", "ハウス", entries([
        ("first_house", "第1ハウス", "First House"), ("second_house", "第2ハウス", "Second House"),
        ("third_house", "第3ハウス", "Third House"), ("fourth_house", "第4ハウス", "Fourth House"),
        ("fifth_house", "第5ハウス", "Fifth House"), ("sixth_house", "第6ハウス", "Sixth House"),
        ("seventh_house", "第7ハウス", "Seventh House"), ("eighth_house", "第8ハウス", "Eighth House"),
        ("ninth_house", "第9ハウス", "Ninth House"), ("tenth_house", "第10ハウス", "Tenth House"),
        ("eleventh_house", "第11ハウス", "Eleventh House"), ("twelfth_house", "第12ハウス", "Twelfth House"),
    ], "{name}に割り当てられる伝統的な生活領域と経験テーマ")),
    ("Aspects", "アスペクト", [
        ("conjunction", "コンジャンクション", "Conjunction", "天体間の黄経差が0度付近となる関係"),
        ("opposition", "オポジション", "Opposition", "天体間の黄経差が180度付近となる関係"),
        ("trine", "トライン", "Trine", "天体間の黄経差が120度付近となる関係"),
        ("square", "スクエア", "Square", "天体間の黄経差が90度付近となる関係"),
        ("sextile", "セクスタイル", "Sextile", "天体間の黄経差が60度付近となる関係"),
        ("quincunx", "クインカンクス", "Quincunx", "天体間の黄経差が150度付近となる関係"),
        ("semisextile", "セミセクスタイル", "Semi-Sextile", "天体間の黄経差が30度付近となる関係"),
        ("semisquare", "セミスクエア", "Semi-Square", "天体間の黄経差が45度付近となる関係"),
        ("sesquiquadrate", "セスキコードレート", "Sesquiquadrate", "天体間の黄経差が135度付近となる関係"),
        ("aspect_orb", "オーブ", "Aspect Orb", "アスペクト成立に許容する角度幅"),
    ]),
    ("Essential Dignities", "品位", [
        ("domicile", "ドミサイル", "Domicile", "惑星が支配するサインに位置する伝統的品位"),
        ("detriment", "デトリメント", "Detriment", "支配サインの反対側に位置する伝統的状態"),
        ("exaltation", "エグザルテーション", "Exaltation", "惑星が高揚するとされるサイン上の品位"),
        ("fall", "フォール", "Fall", "高揚サインの反対側に位置する伝統的状態"),
        ("triplicity", "トリプリシティ", "Triplicity", "エレメント三区分にもとづく伝統的支配関係"),
        ("term", "ターム", "Term", "サイン内の度数区分にもとづく伝統的支配関係"),
        ("face", "フェイス", "Face", "デーカン区分にもとづく伝統的支配関係"),
        ("sect", "セクト", "Sect", "昼夜区分と惑星の所属を結びつける伝統的条件"),
    ]),
    ("Points and Motion", "感受点と運動", [
        ("ascendant", "アセンダント", "Ascendant", "東の地平線と黄道の交点"),
        ("midheaven", "ミッドヘブン", "Midheaven", "子午線上部と黄道の関係から得る主要感受点"),
        ("descendant", "ディセンダント", "Descendant", "西の地平線と黄道の交点"),
        ("imum_coeli", "イムム・コエリ", "Imum Coeli", "子午線下部と黄道の関係から得る主要感受点"),
        ("north_node", "ドラゴンヘッド", "North Node", "月の軌道が黄道を北向きに横切る交点"),
        ("south_node", "ドラゴンテイル", "South Node", "月の軌道が黄道を南向きに横切る交点"),
        ("part_of_fortune", "パート・オブ・フォーチュン", "Part of Fortune", "太陽・月・アセンダントから算出する伝統的感受点"),
        ("chiron", "キロン", "Chiron", "近現代占星術で使用される小天体の象徴"),
        ("vertex", "バーテックス", "Vertex", "プライム・バーティカルと黄道の交点として用いる感受点"),
        ("retrograde_motion", "逆行表示", "Retrograde Motion", "地球から見た天体の見かけの逆向き運動"),
    ]),
    ("Techniques", "技法", [
        ("transit", "トランジット", "Transit", "現在天体と出生図の配置関係を読む技法"),
        ("secondary_progression", "セカンダリー・プログレッション", "Secondary Progression", "出生後の日数を年数へ対応させる進行技法"),
        ("solar_arc", "ソーラーアーク", "Solar Arc", "太陽の進行量を出生図全体へ適用する技法"),
        ("solar_return", "ソーラーリターン", "Solar Return", "太陽が出生時黄経へ戻る時点の図を読む技法"),
        ("lunar_return", "ルナーリターン", "Lunar Return", "月が出生時黄経へ戻る時点の図を読む技法"),
        ("annual_profection", "年齢プロフェクション", "Annual Profection", "年齢ごとにハウスと支配星を移す伝統的技法"),
        ("synastry", "シナストリー", "Synastry", "複数の出生図を重ねて象徴関係を読む技法"),
        ("composite_chart", "コンポジットチャート", "Composite Chart", "二人の天体位置の中間点から関係図を作る技法"),
        ("electional_astrology", "選択占星術", "Electional Astrology", "目的に合わせて開始時刻を選ぶ伝統的技法"),
        ("horary_astrology", "ホラリー占星術", "Horary Astrology", "質問時点の図を用いる伝統的技法"),
    ]),
    ("Synthesis and Limits", "統合と限界", [
        ("house_system_choice", "ハウス方式選択", "House System Choice", "プラシーダス・ホールサイン等の採用方式を明示すること"),
        ("birth_time_sensitivity", "出生時刻感度", "Birth Time Sensitivity", "時刻誤差が角度やハウスへ与える影響を扱うこと"),
        ("chart_rectification", "出生時刻修正", "Chart Rectification", "既知の出来事から出生時刻を推定する流派技法と不確実性"),
        ("element_balance", "エレメント配分", "Element Balance", "サインの火地風水区分の分布を整理すること"),
        ("modality_balance", "三区分配分", "Modality Balance", "活動・不動・柔軟の区分分布を整理すること"),
        ("hemisphere_emphasis", "半球強調", "Hemisphere Emphasis", "出生図上の天体分布を半球別に読む技法"),
        ("chart_ruler", "チャートルーラー", "Chart Ruler", "アセンダントの支配星を全体解釈の手掛かりとすること"),
        ("dispositor_chain", "ディスポジターチェーン", "Dispositor Chain", "サイン支配関係を連鎖として追跡すること"),
        ("stellium", "ステリウム", "Stellium", "複数天体がサインまたはハウスへ集中する配置"),
        ("t_square", "Tスクエア", "T-Square", "二つのスクエアと一つのオポジションからなる配置"),
        ("grand_trine", "グランドトライン", "Grand Trine", "三つのトラインが閉じる配置"),
        ("grand_cross", "グランドクロス", "Grand Cross", "複数のスクエアとオポジションが交差する配置"),
        ("yod", "ヨッド", "Yod", "二つのクインカンクスと一つのセクスタイルからなる配置"),
        ("mutual_reception", "ミューチュアルレセプション", "Mutual Reception", "二惑星が互いの支配サインに位置する関係"),
        ("whole_chart_priority", "全体図優先", "Whole-Chart Priority", "単一サインや天体だけで人物を断定しない原則"),
        ("interpretive_plurality", "解釈多元性", "Interpretive Plurality", "同じ配置に複数の伝統的読みが存在すること"),
        ("uncertainty_disclosure", "不確実性表示", "Uncertainty Disclosure", "入力誤差・方式差・流派差を結果に表示すること"),
        ("non_diagnostic_use", "非診断利用", "Non-Diagnostic Use", "心理診断・医療判断・能力評価へ転用しないこと"),
    ]),
]


PHASES = [("wood", "木", "Wood"), ("fire", "火", "Fire"), ("earth", "土", "Earth"), ("metal", "金", "Metal"), ("water", "水", "Water")]
STEMS = [("jia", "甲", "Jia"), ("yi", "乙", "Yi"), ("bing", "丙", "Bing"), ("ding", "丁", "Ding"), ("wu", "戊", "Wu"), ("ji", "己", "Ji"), ("geng", "庚", "Geng"), ("xin", "辛", "Xin"), ("ren", "壬", "Ren"), ("gui", "癸", "Gui")]
BRANCHES = [("zi", "子", "Zi"), ("chou", "丑", "Chou"), ("yin", "寅", "Yin"), ("mao", "卯", "Mao"), ("chen", "辰", "Chen"), ("si", "巳", "Si"), ("wu", "午", "Wu"), ("wei", "未", "Wei"), ("shen", "申", "Shen"), ("you", "酉", "You"), ("xu", "戌", "Xu"), ("hai", "亥", "Hai")]


WUXING_SECTIONS = [
    ("Foundations", "基礎", [
        ("yin", "陰", "Yin", "相対的な受容・収縮・内向の側面を表す分類"),
        ("yang", "陽", "Yang", "相対的な能動・拡張・外向の側面を表す分類"),
        ("polarity", "陰陽極性", "Yin-Yang Polarity", "陰陽を相互依存する対として扱うこと"),
        ("waxing_waning", "消長", "Waxing and Waning", "陰陽が固定されず増減し転化する過程"),
        ("dynamic_balance", "動的均衡", "Dynamic Balance", "均等ではなく状況に応じた釣り合いを扱うこと"),
        ("correlative_cosmology", "相関的宇宙論", "Correlative Cosmology", "異なる領域を分類上の対応関係で結ぶ伝統的枠組み"),
        ("five_phases", "五行", "Five Phases", "木火土金水を物質でなく変化の様式として扱う分類"),
        ("qi_context", "気の文脈", "Qi Context", "変化と関係を説明する伝統的概念として気を位置づけること"),
        ("seasonal_change", "季節変化", "Seasonal Change", "季節循環を陰陽五行の変化と対応づけること"),
        ("school_context", "学派文脈", "School Context", "時代・地域・思想・占術ごとの差を明示すること"),
    ]),
    ("Five Phases", "五行", entries(PHASES, "五行の{name}に帰属する伝統的な運動・季節・方位などの対応")),
    ("Generating Cycle", "相生", entries([
        ("wood_generates_fire", "木生火", "Wood Generates Fire"),
        ("fire_generates_earth", "火生土", "Fire Generates Earth"),
        ("earth_generates_metal", "土生金", "Earth Generates Metal"),
        ("metal_generates_water", "金生水", "Metal Generates Water"),
        ("water_generates_wood", "水生木", "Water Generates Wood"),
    ], "{name}という五行の生成関係")),
    ("Overcoming Cycle", "相剋", entries([
        ("wood_overcomes_earth", "木剋土", "Wood Overcomes Earth"),
        ("earth_overcomes_water", "土剋水", "Earth Overcomes Water"),
        ("water_overcomes_fire", "水剋火", "Water Overcomes Fire"),
        ("fire_overcomes_metal", "火剋金", "Fire Overcomes Metal"),
        ("metal_overcomes_wood", "金剋木", "Metal Overcomes Wood"),
    ], "{name}という五行の制御関係")),
    ("Phase Polarities", "五行陰陽", []),
]

# Flattened explicitly to keep generated IDs stable and reviewable.
WUXING_SECTIONS[-1] = ("Phase Polarities", "五行陰陽", entries(
    [(polarity + "_" + slug, ("陽の" if polarity == "yang" else "陰の") + ja, ("Yang " if polarity == "yang" else "Yin ") + en)
     for slug, ja, en in PHASES for polarity in ("yang", "yin")],
    "{name}として分類される十干・五行の組合せ",
))
WUXING_SECTIONS.extend([
    ("Heavenly Stems", "十干", entries(STEMS, "十干の{name}に割り当てられる陰陽五行と暦上の位置")),
    ("Earthly Branches", "十二支", entries(BRANCHES, "十二支の{name}に割り当てられる時刻・月・方位・五行などの対応")),
    ("Branch Relations", "地支関係", [
        ("six_harmonies", "六合", "Six Harmonies", "二支間の結びつきを表す伝統的関係群"),
        ("three_harmonies", "三合", "Three Harmonies", "三支が五行局を形成するとする伝統的関係群"),
        ("six_clashes", "六冲", "Six Clashes", "向かい合う地支間の変動関係群"),
        ("six_harms", "六害", "Six Harms", "地支間の害と呼ばれる伝統的関係群"),
        ("punishments", "刑", "Punishments", "地支間の刑と呼ばれる伝統的関係群"),
        ("destructions", "破", "Destructions", "地支間の破と呼ばれる伝統的関係群"),
        ("branch_combinations", "地支合", "Branch Combinations", "複数地支の結合を読む総称"),
        ("seasonal_frames", "方合", "Seasonal Frames", "同季節の地支が方向局を形成する関係"),
        ("hidden_stems", "蔵干", "Hidden Stems", "地支内部に天干を配当する伝統的対応"),
        ("branch_polarity", "地支陰陽", "Branch Polarity", "各地支を陰または陽へ分類すること"),
        ("branch_phase", "地支五行", "Branch Phase", "各地支へ主要な五行を配当すること"),
        ("branch_time", "地支時刻", "Branch Time", "一日を十二の時刻帯へ配当すること"),
    ]),
    ("Season and Process", "季節と過程", [
        ("spring_phase", "春の木", "Spring Wood", "春と木の成長過程を対応づけること"),
        ("summer_phase", "夏の火", "Summer Fire", "夏と火の発現過程を対応づけること"),
        ("seasonal_earth", "季節移行の土", "Seasonal Earth", "季節間の移行と土を対応づけること"),
        ("autumn_phase", "秋の金", "Autumn Metal", "秋と金の収斂過程を対応づけること"),
        ("winter_phase", "冬の水", "Winter Water", "冬と水の蓄積過程を対応づけること"),
        ("birth_stage", "発生段階", "Emergence Stage", "過程が生じ始める段階を分類すること"),
        ("growth_stage", "成長段階", "Growth Stage", "過程が展開する段階を分類すること"),
        ("peak_stage", "旺盛段階", "Peak Stage", "過程が最も明瞭になる段階を分類すること"),
        ("decline_stage", "衰退段階", "Decline Stage", "過程が収まり始める段階を分類すること"),
        ("storage_stage", "収蔵段階", "Storage Stage", "過程が蓄えられ次へ移る段階を分類すること"),
    ]),
    ("Correspondence Domains", "対応領域", entries([
        ("directions", "方位対応", "Direction Correspondence"), ("colors", "色対応", "Color Correspondence"),
        ("tastes", "味対応", "Taste Correspondence"), ("body_symbols", "身体象徴対応", "Body Symbol Correspondence"),
        ("emotion_symbols", "感情象徴対応", "Emotion Symbol Correspondence"), ("climates", "気候対応", "Climate Correspondence"),
        ("planets", "惑星対応", "Planet Correspondence"), ("numbers", "数対応", "Number Correspondence"),
        ("sounds", "音対応", "Sound Correspondence"), ("social_roles", "役割対応", "Social Role Correspondence"),
    ], "五行と{name}を結ぶ伝統的分類であり因果関係を意味しない")),
    ("Interpretation Limits", "解釈限界", [
        ("phase_not_substance", "五行非物質原則", "Phases Are Not Substances", "五行を固定物質ではなく変化の分類として扱うこと"),
        ("relational_reading", "関係的解釈", "Relational Reading", "単独要素より相互関係と時期を優先すること"),
        ("contextual_correspondence", "文脈的対応", "Contextual Correspondence", "対応表を普遍的因果法則とみなさないこと"),
        ("school_variation", "流派差表示", "School Variation Disclosure", "配当や関係規則の流派差を表示すること"),
        ("source_provenance", "出典来歴", "Source Provenance", "対応関係の時代・地域・文献を記録すること"),
        ("translation_variation", "訳語差", "Translation Variation", "element・phase・agent等の訳語差を記録すること"),
        ("calendar_precision", "暦精度", "Calendar Precision", "暦変換と節気境界の計算精度を記録すること"),
        ("cross_cultural_boundary", "文化横断境界", "Cross-Cultural Boundary", "文化的分類を普遍的人格類型へ変換しないこと"),
        ("non_diagnostic_use", "非診断利用", "Non-Diagnostic Use", "精神・身体状態の診断へ用いないこと"),
        ("no_medical_inference", "医療推論禁止", "No Medical Inference", "身体象徴対応から疾患や体質を推定しないこと"),
        ("dynamic_synthesis", "動的統合", "Dynamic Synthesis", "陰陽五行を固定ラベルでなく変化する象徴関係として提示すること"),
    ]),
])


BAZI_SECTIONS = [
    ("Inputs and Calendar", "入力と暦", [
        ("birth_date_input", "生年月日入力", "Birth Date Input", "出生年月日と使用暦を記録すること"),
        ("birth_time_input", "出生時刻入力", "Birth Time Input", "出生時刻と精度を記録すること"),
        ("birth_place_input", "出生地入力", "Birth Place Input", "時差計算に必要な出生地を記録すること"),
        ("time_zone_rule", "時間帯規則", "Time-Zone Rule", "出生時点の標準時と夏時間を適用すること"),
        ("local_solar_time", "地方太陽時", "Local Solar Time", "採用流派に応じた地方時補正を明示すること"),
        ("calendar_conversion", "暦変換", "Calendar Conversion", "入力暦を計算に用いる暦へ変換すること"),
        ("solar_term_boundary", "節気境界", "Solar-Term Boundary", "月柱決定に用いる節入り時刻を扱うこと"),
        ("day_boundary", "日界", "Day Boundary", "日柱が切り替わる時刻規則を明示すること"),
        ("hour_branch_boundary", "時支境界", "Hour-Branch Boundary", "出生時刻を十二時辰へ割り当てる境界"),
        ("input_uncertainty", "入力不確実性", "Input Uncertainty", "不明時刻・推定値・境界付近を結果へ反映すること"),
    ]),
    ("Pillars", "四柱", [
        ("year_stem", "年干", "Year Stem", "年柱の天干"), ("year_branch", "年支", "Year Branch", "年柱の地支"),
        ("month_stem", "月干", "Month Stem", "月柱の天干"), ("month_branch", "月支", "Month Branch", "月柱の地支"),
        ("day_stem", "日干", "Day Stem", "日柱の天干で日主として扱う基準"), ("day_branch", "日支", "Day Branch", "日柱の地支"),
        ("hour_stem", "時干", "Hour Stem", "時柱の天干"), ("hour_branch", "時支", "Hour Branch", "時柱の地支"),
    ]),
    ("Day Master Context", "日主文脈", [
        ("day_master", "日主", "Day Master", "日干を命式内の関係を整理する基準点とすること"),
        ("seasonal_support", "月令", "Seasonal Command", "月支が示す季節的文脈を重視すること"),
        ("root_support", "通根", "Root Support", "日主と同類の気が地支に存在すると読む概念"),
        ("resource_support", "印の扶助", "Resource Support", "日主を生じる五行との関係"),
        ("peer_support", "比劫の扶助", "Peer Support", "日主と同じ五行との関係"),
        ("drain_by_output", "食傷への泄", "Drain by Output", "日主が生じる五行へ力が移ると読む関係"),
        ("control_by_officer", "官殺からの剋", "Control by Officer", "日主を剋す五行との関係"),
        ("wealth_control", "財への剋", "Wealth Control", "日主が剋す五行との関係"),
        ("strength_assessment", "身強身弱評価", "Strength Assessment", "季節・根・扶助・泄剋を合わせて日主の相対状態を読むこと"),
        ("balance_not_score", "強弱非得点原則", "Strength Is Not a Person Score", "身強身弱を人物の優劣や能力値に変換しないこと"),
    ]),
    ("Ten Gods", "十神", entries([
        ("friend", "比肩", "Friend"), ("rob_wealth", "劫財", "Rob Wealth"),
        ("eating_god", "食神", "Eating God"), ("hurting_officer", "傷官", "Hurting Officer"),
        ("direct_wealth", "正財", "Direct Wealth"), ("indirect_wealth", "偏財", "Indirect Wealth"),
        ("direct_officer", "正官", "Direct Officer"), ("seven_killings", "偏官・七殺", "Seven Killings"),
        ("direct_resource", "正印", "Direct Resource"), ("indirect_resource", "偏印", "Indirect Resource"),
    ], "日主と他の天干の陰陽五行関係を{name}として分類すること")),
    ("Branches and Hidden Stems", "地支と蔵干", [
        ("hidden_stem_primary", "本気", "Primary Hidden Stem", "地支の蔵干で中心とされる干"),
        ("hidden_stem_middle", "中気", "Middle Hidden Stem", "地支の蔵干で中間的に配当される干"),
        ("hidden_stem_residual", "余気", "Residual Hidden Stem", "地支の蔵干で補助的に配当される干"),
        ("branch_season", "地支季節", "Branch Season", "月支と季節の対応"),
        ("branch_phase", "地支五行", "Branch Phase", "地支に配当される主要五行"),
        ("branch_polarity", "地支陰陽", "Branch Polarity", "地支に配当される陰陽"),
        ("branch_combination", "地支合", "Branch Combination", "地支間の結合関係"),
        ("branch_clash", "地支冲", "Branch Clash", "地支間の対向・変動関係"),
        ("branch_harm", "地支害", "Branch Harm", "地支間の害と呼ばれる関係"),
        ("branch_punishment", "地支刑", "Branch Punishment", "地支間の刑と呼ばれる関係"),
        ("branch_destruction", "地支破", "Branch Destruction", "地支間の破と呼ばれる関係"),
        ("branch_relation_priority", "地支関係優先度", "Branch Relation Priority", "複数関係が成立するときの流派規則を明示すること"),
    ]),
    ("Stem and Branch Interactions", "干支作用", [
        ("stem_combination", "天干合", "Stem Combination", "天干間の五合関係"),
        ("stem_control", "天干剋", "Stem Control", "天干間の相剋関係"),
        ("combination_transformation", "合化", "Combination Transformation", "合が別の五行へ化すと読む条件"),
        ("three_harmony_frame", "三合局", "Three-Harmony Frame", "三支が五行局を形成すると読む関係"),
        ("seasonal_frame", "方局", "Seasonal Frame", "同季節の三支が方向局を形成すると読む関係"),
        ("six_harmony_pair", "六合", "Six-Harmony Pair", "二支間の六合関係"),
        ("six_clash_pair", "六冲", "Six-Clash Pair", "二支間の六冲関係"),
        ("interaction_activation", "作用発動", "Interaction Activation", "原局と運の重なりで関係が強調されると読むこと"),
        ("interaction_resolution", "作用解消", "Interaction Resolution", "合・冲等が別の関係で変化すると読む流派規則"),
        ("interaction_uncertainty", "作用不確実性", "Interaction Uncertainty", "成立条件と優先順位の流派差を表示すること"),
    ]),
    ("Chart Structures", "格局", [
        ("structure_identification", "格局判定", "Structure Identification", "月令等を基準に命式構造を分類する伝統的手続き"),
        ("regular_structure", "普通格局", "Regular Structure", "一般的な十神関係から構造を分類する枠組み"),
        ("special_structure", "特殊格局", "Special Structure", "特定条件で通常と異なる規則を用いる構造分類"),
        ("follow_structure", "従格", "Follow Structure", "特定の五行傾向へ従うと読む特殊構造"),
        ("transformation_structure", "化格", "Transformation Structure", "天干合化を中心に読む特殊構造"),
        ("useful_god", "用神", "Useful God", "命式の調整上重視する五行・十神を選ぶ伝統概念"),
        ("favorable_element", "喜神", "Favorable Element", "用神を補助すると読む五行"),
        ("unfavorable_element", "忌神", "Unfavorable Element", "調整上過剰または阻害と読む五行"),
        ("climate_adjustment", "調候", "Climate Adjustment", "季節の寒暖燥湿を象徴的に調整する読み"),
        ("structure_school_variation", "格局流派差", "Structure School Variation", "格局・用神判定の流派差を明示すること"),
    ]),
    ("Time Cycles", "運勢周期", [
        ("luck_pillar", "大運", "Luck Pillar", "一定期間ごとの干支を原局との関係で読むモデル"),
        ("luck_direction", "大運順逆", "Luck Direction", "大運配列を順行・逆行とする規則"),
        ("luck_start_age", "起運年齢", "Luck Start Age", "節気までの時間等から開始年齢を求める流派計算"),
        ("annual_pillar", "流年", "Annual Pillar", "各年の干支を原局・大運との関係で読むモデル"),
        ("monthly_pillar", "流月", "Monthly Pillar", "各月の干支を時期文脈として読むモデル"),
        ("daily_pillar", "流日", "Daily Pillar", "各日の干支を短期文脈として読むモデル"),
        ("cycle_overlap", "運周期重合", "Cycle Overlap", "原局・大運・流年等の関係が重なること"),
        ("cycle_transition", "運切替", "Cycle Transition", "大運等の境界時期を不連続な運命決定とみなさず扱うこと"),
        ("timing_uncertainty", "時期不確実性", "Timing Uncertainty", "起運・日界・節気境界の計算差を表示すること"),
        ("non_deterministic_timing", "非決定論的時期表示", "Non-Deterministic Timing", "時期モデルを出来事の確定予言として表示しないこと"),
    ]),
    ("Synthesis", "命式統合", [
        ("whole_chart_synthesis", "命式全体統合", "Whole-Chart Synthesis", "単一の干支や十神だけで結論を出さないこと"),
        ("season_first_context", "季節優先文脈", "Season-First Context", "月令と季節を他要素の解釈文脈として扱うこと"),
        ("relation_network", "関係ネットワーク", "Relation Network", "五行・十神・干支作用を関係網として整理すること"),
        ("contradictory_symbols", "矛盾象徴併記", "Contradictory Symbols", "異なる方向の象徴を消去せず併記すること"),
        ("school_specific_result", "流派別結果", "School-Specific Result", "流派ごとの結果を混ぜず個別に保持すること"),
        ("calculation_trace", "計算追跡", "Calculation Trace", "入力から四柱・関係・解釈までの計算経路を保存すること"),
        ("trait_link_boundary", "性格リンク境界", "Trait-Link Boundary", "心理概念へのリンクを検索補助とし実証的関連とみなさないこと"),
        ("narrative_prompt", "物語プロンプト", "Narrative Prompt", "象徴を内省や会話の問いへ変換すること"),
        ("multiple_hypotheses", "複数仮説表示", "Multiple Hypotheses", "一つの配置から複数の解釈候補を提示すること"),
        ("user_resonance", "本人照合", "User Resonance", "利用者が当てはまり方を選び修正できるようにすること"),
    ]),
    ("Safety and Governance", "安全と統制", [
        ("traditional_evidence_label", "伝統根拠表示", "Traditional Evidence Label", "伝統的解釈であることを常に表示すること"),
        ("no_mental_diagnosis", "精神診断禁止", "No Mental Diagnosis", "命式から精神疾患や心理状態を診断しないこと"),
        ("no_health_prediction", "健康予測禁止", "No Health Prediction", "命式から病気・寿命・妊娠等を予測しないこと"),
        ("no_ability_ranking", "能力序列化禁止", "No Ability Ranking", "命式から知能・適性・価値を序列化しないこと"),
        ("no_relationship_determinism", "相性決定論禁止", "No Relationship Determinism", "関係の成否や危険性を確定しないこと"),
        ("no_fatalism", "宿命論回避", "Avoid Fatalism", "不可避・絶対・運命確定という表示を避けること"),
        ("high_impact_exclusion", "高影響利用禁止", "High-Impact Exclusion", "雇用・教育・保険・信用・法執行等に利用しないこと"),
        ("birth_data_minimization", "出生情報最小化", "Birth-Data Minimization", "出生情報の収集・保持を必要最小限にすること"),
        ("consent_and_deletion", "同意と削除", "Consent and Deletion", "利用目的への同意と入力・派生データの削除手段を用意すること"),
        ("human_readable_disclaimer", "平易な注意表示", "Human-Readable Disclaimer", "専門用語で隠さず限界を利用者へ明示すること"),
    ]),
]


def make_item(prefix, number, slug, name_ja, name_en, focus, config, section_en, section_ja):
    item_id = f"{prefix}-{number:06d}"
    return {
        "filename": f"{item_id}_{slug}.yml",
        "id": item_id,
        "knowledge_type": config["knowledge_type"],
        "name_ja": name_ja,
        "name_en": name_en,
        "category": config["category"],
        "attribute": section_en,
        "definition_ja": f"{name_ja}は、{focus}を表す{config['label']}参照概念。科学的な性格検査・心理診断・確定的予測としては扱わない。",
        "tags": [config["category_tag"], f"CAT:{section_ja}", "EVIDENCE:伝統的解釈"],
        "parent": [section_ja],
        "related": ["自己理解", "文化的象徴", "解釈不確実性"],
        "observable_data": ["利用者が明示的に提供した出生情報", "採用した暦・計算規則・流派", "入力精度と欠測", "計算で得られた象徴配置"],
        "signal_candidates": ["入力と規則から再現可能な象徴配置を得る", "複数要素を解釈候補として提示し単一の性格断定へ短絡させない"],
        "device_level": "本人同意のある入力だけを使用し、高影響判断・診断・能力評価には利用しない",
        "modifiers": ["流派", "地域と時代", "暦と時間規則", "入力精度", "翻訳", "解釈目的"],
        "evidence": "歴史的・文化的な占術体系の参照情報。心理測定上の妥当性や因果的予測力を示すものではない",
        "status": "active",
        "tradition": config["tradition"],
        "source_type": config["source_type"],
        "evidence_class": "traditional_cultural_interpretation",
        "required_inputs": config["required_inputs"],
        "calculation_basis": config["calculation_basis"],
        "trait_links": ["自己理解", "価値観", "意思決定", "対人傾向"],
        "interpretive_scope": "内省・会話・物語生成・娯楽のための解釈候補",
        "safe_expression": f"{config['tradition']}では、{name_ja}を象徴的な手掛かりの一つとして扱います。現実の性格・状態・未来を断定するものではありません。",
        "provenance": config["provenance"],
    }


def build_pack(config, sections):
    items = []
    index_lines = [f"category: {config['category']}", f"name_ja: {config['label']}", "items:"]
    number = 1
    for section_en, section_ja, definitions in sections:
        for slug, name_ja, name_en, focus in definitions:
            item = make_item(config["prefix"], number, slug, name_ja, name_en, focus, config, section_en, section_ja)
            items.append(item)
            index_lines.append(f"  - {item['filename']}")
            number += 1
    if len(items) != 100:
        raise ValueError(f"{config['prefix']}: expected 100 items, got {len(items)}")
    index_lines.extend([
        "notes:",
        "  - 伝統的・文化的解釈として扱い心理学的エビデンスと混同しない",
        "  - 計算方式・流派・入力精度・出典を結果とともに保持する",
        "  - 医療・雇用・教育・保険・信用・法執行など高影響判断には利用しない",
    ])
    pack = {
        "output_dir": config["output_dir"],
        "index_filename": config["index_filename"],
        "index_content": "\n".join(index_lines) + "\n",
        "items": items,
    }
    path = MASTER_ROOT / config["master_filename"]
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(pack, ensure_ascii=False, indent=2), encoding="utf-8")
    print(f"Created: {path} ({len(items)} items)")


CONFIGS = [
    ({
        "prefix": "AST", "knowledge_type": "western_astrology", "category": "Western Astrology",
        "category_tag": "CAT:西洋占星術", "label": "西洋占星術", "tradition": "西洋占星術",
        "source_type": "生年月日・出生時刻・出生地・天体暦",
        "required_inputs": ["生年月日", "出生時刻", "出生地", "時間帯", "採用する黄道", "ハウス方式"],
        "calculation_basis": "天体暦から黄経・感受点・ハウス・角度関係を算出し採用方式を記録する",
        "provenance": "メソポタミア・ヘレニズム以後の西洋占星術史と伝統・近現代諸流派",
        "output_dir": "vol32_western_astrology/western_astrology_001_100",
        "index_filename": "western_astrology_001_100_index.yml",
        "master_filename": "vol32_western_astrology_001_100.json",
    }, WESTERN_SECTIONS),
    ({
        "prefix": "WUX", "knowledge_type": "yin_yang_wuxing", "category": "Yin Yang and Five Phases",
        "category_tag": "CAT:陰陽五行", "label": "陰陽五行", "tradition": "陰陽五行・干支体系",
        "source_type": "暦・節気・伝統的分類規則",
        "required_inputs": ["対象時点", "使用暦", "適用する流派", "参照目的"],
        "calculation_basis": "陰陽・五行・十干十二支・季節循環の対応規則を流派別に適用する",
        "provenance": "中国の相関的宇宙論・干支暦法と東アジアに展開した諸伝統",
        "output_dir": "vol33_yin_yang_wuxing/yin_yang_wuxing_001_100",
        "index_filename": "yin_yang_wuxing_001_100_index.yml",
        "master_filename": "vol33_yin_yang_wuxing_001_100.json",
    }, WUXING_SECTIONS),
    ({
        "prefix": "BAZ", "knowledge_type": "four_pillars", "category": "Four Pillars",
        "category_tag": "CAT:四柱推命", "label": "四柱推命", "tradition": "四柱推命・八字",
        "source_type": "生年月日・出生時刻・出生地・暦・節気",
        "required_inputs": ["生年月日", "出生時刻", "出生地", "時間帯", "使用暦", "日界と節気規則"],
        "calculation_basis": "出生情報を四柱の干支へ変換し陰陽五行・十神・干支関係を流派規則で整理する",
        "provenance": "中国の子平法・八字・四柱推命と東アジアに展開した諸流派",
        "output_dir": "vol34_four_pillars/four_pillars_001_100",
        "index_filename": "four_pillars_001_100_index.yml",
        "master_filename": "vol34_four_pillars_001_100.json",
    }, BAZI_SECTIONS),
]


def main():
    for config, sections in CONFIGS:
        build_pack(config, sections)


if __name__ == "__main__":
    main()
