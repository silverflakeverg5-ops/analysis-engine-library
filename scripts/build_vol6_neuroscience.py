import json
from pathlib import Path

OUT = Path("data/master_packs/vol6_neuroscience_151_200.json")

SECTIONS = [
    {
        "category": "Neuroscience - Consciousness",
        "name_ja": "神経科学・意識",
        "items": [
            ("NEURO-000151", "conscious_awareness", "意識的気づき", "Conscious Awareness", "自分の知覚・思考・感情・行動に気づいている状態。"),
            ("NEURO-000152", "global_workspace", "グローバルワークスペース", "Global Workspace", "複数の認知処理へ情報を広く共有する意識処理の理論的枠組み。"),
            ("NEURO-000153", "attention_and_consciousness", "注意と意識", "Attention and Consciousness", "注意の向け方と意識的経験の関係に関わる神経認知過程。"),
            ("NEURO-000154", "self_awareness", "自己意識", "Self Awareness", "自分自身の状態・行動・存在を対象化して認識する能力。"),
            ("NEURO-000155", "agency", "主体感", "Agency", "自分が行動を起こしていると感じる意識経験。"),
            ("NEURO-000156", "sense_of_ownership", "所有感", "Sense of Ownership", "身体や行動結果が自分に属していると感じる意識経験。"),
            ("NEURO-000157", "mental_simulation", "心的シミュレーション", "Mental Simulation", "現実には起きていない状況や行動を頭の中で想像・予測する過程。"),
            ("NEURO-000158", "internal_speech", "内言", "Internal Speech", "声に出さずに頭の中で言語的に考える認知過程。"),
            ("NEURO-000159", "mind_wandering", "マインドワンダリング", "Mind Wandering", "現在の課題から注意が離れ、内的な思考へ移る状態。"),
            ("NEURO-000160", "meta_awareness", "メタ的気づき", "Meta Awareness", "自分が何を考え、どの状態にあるかに気づく高次の意識過程。")
        ]
    },
    {
        "category": "Neuroscience - Predictive Brain",
        "name_ja": "神経科学・予測脳",
        "items": [
            ("NEURO-000161", "predictive_coding", "予測符号化", "Predictive Coding", "脳が予測と入力の差を使って知覚や行動を更新する考え方。"),
            ("NEURO-000162", "prediction_error", "予測誤差", "Prediction Error", "予測された入力や結果と実際の入力や結果との差。"),
            ("NEURO-000163", "bayesian_brain", "ベイズ脳", "Bayesian Brain", "脳が事前知識と新しい情報を統合して推定するという理論的枠組み。"),
            ("NEURO-000164", "active_inference", "能動的推論", "Active Inference", "予測誤差を減らすために知覚や行動を調整する神経認知過程。"),
            ("NEURO-000165", "sensory_prediction", "感覚予測", "Sensory Prediction", "自分の行動や環境変化によって生じる感覚入力を予測する過程。"),
            ("NEURO-000166", "motor_prediction", "運動予測", "Motor Prediction", "自分の運動がもたらす結果や感覚変化を予測する過程。"),
            ("NEURO-000167", "surprise_processing", "驚き処理", "Surprise Processing", "予測と異なる出来事に対して注意や学習を更新する処理。"),
            ("NEURO-000168", "expectation_updating", "期待更新", "Expectation Updating", "経験や結果に基づいて将来予測や期待値を修正する過程。"),
            ("NEURO-000169", "environmental_modeling", "環境モデル化", "Environmental Modeling", "周囲の規則性や構造を内部モデルとして形成する過程。"),
            ("NEURO-000170", "adaptive_prediction", "適応的予測", "Adaptive Prediction", "状況変化に合わせて予測モデルを柔軟に更新する過程。")
        ]
    },
    {
        "category": "Neuroscience - Learning Signals",
        "name_ja": "神経科学・学習信号",
        "items": [
            ("NEURO-000171", "dopamine_learning_signal", "ドーパミン学習信号", "Dopamine Learning Signal", "報酬予測誤差や動機づけの更新に関わるドーパミン系信号。"),
            ("NEURO-000172", "error_driven_learning", "誤差駆動学習", "Error Driven Learning", "予測や行動結果の誤差を使って学習を進める過程。"),
            ("NEURO-000173", "hebbian_learning", "ヘッブ学習", "Hebbian Learning", "同時に活動する神経細胞間の結合が強まる学習原理。"),
            ("NEURO-000174", "reinforcement_plasticity", "強化可塑性", "Reinforcement Plasticity", "報酬や罰の経験によって神経結合や行動選択が変化する性質。"),
            ("NEURO-000175", "reward_expectation", "報酬期待", "Reward Expectation", "将来得られる報酬の大きさや可能性を予測する神経過程。"),
            ("NEURO-000176", "punishment_learning", "罰学習", "Punishment Learning", "不快な結果や損失を避けるために行動を調整する学習過程。"),
            ("NEURO-000177", "novelty_detection", "新奇性検出", "Novelty Detection", "新しい刺激や予期しない情報を検出し注意や学習を促す過程。"),
            ("NEURO-000178", "salience_coding", "顕著性符号化", "Salience Coding", "重要性や目立ちやすさを神経信号として表現する過程。"),
            ("NEURO-000179", "confidence_signal", "確信度信号", "Confidence Signal", "判断や選択の確かさを表す神経認知的信号。"),
            ("NEURO-000180", "uncertainty_signal", "不確実性信号", "Uncertainty Signal", "結果や環境の不確実性を表す神経認知的信号。")
        ]
    },
    {
        "category": "Neuroscience - Brain Health",
        "name_ja": "神経科学・脳健康",
        "items": [
            ("NEURO-000181", "brain_aging", "脳の加齢", "Brain Aging", "加齢に伴う脳構造・神経機能・認知機能の変化。"),
            ("NEURO-000182", "cognitive_reserve", "認知予備能", "Cognitive Reserve", "脳の変化や負荷に対して認知機能を維持する余力。"),
            ("NEURO-000183", "neurogenesis", "神経新生", "Neurogenesis", "新しい神経細胞が生み出される生物学的過程。"),
            ("NEURO-000184", "synaptic_health", "シナプス健康", "Synaptic Health", "神経細胞間の接続や伝達効率が良好に保たれている状態。"),
            ("NEURO-000185", "white_matter_integrity", "白質健全性", "White Matter Integrity", "脳領域間の情報伝達を支える白質構造の健全性。"),
            ("NEURO-000186", "gray_matter_density", "灰白質密度", "Gray Matter Density", "神経細胞体が多く含まれる灰白質領域の構造的特徴。"),
            ("NEURO-000187", "neuroinflammation", "神経炎症", "Neuroinflammation", "脳や神経系における炎症反応で、認知や気分に影響し得る状態。"),
            ("NEURO-000188", "oxidative_stress", "酸化ストレス", "Oxidative Stress", "活性酸素などによる細胞への負荷が神経機能に影響する状態。"),
            ("NEURO-000189", "brain_energy_metabolism", "脳エネルギー代謝", "Brain Energy Metabolism", "脳活動を支える糖代謝・酸素利用・エネルギー供給の仕組み。"),
            ("NEURO-000190", "recovery_processes", "回復過程", "Recovery Processes", "睡眠・休息・可塑性などを通じて脳機能が回復する過程。")
        ]
    },
    {
        "category": "Neuroscience - Integration",
        "name_ja": "神経科学・統合",
        "items": [
            ("NEURO-000191", "brain_body_interaction", "脳身体相互作用", "Brain Body Interaction", "脳と身体状態が相互に影響し合い認知・感情・行動を形作る仕組み。"),
            ("NEURO-000192", "emotion_cognition_integration", "感情認知統合", "Emotion Cognition Integration", "感情処理と認知処理が統合され判断や行動に影響する過程。"),
            ("NEURO-000193", "memory_emotion_integration", "記憶感情統合", "Memory Emotion Integration", "記憶と感情が相互作用し、想起や評価を変化させる過程。"),
            ("NEURO-000194", "social_brain_integration", "社会脳統合", "Social Brain Integration", "他者理解・感情・報酬・規範処理が統合される神経認知過程。"),
            ("NEURO-000195", "decision_integration", "意思決定統合", "Decision Integration", "価値・感情・記憶・リスクを統合して選択を形成する過程。"),
            ("NEURO-000196", "executive_integration", "実行制御統合", "Executive Integration", "注意・抑制・記憶・目標保持を統合して行動を制御する過程。"),
            ("NEURO-000197", "attention_integration", "注意統合", "Attention Integration", "感覚入力・目標・顕著性を統合して注意を配分する過程。"),
            ("NEURO-000198", "learning_integration", "学習統合", "Learning Integration", "報酬・誤差・記憶・行動結果を統合して学習を更新する過程。"),
            ("NEURO-000199", "adaptive_integration", "適応統合", "Adaptive Integration", "環境変化に対して認知・感情・行動を統合的に調整する過程。"),
            ("NEURO-000200", "human_behavior_integration", "人間行動統合", "Human Behavior Integration", "神経・認知・感情・環境要因を統合して人間行動を理解する枠組み。")
        ]
    }
]


