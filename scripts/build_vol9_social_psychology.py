import json
from pathlib import Path

OUT = Path("data/master_packs/vol9_social_psychology_151_200.json")

SECTIONS = [
    {
        "category": "Social Psychology - Social Decision Making",
        "name_ja": "社会心理・社会的意思決定",
        "items": [
            ("SOCPSY-000151", "social_decision_making", "社会的意思決定", "Social Decision Making", "他者・集団・規範・評判を考慮して選択を行う過程。"),
            ("SOCPSY-000152", "interdependent_decision", "相互依存的意思決定", "Interdependent Decision Making", "自分と他者の結果が互いに影響する状況での意思決定。"),
            ("SOCPSY-000153", "fairness_preference", "公平性選好", "Fairness Preference", "利益や負担が公平に分配されることを好む傾向。"),
            ("SOCPSY-000154", "trust_decision", "信頼意思決定", "Trust Decision", "相手に資源・情報・判断を委ねるかどうかの選択。"),
            ("SOCPSY-000155", "cooperative_choice", "協力選択", "Cooperative Choice", "自己利益だけでなく相互利益や集団利益を考慮して協力を選ぶこと。"),
            ("SOCPSY-000156", "competitive_choice", "競争選択", "Competitive Choice", "他者より優位に立つことや勝利を重視して選ぶこと。"),
            ("SOCPSY-000157", "reputation_based_choice", "評判ベース選択", "Reputation Based Choice", "他者からの評価や評判への影響を考慮した選択。"),
            ("SOCPSY-000158", "norm_based_choice", "規範ベース選択", "Norm Based Choice", "社会的ルールや期待に沿って行動を選ぶこと。"),
            ("SOCPSY-000159", "relationship_preserving_choice", "関係維持選択", "Relationship Preserving Choice", "短期的利益よりも関係維持を重視して選ぶこと。"),
            ("SOCPSY-000160", "social_risk_decision", "社会的リスク意思決定", "Social Risk Decision", "拒絶・批判・評価低下などの社会的リスクを考慮した意思決定。")
        ]
    },
    {
        "category": "Social Psychology - Social Learning",
        "name_ja": "社会心理・社会的学習",
        "items": [
            ("SOCPSY-000161", "social_learning", "社会的学習", "Social Learning", "他者の行動・結果・評価を観察して学ぶ過程。"),
            ("SOCPSY-000162", "modeling", "モデリング", "Modeling", "他者の行動を手本として自分の行動を形成する過程。"),
            ("SOCPSY-000163", "vicarious_reinforcement", "代理強化", "Vicarious Reinforcement", "他者が報酬や罰を受ける様子を見て自分の行動が変わる現象。"),
            ("SOCPSY-000164", "observational_norm_learning", "観察的規範学習", "Observational Norm Learning", "他者の行動観察を通じて場のルールや期待を学ぶ過程。"),
            ("SOCPSY-000165", "peer_modeling", "仲間モデリング", "Peer Modeling", "同年代や同じ立場の人の行動を参考にする学習過程。"),
            ("SOCPSY-000166", "expert_modeling", "専門家モデリング", "Expert Modeling", "熟達者や権威ある人物の行動を参考にする学習過程。"),
            ("SOCPSY-000167", "social_feedback_learning", "社会的フィードバック学習", "Social Feedback Learning", "称賛・批判・反応など社会的フィードバックを通じて行動を調整する過程。"),
            ("SOCPSY-000168", "imitation_learning", "模倣学習", "Imitation Learning", "他者の行動を直接まねることで学ぶ過程。"),
            ("SOCPSY-000169", "cultural_learning", "文化的学習", "Cultural Learning", "集団や文化に共有された知識・価値・行動様式を学ぶ過程。"),
            ("SOCPSY-000170", "social_trial_and_error", "社会的試行錯誤", "Social Trial and Error", "対人反応を見ながら行動や表現を調整していく過程。")
        ]
    },
    {
        "category": "Social Psychology - Social Stress",
        "name_ja": "社会心理・社会的ストレス",
        "items": [
            ("SOCPSY-000171", "social_stress", "社会的ストレス", "Social Stress", "対人評価・関係葛藤・所属不安など社会的要因によるストレス。"),
            ("SOCPSY-000172", "evaluation_stress", "評価ストレス", "Evaluation Stress", "他者から評価される状況で生じる緊張や負荷。"),
            ("SOCPSY-000173", "rejection_stress", "拒絶ストレス", "Rejection Stress", "拒絶・無視・排除の可能性や経験によって生じるストレス。"),
            ("SOCPSY-000174", "status_stress", "地位ストレス", "Status Stress", "地位・序列・役割の変化や比較によって生じるストレス。"),
            ("SOCPSY-000175", "role_stress", "役割ストレス", "Role Stress", "期待される役割や責任が過剰または曖昧なことで生じる負荷。"),
            ("SOCPSY-000176", "minority_stress", "マイノリティストレス", "Minority Stress", "少数派であることや偏見・差別への接触によって生じる慢性的負荷。"),
            ("SOCPSY-000177", "interpersonal_stress", "対人ストレス", "Interpersonal Stress", "人間関係の摩擦・誤解・緊張によって生じるストレス。"),
            ("SOCPSY-000178", "social_overload", "社会的過負荷", "Social Overload", "対人要求・連絡・期待が多すぎて処理負荷が高まる状態。"),
            ("SOCPSY-000179", "social_recovery", "社会的回復", "Social Recovery", "支援的な関係や安心できる場によって社会的負荷から回復する過程。"),
            ("SOCPSY-000180", "belonging_threat", "所属脅威", "Belonging Threat", "自分が集団や関係から外れる可能性を感じる状態。")
        ]
    },
    {
        "category": "Social Psychology - Social Motivation",
        "name_ja": "社会心理・社会的動機",
        "items": [
            ("SOCPSY-000181", "affiliation_motivation", "親和動機", "Affiliation Motivation", "他者とつながり、受け入れられたいという動機づけ。"),
            ("SOCPSY-000182", "power_motivation", "権力動機", "Power Motivation", "他者や状況に影響を与えたいという動機づけ。"),
            ("SOCPSY-000183", "status_motivation", "地位動機", "Status Motivation", "集団内で高い評価や地位を得たいという動機づけ。"),
            ("SOCPSY-000184", "approval_motivation", "承認動機", "Approval Motivation", "他者から好意的に評価されたいという動機づけ。"),
            ("SOCPSY-000185", "belonging_motivation", "所属動機", "Belonging Motivation", "集団や関係の一員でありたいという動機づけ。"),
            ("SOCPSY-000186", "dominance_motivation", "優位性動機", "Dominance Motivation", "対人関係や集団内で主導権を持ちたいという動機づけ。"),
            ("SOCPSY-000187", "care_motivation", "ケア動機", "Care Motivation", "他者を支援し守りたいという動機づけ。"),
            ("SOCPSY-000188", "reciprocity_motivation", "互恵動機", "Reciprocity Motivation", "受けた支援や好意に応えたいという動機づけ。"),
            ("SOCPSY-000189", "social_avoidance_motivation", "社会的回避動機", "Social Avoidance Motivation", "批判・拒絶・対立を避けるために社会的行動を控える動機づけ。"),
            ("SOCPSY-000190", "recognition_motivation", "認知承認動機", "Recognition Motivation", "努力や存在を周囲に認識されたいという動機づけ。")
        ]
    },
    {
        "category": "Social Psychology - Integration",
        "name_ja": "社会心理・統合",
        "items": [
            ("SOCPSY-000191", "social_context_integration", "社会文脈統合", "Social Context Integration", "集団・関係・規範・評価が統合して行動に影響する枠組み。"),
            ("SOCPSY-000192", "relationship_behavior_integration", "関係行動統合", "Relationship Behavior Integration", "信頼・葛藤・支援・距離感が行動に与える影響を統合する視点。"),
            ("SOCPSY-000193", "group_behavior_integration", "集団行動統合", "Group Behavior Integration", "集団規範・役割・同調・協力が行動に与える影響を統合する視点。"),
            ("SOCPSY-000194", "online_offline_social_integration", "オンラインオフライン社会統合", "Online Offline Social Integration", "オンラインと現実の社会関係が相互に影響する状態。"),
            ("SOCPSY-000195", "culture_identity_integration", "文化アイデンティティ統合", "Culture Identity Integration", "文化・集団・自己認識が統合して社会的行動に影響する状態。"),
            ("SOCPSY-000196", "social_emotion_integration", "社会的感情統合", "Social Emotion Integration", "恥・誇り・罪悪感・承認欲求などが対人行動へ影響する枠組み。"),
            ("SOCPSY-000197", "social_learning_integration", "社会的学習統合", "Social Learning Integration", "観察・模倣・フィードバック・規範学習が統合して行動を形成する過程。"),
            ("SOCPSY-000198", "social_decision_integration", "社会的意思決定統合", "Social Decision Integration", "公平性・信頼・評判・関係維持を含む意思決定統合。"),
            ("SOCPSY-000199", "social_support_integration", "社会的支援統合", "Social Support Integration", "感情的・情報的・実用的支援が行動や回復へ与える影響を統合する視点。"),
            ("SOCPSY-000200", "human_social_behavior_integration", "人間社会行動統合", "Human Social Behavior Integration", "個人特性・社会環境・文化・対人関係を統合して人間行動を理解する枠組み。")
        ]
    }
]


