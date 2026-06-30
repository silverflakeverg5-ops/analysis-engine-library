import json
from pathlib import Path

OUT = Path("data/master_packs/vol14_app_use_cases_051_100.json")

SECTIONS = [
    {
        "category": "App Use Cases - Wellbeing",
        "name_ja": "アプリ用途・ウェルビーイング",
        "items": [
            ("APP-000051", "wellbeing_tracking_app", "ウェルビーイング記録アプリ", "Wellbeing Tracking App", "気分・睡眠・疲労・生活リズムを記録し状態理解を支援する用途。"),
            ("APP-000052", "stress_management_app", "ストレス管理アプリ", "Stress Management App", "ストレス兆候や回復行動を把握しセルフケアを支援する用途。"),
            ("APP-000053", "sleep_support_app", "睡眠支援アプリ", "Sleep Support App", "睡眠時間・規則性・回復感を把握し生活改善を支援する用途。"),
            ("APP-000054", "fatigue_monitoring_app", "疲労モニタリングアプリ", "Fatigue Monitoring App", "疲労兆候や過負荷を観測し休息提案に活用する用途。"),
            ("APP-000055", "emotion_journal_app", "感情ジャーナルアプリ", "Emotion Journal App", "感情変化や出来事を記録し自己理解を支援する用途。"),
            ("APP-000056", "habit_health_app", "健康習慣アプリ", "Health Habit App", "運動・食事・睡眠など健康行動の習慣化を支援する用途。"),
            ("APP-000057", "recovery_support_app", "回復支援アプリ", "Recovery Support App", "負荷後の休息・回復・行動再開を支援する用途。"),
            ("APP-000058", "mind_body_awareness_app", "心身気づきアプリ", "Mind Body Awareness App", "身体信号や気分の変化への気づきを促す用途。"),
            ("APP-000059", "lifestyle_balance_app", "生活バランスアプリ", "Lifestyle Balance App", "仕事・学習・休息・余暇のバランス調整を支援する用途。"),
            ("APP-000060", "gentle_support_app", "やさしい支援アプリ", "Gentle Support App", "断定や評価を避け、穏やかな提案で行動支援を行う用途。")
        ]
    },
    {
        "category": "App Use Cases - Social Relationship",
        "name_ja": "アプリ用途・人間関係",
        "items": [
            ("APP-000061", "relationship_reflection_app", "人間関係振り返りアプリ", "Relationship Reflection App", "対人関係の傾向や距離感を振り返る用途。"),
            ("APP-000062", "communication_support_app", "コミュニケーション支援アプリ", "Communication Support App", "返信・自己主張・説明・共感表現を支援する用途。"),
            ("APP-000063", "conflict_prevention_app", "葛藤予防アプリ", "Conflict Prevention App", "対人摩擦や誤解を減らすための行動提案を行う用途。"),
            ("APP-000064", "team_relationship_app", "チーム関係支援アプリ", "Team Relationship App", "チーム内の協力・役割・信頼形成を支援する用途。"),
            ("APP-000065", "social_skill_training_app", "社会スキル練習アプリ", "Social Skill Training App", "会話・主張・傾聴・協力などの社会的技能を練習する用途。"),
            ("APP-000066", "empathy_training_app", "共感トレーニングアプリ", "Empathy Training App", "視点取得や感情理解を練習する用途。"),
            ("APP-000067", "conversation_analysis_app", "会話分析アプリ", "Conversation Analysis App", "発話量・返信・表現傾向から会話行動を振り返る用途。"),
            ("APP-000068", "social_support_matching_app", "社会的支援マッチングアプリ", "Social Support Matching App", "相談先・支援先・協力者を見つけやすくする用途。"),
            ("APP-000069", "online_community_support_app", "オンラインコミュニティ支援アプリ", "Online Community Support App", "オンライン交流の安全性・参加・支援を促す用途。"),
            ("APP-000070", "relationship_boundary_support", "関係境界支援", "Relationship Boundary Support", "距離感・断り方・情報開示の調整を支援する用途。")
        ]
    },
    {
        "category": "App Use Cases - Personalization",
        "name_ja": "アプリ用途・個別化",
        "items": [
            ("APP-000071", "personalization_engine_app", "個別化エンジン用途", "Personalization Engine App", "行動傾向や文脈に合わせて表示・通知・提案を調整する用途。"),
            ("APP-000072", "adaptive_ui_app", "適応UIアプリ", "Adaptive UI App", "利用者の状態や熟達度に応じて画面や操作を調整する用途。"),
            ("APP-000073", "adaptive_notification_app", "適応通知アプリ", "Adaptive Notification App", "通知頻度・タイミング・表現をユーザー文脈に合わせる用途。"),
            ("APP-000074", "recommendation_personalization_app", "推薦個別化アプリ", "Recommendation Personalization App", "興味・履歴・状態に応じて情報や行動を推薦する用途。"),
            ("APP-000075", "difficulty_adaptation_app", "難易度適応アプリ", "Difficulty Adaptation App", "課題やゲームの難易度を能力・状態に合わせて調整する用途。"),
            ("APP-000076", "content_adaptation_app", "コンテンツ適応アプリ", "Content Adaptation App", "説明量・形式・順序を理解度や文脈に応じて変える用途。"),
            ("APP-000077", "tone_adaptation_app", "表現トーン適応アプリ", "Tone Adaptation App", "ユーザー状態や用途に応じて表示表現の強さを調整する用途。"),
            ("APP-000078", "support_timing_app", "支援タイミング調整アプリ", "Support Timing App", "介入や提案を出す時点を状態や文脈に合わせる用途。"),
            ("APP-000079", "user_preference_learning_app", "ユーザー嗜好学習アプリ", "User Preference Learning App", "利用履歴から好みや反応傾向を学習し調整する用途。"),
            ("APP-000080", "adaptive_experience_app", "適応体験アプリ", "Adaptive Experience App", "アプリ体験全体を個人差と文脈に合わせて調整する用途。")
        ]
    },
    {
        "category": "App Use Cases - Safety Ethics",
        "name_ja": "アプリ用途・安全倫理",
        "items": [
            ("APP-000081", "safe_diagnosis_display", "安全な診断表示", "Safe Diagnosis Display", "診断結果を断定・序列化せず安全に提示する用途。"),
            ("APP-000082", "non_diagnostic_feedback_app", "非診断フィードバックアプリ", "Non Diagnostic Feedback App", "医療・性格断定ではなく傾向や可能性として返す用途。"),
            ("APP-000083", "privacy_sensitive_app", "プライバシー配慮アプリ", "Privacy Sensitive App", "個人情報や機微情報を慎重に扱う用途。"),
            ("APP-000084", "minor_safe_app", "未成年配慮アプリ", "Minor Safe App", "未成年ユーザーへの表示・推論・提案を慎重化する用途。"),
            ("APP-000085", "high_stakes_guardrail_app", "高リスク判断ガードレールアプリ", "High Stakes Guardrail App", "進路・健康・雇用など重大判断への過度利用を防ぐ用途。"),
            ("APP-000086", "consent_management_app", "同意管理アプリ", "Consent Management App", "データ利用・推論表示・個別化に関する同意を管理する用途。"),
            ("APP-000087", "explainable_feedback_app", "説明可能フィードバックアプリ", "Explainable Feedback App", "推論材料や根拠を分かりやすく説明する用途。"),
            ("APP-000088", "user_correction_app", "ユーザー修正アプリ", "User Correction App", "ユーザーが推論結果や前提を修正できる用途。"),
            ("APP-000089", "ethical_audit_app", "倫理監査アプリ", "Ethical Audit App", "推論・表示・データ利用が安全か確認する用途。"),
            ("APP-000090", "safe_personalization_app", "安全な個別化アプリ", "Safe Personalization App", "過度な誘導や操作を避けて個別化する用途。")
        ]
    },
    {
        "category": "App Use Cases - Integration",
        "name_ja": "アプリ用途・統合",
        "items": [
            ("APP-000091", "multi_domain_human_analysis_app", "領域横断人間分析アプリ", "Multi Domain Human Analysis App", "認知・性格・行動・環境を横断して傾向理解を支援する用途。"),
            ("APP-000092", "cross_app_knowledge_use", "複数アプリ知識利用", "Cross App Knowledge Use", "共通Knowledge DBを複数アプリで利用する用途。"),
            ("APP-000093", "contextual_inference_app", "文脈推論アプリ", "Contextual Inference App", "観測シグナルを文脈・状態・補正要因と組み合わせる用途。"),
            ("APP-000094", "human_state_support_app", "人間状態支援アプリ", "Human State Support App", "現在状態を推測し負荷・回復・行動支援に活用する用途。"),
            ("APP-000095", "behavior_change_support_app", "行動変容支援アプリ", "Behavior Change Support App", "習慣・目標・環境調整を通じて行動変化を支援する用途。"),
            ("APP-000096", "life_design_support_app", "生活設計支援アプリ", "Life Design Support App", "予定・習慣・学習・仕事・休息を総合的に支援する用途。"),
            ("APP-000097", "personal_growth_app", "自己成長支援アプリ", "Personal Growth App", "強み・学習・習慣・目標を長期的に支援する用途。"),
            ("APP-000098", "human_ai_coach_app", "AIコーチアプリ", "Human AI Coach App", "ユーザーの行動や状態に応じて助言・振り返りを行う用途。"),
            ("APP-000099", "knowledge_library_integration", "知識ライブラリ統合用途", "Knowledge Library Integration", "共通知識DBを各アプリの推論材料として接続する用途。"),
            ("APP-000100", "app_use_case_integration", "アプリ用途統合", "App Use Case Integration", "診断・ゲーム・秘書・教育・仕事支援などの用途を統合管理する枠組み。")
        ]
    }
]


