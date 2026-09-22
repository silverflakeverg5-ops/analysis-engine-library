"""Build Vol31, a non-diagnostic reference catalog for birth-data divination."""

from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "data" / "master_packs" / "vol31_divination_reference_001_100.json"


SECTIONS = [
    ("Reference Foundations", "参照基盤", "comparative", [
        ("interpretive_framework", "解釈体系", "Interpretive Framework", "象徴と規則を組み合わせて意味を組み立てる枠組み"),
        ("tradition_identity", "伝統体系の識別", "Tradition Identity", "異なる占術体系を混同せず名称と文化的背景を記録すること"),
        ("school_variant", "流派差", "School Variant", "同じ名称でも流派により計算規則や意味づけが異なること"),
        ("symbolic_correspondence", "象徴対応", "Symbolic Correspondence", "天体・暦・自然現象と人間経験を象徴的に対応づけること"),
        ("source_provenance", "出典来歴", "Source Provenance", "解釈がどの文献・地域・時代・流派に由来するかを追跡すること"),
        ("evidence_classification", "根拠区分", "Evidence Classification", "科学的知見と歴史的・文化的・伝統的解釈を区別すること"),
        ("interpretive_uncertainty", "解釈不確実性", "Interpretive Uncertainty", "入力精度と流派差と解釈者差による不確実性を明示すること"),
        ("non_diagnostic_boundary", "非診断境界", "Non-Diagnostic Boundary", "占術を医療診断・心理判定・能力評価に使用しない境界"),
    ]),
    ("Birth Data and Calculation", "出生データと計算", "calculation", [
        ("birth_date", "生年月日", "Birth Date", "暦上の日付を計算の基礎入力として扱うこと"),
        ("birth_time", "出生時刻", "Birth Time", "記録された出生時刻とその精度を扱うこと"),
        ("birth_place", "出生地", "Birth Place", "天体位置や地方時の計算に用いる地理的位置"),
        ("time_zone", "時間帯", "Time Zone", "出生時点の標準時と夏時間を含む時差情報"),
        ("calendar_system", "暦法", "Calendar System", "グレゴリオ暦・太陰太陽暦など使用する暦を識別すること"),
        ("ephemeris", "天体暦", "Ephemeris", "指定時刻の天体位置を得るための計算表またはデータ"),
        ("solar_terms", "二十四節気", "Twenty-Four Solar Terms", "太陽黄経にもとづく季節区分を暦計算に用いること"),
        ("input_precision", "入力精度", "Input Precision", "時刻不明・推定値・丸めなど入力の確からしさを記録すること"),
    ]),
    ("Western Zodiac Signs", "西洋占星術・十二宮", "western_astrology", [
        ("aries", "牡羊座", "Aries", "黄道十二宮の牡羊座に帰属する伝統的象徴"),
        ("taurus", "牡牛座", "Taurus", "黄道十二宮の牡牛座に帰属する伝統的象徴"),
        ("gemini", "双子座", "Gemini", "黄道十二宮の双子座に帰属する伝統的象徴"),
        ("cancer", "蟹座", "Cancer", "黄道十二宮の蟹座に帰属する伝統的象徴"),
        ("leo", "獅子座", "Leo", "黄道十二宮の獅子座に帰属する伝統的象徴"),
        ("virgo", "乙女座", "Virgo", "黄道十二宮の乙女座に帰属する伝統的象徴"),
        ("libra", "天秤座", "Libra", "黄道十二宮の天秤座に帰属する伝統的象徴"),
        ("scorpio", "蠍座", "Scorpio", "黄道十二宮の蠍座に帰属する伝統的象徴"),
        ("sagittarius", "射手座", "Sagittarius", "黄道十二宮の射手座に帰属する伝統的象徴"),
        ("capricorn", "山羊座", "Capricorn", "黄道十二宮の山羊座に帰属する伝統的象徴"),
        ("aquarius", "水瓶座", "Aquarius", "黄道十二宮の水瓶座に帰属する伝統的象徴"),
        ("pisces", "魚座", "Pisces", "黄道十二宮の魚座に帰属する伝統的象徴"),
    ]),
    ("Western Planets and Angles", "西洋占星術・天体と感受点", "western_astrology", [
        ("sun", "太陽", "Sun", "出生図における太陽の伝統的象徴"),
        ("moon", "月", "Moon", "出生図における月の伝統的象徴"),
        ("mercury", "水星", "Mercury", "出生図における水星の伝統的象徴"),
        ("venus", "金星", "Venus", "出生図における金星の伝統的象徴"),
        ("mars", "火星", "Mars", "出生図における火星の伝統的象徴"),
        ("jupiter", "木星", "Jupiter", "出生図における木星の伝統的象徴"),
        ("saturn", "土星", "Saturn", "出生図における土星の伝統的象徴"),
        ("uranus", "天王星", "Uranus", "近現代占星術における天王星の象徴"),
        ("neptune", "海王星", "Neptune", "近現代占星術における海王星の象徴"),
        ("pluto", "冥王星", "Pluto", "近現代占星術における冥王星の象徴"),
        ("ascendant", "アセンダント", "Ascendant", "出生地点で東の地平線に昇る黄道上の感受点"),
        ("midheaven", "ミッドヘブン", "Midheaven", "出生図の天頂方向に関係する主要感受点"),
    ]),
    ("Western Houses", "西洋占星術・ハウス", "western_astrology", [
        ("first_house", "第1ハウス", "First House", "自己表現や出発に対応づける伝統的生活領域"),
        ("second_house", "第2ハウス", "Second House", "所有や価値に対応づける伝統的生活領域"),
        ("third_house", "第3ハウス", "Third House", "学習や近距離交流に対応づける伝統的生活領域"),
        ("fourth_house", "第4ハウス", "Fourth House", "家庭や基盤に対応づける伝統的生活領域"),
        ("fifth_house", "第5ハウス", "Fifth House", "創造や遊びに対応づける伝統的生活領域"),
        ("sixth_house", "第6ハウス", "Sixth House", "日課や奉仕に対応づける伝統的生活領域"),
        ("seventh_house", "第7ハウス", "Seventh House", "対人関係や契約に対応づける伝統的生活領域"),
        ("eighth_house", "第8ハウス", "Eighth House", "共有資源や変化に対応づける伝統的生活領域"),
        ("ninth_house", "第9ハウス", "Ninth House", "探究や遠方に対応づける伝統的生活領域"),
        ("tenth_house", "第10ハウス", "Tenth House", "公的役割や達成に対応づける伝統的生活領域"),
        ("eleventh_house", "第11ハウス", "Eleventh House", "仲間や共同目標に対応づける伝統的生活領域"),
        ("twelfth_house", "第12ハウス", "Twelfth House", "内省や境界の曖昧な領域に対応づける伝統的生活領域"),
    ]),
    ("Western Relations and Synthesis", "西洋占星術・関係と統合", "western_astrology", [
        ("conjunction", "コンジャンクション", "Conjunction", "二つの感受点が近い黄経に位置する関係"),
        ("opposition", "オポジション", "Opposition", "二つの感受点がおよそ180度離れる関係"),
        ("trine", "トライン", "Trine", "二つの感受点がおよそ120度離れる関係"),
        ("square", "スクエア", "Square", "二つの感受点がおよそ90度離れる関係"),
        ("sextile", "セクスタイル", "Sextile", "二つの感受点がおよそ60度離れる関係"),
        ("aspect_orb", "アスペクト許容度", "Aspect Orb", "角度関係を成立とみなす許容範囲"),
        ("rulership", "支配星", "Rulership", "惑星とサインを結びつける伝統的対応関係"),
        ("chart_synthesis", "出生図統合", "Natal Chart Synthesis", "単一要素で断定せず配置全体を流派規則に沿って読むこと"),
    ]),
    ("Yin Yang and Five Phases", "陰陽五行", "yin_yang_wuxing", [
        ("yin", "陰", "Yin", "相対的に受容・収縮・内向などへ対応づけられる陰の概念"),
        ("yang", "陽", "Yang", "相対的に能動・拡張・外向などへ対応づけられる陽の概念"),
        ("yin_yang_interaction", "陰陽相互作用", "Yin-Yang Interaction", "陰と陽を固定属性でなく相互依存し変化する関係として捉えること"),
        ("wood_phase", "木", "Wood Phase", "五行の木に帰属する成長と展開の伝統的対応"),
        ("fire_phase", "火", "Fire Phase", "五行の火に帰属する上昇と発現の伝統的対応"),
        ("earth_phase", "土", "Earth Phase", "五行の土に帰属する媒介と育成の伝統的対応"),
        ("metal_phase", "金", "Metal Phase", "五行の金に帰属する収斂と変化の伝統的対応"),
        ("water_phase", "水", "Water Phase", "五行の水に帰属する下降と潤下の伝統的対応"),
        ("generating_cycle", "相生", "Generating Cycle", "木火土金水を生成関係として循環させる五行モデル"),
        ("overcoming_cycle", "相剋", "Overcoming Cycle", "木土水火金を制御関係として循環させる五行モデル"),
    ]),
    ("Heavenly Stems", "十干", "gan_zhi", [
        ("jia", "甲", "Jia", "十干の甲に割り当てられる陽の木という暦上の分類"),
        ("yi", "乙", "Yi", "十干の乙に割り当てられる陰の木という暦上の分類"),
        ("bing", "丙", "Bing", "十干の丙に割り当てられる陽の火という暦上の分類"),
        ("ding", "丁", "Ding", "十干の丁に割り当てられる陰の火という暦上の分類"),
        ("wu", "戊", "Wu", "十干の戊に割り当てられる陽の土という暦上の分類"),
        ("ji", "己", "Ji", "十干の己に割り当てられる陰の土という暦上の分類"),
        ("geng", "庚", "Geng", "十干の庚に割り当てられる陽の金という暦上の分類"),
        ("xin", "辛", "Xin", "十干の辛に割り当てられる陰の金という暦上の分類"),
        ("ren", "壬", "Ren", "十干の壬に割り当てられる陽の水という暦上の分類"),
        ("gui", "癸", "Gui", "十干の癸に割り当てられる陰の水という暦上の分類"),
    ]),
    ("Earthly Branches", "十二支", "gan_zhi", [
        ("zi", "子", "Zi", "十二支の子という暦上の分類"),
        ("chou", "丑", "Chou", "十二支の丑という暦上の分類"),
        ("yin_branch", "寅", "Yin Branch", "十二支の寅という暦上の分類"),
        ("mao", "卯", "Mao", "十二支の卯という暦上の分類"),
        ("chen", "辰", "Chen", "十二支の辰という暦上の分類"),
        ("si", "巳", "Si", "十二支の巳という暦上の分類"),
        ("wu_branch", "午", "Wu Branch", "十二支の午という暦上の分類"),
        ("wei", "未", "Wei", "十二支の未という暦上の分類"),
        ("shen", "申", "Shen", "十二支の申という暦上の分類"),
        ("you", "酉", "You", "十二支の酉という暦上の分類"),
        ("xu", "戌", "Xu", "十二支の戌という暦上の分類"),
        ("hai", "亥", "Hai", "十二支の亥という暦上の分類"),
    ]),
    ("Four Pillars", "四柱推命", "four_pillars", [
        ("year_pillar", "年柱", "Year Pillar", "出生年を干支の組として表す四柱の一部"),
        ("month_pillar", "月柱", "Month Pillar", "節気にもとづく出生月を干支の組として表す四柱の一部"),
        ("day_pillar", "日柱", "Day Pillar", "出生日を干支の組として表す四柱の一部"),
        ("hour_pillar", "時柱", "Hour Pillar", "出生時刻を干支の組として表す四柱の一部"),
        ("day_master", "日主", "Day Master", "日柱の天干を命式解釈の基準点とする概念"),
        ("ten_gods", "通変星・十神", "Ten Gods", "日主と他の干の陰陽五行関係を類型化する枠組み"),
        ("luck_pillars", "大運", "Luck Pillars", "一定期間ごとの干支を命式との関係で扱う伝統的時間モデル"),
        ("four_pillars_synthesis", "命式統合", "Four Pillars Synthesis", "四柱・五行・季節・関係規則を単一要素へ還元せず統合すること"),
    ]),
]


