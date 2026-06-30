import json
from pathlib import Path

OUT = Path("data/master_packs/vol7_environment_001_050.json")

SECTIONS = [
    {
        "category": "Environment - Family",
        "name_ja": "環境要因・家庭",
        "items": [
            ("ENV-000001", "family_structure", "家族構成", "Family Structure", "同居家族・兄弟姉妹・保護者構成など、家庭内の基本的な人的構成。"),
            ("ENV-000002", "parenting_style", "養育スタイル", "Parenting Style", "保護者の関わり方・規律・支援・自律性の与え方に関する環境要因。"),
            ("ENV-000003", "family_communication", "家庭内コミュニケーション", "Family Communication", "家庭内での会話量・感情表現・相談しやすさに関する環境要因。"),
            ("ENV-000004", "family_support", "家庭内支援", "Family Support", "学習・生活・感情面で家族から得られる支援の度合い。"),
            ("ENV-000005", "family_conflict", "家庭内葛藤", "Family Conflict", "家庭内での対立・緊張・不和が行動や感情に影響する環境要因。"),
            ("ENV-000006", "household_routine", "家庭内ルーティン", "Household Routine", "食事・睡眠・学習・家事などの生活リズムや習慣の安定性。"),
            ("ENV-000007", "home_learning_environment", "家庭学習環境", "Home Learning Environment", "家庭内で学習・読書・作業に取り組みやすい物理的・心理的環境。"),
            ("ENV-000008", "emotional_safety_at_home", "家庭内心理的安全性", "Emotional Safety at Home", "家庭内で安心して感情や意見を表現できる度合い。"),
            ("ENV-000009", "family_expectations", "家族からの期待", "Family Expectations", "家族が本人に対して持つ達成・進路・行動面の期待。"),
            ("ENV-000010", "caregiving_responsibility", "家庭内ケア責任", "Caregiving Responsibility", "家族の世話や家事など、本人が担う家庭内責任の度合い。")
        ]
    },
    {
        "category": "Environment - Education",
        "name_ja": "環境要因・教育",
        "items": [
            ("ENV-000011", "school_climate", "学校風土", "School Climate", "学校全体の安全性・支援性・規律・対人関係の雰囲気。"),
            ("ENV-000012", "teacher_support", "教師支援", "Teacher Support", "教師からの説明・励まし・フィードバック・相談対応の得られやすさ。"),
            ("ENV-000013", "peer_learning_environment", "ピア学習環境", "Peer Learning Environment", "友人や同級生と学び合い、助け合える学習環境。"),
            ("ENV-000014", "academic_pressure", "学業プレッシャー", "Academic Pressure", "成績・受験・課題量などによって生じる学業上の圧力。"),
            ("ENV-000015", "evaluation_frequency", "評価頻度", "Evaluation Frequency", "テスト・成績評価・レビューなど、外部評価を受ける頻度。"),
            ("ENV-000016", "feedback_quality", "フィードバック品質", "Feedback Quality", "学習や行動に対して得られるフィードバックの具体性・有用性・タイミング。"),
            ("ENV-000017", "learning_resources", "学習資源", "Learning Resources", "教材・端末・図書・支援者など、学習に使える資源の利用可能性。"),
            ("ENV-000018", "classroom_structure", "授業構造", "Classroom Structure", "授業の進行・課題設計・ルール・参加形式の明確さ。"),
            ("ENV-000019", "autonomy_supportive_education", "自律支援的教育", "Autonomy Supportive Education", "学習者の選択・意見・主体性を尊重する教育環境。"),
            ("ENV-000020", "competitive_school_environment", "競争的学校環境", "Competitive School Environment", "順位・成績・比較が強調される学校や学習環境。")
        ]
    },
    {
        "category": "Environment - Workplace",
        "name_ja": "環境要因・職場",
        "items": [
            ("ENV-000021", "workload", "業務負荷", "Workload", "仕事量・難易度・処理期限などによる職務上の負担。"),
            ("ENV-000022", "job_control", "職務裁量", "Job Control", "仕事の進め方・順序・判断に対して本人が持つ裁量の度合い。"),
            ("ENV-000023", "supervisor_support", "上司支援", "Supervisor Support", "上司からの相談対応・承認・調整・問題解決支援の得られやすさ。"),
            ("ENV-000024", "coworker_support", "同僚支援", "Coworker Support", "同僚からの情報共有・協力・感情的支援の得られやすさ。"),
            ("ENV-000025", "role_clarity", "役割明確性", "Role Clarity", "自分の責任範囲・期待成果・判断権限が明確である度合い。"),
            ("ENV-000026", "role_conflict", "役割葛藤", "Role Conflict", "複数の期待や指示が矛盾し、行動判断が難しくなる職場環境要因。"),
            ("ENV-000027", "psychological_safety_work", "職場心理的安全性", "Psychological Safety at Work", "職場で意見・失敗・懸念を安心して表明できる度合い。"),
            ("ENV-000028", "workplace_feedback", "職場フィードバック", "Workplace Feedback", "仕事の成果や行動に対して得られる評価・助言・修正情報。"),
            ("ENV-000029", "work_time_pressure", "業務時間圧", "Work Time Pressure", "期限・納期・即応要求によって生じる時間的圧力。"),
            ("ENV-000030", "career_uncertainty", "キャリア不確実性", "Career Uncertainty", "雇用・昇進・役割・将来見通しが不明確な状態。")
        ]
    },
    {
        "category": "Environment - Social Relationship",
        "name_ja": "環境要因・人間関係",
        "items": [
            ("ENV-000031", "social_support", "社会的支援", "Social Support", "家族・友人・同僚などから得られる感情的・実用的・情報的支援。"),
            ("ENV-000032", "friendship_quality", "友人関係の質", "Friendship Quality", "友人関係における信頼・安心感・相互支援・葛藤の少なさ。"),
            ("ENV-000033", "social_isolation", "社会的孤立", "Social Isolation", "他者との接点や支援的関係が少ない状態。"),
            ("ENV-000034", "loneliness", "孤独感", "Loneliness", "望む対人関係と実際の対人関係の差から生じる主観的な孤独感。"),
            ("ENV-000035", "peer_pressure", "同調圧力", "Peer Pressure", "周囲の期待や集団規範に合わせるよう求められる社会的圧力。"),
            ("ENV-000036", "relationship_conflict", "対人葛藤", "Relationship Conflict", "他者との意見不一致・感情的対立・摩擦がある状態。"),
            ("ENV-000037", "belongingness", "所属感", "Belongingness", "集団や関係性の中で受け入れられていると感じる度合い。"),
            ("ENV-000038", "social_comparison_environment", "社会的比較環境", "Social Comparison Environment", "他者との成績・外見・生活・成果比較が生じやすい環境。"),
            ("ENV-000039", "mentorship", "メンター関係", "Mentorship", "経験者や支援者から継続的な助言・支援・成長機会を得られる関係。"),
            ("ENV-000040", "community_connection", "コミュニティ接続", "Community Connection", "地域・趣味・オンライン・職場などの共同体とのつながり。")
        ]
    },
    {
        "category": "Environment - Digital",
        "name_ja": "環境要因・デジタル",
        "items": [
            ("ENV-000041", "screen_time_environment", "スクリーン時間環境", "Screen Time Environment", "スマホ・PC・テレビなど画面利用時間に影響する環境。"),
            ("ENV-000042", "notification_environment", "通知環境", "Notification Environment", "通知・アラート・メッセージが注意や行動を中断しやすい環境。"),
            ("ENV-000043", "social_media_exposure", "SNS接触", "Social Media Exposure", "SNS上の投稿・反応・比較・情報流入にさらされる度合い。"),
            ("ENV-000044", "algorithmic_feed_environment", "アルゴリズムフィード環境", "Algorithmic Feed Environment", "推薦アルゴリズムにより情報接触が偏るデジタル環境。"),
            ("ENV-000045", "online_feedback_environment", "オンライン評価環境", "Online Feedback Environment", "いいね・コメント・レビューなどオンライン反応を受けやすい環境。"),
            ("ENV-000046", "digital_distraction", "デジタル誘惑", "Digital Distraction", "アプリ・通知・動画・ゲームなどにより注意が逸れやすい環境要因。"),
            ("ENV-000047", "information_overload_environment", "情報過多環境", "Information Overload Environment", "処理可能量を超える情報量にさらされやすい環境。"),
            ("ENV-000048", "online_anonymity", "オンライン匿名性", "Online Anonymity", "身元や社会的評価が見えにくいオンライン環境の特性。"),
            ("ENV-000049", "digital_access", "デジタルアクセス", "Digital Access", "インターネット・端末・アプリ・情報資源へアクセスできる度合い。"),
            ("ENV-000050", "online_community_environment", "オンラインコミュニティ環境", "Online Community Environment", "オンライン上の集団・交流・規範・支援に関する環境要因。")
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
        "output_dir": "vol7_environment/environment_001_050",
        "index_filename": "environment_001_050_index.yml",
        "index_content": "\n".join(index_lines) + "\n",
        "items": all_items
    }

    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(json.dumps(pack, ensure_ascii=False, indent=2), encoding="utf-8")

    print(f"Created: {OUT}")
    print(f"Items: {len(all_items)}")


if __name__ == "__main__":
    main()