"""Build the Vol28 Decision Strategy master pack (DEC-000001..000100)."""

from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "data" / "master_packs" / "vol28_decision_strategy_001_100.json"


SECTIONS = [
    ("Problem Framing", "問題設定", [
        ("problem_recognition", "問題認識", "Problem Recognition", "判断が必要な問題や機会を捉える過程"),
        ("goal_clarification", "目標明確化", "Goal Clarification", "判断によって達成したい状態を具体化する過程"),
        ("constraint_identification", "制約特定", "Constraint Identification", "利用可能な時間・資源・規則などの制約を把握する過程"),
        ("decision_scope_setting", "判断範囲設定", "Decision Scope Setting", "今回の判断に含める対象と含めない対象を区切る過程"),
        ("stakeholder_identification", "利害関係者特定", "Stakeholder Identification", "判断の影響を受ける関係者を把握する過程"),
        ("time_horizon_setting", "時間軸設定", "Time Horizon Setting", "短期・中期・長期のどこまで結果を考慮するか定める過程"),
        ("success_criteria_setting", "成功基準設定", "Success Criteria Setting", "望ましい結果を評価する基準を設定する過程"),
        ("assumption_explication", "前提明示", "Assumption Explication", "判断の土台となる仮定を言語化する過程"),
        ("reframing_behavior", "問題再構成", "Problem Reframing", "別の視点から問題の捉え方を組み替える過程"),
        ("priority_definition", "優先事項定義", "Priority Definition", "複数の目的や制約の優先順位を定める過程"),
    ]),
    ("Information Search", "情報探索", [
        ("information_need_recognition", "情報必要性認識", "Information Need Recognition", "判断に不足している情報を認識する過程"),
        ("targeted_information_search", "焦点型情報探索", "Targeted Information Search", "特定の疑問に答える情報を絞って探す過程"),
        ("broad_information_search", "広域型情報探索", "Broad Information Search", "未知の選択肢や論点を広く探す過程"),
        ("source_diversification", "情報源多様化", "Source Diversification", "異なる立場や種類の情報源を組み合わせる過程"),
        ("source_credibility_check", "情報源信頼性確認", "Source Credibility Check", "情報源の専門性・独立性・更新性を確かめる過程"),
        ("evidence_comparison", "根拠比較", "Evidence Comparison", "複数の根拠の一致点と相違点を比較する過程"),
        ("missing_information_awareness", "欠落情報認識", "Missing Information Awareness", "確認できていない情報や不明点を明示する過程"),
        ("search_stopping", "探索終了判断", "Search Stopping", "追加探索の費用と価値を比べて探索を終える過程"),
        ("information_overload_management", "情報過多管理", "Information Overload Management", "情報量が多い状況で整理・選別する過程"),
        ("information_search_integration", "情報探索統合", "Information Search Integration", "集めた情報を判断可能な形へ統合する過程"),
    ]),
    ("Option Generation", "選択肢生成", [
        ("option_generation", "選択肢生成", "Option Generation", "実行可能な代替案を作り出す過程"),
        ("alternative_diversity", "代替案多様性", "Alternative Diversity", "性質の異なる複数の代替案を揃える過程"),
        ("default_option_acceptance", "既定選択受容", "Default Option Acceptance", "あらかじめ提示された選択肢を採用する過程"),
        ("creative_alternative_generation", "創造的代替案生成", "Creative Alternative Generation", "既存案にない新しい選択肢を考える過程"),
        ("outside_option_consideration", "選択外案検討", "Outside Option Consideration", "選ばない・延期するなど提示外の案を検討する過程"),
        ("option_decomposition", "選択肢分解", "Option Decomposition", "複雑な案を構成要素や段階へ分ける過程"),
        ("option_combination", "選択肢組合せ", "Option Combination", "複数案の長所を組み合わせる過程"),
        ("contingency_option_generation", "条件分岐案生成", "Contingency Option Generation", "状況変化に応じた予備案を用意する過程"),
        ("reversible_option_design", "可逆案設計", "Reversible Option Design", "後から戻したり変更したりできる案を設計する過程"),
        ("option_set_sufficiency", "選択肢集合充足性", "Option Set Sufficiency", "比較に十分な選択肢が揃ったかを判断する過程"),
    ]),
    ("Evaluation and Tradeoffs", "評価とトレードオフ", [
        ("criteria_weighting", "評価基準重みづけ", "Criteria Weighting", "評価基準ごとの重要度を定める過程"),
        ("benefit_cost_comparison", "便益費用比較", "Benefit Cost Comparison", "期待される利点と必要な負担を比較する過程"),
        ("tradeoff_acceptance", "トレードオフ受容", "Tradeoff Acceptance", "一方を得るために別の価値を譲る必要性を扱う過程"),
        ("multi_criteria_evaluation", "多基準評価", "Multi-Criteria Evaluation", "複数の評価軸を併用して選択肢を比べる過程"),
        ("opportunity_cost_awareness", "機会費用認識", "Opportunity Cost Awareness", "ある案を選ぶことで失う別の可能性を考慮する過程"),
        ("threshold_based_choice", "閾値型選択", "Threshold-Based Choice", "必要条件を満たす案から選ぶ過程"),
        ("lexicographic_choice", "辞書式選択", "Lexicographic Choice", "最重要基準を優先し同点時に次の基準を見る過程"),
        ("satisficing_strategy", "満足化戦略", "Satisficing Strategy", "十分な基準を満たした案を採用する過程"),
        ("maximizing_strategy", "最大化戦略", "Maximizing Strategy", "比較可能な範囲で最良の案を探す過程"),
        ("value_alignment_check", "価値整合確認", "Value Alignment Check", "選択肢が本人や組織の価値・目的に沿うか確かめる過程"),
    ]),
    ("Uncertainty and Probability", "不確実性と確率", [
        ("uncertainty_tolerance", "不確実性許容", "Uncertainty Tolerance", "結果が確定しない状態を抱えながら判断する過程"),
        ("probability_estimation", "確率推定", "Probability Estimation", "複数の結果が起こる見込みを推定する過程"),
        ("confidence_calibration", "確信度較正", "Confidence Calibration", "判断への確信度を根拠の強さに合わせる過程"),
        ("base_rate_consideration", "基準率考慮", "Base Rate Consideration", "個別情報とあわせて一般的な発生頻度を考慮する過程"),
        ("scenario_analysis", "シナリオ分析", "Scenario Analysis", "複数の将来状況を想定して結果を検討する過程"),
        ("sensitivity_analysis", "感度分析", "Sensitivity Analysis", "前提の変化が結論へ与える影響を確かめる過程"),
        ("ambiguity_management", "曖昧性管理", "Ambiguity Management", "確率自体が不明な状況を整理して扱う過程"),
        ("worst_case_consideration", "最悪ケース考慮", "Worst-Case Consideration", "重大な不利益が生じる状況を検討する過程"),
        ("best_case_consideration", "最良ケース考慮", "Best-Case Consideration", "望ましい結果が生じる条件を検討する過程"),
        ("expected_outcome_reasoning", "期待結果推論", "Expected Outcome Reasoning", "結果の価値と起こりやすさを組み合わせて考える過程"),
    ]),
    ("Risk and Loss", "リスクと損失", [
        ("risk_identification", "リスク特定", "Risk Identification", "選択に伴う不利益や障害を洗い出す過程"),
        ("risk_appetite_expression", "リスク許容方針表明", "Risk Appetite Expression", "どの程度のリスクを受け入れるか明示する過程"),
        ("loss_avoidance_strategy", "損失回避戦略", "Loss Avoidance Strategy", "損失の発生確率や規模を抑える案を選ぶ過程"),
        ("downside_protection", "下方保護", "Downside Protection", "不利な結果になった場合の影響を限定する過程"),
        ("risk_diversification", "リスク分散", "Risk Diversification", "資源や選択を分けて単一失敗への依存を減らす過程"),
        ("risk_reversibility", "リスク可逆性", "Risk Reversibility", "失敗時に撤回・修正できる度合いを考慮する過程"),
        ("risk_control_planning", "リスク統制計画", "Risk Control Planning", "検知・予防・対応の手段を事前に定める過程"),
        ("risk_reward_balance", "リスク報酬均衡", "Risk Reward Balance", "見込まれる利益と不利益の釣り合いを評価する過程"),
        ("regret_anticipation", "後悔予期", "Regret Anticipation", "選択後に生じうる後悔を事前に考慮する過程"),
        ("safety_margin_setting", "安全余裕設定", "Safety Margin Setting", "予測誤差や変動に備えて余裕を確保する過程"),
    ]),
    ("Time and Effort", "時間と労力", [
        ("decision_urgency", "判断緊急度評価", "Decision Urgency", "判断を急ぐ必要性を評価する過程"),
        ("deliberation_time_allocation", "熟慮時間配分", "Deliberation Time Allocation", "判断の重要度に応じて考える時間を配分する過程"),
        ("decision_delay", "判断延期", "Decision Delay", "追加情報や適切な時機を待って判断を保留する過程"),
        ("deadline_response", "期限対応", "Deadline Response", "残り時間に応じて探索や比較方法を調整する過程"),
        ("effort_budgeting", "判断労力配分", "Effort Budgeting", "判断へ投入する認知的・実務的労力を配分する過程"),
        ("cognitive_load_management", "認知負荷管理", "Cognitive Load Management", "複雑さを減らして判断可能な状態を保つ過程"),
        ("decision_routine_use", "判断ルーチン利用", "Decision Routine Use", "反復的な判断に定型手順を利用する過程"),
        ("automation_preference", "自動化選好", "Automation Preference", "規則やシステムに判断の一部を委ねる過程"),
        ("delegation_decision", "判断委任", "Delegation Decision", "適切な知識・権限を持つ相手へ判断を委ねる過程"),
        ("timing_strategy", "判断時機戦略", "Timing Strategy", "実行や確定に適した時点を選ぶ過程"),
    ]),
    ("Social Decision Process", "社会的判断過程", [
        ("advice_seeking", "助言探索", "Advice Seeking", "判断前に他者の意見や経験を求める過程"),
        ("expert_consultation", "専門家相談", "Expert Consultation", "専門知識を持つ相手の見解を判断へ取り入れる過程"),
        ("peer_consultation", "同輩相談", "Peer Consultation", "近い立場や経験を持つ相手と選択肢を検討する過程"),
        ("consensus_seeking", "合意探索", "Consensus Seeking", "関係者が受け入れられる共通案を探る過程"),
        ("independent_judgment", "独立判断", "Independent Judgment", "他者の意見を参照しつつ自ら結論を形成する過程"),
        ("perspective_taking", "視点取得", "Perspective Taking", "異なる立場から選択の影響を考える過程"),
        ("dissent_consideration", "異論考慮", "Dissent Consideration", "反対意見や少数意見を検討材料に含める過程"),
        ("group_influence_awareness", "集団影響認識", "Group Influence Awareness", "同調・権威・役割が判断へ与える影響を意識する過程"),
        ("accountability_communication", "説明責任伝達", "Accountability Communication", "判断理由と責任範囲を関係者へ説明する過程"),
        ("shared_decision_making", "共同意思決定", "Shared Decision Making", "関係者が情報・価値・責任を共有して判断する過程"),
    ]),
    ("Commitment and Revision", "確定と修正", [
        ("commitment_strength", "決定確定度", "Commitment Strength", "選んだ案へ資源と注意を向ける度合いを定める過程"),
        ("implementation_intention", "実行意図形成", "Implementation Intention", "いつ・どこで・どのように実行するか具体化する過程"),
        ("decision_follow_through", "決定遂行", "Decision Follow-Through", "確定した選択を実際の行動へ移す過程"),
        ("post_decision_monitoring", "決定後監視", "Post-Decision Monitoring", "実行後の結果や前提変化を継続して確認する過程"),
        ("feedback_based_revision", "フィードバック修正", "Feedback-Based Revision", "新しい結果や情報に基づいて判断を調整する過程"),
        ("decision_reversal", "決定撤回", "Decision Reversal", "条件変化や誤りを受けて以前の決定を取り消す過程"),
        ("sunk_cost_disengagement", "埋没費用離脱", "Sunk Cost Disengagement", "回収不能な過去の投入と今後の判断を分ける過程"),
        ("error_acknowledgment", "判断誤り認識", "Error Acknowledgment", "期待と結果のずれから判断上の誤りを認める過程"),
        ("learning_from_outcomes", "結果学習", "Learning from Outcomes", "判断結果から次の判断に使える知見を抽出する過程"),
        ("decision_recording", "判断記録", "Decision Recording", "前提・選択肢・理由・結果を追跡可能な形で残す過程"),
    ]),
    ("Observation and Integration", "観測と統合", [
        ("decision_latency_signal", "判断潜時シグナル", "Decision Latency Signal", "選択肢提示から確定までの時間を捉える観測概念"),
        ("option_count_signal", "選択肢数シグナル", "Option Count Signal", "生成・閲覧・比較された選択肢数を捉える観測概念"),
        ("information_search_depth_signal", "情報探索深度シグナル", "Information Search Depth Signal", "情報源・閲覧量・確認段階の深さを捉える観測概念"),
        ("comparison_pattern_signal", "比較パターンシグナル", "Comparison Pattern Signal", "選択肢間の往復や評価軸の使い方を捉える観測概念"),
        ("confidence_expression_signal", "確信表明シグナル", "Confidence Expression Signal", "選択時に示される確信度や保留表現を捉える観測概念"),
        ("revision_pattern_signal", "修正パターンシグナル", "Revision Pattern Signal", "新情報後の変更・維持・撤回を捉える観測概念"),
        ("context_dependency", "判断文脈依存性", "Decision Context Dependency", "領域・重要度・時間圧などにより戦略が変わる度合い"),
        ("cross_situation_consistency", "状況横断一貫性", "Cross-Situation Consistency", "異なる判断場面で似た過程が再現する度合い"),
        ("decision_strategy_profile", "意思決定戦略プロファイル", "Decision Strategy Profile", "複数の判断過程を文脈別に整理する枠組み"),
        ("decision_strategy_integration", "意思決定戦略統合", "Decision Strategy Integration", "観測・補正・根拠を安全に接続するための統合枠組み"),
    ]),
]


