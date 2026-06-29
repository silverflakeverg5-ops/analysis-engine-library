import json
from pathlib import Path

OUT = Path("data/master_packs/vol5_cognitive_science_151_200.json")

SECTIONS = [
    {
        "category": "Cognitive Science - Motivation Cognition",
        "name_ja": "認知科学・動機づけ認知",
        "items": [
            ("COGSCI-000151", "intrinsic_motivation", "内発的動機づけ", "Intrinsic Motivation", "活動そのものへの興味や楽しさによって行動が生じる動機づけ。"),
            ("COGSCI-000152", "extrinsic_motivation", "外発的動機づけ", "Extrinsic Motivation", "報酬・評価・罰回避など外部要因によって行動が生じる動機づけ。"),
            ("COGSCI-000153", "self_determination", "自己決定", "Self Determination", "自分で選んで行動している感覚に関わる動機づけ概念。"),
            ("COGSCI-000154", "competence_need", "有能感欲求", "Competence Need", "自分がうまくできている、成長していると感じたい欲求。"),
            ("COGSCI-000155", "autonomy_need", "自律性欲求", "Autonomy Need", "自分の意思で選択・行動したいという欲求。"),
            ("COGSCI-000156", "relatedness_need", "関係性欲求", "Relatedness Need", "他者とつながり、受け入れられていると感じたい欲求。"),
            ("COGSCI-000157", "achievement_motivation", "達成動機", "Achievement Motivation", "目標達成や能力発揮に向かって努力する動機づけ。"),
            ("COGSCI-000158", "avoidance_motivation", "回避動機", "Avoidance Motivation", "失敗・損失・不快を避けるために行動する動機づけ。"),
            ("COGSCI-000159", "approach_motivation", "接近動機", "Approach Motivation", "報酬・成功・好ましい対象へ近づこうとする動機づけ。"),
            ("COGSCI-000160", "goal_orientation", "目標志向性", "Goal Orientation", "学習・達成・評価など、どのような目標基準で行動するかの傾向。")
        ]
    },
    {
        "category": "Cognitive Science - Creativity",
        "name_ja": "認知科学・創造性",
        "items": [
            ("COGSCI-000161", "creativity", "創造性", "Creativity", "新規性と有用性を持つアイデアや解決策を生み出す認知的能力。"),
            ("COGSCI-000162", "divergent_thinking", "拡散的思考", "Divergent Thinking", "一つの問題に対して多様な可能性や発想を広げる思考過程。"),
            ("COGSCI-000163", "convergent_thinking", "収束的思考", "Convergent Thinking", "複数の情報や案から最も適切な解を絞り込む思考過程。"),
            ("COGSCI-000164", "idea_generation", "アイデア生成", "Idea Generation", "新しい選択肢・解決策・表現を生み出す認知過程。"),
            ("COGSCI-000165", "remote_association", "遠隔連想", "Remote Association", "一見離れた概念同士を結びつけて新しい意味や解を作る認知過程。"),
            ("COGSCI-000166", "conceptual_combination", "概念結合", "Conceptual Combination", "複数の概念を組み合わせて新しい概念やアイデアを作る過程。"),
            ("COGSCI-000167", "creative_flexibility", "創造的柔軟性", "Creative Flexibility", "異なる視点や発想カテゴリへ切り替えながら考える性質。"),
            ("COGSCI-000168", "creative_persistence", "創造的粘り強さ", "Creative Persistence", "アイデア探索を続け、改善や再構成を重ねる性質。"),
            ("COGSCI-000169", "incubation_effect", "孵化効果", "Incubation Effect", "一度問題から離れた後に解決や発想が促進される現象。"),
            ("COGSCI-000170", "insight", "洞察", "Insight", "問題構造の再理解により、突然解決や気づきが生じる認知現象。")
        ]
    },
    {
        "category": "Cognitive Science - Decision Architecture",
        "name_ja": "認知科学・選択設計",
        "items": [
            ("COGSCI-000171", "choice_architecture", "選択設計", "Choice Architecture", "選択肢の提示方法や環境設計が意思決定に影響する仕組み。"),
            ("COGSCI-000172", "nudge", "ナッジ", "Nudge", "選択の自由を残しつつ、望ましい行動を取りやすくする設計。"),
            ("COGSCI-000173", "default_option", "デフォルト選択肢", "Default Option", "何もしない場合に選ばれる既定の選択肢。"),
            ("COGSCI-000174", "choice_set", "選択肢集合", "Choice Set", "意思決定場面で提示される選択肢全体。"),
            ("COGSCI-000175", "option_framing", "選択肢フレーミング", "Option Framing", "選択肢の表現や文脈によって評価が変わる提示設計。"),
            ("COGSCI-000176", "commitment_device", "コミットメント装置", "Commitment Device", "将来の行動を維持しやすくするための事前制約や約束の仕組み。"),
            ("COGSCI-000177", "feedback_design", "フィードバック設計", "Feedback Design", "行動結果や進捗を分かりやすく返すことで学習や改善を促す設計。"),
            ("COGSCI-000178", "progress_visualization", "進捗可視化", "Progress Visualization", "目標までの距離や達成状況を視覚的に示す設計。"),
            ("COGSCI-000179", "social_proof_design", "社会的証明設計", "Social Proof Design", "他者の選択や評価を提示して判断に影響を与える設計。"),
            ("COGSCI-000180", "friction_design", "摩擦設計", "Friction Design", "望ましくない行動を抑えるために意図的な手間や確認を加える設計。")
        ]
    },
    {
        "category": "Cognitive Science - Human Computer Interaction",
        "name_ja": "認知科学・HCI",
        "items": [
            ("COGSCI-000181", "usability", "ユーザビリティ", "Usability", "利用者が目的を効果的・効率的・満足に達成できる度合い。"),
            ("COGSCI-000182", "learnability", "学習容易性", "Learnability", "初めて利用する人が操作や仕組みをどれだけ早く理解できるかの性質。"),
            ("COGSCI-000183", "discoverability", "発見可能性", "Discoverability", "機能や操作方法をユーザーが見つけやすい性質。"),
            ("COGSCI-000184", "affordance", "アフォーダンス", "Affordance", "対象がどのように使えるかを知覚させる手がかり。"),
            ("COGSCI-000185", "signifier", "シグニファイア", "Signifier", "ユーザーに操作可能性や意味を示す表示上の手がかり。"),
            ("COGSCI-000186", "cognitive_walkthrough", "認知的ウォークスルー", "Cognitive Walkthrough", "ユーザーが操作手順を理解できるかを検討する評価手法。"),
            ("COGSCI-000187", "error_prevention", "エラー防止", "Error Prevention", "誤操作や判断ミスを起こしにくくする設計。"),
            ("COGSCI-000188", "error_recovery", "エラー回復", "Error Recovery", "誤操作や失敗後に元の状態へ戻れるようにする設計。"),
            ("COGSCI-000189", "interaction_cost", "インタラクションコスト", "Interaction Cost", "目的達成までに必要な操作・注意・判断の負担。"),
            ("COGSCI-000190", "user_flow", "ユーザーフロー", "User Flow", "ユーザーが目的達成までにたどる画面・操作・判断の流れ。")
        ]
    },
    {
        "category": "Cognitive Science - Adaptive Behavior",
        "name_ja": "認知科学・適応行動",
        "items": [
            ("COGSCI-000191", "adaptation", "適応", "Adaptation", "環境や課題の変化に合わせて行動や方略を調整する過程。"),
            ("COGSCI-000192", "behavioral_adaptation", "行動適応", "Behavioral Adaptation", "結果や状況変化に応じて具体的な行動を変える過程。"),
            ("COGSCI-000193", "cognitive_adaptation", "認知的適応", "Cognitive Adaptation", "考え方・判断基準・注意配分を環境に合わせて変える過程。"),
            ("COGSCI-000194", "strategy_shift", "方略転換", "Strategy Shift", "既存の方法が有効でない時に別の方略へ切り替える過程。"),
            ("COGSCI-000195", "resilience_process", "レジリエンス過程", "Resilience Process", "失敗や負荷の後に機能や行動を回復・再構成する過程。"),
            ("COGSCI-000196", "behavioral_plasticity", "行動可塑性", "Behavioral Plasticity", "経験や環境によって行動パターンが変化し得る性質。"),
            ("COGSCI-000197", "context_sensitivity", "文脈感受性", "Context Sensitivity", "状況や環境の違いに応じて判断や行動が変わる性質。"),
            ("COGSCI-000198", "transfer_adaptation", "転移適応", "Transfer Adaptation", "別場面で得た学習を新しい環境に合わせて応用する過程。"),
            ("COGSCI-000199", "novelty_adaptation", "新奇性適応", "Novelty Adaptation", "新しい刺激や環境に慣れ、適切に反応できるようになる過程。"),
            ("COGSCI-000200", "uncertainty_adaptation", "不確実性適応", "Uncertainty Adaptation", "不確実な状況で情報収集や試行錯誤を通じて行動を調整する過程。")
        ]
    }
]