def make_item(item_id, slug, name_ja, name_en, definition_ja, category, parent_ja):
    return {
        "filename": f"{item_id}_{slug}.yml",
        "id": item_id,
        "knowledge_type": "app_use_case",
        "name_ja": name_ja,
        "name_en": name_en,
        "category": "App Use Case",
        "attribute": category.replace("App Use Cases - ", ""),
        "definition_ja": definition_ja,
        "tags": ["CAT:アプリ用途", f"CAT:{parent_ja}", "ATTR:利用領域"],
        "parent": [parent_ja],
        "related": ["観測シグナル", "補正要因", "表示設計"],
        "observable_data": [
            f"{name_ja}利用文脈",
            f"{name_ja}対象シグナル",
            f"{name_ja}補正要因",
            f"{name_ja}表示目的"
        ],
        "signal_candidates": [
            f"{name_ja}で利用可能な知識項目を選定する材料になる",
            "アプリ用途に応じた推論・表示・補正の切り替え材料になる"
        ],
        "device_level": "DB管理用",
        "modifiers": ["用途", "対象ユーザー", "安全性", "表示形式"],
        "evidence": "HCI・UX設計・教育工学・行動支援設計で使用",
        "status": "active"
    }


def main():
    all_items = []
    index_lines = ["category: App Use Case", "name_ja: アプリ用途", "items:"]

    for section in SECTIONS:
        parent_ja = section["name_ja"].replace("アプリ用途・", "")
        for raw in section["items"]:
            item = make_item(*raw, category=section["category"], parent_ja=parent_ja)
            all_items.append(item)
            index_lines.append(f"  - {item['filename']}")

    index_lines.extend([
        "notes:",
        "  - アプリ用途はDB分類ではなく利用文脈の管理材料として扱う",
        "  - Knowledge DB側ではアプリ別推論を行わない",
        "  - アプリ側で用途に応じた推論・表示・補正を行う"
    ])

    pack = {
        "output_dir": "vol14_app_use_cases/app_use_cases_051_100",
        "index_filename": "app_use_cases_051_100_index.yml",
        "index_content": "\n".join(index_lines) + "\n",
        "items": all_items
    }

    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(json.dumps(pack, ensure_ascii=False, indent=2), encoding="utf-8")

    print(f"Created: {OUT}")
    print(f"Items: {len(all_items)}")


if __name__ == "__main__":
    main()