def make_item(item_id, slug, name_ja, name_en, definition_ja, category, parent_ja):
    return {
        "filename": f"{item_id}_{slug}.yml",
        "id": item_id,
        "knowledge_type": "neuroscience",
        "name_ja": name_ja,
        "name_en": name_en,
        "category": "Neuroscience",
        "attribute": category.replace("Neuroscience - ", ""),
        "definition_ja": definition_ja,
        "tags": ["CAT:神経科学", f"CAT:{parent_ja}", "ATTR:神経基盤"],
        "parent": [parent_ja],
        "related": ["認知科学", "行動観測", "生理"],
        "observable_data": [
            f"{name_ja}関連反応時間",
            f"{name_ja}関連行動変化",
            f"{name_ja}関連注意変化",
            f"{name_ja}関連ストレス反応"
        ],
        "signal_candidates": [
            f"{name_ja}に関連する行動・反応パターンが観測される",
            "負荷や報酬条件の変化に応じて反応が変化する"
        ],
        "device_level": "スマホ・PCのみ推定可能",
        "modifiers": ["睡眠", "疲労", "ストレス", "覚醒水準"],
        "evidence": "神経科学・認知神経科学・生理心理学で使用",
        "status": "active"
    }


def main():
    all_items = []
    index_lines = ["category: Neuroscience", "name_ja: 神経科学", "items:"]

    for section in SECTIONS:
        parent_ja = section["name_ja"].replace("神経科学・", "")
        for raw in section["items"]:
            item = make_item(*raw, category=section["category"], parent_ja=parent_ja)
            all_items.append(item)
            index_lines.append(f"  - {item['filename']}")

    index_lines.extend([
        "notes:",
        "  - 神経科学は医療診断ではなく推論材料として扱う",
        "  - 観測可能データとSignal候補を中心に管理する",
        "  - アプリ側でスコアリング・推論・表示を行う"
    ])

    pack = {
        "output_dir": "vol6_neuroscience/neuroscience_151_200",
        "index_filename": "neuroscience_151_200_index.yml",
        "index_content": "\n".join(index_lines) + "\n",
        "items": all_items
    }

    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(json.dumps(pack, ensure_ascii=False, indent=2), encoding="utf-8")

    print(f"Created: {OUT}")
    print(f"Items: {len(all_items)}")


if __name__ == "__main__":
    main()