def section_metadata(kind: str) -> dict[str, object]:
    if kind == "western_astrology":
        return {
            "tradition": "西洋占星術",
            "source_type": "出生日時・出生地・天体暦",
            "required_inputs": ["生年月日", "出生時刻", "出生地", "時間帯"],
            "calculation_basis": "黄道上の天体・感受点・ハウス・角度関係。採用する黄道とハウス方式を別途記録する",
            "provenance": "メソポタミア・ヘレニズム以後の西洋占星術史と近現代の諸流派",
        }
    if kind in {"yin_yang_wuxing", "gan_zhi", "four_pillars"}:
        inputs = ["生年月日", "出生時刻", "出生地", "時間帯", "使用暦", "節気境界"]
        if kind != "four_pillars":
            inputs = ["使用する暦・時点", "適用する流派規則"]
        return {
            "tradition": {
                "yin_yang_wuxing": "陰陽五行思想",
                "gan_zhi": "干支暦法",
                "four_pillars": "四柱推命",
            }[kind],
            "source_type": "生年月日時・暦・節気" if kind == "four_pillars" else "暦・伝統的分類体系",
            "required_inputs": inputs,
            "calculation_basis": "十干十二支・陰陽五行・節気を用いる。暦変換と日界・時刻規則は流派と実装で固定する",
            "provenance": "中国の相関的宇宙論・干支暦法と、それを用いる東アジアの諸伝統",
        }
    if kind == "calculation":
        return {
            "tradition": "占術共通計算基盤",
            "source_type": "利用者が明示的に提供した出生データ",
            "required_inputs": ["利用目的", "同意", "利用可能な出生データ", "入力精度"],
            "calculation_basis": "採用する暦・時間帯・位置計算・境界規則を再現可能な形で記録する",
            "provenance": "暦法・時刻制度・天体位置計算の記録仕様",
        }
    return {
        "tradition": "占術横断",
        "source_type": "伝統資料・流派規則・利用者入力",
        "required_inputs": ["利用目的", "同意", "採用する占術体系", "流派", "出典"],
        "calculation_basis": "体系ごとの規則を混同せず、入力から結果までの変換過程を記録する",
        "provenance": "比較文化・宗教史・占術史と各伝統の一次・二次資料",
    }


