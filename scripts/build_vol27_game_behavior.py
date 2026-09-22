import json
from pathlib import Path


OUT = Path("data/master_packs/vol27_game_behavior_001_100.json")

SECTIONS = [
    ("Engagement", "参加とセッション", [
        ("session_start_behavior", "セッション開始行動", "Session Start Behavior", "ゲームを起動しプレイを始める時間と条件"),
        ("session_frequency", "セッション頻度", "Session Frequency", "一定期間にプレイを開始する回数"),
        ("session_duration", "セッション時間", "Session Duration", "一回のプレイを継続する時間"),
        ("return_interval", "復帰間隔", "Return Interval", "終了から次回プレイまでの時間"),
        ("voluntary_engagement", "自発的参加", "Voluntary Engagement", "外部要求なしにプレイを選ぶ行動"),
        ("prompted_engagement", "促進後参加", "Prompted Engagement", "通知や招待を受けてプレイを始める行動"),
        ("session_extension", "セッション延長", "Session Extension", "予定や区切りを越えてプレイを続ける行動"),
        ("natural_stopping", "自然終了", "Natural Stopping", "目標達成や区切りで自発的に終了する行動"),
        ("abrupt_exit", "突然終了", "Abrupt Exit", "区切りを待たず急にプレイを終える行動"),
        ("reengagement_behavior", "再関与行動", "Reengagement Behavior", "中断や休止後にゲームへ戻る行動"),
    ]),
    ("Exploration", "探索", [
        ("environment_exploration", "環境探索", "Environment Exploration", "必須経路以外の空間や対象を調べる行動"),
        ("optional_content_search", "任意コンテンツ探索", "Optional Content Search", "主目標外のイベントや収集物を探す行動"),
        ("map_coverage", "マップ踏破", "Map Coverage", "利用可能な空間を広く訪れる行動"),
        ("novel_route_choice", "新規経路選択", "Novel Route Choice", "未経験の経路や方法を選ぶ行動"),
        ("repeated_route_choice", "反復経路選択", "Repeated Route Choice", "既知の安全な経路を繰り返し選ぶ行動"),
        ("object_inspection", "対象確認", "Object Inspection", "環境内の物体や説明を詳しく確認する行動"),
        ("secret_discovery", "隠し要素発見", "Secret Discovery", "明示されない要素を探索して見つける行動"),
        ("information_search", "攻略情報探索", "Information Search", "ゲーム内外で手がかりや攻略情報を調べる行動"),
        ("experimentative_play", "実験的プレイ", "Experimentative Play", "未知の組合せや操作を試す行動"),
        ("exploration_saturation", "探索飽和", "Exploration Saturation", "探索の追加価値が低下し次へ進む状態"),
    ]),
    ("Goals and Progression", "目標と進行", [
        ("main_goal_focus", "主目標集中", "Main Goal Focus", "主要目標を優先して進める行動"),
        ("side_goal_engagement", "副目標関与", "Side Goal Engagement", "任意目標やサブクエストへ取り組む行動"),
        ("goal_prioritization", "目標優先順位", "Goal Prioritization", "複数目標の順序を決める行動"),
        ("progress_monitoring", "進捗確認", "Progress Monitoring", "達成率や残課題を確認する行動"),
        ("completion_seeking", "完遂追求", "Completion Seeking", "未完了要素を減らし完了を目指す行動"),
        ("collection_behavior", "収集行動", "Collection Behavior", "アイテムや実績などを集める行動"),
        ("achievement_pursuit", "実績追求", "Achievement Pursuit", "明示された実績条件の達成を目指す行動"),
        ("self_set_goal", "自己設定目標", "Self Set Goal", "システム指定外の目標を自分で設定する行動"),
        ("goal_switching", "目標切替", "Goal Switching", "状況に応じて取り組む目標を変える行動"),
        ("unfinished_goal_return", "未完目標復帰", "Unfinished Goal Return", "中断した目標へ後から戻る行動"),
    ]),
    ("Challenge and Failure", "挑戦と失敗", [
        ("difficulty_selection", "難度選択", "Difficulty Selection", "プレイ開始時や途中で難度を選ぶ行動"),
        ("challenge_acceptance", "挑戦受容", "Challenge Acceptance", "高難度や不確実な課題へ取り組む行動"),
        ("challenge_avoidance", "挑戦回避", "Challenge Avoidance", "高負荷の課題を避け別経路を選ぶ行動"),
        ("failure_response", "失敗反応", "Failure Response", "敗北や失敗直後に示す選択と行動"),
        ("immediate_retry", "即時再試行", "Immediate Retry", "失敗後すぐ同じ課題へ再挑戦する行動"),
        ("strategy_change_after_failure", "失敗後方略変更", "Strategy Change After Failure", "失敗後に装備や戦術を変える行動"),
        ("difficulty_reduction", "難度低減", "Difficulty Reduction", "進行のため難度や制約を下げる行動"),
        ("help_seeking_after_failure", "失敗後援助要請", "Help Seeking After Failure", "失敗後にヒントや協力を求める行動"),
        ("frustration_exit", "挫折離脱", "Frustration Exit", "反復失敗や負荷の後に終了する行動"),
        ("failure_recovery", "失敗回復", "Failure Recovery", "失敗による低下から通常プレイへ戻る過程"),
    ]),
    ("Decision and Risk", "意思決定とリスク", [
        ("choice_deliberation", "選択熟考", "Choice Deliberation", "選択前に情報比較へ時間を使う行動"),
        ("rapid_choice", "即時選択", "Rapid Choice", "短時間で選択肢を決定する行動"),
        ("risk_taking_choice", "リスク選択", "Risk Taking Choice", "不確実だが高い利益を持つ選択を取る行動"),
        ("safe_choice", "安全選択", "Safe Choice", "結果の予測可能性が高い選択を取る行動"),
        ("resource_conservation", "資源温存", "Resource Conservation", "消費可能資源を将来のため保持する行動"),
        ("resource_expenditure", "資源投入", "Resource Expenditure", "現在の課題へ資源を積極的に使う行動"),
        ("uncertainty_checking", "不確実性確認", "Uncertainty Checking", "決定前に追加情報や安全性を確認する行動"),
        ("branch_exploration", "分岐探索", "Branch Exploration", "複数の選択結果を試して比較する行動"),
        ("save_reload_behavior", "保存再読込行動", "Save Reload Behavior", "結果を調整するため保存状態へ戻る行動"),
        ("decision_consistency", "意思決定一貫性", "Decision Consistency", "似た状況で同様の選択を行う度合い"),
    ]),
    ("Reward and Economy", "報酬と経済", [
        ("reward_response", "報酬反応", "Reward Response", "報酬提示前後で行動量が変化する反応"),
        ("immediate_reward_preference", "即時報酬選好", "Immediate Reward Preference", "小さく早い報酬を選ぶ行動"),
        ("delayed_reward_preference", "遅延報酬選好", "Delayed Reward Preference", "待機を伴う大きな報酬を選ぶ行動"),
        ("loot_seeking", "戦利品探索", "Loot Seeking", "装備やアイテム獲得を目指す行動"),
        ("currency_saving", "通貨貯蓄", "Currency Saving", "ゲーム内通貨を消費せず蓄える行動"),
        ("currency_spending", "通貨消費", "Currency Spending", "ゲーム内通貨を強化や装飾へ使う行動"),
        ("upgrade_investment", "強化投資", "Upgrade Investment", "性能向上へ資源を投入する行動"),
        ("cosmetic_preference", "装飾選好", "Cosmetic Preference", "性能以外の外見要素へ価値を置く行動"),
        ("random_reward_engagement", "ランダム報酬関与", "Random Reward Engagement", "確率的な報酬仕組みへ参加する行動"),
        ("reward_satiation_behavior", "報酬飽和行動", "Reward Satiation Behavior", "同一報酬の反復後に行動量が低下する反応"),
    ]),
    ("Cooperation", "協力と社会行動", [
        ("cooperative_play", "協力プレイ", "Cooperative Play", "他プレイヤーと共通目標へ取り組む行動"),
        ("helping_behavior", "援助行動", "Helping Behavior", "他プレイヤーの進行や回復を支援する行動"),
        ("resource_sharing_game", "ゲーム内資源共有", "Game Resource Sharing", "所有資源を他プレイヤーへ分ける行動"),
        ("role_specialization", "役割特化", "Role Specialization", "チーム内で特定役割を継続して担う行動"),
        ("team_coordination", "チーム調整", "Team Coordination", "位置・目標・タイミングを仲間とそろえる行動"),
        ("communication_during_play", "プレイ中伝達", "Communication During Play", "協力のため情報や意図を共有する行動"),
        ("revive_support", "救助支援", "Revive Support", "不利な仲間を救助または回復する行動"),
        ("group_joining", "グループ参加", "Group Joining", "ギルドやパーティーへ参加する行動"),
        ("group_leaving", "グループ離脱", "Group Leaving", "所属グループから離れる行動"),
        ("social_reciprocity_game", "ゲーム内互恵性", "Game Social Reciprocity", "受けた支援や協力へ応答する行動"),
    ]),
    ("Competition", "競争", [
        ("competitive_play", "競争プレイ", "Competitive Play", "他者との勝敗や順位を伴う活動へ参加する行動"),
        ("ranked_mode_engagement", "ランク戦関与", "Ranked Mode Engagement", "評価や順位が変動するモードを選ぶ行動"),
        ("leaderboard_checking", "順位表確認", "Leaderboard Checking", "自分や他者の順位を確認する行動"),
        ("performance_comparison", "成績比較", "Performance Comparison", "スコアや記録を他者と比較する行動"),
        ("opponent_adaptation", "対戦相手適応", "Opponent Adaptation", "相手の行動に応じ戦術を変える行動"),
        ("rematch_behavior", "再戦行動", "Rematch Behavior", "対戦終了後に同じ相手との再戦を選ぶ行動"),
        ("win_streak_continuation", "連勝継続", "Win Streak Continuation", "連勝中にプレイを続ける行動"),
        ("loss_streak_response", "連敗反応", "Loss Streak Response", "連敗中に示す継続・変更・終了行動"),
        ("sportsmanship_behavior", "スポーツマンシップ行動", "Sportsmanship Behavior", "勝敗後も規範と相手への敬意を保つ行動"),
        ("competitive_toxicity_signal", "競争的有害行動シグナル", "Competitive Toxicity Signal", "競争場面の攻撃・侮辱・妨害を捉える観測概念"),
    ]),
    ("Play Style", "プレイスタイル", [
        ("planning_play_style", "計画型プレイ", "Planning Play Style", "事前に装備や手順を整えて進める行動"),
        ("improvisational_play_style", "即興型プレイ", "Improvisational Play Style", "状況に応じその場で方法を変える行動"),
        ("optimization_behavior", "最適化行動", "Optimization Behavior", "効率や性能を比較して改善する行動"),
        ("role_play_expression", "ロールプレイ表現", "Role Play Expression", "選んだ人物像や物語設定に沿って行動するプレイ"),
        ("customization_behavior", "カスタマイズ行動", "Customization Behavior", "外見・能力・操作環境を自分向けに調整する行動"),
        ("tutorial_engagement", "チュートリアル関与", "Tutorial Engagement", "説明や練習機能を利用して学ぶ行動"),
        ("control_mastery", "操作習熟", "Control Mastery", "操作精度や速度が経験とともに高まる過程"),
        ("mechanic_experimentation", "メカニクス実験", "Mechanic Experimentation", "ゲーム規則や操作の組合せを試す行動"),
        ("accessibility_setting_use", "アクセシビリティ設定利用", "Accessibility Setting Use", "必要に応じ表示や操作支援を利用する行動"),
        ("play_style_switching", "プレイスタイル切替", "Play Style Switching", "目的や状況に応じ遊び方を変える行動"),
    ]),
    ("Observation and Integration", "観測と統合", [
        ("gameplay_choice_signal", "プレイ選択シグナル", "Gameplay Choice Signal", "反復するゲーム内選択を捉える観測概念"),
        ("gameplay_effort_signal", "プレイ努力シグナル", "Gameplay Effort Signal", "試行回数・時間・準備量を捉える観測概念"),
        ("gameplay_persistence_signal", "プレイ持続シグナル", "Gameplay Persistence Signal", "課題やセッションの継続を捉える観測概念"),
        ("gameplay_abandonment_signal", "プレイ離脱シグナル", "Gameplay Abandonment Signal", "終了・放棄・休止の文脈を捉える観測概念"),
        ("gameplay_learning_signal", "プレイ学習シグナル", "Gameplay Learning Signal", "失敗後の改善や習熟を捉える観測概念"),
        ("gameplay_social_signal", "プレイ社会行動シグナル", "Gameplay Social Signal", "協力・競争・交流の推移を捉える観測概念"),
        ("game_design_dependency", "ゲーム設計依存性", "Game Design Dependency", "観測行動がルールやUIに制約される度合い"),
        ("game_behavior_profile", "ゲーム行動プロファイル", "Game Behavior Profile", "複数のプレイ傾向をゲーム別に整理する枠組み"),
        ("cross_game_mapping", "ゲーム横断マッピング", "Cross Game Mapping", "異なるゲーム間で比較可能な行動へ対応づける枠組み"),
        ("game_behavior_integration", "ゲーム行動統合", "Game Behavior Integration", "観測・動機・補正・根拠を安全に接続する枠組み"),
    ]),
]


