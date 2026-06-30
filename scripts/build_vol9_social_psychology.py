import json
from pathlib import Path

OUT = Path("data/master_packs/vol9_social_psychology_101_150.json")

SECTIONS = [
    {
        "category": "Social Psychology - Leadership Power",
        "name_ja": "社会心理・リーダーシップ権力",
        "items": [
            ("SOCPSY-000101", "leadership", "リーダーシップ", "Leadership", "集団や他者の行動・目標・方向性に影響を与える過程。"),
            ("SOCPSY-000102", "transformational_leadership", "変革型リーダーシップ", "Transformational Leadership", "ビジョンや意味づけを通じて他者の動機づけや成長を促すリーダーシップ。"),
            ("SOCPSY-000103", "transactional_leadership", "交換型リーダーシップ", "Transactional Leadership", "報酬・評価・役割明確化を通じて行動を調整するリーダーシップ。"),
            ("SOCPSY-000104", "servant_leadership", "サーバントリーダーシップ", "Servant Leadership", "メンバー支援や成長を優先するリーダーシップ。"),
            ("SOCPSY-000105", "authoritarian_leadership", "権威主義的リーダーシップ", "Authoritarian Leadership", "強い指示・統制・上下関係に基づくリーダーシップ。"),
            ("SOCPSY-000106", "participative_leadership", "参加型リーダーシップ", "Participative Leadership", "メンバーの意見や参加を重視するリーダーシップ。"),
            ("SOCPSY-000107", "power_dynamics", "権力関係", "Power Dynamics", "地位・資源・情報・影響力の差が対人行動に与える関係性。"),
            ("SOCPSY-000108", "authority_relation", "権威関係", "Authority Relation", "権威を持つ人物や制度との関係が判断や行動に影響する状態。"),
            ("SOCPSY-000109", "status_influence", "地位影響", "Status Influence", "社会的地位や序列が発言力・評価・行動に影響する現象。"),
            ("SOCPSY-000110", "followership", "フォロワーシップ", "Followership", "リーダーや集団目標を支え、主体的に貢献する対人行動。")
        ]
    },
    {
        "category": "Social Psychology - Cooperation Competition",
        "name_ja": "社会心理・協力競争",
        "items": [
            ("SOCPSY-000111", "cooperation", "協力", "Cooperation", "複数人が共有目標や相互利益のために行動を調整すること。"),
            ("SOCPSY-000112", "competition", "競争", "Competition", "限られた報酬・地位・成果をめぐって他者と競う状態。"),
            ("SOCPSY-000113", "coordination", "協調調整", "Coordination", "複数人の行動タイミング・役割・情報を合わせる過程。"),
            ("SOCPSY-000114", "shared_goal", "共有目標", "Shared Goal", "集団や関係者が共通して目指す成果や状態。"),
            ("SOCPSY-000115", "collective_action", "集合行動", "Collective Action", "集団が共通目的のためにまとまって行動すること。"),
            ("SOCPSY-000116", "public_goods_dilemma", "公共財ジレンマ", "Public Goods Dilemma", "個人利益と集団利益が衝突する協力問題。"),
            ("SOCPSY-000117", "free_riding", "フリーライド", "Free Riding", "集団の利益を受けながら自分の貢献を少なくする行動。"),
            ("SOCPSY-000118", "trust_game_behavior", "信頼ゲーム行動", "Trust Game Behavior", "相手を信頼して資源や意思決定を委ねる対人選択行動。"),
            ("SOCPSY-000119", "reciprocal_cooperation", "互恵的協力", "Reciprocal Cooperation", "相手の協力に応じて自分も協力する関係的行動。"),
            ("SOCPSY-000120", "competitive_arousal", "競争覚醒", "Competitive Arousal", "競争場面で覚醒や興奮が高まり、判断や行動が変化する状態。")
        ]
    },
    {
        "category": "Social Psychology - Moral Social Judgment",
        "name_ja": "社会心理・道徳社会判断",
        "items": [
            ("SOCPSY-000121", "moral_judgment_social", "道徳判断", "Moral Judgment", "善悪・公正・責任・危害などに基づいて行動や人物を評価する判断。"),
            ("SOCPSY-000122", "fairness_judgment", "公平性判断", "Fairness Judgment", "分配・手続き・扱いが公平かどうかを判断する過程。"),
            ("SOCPSY-000123", "justice_sensitivity", "公正感受性", "Justice Sensitivity", "不公平や不正に気づきやすく反応しやすい傾向。"),
            ("SOCPSY-000124", "responsibility_attribution", "責任帰属", "Responsibility Attribution", "出来事や結果について誰にどの程度責任があるか判断する過程。"),
            ("SOCPSY-000125", "blame_judgment", "非難判断", "Blame Judgment", "相手の行動に対して非難や責任をどの程度向けるかの判断。"),
            ("SOCPSY-000126", "forgiveness", "許し", "Forgiveness", "被害や不満の後に相手への否定的感情を弱める過程。"),
            ("SOCPSY-000127", "moral_outrage", "道徳的憤り", "Moral Outrage", "不正や規範違反に対して強い怒りや非難を感じる状態。"),
            ("SOCPSY-000128", "norm_violation_detection", "規範違反検出", "Norm Violation Detection", "社会的ルールや期待から外れた行動に気づく過程。"),
            ("SOCPSY-000129", "punishment_preference", "罰選好", "Punishment Preference", "規範違反者に罰や制裁を与えることを支持する傾向。"),
            ("SOCPSY-000130", "restorative_orientation", "修復志向", "Restorative Orientation", "罰よりも関係修復・再発防止・対話を重視する傾向。")
        ]
    },
    {
        "category": "Social Psychology - Social Emotion",
        "name_ja": "社会心理・社会的感情",
        "items": [
            ("SOCPSY-000131", "shame", "恥", "Shame", "自分全体が否定的に見られていると感じる社会的感情。"),
            ("SOCPSY-000132", "guilt", "罪悪感", "Guilt", "自分の行動が他者や規範に悪影響を与えたと感じる感情。"),
            ("SOCPSY-000133", "embarrassment", "気まずさ", "Embarrassment", "社会的場面で失敗や逸脱が見られたと感じる一時的な感情。"),
            ("SOCPSY-000134", "pride", "誇り", "Pride", "自分や所属集団の達成・価値に対して肯定的に感じる感情。"),
            ("SOCPSY-000135", "envy", "羨望", "Envy", "他者が持つ望ましいものや地位を自分も欲しいと感じる感情。"),
            ("SOCPSY-000136", "jealousy", "嫉妬", "Jealousy", "大切な関係や地位を他者に奪われる可能性に対する感情。"),
            ("SOCPSY-000137", "gratitude", "感謝", "Gratitude", "他者から受けた恩恵や支援に対してありがたさを感じる感情。"),
            ("SOCPSY-000138", "admiration", "賞賛", "Admiration", "他者の能力・行動・人格に対して尊敬や好意を感じる感情。"),
            ("SOCPSY-000139", "social_anxiety", "社会不安", "Social Anxiety", "他者からの評価や対人場面に対する不安や緊張。"),
            ("SOCPSY-000140", "rejection_sensitivity", "拒絶感受性", "Rejection Sensitivity", "拒絶や否定的反応を予期しやすく、それに強く反応する傾向。")
        ]
    },
    {
        "category": "Social Psychology - Collective Culture",
        "name_ja": "社会心理・集合文化",
        "items": [
            ("SOCPSY-000141", "collective_identity", "集合的アイデンティティ", "Collective Identity", "特定の集団や共同体の一員として自己を認識すること。"),
            ("SOCPSY-000142", "cultural_frame_switching", "文化フレーム切替", "Cultural Frame Switching", "文脈に応じて異なる文化的価値観や行動様式を切り替える現象。"),
            ("SOCPSY-000143", "acculturation", "文化適応", "Acculturation", "異なる文化環境に接触し、価値観や行動様式が変化する過程。"),
            ("SOCPSY-000144", "bicultural_identity", "二文化アイデンティティ", "Bicultural Identity", "二つ以上の文化的背景を自己の一部として統合する状態。"),
            ("SOCPSY-000145", "collective_memory", "集合記憶", "Collective Memory", "集団や社会で共有される過去の出来事に関する記憶や物語。"),
            ("SOCPSY-000146", "social_ritual", "社会的儀礼", "Social Ritual", "集団の規範・結束・意味づけを支える反復的な社会行動。"),
            ("SOCPSY-000147", "cultural_script", "文化的スクリプト", "Cultural Script", "特定文化で期待される典型的な行動順序や表現様式。"),
            ("SOCPSY-000148", "norm_internalization", "規範内在化", "Norm Internalization", "社会的規範が自分の価値観や判断基準として取り込まれる過程。"),
            ("SOCPSY-000149", "social_capital", "社会関係資本", "Social Capital", "信頼・ネットワーク・互酬性など、社会関係から得られる資源。"),
            ("SOCPSY-000150", "collective_resilience", "集合的レジリエンス", "Collective Resilience", "集団やコミュニティが困難後に回復し適応する力。")
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
        "output_dir": "vol9_social_psychology/social_psychology_101_150",
        "index_filename": "social_psychology_101_150_index.yml",
        "index_content": "\n".join(index_lines) + "\n",
        "items": all_items
    }

    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(json.dumps(pack, ensure_ascii=False, indent=2), encoding="utf-8")

    print(f"Created: {OUT}")
    print(f"Items: {len(all_items)}")


if __name__ == "__main__":
    main()