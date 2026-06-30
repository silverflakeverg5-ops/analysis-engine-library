import json
from pathlib import Path

OUT = Path("data/master_packs/vol7_environment_101_150.json")

SECTIONS = [
    {
        "category": "Environment - Health Lifestyle",
        "name_ja": "環境要因・健康生活",
        "items": [
            ("ENV-000101", "physical_activity_environment", "身体活動環境", "Physical Activity Environment", "運動・歩行・身体活動を行いやすい生活環境。"),
            ("ENV-000102", "exercise_access", "運動アクセス", "Exercise Access", "ジム・公園・運動施設・時間など運動機会へのアクセス。"),
            ("ENV-000103", "sedentary_environment", "座位中心環境", "Sedentary Environment", "長時間座位や低活動状態が続きやすい生活・職場環境。"),
            ("ENV-000104", "nutrition_environment", "栄養環境", "Nutrition Environment", "食事内容・栄養バランス・食材選択に影響する環境。"),
            ("ENV-000105", "substance_exposure_environment", "嗜好品接触環境", "Substance Exposure Environment", "飲酒・喫煙・カフェインなど嗜好品に接触しやすい環境。"),
            ("ENV-000106", "healthcare_access", "医療アクセス", "Healthcare Access", "医療機関・相談先・予防支援へアクセスできる度合い。"),
            ("ENV-000107", "preventive_health_environment", "予防健康環境", "Preventive Health Environment", "健康診断・予防接種・生活改善支援を受けやすい環境。"),
            ("ENV-000108", "illness_management_environment", "疾病管理環境", "Illness Management Environment", "体調不良や慢性症状を管理しやすい支援・生活環境。"),
            ("ENV-000109", "recovery_support", "回復支援", "Recovery Support", "病気・疲労・ストレスから回復するための支援や休息環境。"),
            ("ENV-000110", "health_literacy_environment", "健康リテラシー環境", "Health Literacy Environment", "健康情報を理解・活用しやすい情報環境。")
        ]
    },
    {
        "category": "Environment - Information Media",
        "name_ja": "環境要因・情報メディア",
        "items": [
            ("ENV-000111", "news_exposure", "ニュース接触", "News Exposure", "ニュースや時事情報に接触する頻度・媒体・偏り。"),
            ("ENV-000112", "media_trust_environment", "メディア信頼環境", "Media Trust Environment", "情報源や媒体への信頼が形成される情報環境。"),
            ("ENV-000113", "echo_chamber_environment", "エコーチェンバー環境", "Echo Chamber Environment", "似た意見や価値観の情報に偏って接触しやすい環境。"),
            ("ENV-000114", "misinformation_exposure", "誤情報接触", "Misinformation Exposure", "誤情報・不正確情報・誘導的情報に接触しやすい環境。"),
            ("ENV-000115", "information_quality", "情報品質", "Information Quality", "接触する情報の正確性・明確性・根拠の質。"),
            ("ENV-000116", "content_recommendation_environment", "コンテンツ推薦環境", "Content Recommendation Environment", "推薦システムによって情報接触が形成される環境。"),
            ("ENV-000117", "attention_economy_environment", "注意経済環境", "Attention Economy Environment", "注意を奪う設計や刺激が多い情報環境。"),
            ("ENV-000118", "media_multitasking_environment", "メディアマルチタスク環境", "Media Multitasking Environment", "複数媒体を同時利用しやすい情報環境。"),
            ("ENV-000119", "visual_media_environment", "視覚メディア環境", "Visual Media Environment", "画像・動画・短尺コンテンツ中心の情報接触環境。"),
            ("ENV-000120", "long_form_information_access", "長文情報アクセス", "Long Form Information Access", "書籍・記事・論文など長文情報へ接触できる環境。")
        ]
    },
    {
        "category": "Environment - Task Context",
        "name_ja": "環境要因・課題文脈",
        "items": [
            ("ENV-000121", "task_complexity", "課題複雑性", "Task Complexity", "課題に含まれる要素数・手順・判断量の多さ。"),
            ("ENV-000122", "task_clarity", "課題明確性", "Task Clarity", "何をすべきか、成功条件がどれだけ明確かを示す環境要因。"),
            ("ENV-000123", "task_novelty", "課題新奇性", "Task Novelty", "課題が本人にとって新しい・未知である度合い。"),
            ("ENV-000124", "task_autonomy", "課題裁量", "Task Autonomy", "課題の進め方や選択に本人が関与できる度合い。"),
            ("ENV-000125", "task_feedback_availability", "課題フィードバック利用可能性", "Task Feedback Availability", "課題遂行中に結果や改善情報を得られる度合い。"),
            ("ENV-000126", "task_consequence", "課題結果影響度", "Task Consequence", "課題の成否が本人や周囲に与える影響の大きさ。"),
            ("ENV-000127", "task_interruptions", "課題中断", "Task Interruptions", "課題中に通知・呼びかけ・割込みが発生する度合い。"),
            ("ENV-000128", "task_resource_fit", "課題資源適合", "Task Resource Fit", "課題要求に対して時間・知識・道具が足りている度合い。"),
            ("ENV-000129", "task_repetition", "課題反復性", "Task Repetition", "同じ課題や類似作業を繰り返す度合い。"),
            ("ENV-000130", "task_meaningfulness", "課題意味づけ", "Task Meaningfulness", "課題が本人にとって価値や意味を持つ度合い。")
        ]
    },
    {
        "category": "Environment - Social Evaluation",
        "name_ja": "環境要因・社会的評価",
        "items": [
            ("ENV-000131", "evaluation_visibility", "評価可視性", "Evaluation Visibility", "本人の成果や行動が他者から見える度合い。"),
            ("ENV-000132", "public_performance_context", "公開パフォーマンス文脈", "Public Performance Context", "人前で成果や能力を示す必要がある環境。"),
            ("ENV-000133", "reputation_pressure", "評判プレッシャー", "Reputation Pressure", "周囲からの評価や評判を意識しやすい環境圧。"),
            ("ENV-000134", "comparison_metrics", "比較指標", "Comparison Metrics", "順位・点数・フォロワー数など他者比較を促す指標。"),
            ("ENV-000135", "approval_environment", "承認環境", "Approval Environment", "承認・称賛・いいねなどが得られやすい、または重視される環境。"),
            ("ENV-000136", "criticism_environment", "批判環境", "Criticism Environment", "批判・指摘・否定的評価を受けやすい環境。"),
            ("ENV-000137", "accountability_context", "説明責任文脈", "Accountability Context", "判断や行動について説明責任を求められる環境。"),
            ("ENV-000138", "status_hierarchy", "地位階層", "Status Hierarchy", "立場や地位の差が行動や発言に影響する環境。"),
            ("ENV-000139", "peer_recognition", "仲間からの承認", "Peer Recognition", "同年代・同僚・仲間からの承認が行動に影響する環境。"),
            ("ENV-000140", "social_penalty_risk", "社会的ペナルティリスク", "Social Penalty Risk", "失敗・逸脱・発言によって社会的評価が下がる可能性。")
        ]
    },
    {
        "category": "Environment - Support Systems",
        "name_ja": "環境要因・支援制度",
        "items": [
            ("ENV-000141", "formal_support_system", "公式支援制度", "Formal Support System", "学校・職場・行政などによる制度的支援。"),
            ("ENV-000142", "informal_support_network", "非公式支援ネットワーク", "Informal Support Network", "家族・友人・知人などによる非制度的支援。"),
            ("ENV-000143", "mental_health_support", "メンタルヘルス支援", "Mental Health Support", "心理相談・カウンセリング・相談窓口などの支援環境。"),
            ("ENV-000144", "learning_support_system", "学習支援制度", "Learning Support System", "補習・教材・チューター・学習相談などの支援。"),
            ("ENV-000145", "career_support_system", "キャリア支援制度", "Career Support System", "進路・就職・転職・能力開発を支える制度や人材。"),
            ("ENV-000146", "financial_support_system", "経済支援制度", "Financial Support System", "奨学金・補助金・扶助・貸付など経済的支援。"),
            ("ENV-000147", "accessibility_support", "アクセシビリティ支援", "Accessibility Support", "障壁を減らし利用や参加を可能にする支援。"),
            ("ENV-000148", "crisis_support", "危機時支援", "Crisis Support", "急な困難・災害・失業・健康問題への緊急支援。"),
            ("ENV-000149", "community_support", "地域支援", "Community Support", "地域やコミュニティによる生活・交流・安心の支援。"),
            ("ENV-000150", "digital_support_tools", "デジタル支援ツール", "Digital Support Tools", "予定管理・学習支援・健康管理などを補助するデジタルツール環境。")
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
        "output_dir": "vol7_environment/environment_101_150",
        "index_filename": "environment_101_150_index.yml",
        "index_content": "\n".join(index_lines) + "\n",
        "items": all_items
    }

    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(json.dumps(pack, ensure_ascii=False, indent=2), encoding="utf-8")

    print(f"Created: {OUT}")
    print(f"Items: {len(all_items)}")


if __name__ == "__main__":
    main()