def make_item(item_id, slug, name_ja, name_en, focus, section_en, section_ja):
    return {
        "filename": f"{item_id}_{slug}.yml",
        "id": item_id,
        "knowledge_type": "game_behavior",
        "name_ja": name_ja,
        "name_en": name_en,
        "category": "Game Behavior",
        "attribute": section_en,
        "definition_ja": f"{name_ja}は、{focus}を表すゲーム行動概念。単一ゲームから人格を断定しない。",
        "tags": ["CAT:ゲーム行動", f"CAT:{section_ja}", "ATTR:観測行動"],
        "parent": [section_ja],
        "related": ["行動観測", "動機づけ", "意思決定"],
        "observable_data": ["選択ログ", "操作時刻と所要時間", "成功・失敗・再試行", "セッションと離脱の推移"],
        "signal_candidates": [
            f"{name_ja}と整合する行動が複数セッションで観測される",
            "難度・報酬・UI・ゲームジャンルの変化に伴って行動が変化する",
        ],
        "device_level": "ゲームクライアントまたはサーバーの同意済みイベントログから観測可能",
        "modifiers": ["ゲームジャンル", "ゲーム設計", "難度", "習熟度", "端末", "プレイ時間", "社会的状況"],
        "evidence": "ゲーム研究・ゲームUX・行動科学・学習科学・HCI研究を参照",
        "status": "active",
    }