def make_item(number, slug, name_ja, name_en, focus, section_en, section_ja, kind):
    metadata = section_metadata(kind)
    item_id = f"DIV-{number:06d}"
    return {
        "filename": f"{item_id}_{slug}.yml",
        "id": item_id,
        "knowledge_type": "divination_reference",
        "name_ja": name_ja,
        "name_en": name_en,
        "category": "Divination Reference",
        "attribute": section_en,
        "definition_ja": f"{name_ja}は、{focus}を表す占術参照概念。科学的な性格検査・心理診断・未来予測としては扱わない。",
        "tags": ["CAT:占術参照", f"CAT:{section_ja}", "EVIDENCE:伝統的解釈"],
        "parent": [section_ja],
        "related": ["自己理解", "文化的象徴", "解釈不確実性"],
        "observable_data": ["利用者が明示的に提供した入力", "採用した計算規則と流派", "入力精度と欠測", "生成された象徴配置"],
        "signal_candidates": ["入力と計算規則から再現可能な象徴配置を取得する", "複数の象徴を単一の性格断定へ短絡させず解釈候補として提示する"],
        "device_level": "本人同意のある入力だけを使用し、医療・雇用・教育・保険・信用・法執行の判断には利用しない",
        "modifiers": ["流派", "地域と時代", "暦法", "入力精度", "翻訳", "解釈目的"],
        "evidence": "歴史的・文化的な占術体系の参照情報。心理測定上の妥当性や因果的予測力を示すものではない",
        "status": "active",
        "tradition": metadata["tradition"],
        "source_type": metadata["source_type"],
        "evidence_class": "traditional_cultural_interpretation",
        "required_inputs": metadata["required_inputs"],
        "calculation_basis": metadata["calculation_basis"],
        "trait_links": ["自己理解", "価値観", "意思決定", "対人傾向"],
        "interpretive_scope": "内省・会話・物語生成・娯楽のための解釈候補",
        "safe_expression": f"{metadata['tradition']}では、{name_ja}を象徴的な手掛かりの一つとして解釈します。現実の性格や状態を断定するものではありません。",
        "provenance": metadata["provenance"],
    }


