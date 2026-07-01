import json
from pathlib import Path

OUT = Path("data/master_packs/vol15_display_design_051_100.json")

SECTIONS = [
    {
        "category": "Display Design - Personalization",
        "name_ja": "表示設計・個別化",
        "items": [
            ("DISPLAY-000051", "personalized_result_display", "個別化結果表示", "Personalized Result Display", "ユーザーの文脈や履歴に合わせて結果表示を調整する設計。"),
            ("DISPLAY-000052", "adaptive_detail_level", "詳細度適応", "Adaptive Detail Level", "ユーザーの理解度や関心に応じて説明量を変える表示設計。"),
            ("DISPLAY-000053", "adaptive_tone_display", "トーン適応表示", "Adaptive Tone Display", "状態や用途に応じて表現の柔らかさや具体性を調整する設計。"),
            ("DISPLAY-000054", "user_selected_display_mode", "ユーザー選択表示モード", "User Selected Display Mode", "ユーザーが表示形式や説明量を選べる設計。"),
            ("DISPLAY-000055", "beginner_friendly_display", "初心者向け表示", "Beginner Friendly Display", "初めて利用するユーザーにも分かりやすい表示設計。"),
            ("DISPLAY-000056", "expert_mode_display", "詳細モード表示", "Expert Mode Display", "より詳しい根拠やシグナルを確認できる表示設計。"),
            ("DISPLAY-000057", "accessibility_display", "アクセシビリティ表示", "Accessibility Display", "読みやすさ・操作しやすさ・理解しやすさに配慮した表示設計。"),
            ("DISPLAY-000058", "low_cognitive_load_display", "低認知負荷表示", "Low Cognitive Load Display", "情報量や選択肢を整理し、理解負荷を下げる表示設計。"),
            ("DISPLAY-000059", "context_aware_copy", "文脈対応コピー", "Context Aware Copy", "時間・場所・状態に合わせて文言を調整する表示設計。"),
            ("DISPLAY-000060", "personalization_control_display", "個別化制御表示", "Personalization Control Display", "個別化の有無や範囲をユーザーが確認・変更できる表示設計。")
        ]
    },
    {
        "category": "Display Design - Feedback Loop",
        "name_ja": "表示設計・フィードバックループ",
        "items": [
            ("DISPLAY-000061", "result_feedback_button", "結果フィードバックボタン", "Result Feedback Button", "表示結果が合っているかユーザーが反応できる導線。"),
            ("DISPLAY-000062", "not_applicable_option", "該当しない選択肢", "Not Applicable Option", "ユーザーが結果や提案を該当しないと示せる設計。"),
            ("DISPLAY-000063", "correction_input_display", "修正入力表示", "Correction Input Display", "ユーザーが前提や文脈を修正入力できる表示設計。"),
            ("DISPLAY-000064", "preference_feedback_display", "嗜好フィードバック表示", "Preference Feedback Display", "表示内容や提案への好みを返せる設計。"),
            ("DISPLAY-000065", "explanation_request_button", "説明要求ボタン", "Explanation Request Button", "ユーザーが詳細説明を求められる導線。"),
            ("DISPLAY-000066", "dismiss_reason_prompt", "非表示理由確認", "Dismiss Reason Prompt", "提案を閉じた理由を任意で確認する表示設計。"),
            ("DISPLAY-000067", "usefulness_rating", "有用度評価", "Usefulness Rating", "表示や提案が役に立ったか評価できる設計。"),
            ("DISPLAY-000068", "feedback_history_display", "フィードバック履歴表示", "Feedback History Display", "過去の修正や反応を確認できる表示設計。"),
            ("DISPLAY-000069", "adaptive_learning_notice", "適応学習通知", "Adaptive Learning Notice", "ユーザー反応を今後の表示調整に使うことを知らせる設計。"),
            ("DISPLAY-000070", "feedback_loop_integration", "フィードバックループ統合", "Feedback Loop Integration", "ユーザー反応を表示改善や推論補正に接続する設計。")
        ]
    },
    {
        "category": "Display Design - Notification",
        "name_ja": "表示設計・通知",
        "items": [
            ("DISPLAY-000071", "gentle_notification", "やさしい通知", "Gentle Notification", "負担感や圧迫感を抑えた通知表現。"),
            ("DISPLAY-000072", "timely_notification", "適時通知", "Timely Notification", "ユーザー文脈に合うタイミングで出す通知設計。"),
            ("DISPLAY-000073", "low_priority_notification", "低優先通知", "Low Priority Notification", "緊急性が低い情報を控えめに届ける通知設計。"),
            ("DISPLAY-000074", "high_importance_notification", "重要通知", "High Importance Notification", "見逃すと困る情報を明確に届ける通知設計。"),
            ("DISPLAY-000075", "notification_frequency_control", "通知頻度制御", "Notification Frequency Control", "通知回数を調整し過剰通知を避ける設計。"),
            ("DISPLAY-000076", "notification_batching", "通知まとめ表示", "Notification Batching", "複数通知をまとめて提示し中断を減らす設計。"),
            ("DISPLAY-000077", "snooze_option", "後で通知オプション", "Snooze Option", "ユーザーが通知を後回しにできる設計。"),
            ("DISPLAY-000078", "notification_reason_display", "通知理由表示", "Notification Reason Display", "なぜ通知されたのかを示す表示設計。"),
            ("DISPLAY-000079", "context_sensitive_reminder", "文脈感知リマインダー", "Context Sensitive Reminder", "時間・場所・予定・状態に応じたリマインダー設計。"),
            ("DISPLAY-000080", "notification_safety_guard", "通知安全ガード", "Notification Safety Guard", "不適切なタイミングや過度な介入を避ける通知設計。")
        ]
    },
    {
        "category": "Display Design - Data Transparency",
        "name_ja": "表示設計・データ透明性",
        "items": [
            ("DISPLAY-000081", "data_used_display", "使用データ表示", "Data Used Display", "結果や提案に使われたデータ種別を示す表示設計。"),
            ("DISPLAY-000082", "data_not_used_display", "未使用データ表示", "Data Not Used Display", "使っていないデータを明示し誤解を減らす表示設計。"),
            ("DISPLAY-000083", "data_recency_display", "データ鮮度表示", "Data Recency Display", "どの時点のデータに基づく結果かを示す表示設計。"),
            ("DISPLAY-000084", "data_amount_display", "データ量表示", "Data Amount Display", "観測量やサンプル数を示す表示設計。"),
            ("DISPLAY-000085", "data_quality_warning", "データ品質注意表示", "Data Quality Warning", "欠損やノイズが多い場合に注意を示す表示設計。"),
            ("DISPLAY-000086", "privacy_scope_display", "プライバシー範囲表示", "Privacy Scope Display", "どの範囲の情報が扱われるかを示す表示設計。"),
            ("DISPLAY-000087", "consent_status_display", "同意状態表示", "Consent Status Display", "データ利用や個別化への同意状態を示す表示設計。"),
            ("DISPLAY-000088", "delete_data_path_display", "データ削除導線表示", "Delete Data Path Display", "ユーザーがデータ削除や停止に進める導線。"),
            ("DISPLAY-000089", "data_export_notice", "データ確認案内", "Data Export Notice", "ユーザーが自分のデータを確認できることを示す表示。"),
            ("DISPLAY-000090", "transparency_integration", "透明性統合", "Transparency Integration", "使用データ・根拠・同意・制御を統合して示す表示設計。")
        ]
    },
    {
        "category": "Display Design - Integration",
        "name_ja": "表示設計・統合",
        "items": [
            ("DISPLAY-000091", "display_policy", "表示方針", "Display Policy", "アプリ全体で一貫した結果表示・説明・安全表現の方針。"),
            ("DISPLAY-000092", "result_card_template", "結果カードテンプレート", "Result Card Template", "結果・理由・信頼度・次アクションをまとめる表示テンプレート。"),
            ("DISPLAY-000093", "safe_result_template", "安全結果テンプレート", "Safe Result Template", "断定や不安を避けて結果を提示するテンプレート。"),
            ("DISPLAY-000094", "explanation_template", "説明テンプレート", "Explanation Template", "使用シグナル・補正・根拠を説明するテンプレート。"),
            ("DISPLAY-000095", "suggestion_template", "提案テンプレート", "Suggestion Template", "小さな次アクションを提示するテンプレート。"),
            ("DISPLAY-000096", "uncertainty_template", "不確実性テンプレート", "Uncertainty Template", "データ不足や曖昧さを安全に伝えるテンプレート。"),
            ("DISPLAY-000097", "user_control_template", "ユーザー制御テンプレート", "User Control Template", "表示・個別化・データ利用を調整できる導線設計。"),
            ("DISPLAY-000098", "multi_app_display_consistency", "複数アプリ表示一貫性", "Multi App Display Consistency", "複数アプリで共通知識を使う際の表示整合性を保つ設計。"),
            ("DISPLAY-000099", "display_audit", "表示監査", "Display Audit", "表示内容が安全・非断定的・説明可能か確認する管理概念。"),
            ("DISPLAY-000100", "display_design_integration", "表示設計統合", "Display Design Integration", "結果表現・説明・可視化・通知・透明性を統合する枠組み。")
        ]
    }
]