def make_item(item_id, slug, name_ja, name_en, focus, section_en, section_ja):
    return {
        "filename": f"{item_id}_{slug}.yml",
        "id": item_id,
        "knowledge_type": "decision_strategy",
        "name_ja": name_ja,
        "name_en": name_en,
        "category": "Decision Strategy",
        "attribute": section_en,
        "definition_ja": f"{name_ja}は、{focus}を表す意思決定概念。単独の選択から能力・人格・合理性を断定しない。",
        "tags": ["CAT:意思決定戦略", f"CAT:{section_ja}", "ATTR:判断過程"],
        "parent": [section_ja],
        "related": ["意思決定", "行動観測", "認知過程"],
        "observable_data": ["選択肢の提示・閲覧・比較ログ", "情報探索と確認の時系列", "判断・保留・変更の時刻", "選択後の実行と結果"],
        "signal_candidates": [
            f"{name_ja}と整合する判断過程が複数場面で観測される",
            "重要度・時間圧・知識量・可逆性の変化に伴って判断過程が変化する",
        ],
        "device_level": "アプリまたはゲーム内の同意済みイベントログ、明示回答、操作系列から観測可能",
        "modifiers": ["判断領域", "結果の重要度", "領域知識", "情報利用可能性", "時間圧", "感情・身体状態", "社会的役割", "可逆性"],
        "evidence": "意思決定科学・認知心理学・行動経済学・組織行動・HCI研究を参照",
        "status": "active",
    }


