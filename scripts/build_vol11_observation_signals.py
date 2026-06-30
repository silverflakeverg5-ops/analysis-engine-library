import json
from pathlib import Path

OUT = Path("data/master_packs/vol11_observation_signals_101_150.json")

SECTIONS = [
    {
        "category": "Observation Signals - Goal Achievement",
        "name_ja": "観測シグナル・目標達成",
        "items": [
            ("SIGNAL-000101", "goal_creation_count", "目標作成回数", "Goal Creation Count", "一定期間内に新しい目標を作成した回数。"),
            ("SIGNAL-000102", "goal_update_count", "目標更新回数", "Goal Update Count", "設定済み目標の内容・期限・条件を更新した回数。"),
            ("SIGNAL-000103", "goal_completion_rate", "目標完了率", "Goal Completion Rate", "設定した目標のうち完了まで到達した割合。"),
            ("SIGNAL-000104", "goal_abandonment_rate", "目標放棄率", "Goal Abandonment Rate", "設定した目標が途中で放棄された割合。"),
            ("SIGNAL-000105", "progress_check_count", "進捗確認回数", "Progress Check Count", "目標や課題の進捗を確認した回数。"),
            ("SIGNAL-000106", "deadline_adherence_rate", "期限遵守率", "Deadline Adherence Rate", "設定期限内に課題や目標を完了した割合。"),
            ("SIGNAL-000107", "priority_change_count", "優先順位変更回数", "Priority Change Count", "タスクや目標の優先順位を変更した回数。"),
            ("SIGNAL-000108", "task_completion_order", "タスク完了順序", "Task Completion Order", "複数タスクをどの順序で完了したかを示す指標。"),
            ("SIGNAL-000109", "unfinished_task_count", "未完了タスク数", "Unfinished Task Count", "開始または登録されたが完了していないタスク数。"),
            ("SIGNAL-000110", "restart_after_pause_count", "中断後再開回数", "Restart After Pause Count", "中断された課題や目標を再開した回数。")
        ]
    },
    {
        "category": "Observation Signals - Communication",
        "name_ja": "観測シグナル・コミュニケーション",
        "items": [
            ("SIGNAL-000111", "message_length_average", "平均メッセージ長", "Average Message Length", "送信されたメッセージや発話の平均文字数・語数。"),
            ("SIGNAL-000112", "clarification_question_count", "確認質問回数", "Clarification Question Count", "曖昧な情報に対して確認や質問を行った回数。"),
            ("SIGNAL-000113", "assertive_statement_count", "自己主張表現回数", "Assertive Statement Count", "意見・希望・拒否・境界を明確に表現した回数。"),
            ("SIGNAL-000114", "indirect_expression_rate", "間接表現率", "Indirect Expression Rate", "婉曲・含意・曖昧表現が使われた割合。"),
            ("SIGNAL-000115", "feedback_given_count", "フィードバック提供回数", "Feedback Given Count", "他者へ評価・助言・反応を返した回数。"),
            ("SIGNAL-000116", "feedback_received_count", "フィードバック受領回数", "Feedback Received Count", "他者から評価・助言・反応を受け取った回数。"),
            ("SIGNAL-000117", "apology_expression_count", "謝罪表現回数", "Apology Expression Count", "謝罪・修復・責任認識を示す表現の回数。"),
            ("SIGNAL-000118", "gratitude_expression_count", "感謝表現回数", "Gratitude Expression Count", "感謝や謝意を示す表現の回数。"),
            ("SIGNAL-000119", "conversation_initiation_count", "会話開始回数", "Conversation Initiation Count", "本人から会話や連絡を開始した回数。"),
            ("SIGNAL-000120", "conversation_closure_rate", "会話完了率", "Conversation Closure Rate", "会話ややり取りが自然に完了した割合。")
        ]
    },
    {
        "category": "Observation Signals - Exploration",
        "name_ja": "観測シグナル・探索",
        "items": [
            ("SIGNAL-000121", "new_feature_trial_count", "新機能試行回数", "New Feature Trial Count", "未使用または新規機能を試した回数。"),
            ("SIGNAL-000122", "unknown_option_selection_rate", "未知選択肢選択率", "Unknown Option Selection Rate", "未知または未経験の選択肢を選んだ割合。"),
            ("SIGNAL-000123", "search_query_count", "検索回数", "Search Query Count", "検索・問い合わせ・探索入力を行った回数。"),
            ("SIGNAL-000124", "category_breadth", "閲覧カテゴリ幅", "Category Breadth", "閲覧・選択したカテゴリの広がり。"),
            ("SIGNAL-000125", "novelty_response_rate", "新奇反応率", "Novelty Response Rate", "新しい情報や刺激に反応した割合。"),
            ("SIGNAL-000126", "exploration_depth", "探索深度", "Exploration Depth", "一つの対象やテーマをどの程度深く探索したか。"),
            ("SIGNAL-000127", "exploration_breadth", "探索幅", "Exploration Breadth", "複数対象やテーマをどの程度広く探索したか。"),
            ("SIGNAL-000128", "trial_variation_count", "試行バリエーション数", "Trial Variation Count", "異なる方法・条件・選択肢を試した数。"),
            ("SIGNAL-000129", "curiosity_click_rate", "好奇心クリック率", "Curiosity Click Rate", "未知・おすすめ・詳細表示など好奇心を誘う対象へのクリック率。"),
            ("SIGNAL-000130", "exploration_to_completion_rate", "探索後完了率", "Exploration to Completion Rate", "探索行動後に課題や選択が完了した割合。")
        ]
    },
    {
        "category": "Observation Signals - Context",
        "name_ja": "観測シグナル・文脈",
        "items": [
            ("SIGNAL-000131", "location_context_change", "場所文脈変化", "Location Context Change", "利用や行動が発生する場所文脈の変化。"),
            ("SIGNAL-000132", "time_context_change", "時間文脈変化", "Time Context Change", "利用や行動が発生する時間帯・曜日の変化。"),
            ("SIGNAL-000133", "device_context_change", "端末文脈変化", "Device Context Change", "利用端末や入力環境が変化すること。"),
            ("SIGNAL-000134", "social_context_presence", "社会的文脈存在", "Social Context Presence", "単独・共同・対人場面など社会的文脈の有無。"),
            ("SIGNAL-000135", "environmental_noise_proxy", "環境騒音推定", "Environmental Noise Proxy", "音声入力失敗・中断・場所情報などから推定される騒音文脈。"),
            ("SIGNAL-000136", "interruption_context_count", "中断文脈回数", "Interruption Context Count", "通知・着信・画面切替など文脈中断が発生した回数。"),
            ("SIGNAL-000137", "work_context_signal", "仕事文脈シグナル", "Work Context Signal", "仕事・学業・作業中と推定される利用文脈。"),
            ("SIGNAL-000138", "leisure_context_signal", "余暇文脈シグナル", "Leisure Context Signal", "休憩・娯楽・余暇中と推定される利用文脈。"),
            ("SIGNAL-000139", "commute_context_signal", "移動文脈シグナル", "Commute Context Signal", "通勤通学や移動中と推定される利用文脈。"),
            ("SIGNAL-000140", "context_stability_score", "文脈安定スコア", "Context Stability Score", "行動が発生する文脈がどの程度安定しているか。")
        ]
    },
    {
        "category": "Observation Signals - Integration",
        "name_ja": "観測シグナル・統合",
        "items": [
            ("SIGNAL-000141", "behavior_baseline", "行動ベースライン", "Behavior Baseline", "本人の通常時の行動・反応・利用傾向。"),
            ("SIGNAL-000142", "baseline_deviation_score", "ベースライン乖離スコア", "Baseline Deviation Score", "現在の行動指標が通常傾向からどの程度外れているか。"),
            ("SIGNAL-000143", "multi_signal_change", "複合シグナル変化", "Multi Signal Change", "複数の観測指標が同時に変化すること。"),
            ("SIGNAL-000144", "signal_consistency", "シグナル一貫性", "Signal Consistency", "複数回または複数文脈で同じ傾向が観測される度合い。"),
            ("SIGNAL-000145", "signal_volatility", "シグナル変動性", "Signal Volatility", "観測指標が短期間でどの程度変動するか。"),
            ("SIGNAL-000146", "state_transition_signal", "状態遷移シグナル", "State Transition Signal", "通常・負荷・回復など状態の移行を示す観測指標。"),
            ("SIGNAL-000147", "context_adjusted_signal", "文脈補正シグナル", "Context Adjusted Signal", "時間・場所・端末・状況を考慮して補正された観測指標。"),
            ("SIGNAL-000148", "longitudinal_trend_signal", "長期傾向シグナル", "Longitudinal Trend Signal", "長期間の時系列で見た行動や状態の変化傾向。"),
            ("SIGNAL-000149", "short_term_anomaly_signal", "短期異常シグナル", "Short Term Anomaly Signal", "短期間で通常傾向から大きく外れた観測値。"),
            ("SIGNAL-000150", "human_state_observation_integration", "人間状態観測統合", "Human State Observation Integration", "複数の観測シグナルを統合して人間状態の推論材料とする枠組み。")
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
        "output_dir": "vol11_observation_signals/observation_signals_101_150",
        "index_filename": "observation_signals_101_150_index.yml",
        "index_content": "\n".join(index_lines) + "\n",
        "items": all_items
    }

    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(json.dumps(pack, ensure_ascii=False, indent=2), encoding="utf-8")

    print(f"Created: {OUT}")
    print(f"Items: {len(all_items)}")


if __name__ == "__main__":
    main()