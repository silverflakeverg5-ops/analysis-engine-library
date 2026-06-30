import json
from pathlib import Path

OUT = Path("data/master_packs/vol11_observation_signals_051_100.json")

SECTIONS = [
    {
        "category": "Observation Signals - Emotion",
        "name_ja": "観測シグナル・感情",
        "items": [
            ("SIGNAL-000051", "emotion_word_rate", "感情語使用率", "Emotion Word Rate", "発話や入力文に含まれる感情語の割合。"),
            ("SIGNAL-000052", "positive_expression_rate", "肯定表現率", "Positive Expression Rate", "肯定的・前向きな表現が使われる割合。"),
            ("SIGNAL-000053", "negative_expression_rate", "否定表現率", "Negative Expression Rate", "否定的・不満・不安を示す表現が使われる割合。"),
            ("SIGNAL-000054", "emotion_volatility_signal", "感情変動シグナル", "Emotion Volatility Signal", "短期間で感情表現や反応傾向が大きく変化する兆候。"),
            ("SIGNAL-000055", "frustration_expression_count", "苛立ち表現回数", "Frustration Expression Count", "苛立ち・怒り・不満を示す表現や反応の回数。"),
            ("SIGNAL-000056", "anxiety_expression_count", "不安表現回数", "Anxiety Expression Count", "心配・不安・迷いを示す表現の回数。"),
            ("SIGNAL-000057", "confidence_expression_rate", "自信表現率", "Confidence Expression Rate", "確信・自信・断定を示す表現の割合。"),
            ("SIGNAL-000058", "uncertainty_expression_rate", "不確実表現率", "Uncertainty Expression Rate", "迷い・保留・曖昧さを示す表現の割合。"),
            ("SIGNAL-000059", "sentiment_shift", "感情極性変化", "Sentiment Shift", "発話や反応の感情極性が時間とともに変化すること。"),
            ("SIGNAL-000060", "emotional_recovery_signal", "感情回復シグナル", "Emotional Recovery Signal", "否定的感情表現の後に通常または肯定的状態へ戻る兆候。")
        ]
    },
    {
        "category": "Observation Signals - Attention",
        "name_ja": "観測シグナル・注意",
        "items": [
            ("SIGNAL-000061", "focus_duration", "集中持続時間", "Focus Duration", "中断なしで一つの課題や画面に集中している時間。"),
            ("SIGNAL-000062", "distraction_count", "注意逸脱回数", "Distraction Count", "別画面・別機能・通知などへ注意が逸れた回数。"),
            ("SIGNAL-000063", "task_switch_count", "タスク切替回数", "Task Switch Count", "短時間内に課題や画面を切り替えた回数。"),
            ("SIGNAL-000064", "idle_time", "無操作時間", "Idle Time", "表示中にもかかわらず操作が止まっている時間。"),
            ("SIGNAL-000065", "scroll_depth", "スクロール深度", "Scroll Depth", "ページやコンテンツをどこまで閲覧したかを示す指標。"),
            ("SIGNAL-000066", "content_skip_rate", "コンテンツスキップ率", "Content Skip Rate", "提示された情報や説明を飛ばした割合。"),
            ("SIGNAL-000067", "reread_count", "再読回数", "Reread Count", "同じ説明・設問・情報を再度確認した回数。"),
            ("SIGNAL-000068", "attention_recovery_time", "注意回復時間", "Attention Recovery Time", "中断後に元の課題へ戻るまでの時間。"),
            ("SIGNAL-000069", "notification_interruption_rate", "通知中断率", "Notification Interruption Rate", "通知によって作業や閲覧が中断された割合。"),
            ("SIGNAL-000070", "focus_variability", "集中変動性", "Focus Variability", "集中時間や操作ペースがどの程度変動するか。")
        ]
    },
    {
        "category": "Observation Signals - Decision",
        "name_ja": "観測シグナル・意思決定",
        "items": [
            ("SIGNAL-000071", "choice_change_count", "選択変更回数", "Choice Change Count", "一度選んだ選択肢を変更した回数。"),
            ("SIGNAL-000072", "option_comparison_count", "選択肢比較回数", "Option Comparison Count", "複数選択肢を比較・往復確認した回数。"),
            ("SIGNAL-000073", "default_choice_rate", "デフォルト選択率", "Default Choice Rate", "初期設定や既定選択肢をそのまま選んだ割合。"),
            ("SIGNAL-000074", "risk_option_rate", "リスク選択率", "Risk Option Rate", "不確実性や損失可能性を含む選択肢を選んだ割合。"),
            ("SIGNAL-000075", "safe_option_rate", "安全選択率", "Safe Option Rate", "損失や失敗を避けやすい安全な選択肢を選んだ割合。"),
            ("SIGNAL-000076", "delay_choice_rate", "遅延報酬選択率", "Delayed Reward Choice Rate", "即時報酬より将来報酬を選んだ割合。"),
            ("SIGNAL-000077", "immediate_choice_rate", "即時報酬選択率", "Immediate Reward Choice Rate", "将来報酬より即時報酬を選んだ割合。"),
            ("SIGNAL-000078", "decision_reversal_rate", "判断撤回率", "Decision Reversal Rate", "決定後に判断を撤回・変更した割合。"),
            ("SIGNAL-000079", "choice_conflict_signal", "選択葛藤シグナル", "Choice Conflict Signal", "比較・迷い・保留が増えることで現れる意思決定葛藤の兆候。"),
            ("SIGNAL-000080", "decision_consistency", "選択一貫性", "Decision Consistency", "同条件または類似条件で選択傾向がどの程度一貫しているか。")
        ]
    },
    {
        "category": "Observation Signals - Habit Routine",
        "name_ja": "観測シグナル・習慣ルーティン",
        "items": [
            ("SIGNAL-000081", "routine_consistency", "ルーティン一貫性", "Routine Consistency", "同じ時間・順序・文脈で行動が繰り返される度合い。"),
            ("SIGNAL-000082", "habit_streak", "習慣連続記録", "Habit Streak", "特定行動が連続して実行された日数や回数。"),
            ("SIGNAL-000083", "habit_break_count", "習慣中断回数", "Habit Break Count", "継続していた習慣行動が途切れた回数。"),
            ("SIGNAL-000084", "routine_start_time", "ルーティン開始時刻", "Routine Start Time", "特定行動が開始される時刻の傾向。"),
            ("SIGNAL-000085", "routine_completion_rate", "ルーティン完了率", "Routine Completion Rate", "予定された習慣や一連の行動が完了した割合。"),
            ("SIGNAL-000086", "automatic_action_rate", "自動化行動率", "Automatic Action Rate", "迷いや確認が少なく実行される行動の割合。"),
            ("SIGNAL-000087", "cue_response_rate", "手がかり反応率", "Cue Response Rate", "通知・時刻・場所などの手がかりに対して行動が起きた割合。"),
            ("SIGNAL-000088", "routine_recovery_rate", "ルーティン回復率", "Routine Recovery Rate", "中断後に元の習慣やリズムへ戻った割合。"),
            ("SIGNAL-000089", "weekly_pattern_stability", "週次パターン安定性", "Weekly Pattern Stability", "曜日ごとの行動パターンがどの程度安定しているか。"),
            ("SIGNAL-000090", "habit_context_dependency", "習慣文脈依存性", "Habit Context Dependency", "場所・時間・状況が変わると習慣行動が変化する度合い。")
        ]
    },
    {
        "category": "Observation Signals - Physiology Proxy",
        "name_ja": "観測シグナル・生理推定",
        "items": [
            ("SIGNAL-000091", "sleep_log_duration", "睡眠ログ時間", "Sleep Log Duration", "記録または推定された睡眠時間。"),
            ("SIGNAL-000092", "activity_level_proxy", "活動量推定", "Activity Level Proxy", "歩数・移動・端末利用などから推定される活動量。"),
            ("SIGNAL-000093", "late_night_usage", "深夜利用", "Late Night Usage", "深夜帯にアプリや端末を利用している状態。"),
            ("SIGNAL-000094", "morning_activation_signal", "朝の活性化シグナル", "Morning Activation Signal", "起床後や朝時間帯の利用・反応・行動開始の兆候。"),
            ("SIGNAL-000095", "fatigue_proxy_signal", "疲労推定シグナル", "Fatigue Proxy Signal", "反応遅延・エラー増加・利用低下などから推定される疲労兆候。"),
            ("SIGNAL-000096", "stress_proxy_signal", "ストレス推定シグナル", "Stress Proxy Signal", "操作乱れ・回避増加・感情表現変化などから推定されるストレス兆候。"),
            ("SIGNAL-000097", "recovery_proxy_signal", "回復推定シグナル", "Recovery Proxy Signal", "反応速度・正答率・利用リズムが通常へ戻る兆候。"),
            ("SIGNAL-000098", "circadian_disruption_signal", "概日乱れシグナル", "Circadian Disruption Signal", "利用時間帯や睡眠推定が通常リズムからずれる兆候。"),
            ("SIGNAL-000099", "overload_proxy_signal", "過負荷推定シグナル", "Overload Proxy Signal", "エラー・離脱・反応遅延・中断が同時に増える兆候。"),
            ("SIGNAL-000100", "state_baseline_deviation", "状態ベースライン乖離", "State Baseline Deviation", "本人の通常状態から行動・反応・利用傾向がどの程度ずれているか。")
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
        "output_dir": "vol11_observation_signals/observation_signals_051_100",
        "index_filename": "observation_signals_051_100_index.yml",
        "index_content": "\n".join(index_lines) + "\n",
        "items": all_items
    }

    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(json.dumps(pack, ensure_ascii=False, indent=2), encoding="utf-8")

    print(f"Created: {OUT}")
    print(f"Items: {len(all_items)}")


if __name__ == "__main__":
    main()