def make_item(item_id, slug, name_ja, name_en, definition_ja, category, parent_ja):
    return {
        "filename": f"{item_id}_{slug}.yml",
        "id": item_id,
        "knowledge_type": "cognitive_science",
        "name_ja": name_ja,
        "name_en": name_en,
        "category": "Cognitive Science",
        "attribute": category.replace("Cognitive Science - ", ""),
        "definition_ja": definition_ja,
        "tags": ["CAT:認知科学", f"CAT:{parent_ja}", "ATTR:認知機能"],
        "parent": [parent_ja],
        "related": ["認知能力", "行動観測", "認知バイアス"],
        "observable_data": [
            f"{name_ja}関連反応時間",
            f"{name_ja}関連正答率",
            f"{name_ja}関連エラー率",
            f"{name_ja}関連行動変化"
        ],
        "signal_candidates": [
            f"{name_ja}に関連する行動パターンが観測される",
            "課題条件の変化に応じて反応や成績が変化する"
        ],
        "device_level": "スマホ・PCのみ推定可能",
        "modifiers": ["疲労", "注意", "ストレス", "課題難易度"],
        "evidence": "認知科学・認知心理学・HCI研究で使用",
        "status": "active"
    }


def main():
    all_items = []
    index_lines = ["category: Cognitive Science", "name_ja: 認知科学", "items:"]

    for section in SECTIONS:
        parent_ja = section["name_ja"].replace("認知科学・", "")
        for raw in section["items"]:
            item = make_item(*raw, category=section["category"], parent_ja=parent_ja)
            all_items.append(item)
            index_lines.append(f"  - {item['filename']}")

    index_lines.extend([
        "notes:",
        "  - 認知科学は能力評価そのものではなく推論材料として扱う",
        "  - 観測可能データとSignal候補を中心に管理する",
        "  - アプリ側でスコアリング・推論・表示を行う"
    ])

    pack = {
        "output_dir": "vol5_cognitive_science/cognitive_science_151_200",
        "index_filename": "cognitive_science_151_200_index.yml",
        "index_content": "\n".join(index_lines) + "\n",
        "items": all_items
    }

    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(json.dumps(pack, ensure_ascii=False, indent=2), encoding="utf-8")

    print(f"Created: {OUT}")
    print(f"Items: {len(all_items)}")


if __name__ == "__main__":
    main()