def main():
    items = []
    index_lines = ["category: Divination Reference", "name_ja: 占術参照", "items:"]
    number = 1
    for section_en, section_ja, kind, definitions in SECTIONS:
        for slug, name_ja, name_en, focus in definitions:
            item = make_item(number, slug, name_ja, name_en, focus, section_en, section_ja, kind)
            items.append(item)
            index_lines.append(f"  - {item['filename']}")
            number += 1
    if len(items) != 100:
        raise ValueError(f"Expected 100 items, got {len(items)}")
    index_lines.extend([
        "notes:",
        "  - 心理学的知識項目と占術項目を根拠上同一に扱わない",
        "  - 占術項目は内省・会話・物語生成・娯楽の参照用途に限定する",
        "  - 出生時刻・出生地などの個人情報は明示的同意と最小化原則に従う",
        "  - 医療・雇用・教育・保険・信用・法執行など高影響判断には利用しない",
    ])
    pack = {
        "output_dir": "vol31_divination_reference/divination_reference_001_100",
        "index_filename": "divination_reference_001_100_index.yml",
        "index_content": "\n".join(index_lines) + "\n",
        "items": items,
    }
    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(json.dumps(pack, ensure_ascii=False, indent=2), encoding="utf-8")
    print(f"Created: {OUT}")
    print(f"Items: {len(items)}")


if __name__ == "__main__":
    main()
