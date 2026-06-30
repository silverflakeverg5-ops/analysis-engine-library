import json
from pathlib import Path

OUT = Path("data/master_packs/vol11_observation_signals_151_200.json")

SECTIONS = [
    {
        "category": "Observation Signals - Bias",
        "name_ja": "観測シグナル・バイアス",
        "items": [
            ("SIGNAL-000151", "confirmation_search_pattern", "確証探索パターン", "Confirmation Search Pattern", "自分の選択や仮説を支持する情報へ検索・閲覧が偏る傾向。"),
            ("SIGNAL-000152", "anchor_dependency_signal", "アンカー依存シグナル", "Anchor Dependency Signal", "初期提示値や最初の選択に判断が近づく傾向。"),
            ("SIGNAL-000153", "default_retention_signal", "デフォルト維持シグナル", "Default Retention Signal", "初期設定や既定選択肢を変更せず維持する傾向。"),
            ("SIGNAL-000154", "loss_avoidance_signal", "損失回避シグナル", "Loss Avoidance Signal", "損失や失敗を避ける選択が増える傾向。"),
            ("SIGNAL-000155", "recency_dependency_signal", "直近依存シグナル", "Recency Dependency Signal", "直近の結果や情報に選択・評価が引き寄せられる傾向。"),
            ("SIGNAL-000156", "social_proof_dependency_signal", "社会的証明依存シグナル", "Social Proof Dependency Signal", "人気・評価・多数派表示に選択が影響される傾向。"),
            ("SIGNAL-000157", "authority_reference_signal", "権威参照シグナル", "Authority Reference Signal", "専門家・公式・肩書き表示への反応が強い傾向。"),
            ("SIGNAL-000158", "scarcity_response_signal", "希少性反応シグナル", "Scarcity Response Signal", "限定・残りわずか・期限表示に反応して選択が変化する傾向。"),
            ("SIGNAL-000159", "choice_overload_signal", "選択過多シグナル", "Choice Overload Signal", "選択肢増加時に迷い・離脱・決定遅延が増える傾向。"),
            ("SIGNAL-000160", "present_bias_signal", "現在バイアスシグナル", "Present Bias Signal", "将来利益より即時報酬や短期的負担軽減を選ぶ傾向。")
        ]
    },
    {
        "category": "Observation Signals - Motivation",
        "name_ja": "観測シグナル・動機づけ",
        "items": [
            ("SIGNAL-000161", "reward_response_rate", "報酬反応率", "Reward Response Rate", "報酬表示や達成報酬に対して行動が増える割合。"),
            ("SIGNAL-000162", "badge_response_rate", "バッジ反応率", "Badge Response Rate", "バッジ・称号・実績表示後に行動が増える割合。"),
            ("SIGNAL-000163", "streak_preservation_behavior", "連続記録維持行動", "Streak Preservation Behavior", "連続記録を維持するために行動する傾向。"),
            ("SIGNAL-000164", "goal_proximity_acceleration", "目標接近加速", "Goal Proximity Acceleration", "目標達成が近づくほど行動量や速度が高まる傾向。"),
            ("SIGNAL-000165", "challenge_acceptance_rate", "挑戦受諾率", "Challenge Acceptance Rate", "難度の高い課題や新しい挑戦を受け入れた割合。"),
            ("SIGNAL-000166", "challenge_avoidance_rate", "挑戦回避率", "Challenge Avoidance Rate", "難度の高い課題や新しい挑戦を避けた割合。"),
            ("SIGNAL-000167", "self_initiated_action_count", "自発行動回数", "Self Initiated Action Count", "外部指示や通知なしに本人から開始した行動回数。"),
            ("SIGNAL-000168", "reward_removal_drop", "報酬除去後低下", "Reward Removal Drop", "報酬がなくなった後に行動頻度や継続率が低下する変化。"),
            ("SIGNAL-000169", "effort_investment_signal", "努力投入シグナル", "Effort Investment Signal", "難所や重要課題に時間・再試行・確認を投入する傾向。"),
            ("SIGNAL-000170", "motivation_recovery_signal", "動機回復シグナル", "Motivation Recovery Signal", "低下した行動量や継続率が再び通常水準へ戻る兆候。")
        ]
    },
    {
        "category": "Observation Signals - Safety Ethics",
        "name_ja": "観測シグナル・安全倫理",
        "items": [
            ("SIGNAL-000171", "sensitive_input_signal", "センシティブ入力シグナル", "Sensitive Input Signal", "健康・個人情報・人間関係など慎重に扱うべき入力が含まれる兆候。"),
            ("SIGNAL-000172", "distress_expression_signal", "苦痛表現シグナル", "Distress Expression Signal", "強い苦痛・困難・切迫感を示す表現が観測される兆候。"),
            ("SIGNAL-000173", "dependency_risk_signal", "依存リスクシグナル", "Dependency Risk Signal", "過度な利用・確認・依存的反応が増える兆候。"),
            ("SIGNAL-000174", "privacy_risk_signal", "プライバシーリスクシグナル", "Privacy Risk Signal", "本人や他者の個人情報が入力・共有されるリスクの兆候。"),
            ("SIGNAL-000175", "manipulation_susceptibility_signal", "操作影響受容シグナル", "Manipulation Susceptibility Signal", "誘導・報酬・社会的圧力により判断が過度に動く兆候。"),
            ("SIGNAL-000176", "over_disclosure_signal", "過剰開示シグナル", "Over Disclosure Signal", "必要以上に個人的・機微な情報を開示する傾向。"),
            ("SIGNAL-000177", "boundary_violation_signal", "境界侵害シグナル", "Boundary Violation Signal", "他者または本人の心理的・情報的境界が侵害される兆候。"),
            ("SIGNAL-000178", "harmful_interaction_signal", "有害相互作用シグナル", "Harmful Interaction Signal", "攻撃・侮辱・排除・強い否定など有害な対人反応の兆候。"),
            ("SIGNAL-000179", "safety_escalation_signal", "安全確認強化シグナル", "Safety Escalation Signal", "通常応答より安全確認や慎重な扱いが必要な入力兆候。"),
            ("SIGNAL-000180", "ethical_review_signal", "倫理レビューシグナル", "Ethical Review Signal", "推論・表示・介入前に倫理的確認が必要な状態を示す兆候。")
        ]
    },
    {
        "category": "Observation Signals - Quality Reliability",
        "name_ja": "観測シグナル・品質信頼性",
        "items": [
            ("SIGNAL-000181", "data_missing_rate", "データ欠損率", "Data Missing Rate", "必要な観測データが取得できていない割合。"),
            ("SIGNAL-000182", "data_noise_level", "データノイズ水準", "Data Noise Level", "観測データに含まれる誤差・ばらつき・不安定性の度合い。"),
            ("SIGNAL-000183", "signal_confidence_score", "シグナル信頼度スコア", "Signal Confidence Score", "観測シグナルを推論材料として使える信頼度。"),
            ("SIGNAL-000184", "sample_size_signal", "サンプル数シグナル", "Sample Size Signal", "判断に使える観測回数や期間の十分性。"),
            ("SIGNAL-000185", "measurement_context_signal", "測定文脈シグナル", "Measurement Context Signal", "観測が行われた端末・時間・状況などの文脈情報。"),
            ("SIGNAL-000186", "outlier_detection_signal", "外れ値検出シグナル", "Outlier Detection Signal", "通常範囲から大きく外れた観測値の検出。"),
            ("SIGNAL-000187", "duplicate_event_signal", "重複イベントシグナル", "Duplicate Event Signal", "同一または近接イベントが重複して記録された可能性。"),
            ("SIGNAL-000188", "sensor_reliability_signal", "センサー信頼性シグナル", "Sensor Reliability Signal", "端末・入力・センサー由来データの信頼性。"),
            ("SIGNAL-000189", "self_report_consistency", "自己報告一貫性", "Self Report Consistency", "本人入力や自己申告が時系列・文脈間で一貫している度合い。"),
            ("SIGNAL-000190", "behavior_report_gap", "行動報告ギャップ", "Behavior Report Gap", "自己報告と実際の行動ログに差がある状態。")
        ]
    },
    {
        "category": "Observation Signals - Application Integration",
        "name_ja": "観測シグナル・アプリ統合",
        "items": [
            ("SIGNAL-000191", "diagnosis_app_signal", "診断アプリ用シグナル", "Diagnosis App Signal", "診断・自己理解アプリで利用しやすい観測指標候補。"),
            ("SIGNAL-000192", "game_behavior_signal", "ゲーム行動シグナル", "Game Behavior Signal", "ゲーム内選択・探索・再挑戦・反応から得られる観測指標候補。"),
            ("SIGNAL-000193", "assistant_app_signal", "秘書アプリ用シグナル", "Assistant App Signal", "予定・通知・タスク・生活文脈から得られる観測指標候補。"),
            ("SIGNAL-000194", "education_app_signal", "教育アプリ用シグナル", "Education App Signal", "学習ログ・成績・復習・フィードバックから得られる観測指標候補。"),
            ("SIGNAL-000195", "work_support_signal", "仕事支援シグナル", "Work Support Signal", "タスク・集中・中断・優先順位から得られる仕事支援用観測指標。"),
            ("SIGNAL-000196", "wellbeing_signal", "ウェルビーイングシグナル", "Wellbeing Signal", "睡眠・疲労・感情・生活リズムから得られる状態推定用指標。"),
            ("SIGNAL-000197", "compatibility_signal", "相性推定シグナル", "Compatibility Signal", "対人反応・価値観・行動傾向から相性推定材料となる指標候補。"),
            ("SIGNAL-000198", "personalization_signal", "個別化シグナル", "Personalization Signal", "表示・通知・難易度・提案を個別調整するための観測指標。"),
            ("SIGNAL-000199", "intervention_timing_signal", "介入タイミングシグナル", "Intervention Timing Signal", "通知・提案・支援を出す適切なタイミングを推定する材料。"),
            ("SIGNAL-000200", "observation_signal_integration", "観測シグナル統合", "Observation Signal Integration", "複数アプリや複数文脈の観測指標を統合して推論材料化する枠組み。")
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
        "output_dir": "vol11_observation_signals/observation_signals_151_200",
        "index_filename": "observation_signals_151_200_index.yml",
        "index_content": "\n".join(index_lines) + "\n",
        "items": all_items
    }

    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(json.dumps(pack, ensure_ascii=False, indent=2), encoding="utf-8")

    print(f"Created: {OUT}")
    print(f"Items: {len(all_items)}")


if __name__ == "__main__":
    main()