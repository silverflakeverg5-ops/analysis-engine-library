import json
from pathlib import Path

OUT = Path("data/master_packs/vol7_environment_151_200.json")

SECTIONS = [
    {
        "category": "Environment - Motivation Context",
        "name_ja": "環境要因・動機づけ文脈",
        "items": [
            ("ENV-000151", "reward_rich_environment", "報酬豊富環境", "Reward Rich Environment", "成功・報酬・称賛を得やすく行動意欲が高まりやすい環境。"),
            ("ENV-000152", "punishment_focused_environment", "罰重視環境", "Punishment Focused Environment", "失敗回避や罰を避けることが重視される環境。"),
            ("ENV-000153", "goal_visibility", "目標可視性", "Goal Visibility", "目標や進捗が明確に見える環境。"),
            ("ENV-000154", "progress_feedback_environment", "進捗フィードバック環境", "Progress Feedback Environment", "進捗状況を継続的に確認できる環境。"),
            ("ENV-000155", "autonomy_environment", "自律性環境", "Autonomy Environment", "自分で選択・決定・工夫できる余地が大きい環境。"),
            ("ENV-000156", "competence_support_environment", "有能感支援環境", "Competence Support Environment", "成長や達成感を得やすい支援がある環境。"),
            ("ENV-000157", "relatedness_support_environment", "関係性支援環境", "Relatedness Support Environment", "所属感や人とのつながりを得やすい環境。"),
            ("ENV-000158", "achievement_tracking", "達成記録環境", "Achievement Tracking", "成果や努力が継続的に記録・可視化される環境。"),
            ("ENV-000159", "challenge_level_environment", "挑戦水準環境", "Challenge Level Environment", "課題難易度が能力と適切に釣り合っている環境。"),
            ("ENV-000160", "mastery_environment", "熟達志向環境", "Mastery Environment", "能力向上や学習そのものが重視される環境。")
        ]
    },
    {
        "category": "Environment - Technology",
        "name_ja": "環境要因・テクノロジー",
        "items": [
            ("ENV-000161", "ai_assistance_environment", "AI支援環境", "AI Assistance Environment", "AIによる補助・提案・自動化を受けられる環境。"),
            ("ENV-000162", "automation_environment", "自動化環境", "Automation Environment", "反復作業や判断の一部が自動化されている環境。"),
            ("ENV-000163", "digital_collaboration", "デジタル協働環境", "Digital Collaboration", "オンラインツールで共同作業しやすい環境。"),
            ("ENV-000164", "cloud_access", "クラウドアクセス", "Cloud Access", "クラウドサービスを利用しやすい環境。"),
            ("ENV-000165", "device_quality", "デバイス品質", "Device Quality", "利用端末の性能や安定性が十分である環境。"),
            ("ENV-000166", "internet_quality", "通信品質", "Internet Quality", "通信速度や接続安定性が十分である環境。"),
            ("ENV-000167", "digital_security_environment", "デジタル安全環境", "Digital Security Environment", "セキュリティ対策が十分なIT環境。"),
            ("ENV-000168", "multi_device_environment", "マルチデバイス環境", "Multi Device Environment", "複数端末を柔軟に利用できる環境。"),
            ("ENV-000169", "assistive_technology", "支援技術環境", "Assistive Technology", "認知・身体・学習を補助する技術が利用できる環境。"),
            ("ENV-000170", "technology_change_rate", "技術変化速度", "Technology Change Rate", "利用環境の技術変化が速い度合い。")
        ]
    },
    {
        "category": "Environment - Organizational",
        "name_ja": "環境要因・組織",
        "items": [
            ("ENV-000171", "organizational_culture", "組織文化", "Organizational Culture", "組織内で共有される価値観・行動様式・規範。"),
            ("ENV-000172", "innovation_climate", "革新風土", "Innovation Climate", "挑戦や改善提案が歓迎される組織環境。"),
            ("ENV-000173", "bureaucracy_level", "官僚性", "Bureaucracy Level", "ルール・手続き・承認が多い組織環境。"),
            ("ENV-000174", "decision_speed_environment", "意思決定速度環境", "Decision Speed Environment", "組織内の意思決定が迅速かどうか。"),
            ("ENV-000175", "organizational_transparency", "組織透明性", "Organizational Transparency", "情報共有や意思決定過程が見えやすい環境。"),
            ("ENV-000176", "leadership_style_environment", "リーダーシップ環境", "Leadership Style Environment", "上位者の指導・支援スタイルに関する環境。"),
            ("ENV-000177", "team_cohesion", "チーム結束", "Team Cohesion", "メンバー同士の協力・信頼・一体感。"),
            ("ENV-000178", "organizational_fairness", "組織公平性", "Organizational Fairness", "評価・処遇・意思決定が公平と感じられる環境。"),
            ("ENV-000179", "change_frequency", "変化頻度", "Change Frequency", "制度・方針・担当などが頻繁に変化する環境。"),
            ("ENV-000180", "organizational_stability", "組織安定性", "Organizational Stability", "役割や方針が安定している環境。")
        ]
    },
    {
        "category": "Environment - Regional",
        "name_ja": "環境要因・地域",
        "items": [
            ("ENV-000181", "urban_environment", "都市環境", "Urban Environment", "都市部特有の人口密度・交通・情報量を持つ環境。"),
            ("ENV-000182", "rural_environment", "地方環境", "Rural Environment", "地方・農村特有の生活・人間関係・自然環境。"),
            ("ENV-000183", "community_safety", "地域安全性", "Community Safety", "地域全体の安全・安心の度合い。"),
            ("ENV-000184", "public_service_access", "公共サービスアクセス", "Public Service Access", "行政・教育・医療など公共サービスへのアクセス。"),
            ("ENV-000185", "green_space_access", "緑地アクセス", "Green Space Access", "自然や公園へアクセスしやすい環境。"),
            ("ENV-000186", "disaster_risk_environment", "災害リスク環境", "Disaster Risk Environment", "自然災害や事故リスクが高い地域環境。"),
            ("ENV-000187", "climate_environment", "気候環境", "Climate Environment", "気温・湿度・季節変化などの地域環境。"),
            ("ENV-000188", "population_density", "人口密度", "Population Density", "生活圏内の人口集中度。"),
            ("ENV-000189", "regional_economic_environment", "地域経済環境", "Regional Economic Environment", "地域の雇用・産業・経済状況。"),
            ("ENV-000190", "local_identity", "地域アイデンティティ", "Local Identity", "地域への愛着や帰属意識。")
        ]
    },
    {
        "category": "Environment - Global",
        "name_ja": "環境要因・グローバル",
        "items": [
            ("ENV-000191", "globalization_environment", "グローバル化環境", "Globalization Environment", "国境を越えた情報・文化・経済交流が進んだ環境。"),
            ("ENV-000192", "multicultural_environment", "多文化環境", "Multicultural Environment", "複数文化が共存する生活・教育・職場環境。"),
            ("ENV-000193", "language_diversity", "言語多様性", "Language Diversity", "複数言語が利用される環境。"),
            ("ENV-000194", "international_collaboration", "国際協働環境", "International Collaboration", "国や文化を超えた共同作業環境。"),
            ("ENV-000195", "global_information_flow", "国際情報流通", "Global Information Flow", "海外情報へ接触しやすい環境。"),
            ("ENV-000196", "cross_cultural_experience", "異文化経験", "Cross Cultural Experience", "異文化交流や海外経験が得られる環境。"),
            ("ENV-000197", "mobility_environment", "移動性環境", "Mobility Environment", "国内外への移動や生活拠点変更が容易な環境。"),
            ("ENV-000198", "global_crisis_exposure", "世界的危機接触", "Global Crisis Exposure", "感染症・戦争・経済危機など世界規模の出来事の影響。"),
            ("ENV-000199", "global_opportunity_environment", "国際機会環境", "Global Opportunity Environment", "海外で学習・仕事・交流の機会を得やすい環境。"),
            ("ENV-000200", "environmental_integration", "環境統合", "Environmental Integration", "家庭・学校・社会・文化など複数環境が統合して人に影響する状態。")
        ]
    }
]