def main():
    items = []
    index_lines = ["category: Decision Strategy", "name_ja: 意思決定戦略", "items:"]
    number = 1
    for section_en, section_ja, definitions in SECTIONS:
        for slug, name_ja, name_en, focus in definitions:
            item_id = f"DEC-{number:06d}"
            item = make_item(item_id, slug, name_ja, name_en, focus, section_en, section_ja)
            items.append(item)
            index_lines.append(f"  - {item['filename']}")
            number += 1
    if len(items) != 100:
        raise ValueError(f"Expected 100 items, got {len(items)}")
    index_lines.extend([
        "notes:",
        "  - 意思決定戦略は文脈・重要度・知識・時間圧に依存し、能力や人格を単独で断定しない",
        "  - 複数場面・複数時点の観測とModifierを組み合わせ、推論アプリ側で慎重に扱う",
        "  - 医療・法律・採用・金融など高影響領域の自動判断には直接利用しない",
    ])
    pack = {
        "output_dir": "vol28_decision_strategy/decision_strategy_001_100",
        "index_filename": "decision_strategy_001_100_index.yml",
        "index_content": "\n".join(index_lines) + "\n",
        "items": items,
    }
    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(json.dumps(pack, ensure_ascii=False, indent=2), encoding="utf-8")
    print(f"Created: {OUT}")
    print(f"Items: {len(items)}")


if __name__ == "__main__":
    main()