def make_item(item_id, slug, name_ja, name_en, definition_ja, category, parent_ja):
    return {
        "filename": f"{item_id}_{slug}.yml",
        "id": item_id,
        "knowledge_type": "display_design",
        "name_ja": name_ja,
        "name_en": name_en,
        "category": "Display Design",
        "attribute": category.replace("Display Design - ", ""),
        "definition_ja": definition_ja,
        "tags": ["CAT:表示設計", f"CAT:{parent_ja}", "ATTR:表示方針"],
        "parent": [parent_ja],
        "related": ["アプリ用途", "補正要因", "安全設計"],
        "observable_data": [
            f"{name_ja}適用文脈",
            f"{name_ja}対象結果",
            f"{name_ja}安全性条件",
            f"{name_ja}ユーザー反応"
        ],
        "signal_candidates": [
            f"{name_ja}を表示方針として利用できる",
            "アプリ側で結果表示・説明・提案を調整する材料になる"
        ],
        "device_level": "DB管理用",
        "modifiers": ["用途", "安全性", "不確実性", "ユーザー状態"],
        "evidence": "UXライティング・HCI・リスクコミュニケーション・行動支援設計で使用",
        "status": "active"
    }


def main():
    all_items = []
    index_lines = ["category: Display Design", "name_ja: 表示設計", "items:"]

    for section in SECTIONS:
        parent_ja = section["name_ja"].replace("表示設計・", "")
        for raw in section["items"]:
            item = make_item(*raw, category=section["category"], parent_ja=parent_ja)
            all_items.append(item)
            index_lines.append(f"  - {item['filename']}")

    index_lines.extend([
        "notes:",
        "  - 表示設計は推論結果ではなくアプリ側の表現材料として扱う",
        "  - Knowledge DB側ではスコアリングしない",
        "  - アプリ側で用途・安全性・文脈に応じて表示を調整する"
    ])

    pack = {
        "output_dir": "vol15_display_design/display_design_051_100",
        "index_filename": "display_design_051_100_index.yml",
        "index_content": "\n".join(index_lines) + "\n",
        "items": all_items
    }

    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(json.dumps(pack, ensure_ascii=False, indent=2), encoding="utf-8")

    print(f"Created: {OUT}")
    print(f"Items: {len(all_items)}")


if __name__ == "__main__":
    main()