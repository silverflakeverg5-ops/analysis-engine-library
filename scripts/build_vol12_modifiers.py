import json
from pathlib import Path

OUT = Path("data/master_packs/vol12_modifiers_051_100.json")

SECTIONS = [
    {
        "category": "Modifiers - App Domain Correction",
        "name_ja": "補正要因・アプリ領域補正",
        "items": [
            ("MOD-000051", "diagnosis_app_modifier", "診断アプリ補正", "Diagnosis App Modifier", "診断・自己理解アプリでの表示や推論強度を補正する要因。"),
            ("MOD-000052", "game_app_modifier", "ゲームアプリ補正", "Game App Modifier", "ゲーム内行動が娯楽文脈で発生していることを補正する要因。"),
            ("MOD-000053", "assistant_app_modifier", "秘書アプリ補正", "Assistant App Modifier", "予定・通知・タスク支援アプリでの生活文脈を補正する要因。"),
            ("MOD-000054", "education_app_modifier", "教育アプリ補正", "Education App Modifier", "学習ログや成績が教材・難易度・評価設計に左右されることを補正する要因。"),
            ("MOD-000055", "work_support_modifier", "仕事支援補正", "Work Support Modifier", "業務文脈での行動が役割・期限・組織要因に左右されることを補正する要因。"),
            ("MOD-000056", "wellbeing_app_modifier", "ウェルビーイング補正", "Wellbeing App Modifier", "健康・気分・生活記録に関する推論を慎重化する補正要因。"),
            ("MOD-000057", "compatibility_app_modifier", "相性アプリ補正", "Compatibility App Modifier", "相性推定において断定や優劣評価を避けるための補正要因。"),
            ("MOD-000058", "social_app_modifier", "SNSアプリ補正", "Social App Modifier", "SNS上の行動が表示設計・社会的評価・文脈に影響されることを補正する要因。"),
            ("MOD-000059", "productivity_app_modifier", "生産性アプリ補正", "Productivity App Modifier", "タスク・集中・完了率が業務量や外部要求に左右されることを補正する要因。"),
            ("MOD-000060", "multi_app_modifier", "複数アプリ横断補正", "Multi App Modifier", "複数アプリ間で観測文脈やデータ粒度が異なることを補正する要因。")
        ]
    },
    {
        "category": "Modifiers - Temporal Correction",
        "name_ja": "補正要因・時系列補正",
        "items": [
            ("MOD-000061", "short_term_state_modifier", "短期状態補正", "Short Term State Modifier", "一時的な状態変化を長期傾向と誤認しないための補正要因。"),
            ("MOD-000062", "long_term_trait_modifier", "長期傾向補正", "Long Term Trait Modifier", "長期間安定して観測される傾向を重視する補正要因。"),
            ("MOD-000063", "trend_modifier", "傾向変化補正", "Trend Modifier", "時系列上の増加・低下・安定傾向を反映する補正要因。"),
            ("MOD-000064", "seasonality_modifier", "季節性補正", "Seasonality Modifier", "季節・年度・イベント周期による行動変化を補正する要因。"),
            ("MOD-000065", "event_window_modifier", "イベント期間補正", "Event Window Modifier", "試験・繁忙期・旅行・体調不良など特定期間の影響を補正する要因。"),
            ("MOD-000066", "adaptation_period_modifier", "適応期間補正", "Adaptation Period Modifier", "新環境・新機能・新課題への慣れによる変化を補正する要因。"),
            ("MOD-000067", "recency_weight_modifier", "直近重み補正", "Recency Weight Modifier", "直近データをどの程度重視するかを調整する補正要因。"),
            ("MOD-000068", "history_length_modifier", "履歴長補正", "History Length Modifier", "利用可能な履歴期間の長短による推論信頼度を補正する要因。"),
            ("MOD-000069", "recovery_window_modifier", "回復期間補正", "Recovery Window Modifier", "負荷や低下後に回復するまでの期間を考慮する補正要因。"),
            ("MOD-000070", "change_point_modifier", "変化点補正", "Change Point Modifier", "行動や状態が大きく変わった時点を考慮する補正要因。")
        ]
    },
    {
        "category": "Modifiers - Social Correction",
        "name_ja": "補正要因・社会補正",
        "items": [
            ("MOD-000071", "public_visibility_modifier", "公開性補正", "Public Visibility Modifier", "他者から見える場面で行動や表現が変わることを補正する要因。"),
            ("MOD-000072", "anonymous_context_modifier", "匿名文脈補正", "Anonymous Context Modifier", "匿名性によって自己開示や攻撃性が変化することを補正する要因。"),
            ("MOD-000073", "authority_presence_modifier", "権威存在補正", "Authority Presence Modifier", "上司・教師・専門家など権威の存在による行動差を補正する要因。"),
            ("MOD-000074", "peer_presence_modifier", "仲間存在補正", "Peer Presence Modifier", "仲間や同年代の存在による同調・競争・自己呈示の影響を補正する要因。"),
            ("MOD-000075", "group_norm_modifier", "集団規範補正", "Group Norm Modifier", "集団の暗黙ルールや期待による行動差を補正する要因。"),
            ("MOD-000076", "relationship_closeness_modifier", "関係親密度補正", "Relationship Closeness Modifier", "相手との親密さや距離感による表現・反応差を補正する要因。"),
            ("MOD-000077", "power_distance_modifier", "権力距離補正", "Power Distance Modifier", "上下関係や地位差による発言・選択の変化を補正する要因。"),
            ("MOD-000078", "social_evaluation_modifier", "社会的評価補正", "Social Evaluation Modifier", "評価・評判・承認への意識による行動変化を補正する要因。"),
            ("MOD-000079", "conflict_context_modifier", "葛藤文脈補正", "Conflict Context Modifier", "対立や不和の文脈で行動や感情が変わることを補正する要因。"),
            ("MOD-000080", "support_presence_modifier", "支援存在補正", "Support Presence Modifier", "周囲の支援や相談先の有無による行動差を補正する要因。")
        ]
    },
    {
        "category": "Modifiers - Interpretation Correction",
        "name_ja": "補正要因・解釈補正",
        "items": [
            ("MOD-000081", "non_diagnostic_modifier", "非診断補正", "Non Diagnostic Modifier", "観測結果を診断や断定として扱わないための補正要因。"),
            ("MOD-000082", "possibility_expression_modifier", "可能性表現補正", "Possibility Expression Modifier", "推論結果を可能性や傾向として表現するための補正要因。"),
            ("MOD-000083", "uncertainty_expression_modifier", "不確実性表現補正", "Uncertainty Expression Modifier", "データ不足や文脈不明時に不確実性を明示する補正要因。"),
            ("MOD-000084", "strength_scaling_modifier", "推論強度調整補正", "Strength Scaling Modifier", "根拠の量や一貫性に応じて推論強度を調整する補正要因。"),
            ("MOD-000085", "alternative_explanation_modifier", "代替説明補正", "Alternative Explanation Modifier", "一つの解釈に固定せず複数の説明可能性を残す補正要因。"),
            ("MOD-000086", "contextual_display_modifier", "文脈付き表示補正", "Contextual Display Modifier", "結果を文脈条件とセットで表示するための補正要因。"),
            ("MOD-000087", "supportive_tone_modifier", "支援的表現補正", "Supportive Tone Modifier", "評価的・断定的ではなく支援的に表示するための補正要因。"),
            ("MOD-000088", "user_control_modifier", "ユーザー主導補正", "User Control Modifier", "推論表示や提案をユーザーが選択・調整できるようにする補正要因。"),
            ("MOD-000089", "explainability_modifier", "説明可能性補正", "Explainability Modifier", "なぜその推論材料が使われたか説明しやすくする補正要因。"),
            ("MOD-000090", "feedback_loop_modifier", "フィードバックループ補正", "Feedback Loop Modifier", "ユーザーの修正・否定・確認を次回推論に反映する補正要因。")
        ]
    },
    {
        "category": "Modifiers - Integration",
        "name_ja": "補正要因・統合",
        "items": [
            ("MOD-000091", "modifier_priority", "補正優先度", "Modifier Priority", "複数補正要因がある場合にどれを優先するかの管理概念。"),
            ("MOD-000092", "modifier_conflict_resolution", "補正競合解決", "Modifier Conflict Resolution", "補正要因同士が矛盾する場合に解釈を調整する枠組み。"),
            ("MOD-000093", "modifier_stack", "補正スタック", "Modifier Stack", "複数の補正要因を重ねて適用するための管理概念。"),
            ("MOD-000094", "confidence_adjustment", "信頼度調整", "Confidence Adjustment", "観測量・一貫性・文脈をもとに推論信頼度を調整する概念。"),
            ("MOD-000095", "interpretation_guardrail", "解釈ガードレール", "Interpretation Guardrail", "過度な断定・偏見・不適切表示を防ぐ補正枠組み。"),
            ("MOD-000096", "cross_domain_modifier", "領域横断補正", "Cross Domain Modifier", "複数領域のデータや知識を横断する際の補正要因。"),
            ("MOD-000097", "human_review_modifier", "人間確認補正", "Human Review Modifier", "高リスク推論や曖昧な結果に人間確認を挟む補正要因。"),
            ("MOD-000098", "adaptive_modifier", "適応的補正", "Adaptive Modifier", "利用履歴やユーザー反応に応じて補正のかけ方を調整する概念。"),
            ("MOD-000099", "modifier_audit_signal", "補正監査シグナル", "Modifier Audit Signal", "補正が適切に適用されたか確認するための監査材料。"),
            ("MOD-000100", "modifier_integration", "補正統合", "Modifier Integration", "文脈・状態・品質・安全性を統合して推論を調整する枠組み。")
        ]
    }
]