def main():
    items = []
    index_lines = ["category: Game Behavior", "name_ja: ゲーム行動", "items:"]
    number = 1
    for section_en, section_ja, definitions in SECTIONS:
        for slug, name_ja, name_en, focus in definitions:
            item_id = f"GMB-{number:06d}"
            item = make_item(item_id, slug, name_ja, name_en, focus, section_en, section_ja)
            items.append(item)
            index_lines.append(f"  - {item['filename']}")
            number += 1
    if len(items) != 100:
        raise ValueError(f"Expected 100 items, got {len(items)}")
    index_lines.extend([
        "notes:",
        "  - ゲーム行動はゲーム設計・難度・習熟度に強く依存し、人格を単独で断定しない",
        "  - 複数ゲーム・複数セッション・Modifierを組み合わせて推論材料として扱う",
        "  - 課金・未成年・有害行動に関するデータは安全倫理と同意管理を優先する",
    ])
    pack = {
        "output_dir": "vol27_game_behavior/game_behavior_001_100",
        "index_filename": "game_behavior_001_100_index.yml",
        "index_content": "\n".join(index_lines) + "\n",
        "items": items,
    }
    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(json.dumps(pack, ensure_ascii=False, indent=2), encoding="utf-8")
    print(f"Created: {OUT}")
    print(f"Items: {len(items)}")


if __name__ == "__main__":
    main()