def make_item(item_id, slug, name_ja, name_en, definition_ja, category, parent_ja):
    return {
        "filename": f"{item_id}_{slug}.yml",
        "id": item_id,
        "knowledge_type": "environment_factor",
        "name_ja": name_ja,
        "name_en": name_en,
        "category": "Environment",
        "attribute": category.replace("Environment - ", ""),
        "definition_ja": definition_ja,
        "tags": ["CAT:環境要因", f"CAT:{parent_ja}", "ATTR:補正要因"],
        "parent": [parent_ja],
        "related": ["行動観測", "性格", "認知科学"],
        "observable_data": [
            f"{name_ja}関連行動変化",
            f"{name_ja}関連反応時間",
            f"{name_ja}関連継続率",
            f"{name_ja}関連ストレス反応"
        ],
        "signal_candidates": [
            f"{name_ja}が行動・感情・判断に影響している可能性がある",
            "環境条件の変化に応じて行動パターンが変化する"
        ],
        "device_level": "スマホ・PCのみ推定可能",
        "modifiers": ["年齢", "文化", "生活状況", "個人差"],
        "evidence": "環境心理学・発達心理学・社会心理学・HCI研究で使用",
        "status": "active"
    }


def main():
    all_items = []
    index_lines = ["category: Environment", "name_ja: 環境要因", "items:"]

    for section in SECTIONS:
        parent_ja = section["name_ja"].replace("環境要因・", "")
        for raw in section["items"]:
            item = make_item(*raw, category=section["category"], parent_ja=parent_ja)
            all_items.append(item)
            index_lines.append(f"  - {item['filename']}")

    index_lines.extend([
        "notes:",
        "  - 環境要因は本人特性ではなく補正要因として扱う",
        "  - 観測可能データとSignal候補を中心に管理する",
        "  - アプリ側でスコアリング・推論・表示を行う"
    ])

    pack = {
        "output_dir": "vol7_environment/environment_151_200",
        "index_filename": "environment_151_200_index.yml",
        "index_content": "\n".join(index_lines) + "\n",
        "items": all_items
    }

    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(json.dumps(pack, ensure_ascii=False, indent=2), encoding="utf-8")

    print(f"Created: {OUT}")
    print(f"Items: {len(all_items)}")


if __name__ == "__main__":
    main()