def make_item(item_id, slug, name_ja, name_en, definition_ja, category, parent_ja):
    return {
        "filename": f"{item_id}_{slug}.yml",
        "id": item_id,
        "knowledge_type": "modifier",
        "name_ja": name_ja,
        "name_en": name_en,
        "category": "Modifier",
        "attribute": category.replace("Modifiers - ", ""),
        "definition_ja": definition_ja,
        "tags": ["CAT:補正要因", f"CAT:{parent_ja}", "ATTR:推論補正"],
        "parent": [parent_ja],
        "related": ["観測シグナル", "推論材料", "安全設計"],
        "observable_data": [
            f"{name_ja}適用条件",
            f"{name_ja}補正対象",
            f"{name_ja}信頼度影響",
            f"{name_ja}時系列影響"
        ],
        "signal_candidates": [
            f"{name_ja}が必要な文脈が観測される",
            "推論結果の強さや表示表現を補正する材料になる"
        ],
        "device_level": "スマホ・PCで推定可能",
        "modifiers": ["文脈", "データ品質", "個人差", "安全性"],
        "evidence": "心理測定・HCI・UX研究・安全設計で使用",
        "status": "active"
    }


def main():
    all_items = []
    index_lines = ["category: Modifier", "name_ja: 補正要因", "items:"]

    for section in SECTIONS:
        parent_ja = section["name_ja"].replace("補正要因・", "")
        for raw in section["items"]:
            item = make_item(*raw, category=section["category"], parent_ja=parent_ja)
            all_items.append(item)
            index_lines.append(f"  - {item['filename']}")

    index_lines.extend([
        "notes:",
        "  - 補正要因は推論結果ではなく調整材料として扱う",
        "  - Knowledge DB側ではスコアリングしない",
        "  - アプリ側で推論強度・信頼度・表示表現を補正する"
    ])

    pack = {
        "output_dir": "vol12_modifiers/modifiers_051_100",
        "index_filename": "modifiers_051_100_index.yml",
        "index_content": "\n".join(index_lines) + "\n",
        "items": all_items
    }

    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(json.dumps(pack, ensure_ascii=False, indent=2), encoding="utf-8")

    print(f"Created: {OUT}")
    print(f"Items: {len(all_items)}")


if __name__ == "__main__":
    main()