def make_item(item_id, slug, name_ja, name_en, definition_ja, category, parent_ja):
    return {
        "filename": f"{item_id}_{slug}.yml",
        "id": item_id,
        "knowledge_type": "social_psychology",
        "name_ja": name_ja,
        "name_en": name_en,
        "category": "Social Psychology",
        "attribute": category.replace("Social Psychology - ", ""),
        "definition_ja": definition_ja,
        "tags": ["CAT:社会心理", f"CAT:{parent_ja}", "ATTR:社会的要因"],
        "parent": [parent_ja],
        "related": ["性格", "行動観測", "環境要因"],
        "observable_data": [
            f"{name_ja}関連行動変化",
            f"{name_ja}関連反応時間",
            f"{name_ja}関連選択率",
            f"{name_ja}関連対人反応"
        ],
        "signal_candidates": [
            f"{name_ja}が対人判断・行動・感情に影響している可能性がある",
            "社会的条件の変化に応じて行動パターンが変化する"
        ],
        "device_level": "スマホ・PCのみ推定可能",
        "modifiers": ["文化", "関係性", "集団規範", "評価環境"],
        "evidence": "社会心理学・対人心理学・組織心理学・HCI研究で使用",
        "status": "active"
    }


def main():
    all_items = []
    index_lines = ["category: Social Psychology", "name_ja: 社会心理", "items:"]

    for section in SECTIONS:
        parent_ja = section["name_ja"].replace("社会心理・", "")
        for raw in section["items"]:
            item = make_item(*raw, category=section["category"], parent_ja=parent_ja)
            all_items.append(item)
            index_lines.append(f"  - {item['filename']}")

    index_lines.extend([
        "notes:",
        "  - 社会心理は性格断定ではなく推論材料として扱う",
        "  - 観測可能データとSignal候補を中心に管理する",
        "  - アプリ側でスコアリング・推論・表示を行う"
    ])

    pack = {
        "output_dir": "vol9_social_psychology/social_psychology_151_200",
        "index_filename": "social_psychology_151_200_index.yml",
        "index_content": "\n".join(index_lines) + "\n",
        "items": all_items
    }

    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(json.dumps(pack, ensure_ascii=False, indent=2), encoding="utf-8")

    print(f"Created: {OUT}")
    print(f"Items: {len(all_items)}")


if __name__ == "__main__":
    main()