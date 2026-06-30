import json
from pathlib import Path

OUT = Path("data/master_packs/vol11_observation_signals_001_050.json")

SECTIONS = [
    {
        "category": "Observation Signals - App Usage",
        "name_ja": "観測シグナル・アプリ利用",
        "items": [
            ("SIGNAL-000001", "session_frequency", "セッション頻度", "Session Frequency", "一定期間内にアプリやサービスを利用した回数。"),
            ("SIGNAL-000002", "session_duration", "セッション時間", "Session Duration", "一回の利用開始から終了までの継続時間。"),
            ("SIGNAL-000003", "return_interval", "再訪間隔", "Return Interval", "前回利用から次回利用までの時間間隔。"),
            ("SIGNAL-000004", "active_days", "利用日数", "Active Days", "一定期間内に利用が確認された日数。"),
            ("SIGNAL-000005", "usage_time_of_day", "利用時間帯", "Usage Time of Day", "利用が発生しやすい時刻や時間帯。"),
            ("SIGNAL-000006", "dropoff_point", "離脱地点", "Dropoff Point", "利用や課題の途中で離脱しやすい画面・手順・段階。"),
            ("SIGNAL-000007", "reengagement_signal", "再関与シグナル", "Reengagement Signal", "離脱後に再び利用や行動を開始する兆候。"),
            ("SIGNAL-000008", "feature_usage_rate", "機能利用率", "Feature Usage Rate", "特定機能が利用された割合や頻度。"),
            ("SIGNAL-000009", "settings_change_count", "設定変更回数", "Settings Change Count", "表示・通知・プロフィールなど設定を変更した回数。"),
            ("SIGNAL-000010", "notification_response_time", "通知反応時間", "Notification Response Time", "通知表示から開封・行動開始までの時間。")
        ]
    },
    {
        "category": "Observation Signals - Interaction",
        "name_ja": "観測シグナル・操作",
        "items": [
            ("SIGNAL-000011", "tap_interval", "タップ間隔", "Tap Interval", "タップやクリックの間に生じる時間間隔。"),
            ("SIGNAL-000012", "input_speed", "入力速度", "Input Speed", "文字入力や選択操作の速さ。"),
            ("SIGNAL-000013", "reaction_time", "反応時間", "Reaction Time", "刺激や設問提示から反応までにかかる時間。"),
            ("SIGNAL-000014", "decision_latency", "選択潜時", "Decision Latency", "選択肢提示から意思決定までにかかる時間。"),
            ("SIGNAL-000015", "correction_count", "修正回数", "Correction Count", "入力・選択・回答を修正した回数。"),
            ("SIGNAL-000016", "undo_count", "取り消し回数", "Undo Count", "操作の取り消しや戻る操作を行った回数。"),
            ("SIGNAL-000017", "backtracking_rate", "戻り操作率", "Backtracking Rate", "前画面や前段階へ戻る操作の割合。"),
            ("SIGNAL-000018", "hover_or_pause_time", "迷い停止時間", "Hover or Pause Time", "操作前に停止・待機・迷いが見られる時間。"),
            ("SIGNAL-000019", "error_rate", "エラー率", "Error Rate", "誤操作・誤答・失敗が発生した割合。"),
            ("SIGNAL-000020", "retry_count", "再試行回数", "Retry Count", "失敗後に再挑戦した回数。")
        ]
    },
    {
        "category": "Observation Signals - Learning",
        "name_ja": "観測シグナル・学習",
        "items": [
            ("SIGNAL-000021", "correct_answer_rate", "正答率", "Correct Answer Rate", "課題や設問に対する正答の割合。"),
            ("SIGNAL-000022", "improvement_rate", "改善率", "Improvement Rate", "時間経過や練習に伴う成績向上の割合。"),
            ("SIGNAL-000023", "hint_usage_count", "ヒント使用回数", "Hint Usage Count", "課題中にヒントや支援情報を利用した回数。"),
            ("SIGNAL-000024", "explanation_view_count", "説明閲覧回数", "Explanation View Count", "説明・解説・ヘルプを閲覧した回数。"),
            ("SIGNAL-000025", "review_behavior_count", "復習行動回数", "Review Behavior Count", "過去内容や間違いを見直した回数。"),
            ("SIGNAL-000026", "practice_repetition", "練習反復数", "Practice Repetition", "同じ課題や類似課題を繰り返した回数。"),
            ("SIGNAL-000027", "learning_streak", "学習連続記録", "Learning Streak", "連続して学習行動が発生した日数や回数。"),
            ("SIGNAL-000028", "time_on_task", "課題滞在時間", "Time on Task", "特定課題に取り組んだ時間。"),
            ("SIGNAL-000029", "post_feedback_change", "フィードバック後変化", "Post Feedback Change", "フィードバック後に行動・成績・選択が変化した度合い。"),
            ("SIGNAL-000030", "transfer_success_rate", "転移成功率", "Transfer Success Rate", "学習済み内容を別課題へ応用できた割合。")
        ]
    },
    {
        "category": "Observation Signals - Social",
        "name_ja": "観測シグナル・社会行動",
        "items": [
            ("SIGNAL-000031", "message_frequency", "メッセージ頻度", "Message Frequency", "一定期間内に送信されたメッセージや発話の回数。"),
            ("SIGNAL-000032", "response_delay", "返信遅延", "Response Delay", "相手の発信から返信までにかかる時間。"),
            ("SIGNAL-000033", "help_request_count", "援助要請回数", "Help Request Count", "質問・相談・支援依頼が行われた回数。"),
            ("SIGNAL-000034", "help_offer_count", "援助提供回数", "Help Offer Count", "他者への助言・支援・補助が行われた回数。"),
            ("SIGNAL-000035", "reaction_count", "リアクション回数", "Reaction Count", "いいね・スタンプ・評価など簡易反応を行った回数。"),
            ("SIGNAL-000036", "turn_taking_balance", "会話交替バランス", "Turn Taking Balance", "会話や共同作業における発話・反応の分布バランス。"),
            ("SIGNAL-000037", "group_participation_rate", "集団参加率", "Group Participation Rate", "共同活動やグループ内行動へ参加した割合。"),
            ("SIGNAL-000038", "conflict_expression_count", "葛藤表出回数", "Conflict Expression Count", "反対意見・拒否・不満表明が観測された回数。"),
            ("SIGNAL-000039", "agreement_rate", "同意率", "Agreement Rate", "他者意見や提案に同意した割合。"),
            ("SIGNAL-000040", "social_withdrawal_signal", "社会的撤退シグナル", "Social Withdrawal Signal", "対人反応や参加頻度の低下として現れる撤退傾向。")
        ]
    },
    {
        "category": "Observation Signals - State Change",
        "name_ja": "観測シグナル・状態変化",
        "items": [
            ("SIGNAL-000041", "performance_drop", "成績低下", "Performance Drop", "通常水準と比べて成績や正確性が低下した状態。"),
            ("SIGNAL-000042", "response_slowdown", "反応遅延化", "Response Slowdown", "通常より反応や操作が遅くなる変化。"),
            ("SIGNAL-000043", "error_spike", "エラー急増", "Error Spike", "短期間に誤答・誤操作・失敗が増加する変化。"),
            ("SIGNAL-000044", "engagement_drop", "関与低下", "Engagement Drop", "利用・参加・継続行動が低下する変化。"),
            ("SIGNAL-000045", "avoidance_increase", "回避増加", "Avoidance Increase", "課題・選択・対人行動を避ける行動が増える変化。"),
            ("SIGNAL-000046", "risk_taking_change", "リスク選択変化", "Risk Taking Change", "安全策またはリスク選択への偏りが変化すること。"),
            ("SIGNAL-000047", "exploration_change", "探索行動変化", "Exploration Change", "新機能・新情報・未知選択肢を試す頻度の変化。"),
            ("SIGNAL-000048", "persistence_change", "継続行動変化", "Persistence Change", "失敗後や困難時の継続・再挑戦行動の変化。"),
            ("SIGNAL-000049", "routine_disruption", "ルーティン乱れ", "Routine Disruption", "通常の利用時間・生活リズム・行動順序が乱れる変化。"),
            ("SIGNAL-000050", "recovery_signal", "回復シグナル", "Recovery Signal", "低下・中断・負荷後に通常状態へ戻る兆候。")
        ]
    }
]


