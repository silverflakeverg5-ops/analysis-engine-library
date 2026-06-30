import json
from pathlib import Path

OUT = Path("data/master_packs/vol14_app_use_cases_001_050.json")

SECTIONS = [
    {
        "category": "App Use Cases - Diagnosis",
        "name_ja": "アプリ用途・診断",
        "items": [
            ("APP-000001", "personality_diagnosis_app", "性格診断アプリ", "Personality Diagnosis App", "行動・回答・選択傾向から性格傾向を推測して表示するアプリ用途。"),
            ("APP-000002", "compatibility_diagnosis_app", "相性診断アプリ", "Compatibility Diagnosis App", "複数人の傾向や価値観から相性をエンタメ的に推測するアプリ用途。"),
            ("APP-000003", "self_understanding_app", "自己理解アプリ", "Self Understanding App", "自分の傾向・強み・注意点を知るためのアプリ用途。"),
            ("APP-000004", "behavior_style_diagnosis", "行動スタイル診断", "Behavior Style Diagnosis", "意思決定・学習・対人行動などの行動傾向を推測する用途。"),
            ("APP-000005", "work_style_diagnosis", "仕事スタイル診断", "Work Style Diagnosis", "集中・協力・判断・タスク管理など仕事上の傾向を推測する用途。"),
            ("APP-000006", "learning_style_diagnosis", "学習スタイル診断", "Learning Style Diagnosis", "学習方略・継続・理解・復習傾向を推測する用途。"),
            ("APP-000007", "communication_style_diagnosis", "コミュニケーション診断", "Communication Style Diagnosis", "発話・返信・自己主張・共感など対人表現傾向を推測する用途。"),
            ("APP-000008", "stress_tendency_diagnosis", "ストレス傾向診断", "Stress Tendency Diagnosis", "負荷・回復・回避・感情変化の傾向を推測する用途。"),
            ("APP-000009", "motivation_tendency_diagnosis", "動機づけ傾向診断", "Motivation Tendency Diagnosis", "報酬・達成・承認・自律性への反応傾向を推測する用途。"),
            ("APP-000010", "decision_tendency_diagnosis", "意思決定傾向診断", "Decision Tendency Diagnosis", "リスク選択・迷い・即断・慎重さなどの判断傾向を推測する用途。")
        ]
    },
    {
        "category": "App Use Cases - Game",
        "name_ja": "アプリ用途・ゲーム",
        "items": [
            ("APP-000011", "personality_game_app", "性格ゲームアプリ", "Personality Game App", "ゲーム内行動から性格や行動傾向を推測して楽しむアプリ用途。"),
            ("APP-000012", "choice_based_game_analysis", "選択型ゲーム分析", "Choice Based Game Analysis", "分岐選択や判断履歴から傾向を推測するゲーム用途。"),
            ("APP-000013", "puzzle_behavior_analysis", "パズル行動分析", "Puzzle Behavior Analysis", "パズルの解き方・試行錯誤・ヒント利用から認知傾向を推測する用途。"),
            ("APP-000014", "strategy_game_analysis", "戦略ゲーム分析", "Strategy Game Analysis", "計画・資源配分・リスク選択から思考傾向を推測する用途。"),
            ("APP-000015", "reaction_game_analysis", "反応ゲーム分析", "Reaction Game Analysis", "反応時間・ミス・集中持続から状態や傾向を推測する用途。"),
            ("APP-000016", "social_game_analysis", "ソーシャルゲーム分析", "Social Game Analysis", "協力・競争・援助・交流から対人傾向を推測する用途。"),
            ("APP-000017", "simulation_game_analysis", "シミュレーションゲーム分析", "Simulation Game Analysis", "仮想環境での選択・管理・優先順位から傾向を推測する用途。"),
            ("APP-000018", "mini_game_signal_collection", "ミニゲームシグナル収集", "Mini Game Signal Collection", "短時間ゲームから観測シグナルを取得する用途。"),
            ("APP-000019", "game_based_learning_support", "ゲーム型学習支援", "Game Based Learning Support", "ゲーム要素を使って学習行動や継続を支援する用途。"),
            ("APP-000020", "entertainment_analysis_app", "エンタメ分析アプリ", "Entertainment Analysis App", "断定ではなく遊びとして傾向推測を提示するアプリ用途。")
        ]
    },
    {
        "category": "App Use Cases - Assistant",
        "name_ja": "アプリ用途・秘書",
        "items": [
            ("APP-000021", "personal_assistant_app", "個人秘書アプリ", "Personal Assistant App", "予定・タスク・生活文脈に応じて支援や提案を行うアプリ用途。"),
            ("APP-000022", "schedule_support_app", "スケジュール支援アプリ", "Schedule Support App", "予定登録・通知・準備・移動を支援する用途。"),
            ("APP-000023", "task_management_support", "タスク管理支援", "Task Management Support", "優先順位・期限・進捗・中断復帰を支援する用途。"),
            ("APP-000024", "context_aware_reminder", "文脈対応リマインダー", "Context Aware Reminder", "時間・場所・状態・予定に応じて通知する用途。"),
            ("APP-000025", "proactive_suggestion_app", "先回り提案アプリ", "Proactive Suggestion App", "予定や行動文脈から必要な提案を先回りして出す用途。"),
            ("APP-000026", "travel_planning_assistant", "旅行計画秘書", "Travel Planning Assistant", "旅行予定に合わせて準備・移動・天気・候補地を支援する用途。"),
            ("APP-000027", "daily_briefing_assistant", "日次ブリーフィング秘書", "Daily Briefing Assistant", "予定・天気・タスク・注意点を日次で整理する用途。"),
            ("APP-000028", "work_assistant_app", "仕事秘書アプリ", "Work Assistant App", "業務予定・集中・会議・タスク整理を支援する用途。"),
            ("APP-000029", "life_log_assistant", "ライフログ秘書", "Life Log Assistant", "生活リズム・行動履歴・状態変化を記録し支援する用途。"),
            ("APP-000030", "adaptive_notification_assistant", "適応通知秘書", "Adaptive Notification Assistant", "ユーザー状態や文脈に合わせて通知タイミングを調整する用途。")
        ]
    },
    {
        "category": "App Use Cases - Education",
        "name_ja": "アプリ用途・教育",
        "items": [
            ("APP-000031", "learning_support_app", "学習支援アプリ", "Learning Support App", "学習計画・復習・理解確認・継続を支援するアプリ用途。"),
            ("APP-000032", "adaptive_learning_app", "適応学習アプリ", "Adaptive Learning App", "学習者の成績や状態に応じて内容や難易度を調整する用途。"),
            ("APP-000033", "study_habit_app", "学習習慣アプリ", "Study Habit App", "学習継続・復習・目標達成を習慣化する用途。"),
            ("APP-000034", "exam_preparation_app", "試験対策アプリ", "Exam Preparation App", "試験に向けた学習計画・弱点補強・復習管理を支援する用途。"),
            ("APP-000035", "metacognition_training_app", "メタ認知訓練アプリ", "Metacognition Training App", "理解度判断・振り返り・方略調整を支援する用途。"),
            ("APP-000036", "feedback_learning_app", "フィードバック学習アプリ", "Feedback Learning App", "正誤・解説・改善提案を通じて学習を支援する用途。"),
            ("APP-000037", "collaborative_learning_app", "協同学習アプリ", "Collaborative Learning App", "学習者同士の共有・説明・相互支援を促す用途。"),
            ("APP-000038", "skill_training_app", "技能訓練アプリ", "Skill Training App", "反復練習・熟達化・進捗可視化を支援する用途。"),
            ("APP-000039", "learning_analytics_app", "学習分析アプリ", "Learning Analytics App", "学習ログを可視化し改善や支援に使う用途。"),
            ("APP-000040", "career_learning_app", "キャリア学習アプリ", "Career Learning App", "仕事や進路に必要な学習・スキル形成を支援する用途。")
        ]
    },
    {
        "category": "App Use Cases - Work Support",
        "name_ja": "アプリ用途・仕事支援",
        "items": [
            ("APP-000041", "productivity_support_app", "生産性支援アプリ", "Productivity Support App", "集中・タスク・優先順位・進捗を支援するアプリ用途。"),
            ("APP-000042", "focus_support_app", "集中支援アプリ", "Focus Support App", "中断管理・作業時間・休憩・集中維持を支援する用途。"),
            ("APP-000043", "meeting_support_app", "会議支援アプリ", "Meeting Support App", "議題・発言・要約・次アクション整理を支援する用途。"),
            ("APP-000044", "team_collaboration_support", "チーム協働支援", "Team Collaboration Support", "役割・進捗・協力・情報共有を支援する用途。"),
            ("APP-000045", "workload_monitoring_app", "業務負荷モニタリング", "Workload Monitoring App", "業務量・中断・疲労兆候を把握し支援する用途。"),
            ("APP-000046", "career_support_app", "キャリア支援アプリ", "Career Support App", "スキル・目標・職務適性・成長計画を支援する用途。"),
            ("APP-000047", "decision_support_app", "意思決定支援アプリ", "Decision Support App", "選択肢比較・リスク・優先順位判断を支援する用途。"),
            ("APP-000048", "workflow_optimization_app", "ワークフロー最適化アプリ", "Workflow Optimization App", "作業手順・自動化・中断削減を支援する用途。"),
            ("APP-000049", "work_wellbeing_support", "職場ウェルビーイング支援", "Work Wellbeing Support", "ストレス・疲労・回復・心理的安全性を支援する用途。"),
            ("APP-000050", "human_performance_support", "人間パフォーマンス支援", "Human Performance Support", "認知・状態・環境を考慮して行動成果を支援する用途。")
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
        "output_dir": "vol14_app_use_cases/app_use_cases_001_050",
        "index_filename": "app_use_cases_001_050_index.yml",
        "index_content": "\n".join(index_lines) + "\n",
        "items": all_items
    }

    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(json.dumps(pack, ensure_ascii=False, indent=2), encoding="utf-8")

    print(f"Created: {OUT}")
    print(f"Items: {len(all_items)}")


if __name__ == "__main__":
    main()