def make_item(item_id, slug, name_ja, name_en, definition_ja, category, parent_ja):
    return {
        "filename": f"{item_id}_{slug}.yml",
        "id": item_id,
        "knowledge_type": "observation_signal",
        "name_ja": name_ja,
        "name_en": name_en,
        "category": "Observation Signal",
        "attribute": category.replace("Observation Signals - ", ""),
        "definition_ja": definition_ja,
        "tags": ["CAT:観測シグナル", f"CAT:{parent_ja}", "ATTR:観測可能データ"],
        "parent": [parent_ja],
        "related": ["行動観測", "推論材料", "補正要因"],
        "observable_data": [
            name_ja,
            f"{name_ja}の増減",
            f"{name_ja}の平均との差",
            f"{name_ja}の時系列変化"
        ],
        "signal_candidates": [
            f"{name_ja}が通常傾向から変化している",
            "時系列で変化した場合に状態変化の材料になる"
        ],
        "device_level": "スマホ・PCで観測可能",
        "modifiers": ["端末差", "利用文脈", "生活状況", "データ欠損"],
        "evidence": "HCI・行動ログ分析・心理測定・学習分析で使用",
        "status": "active"
    }


def main():
    all_items = []
    index_lines = ["category: Observation Signal", "name_ja: 観測シグナル", "items:"]

    for section in SECTIONS:
        parent_ja = section["name_ja"].replace("観測シグナル・", "")
        for raw in section["items"]:
            item = make_item(*raw, category=section["category"], parent_ja=parent_ja)
            all_items.append(item)
            index_lines.append(f"  - {item['filename']}")

    index_lines.extend([
        "notes:",
        "  - 観測シグナルは推論結果ではなく入力材料として扱う",
        "  - アプリ側でスコアリング・推論・表示を行う",
        "  - 生データではなく観測可能な指標候補として管理する"
    ])

    pack = {
        "output_dir": "vol11_observation_signals/observation_signals_001_050",
        "index_filename": "observation_signals_001_050_index.yml",
        "index_content": "\n".join(index_lines) + "\n",
        "items": all_items
    }

    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(json.dumps(pack, ensure_ascii=False, indent=2), encoding="utf-8")

    print(f"Created: {OUT}")
    print(f"Items: {len(all_items)}")


if __name__ == "__main__":
    main()