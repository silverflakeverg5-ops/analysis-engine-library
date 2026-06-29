import json
from pathlib import Path

OUT = Path("data/master_packs/vol6_neuroscience_051_100.json")

SECTIONS = [
    {
        "category": "Neuroscience - Attention Control",
        "name_ja": "神経科学・注意制御",
        "items": [
            ("NEURO-000051", "neural_attention_control", "注意制御の神経基盤", "Neural Attention Control", "目的に応じた注意の方向づけや維持に関わる神経メカニズム。"),
            ("NEURO-000052", "top_down_attention", "トップダウン注意", "Top Down Attention", "目標や意図に基づいて注意を制御する神経認知過程。"),
            ("NEURO-000053", "bottom_up_attention", "ボトムアップ注意", "Bottom Up Attention", "目立つ刺激や予期しない刺激によって注意が引き寄せられる過程。"),
            ("NEURO-000054", "attentional_switching_neural_basis", "注意切替の神経基盤", "Neural Basis of Attentional Switching", "注意対象を切り替える際に働く神経ネットワーク。"),
            ("NEURO-000055", "alerting_network", "警戒ネットワーク", "Alerting Network", "覚醒水準を高め、刺激に備える注意ネットワーク。"),
            ("NEURO-000056", "orienting_network", "定位ネットワーク", "Orienting Network", "特定の場所や対象へ注意を向ける注意ネットワーク。"),
            ("NEURO-000057", "executive_attention_network", "実行注意ネットワーク", "Executive Attention Network", "葛藤解決や抑制制御に関わる注意ネットワーク。"),
            ("NEURO-000058", "visual_search_neural_basis", "視覚探索の神経基盤", "Neural Basis of Visual Search", "複数の視覚情報から対象を探す際に働く神経過程。"),
            ("NEURO-000059", "sustained_attention_neural_basis", "持続的注意の神経基盤", "Neural Basis of Sustained Attention", "長時間にわたり注意を保つ神経メカニズム。"),
            ("NEURO-000060", "attention_fatigue", "注意疲労", "Attention Fatigue", "注意制御を続けることで反応性や集中維持が低下する状態。")
        ]
    },
    {
        "category": "Neuroscience - Memory Systems",
        "name_ja": "神経科学・記憶システム",
        "items": [
            ("NEURO-000061", "episodic_memory_network", "エピソード記憶ネットワーク", "Episodic Memory Network", "海馬や内側側頭葉を中心に個人的経験を保持・想起する神経ネットワーク。"),
            ("NEURO-000062", "semantic_memory_network", "意味記憶ネットワーク", "Semantic Memory Network", "概念・事実・言語知識を処理する神経ネットワーク。"),
            ("NEURO-000063", "procedural_memory_system", "手続き記憶システム", "Procedural Memory System", "技能や習慣的操作の学習・保持に関わる神経システム。"),
            ("NEURO-000064", "working_memory_network", "ワーキングメモリネットワーク", "Working Memory Network", "前頭前野と頭頂領域を中心に一時保持と操作を行う神経ネットワーク。"),
            ("NEURO-000065", "memory_encoding_neural_basis", "記憶符号化の神経基盤", "Neural Basis of Memory Encoding", "情報を記憶として保存可能な形に変換する神経過程。"),
            ("NEURO-000066", "memory_retrieval_neural_basis", "記憶想起の神経基盤", "Neural Basis of Memory Retrieval", "保存された記憶を取り出す際に働く神経過程。"),
            ("NEURO-000067", "memory_reconsolidation", "記憶再固定", "Memory Reconsolidation", "想起された記憶が再び不安定化し、更新されて固定される過程。"),
            ("NEURO-000068", "spatial_memory_system", "空間記憶システム", "Spatial Memory System", "位置・経路・環境配置の記憶に関わる神経システム。"),
            ("NEURO-000069", "emotional_memory_system", "情動記憶システム", "Emotional Memory System", "感情を伴う経験の記憶を強める神経システム。"),
            ("NEURO-000070", "forgetting_neural_process", "忘却の神経過程", "Neural Process of Forgetting", "記憶痕跡の弱化・干渉・更新によって想起しにくくなる過程。")
        ]
    },
    {
        "category": "Neuroscience - Executive Control",
        "name_ja": "神経科学・実行制御",
        "items": [
            ("NEURO-000071", "inhibitory_control_neural_basis", "抑制制御の神経基盤", "Neural Basis of Inhibitory Control", "衝動的反応や不要な行動を抑える神経メカニズム。"),
            ("NEURO-000072", "conflict_monitoring", "葛藤モニタリング", "Conflict Monitoring", "複数の反応や目標が競合する状態を検出する神経過程。"),
            ("NEURO-000073", "error_detection_neural_basis", "エラー検出の神経基盤", "Neural Basis of Error Detection", "行動結果や反応の誤りを検出する神経過程。"),
            ("NEURO-000074", "cognitive_control_network", "認知制御ネットワーク", "Cognitive Control Network", "目標に沿って注意・記憶・行動を調整する神経ネットワーク。"),
            ("NEURO-000075", "task_set_maintenance", "課題セット保持", "Task Set Maintenance", "現在のルールや目標状態を維持する神経認知過程。"),
            ("NEURO-000076", "response_inhibition", "反応抑制", "Response Inhibition", "不適切または早すぎる反応を止める神経認知機能。"),
            ("NEURO-000077", "performance_monitoring", "パフォーマンスモニタリング", "Performance Monitoring", "行動の正確性・速度・結果を監視する神経認知過程。"),
            ("NEURO-000078", "cognitive_flexibility_neural_basis", "認知的柔軟性の神経基盤", "Neural Basis of Cognitive Flexibility", "状況変化に応じてルールや方略を切り替える神経メカニズム。"),
            ("NEURO-000079", "decision_threshold_adjustment", "意思決定閾値調整", "Decision Threshold Adjustment", "速さと正確さのバランスに応じて反応基準を変える神経認知過程。"),
            ("NEURO-000080", "executive_resource_depletion", "実行資源消耗", "Executive Resource Depletion", "継続的な制御要求によって認知制御の効率が低下する状態。")
        ]
    },
    {
        "category": "Neuroscience - Social Neuroscience",
        "name_ja": "神経科学・社会神経科学",
        "items": [
            ("NEURO-000081", "mentalizing_network", "メンタライジングネットワーク", "Mentalizing Network", "他者の信念・意図・感情を推測する神経ネットワーク。"),
            ("NEURO-000082", "mirror_neuron_system", "ミラーニューロンシステム", "Mirror Neuron System", "他者の行動観察と自己の行動表象を結びつける神経システム。"),
            ("NEURO-000083", "empathy_neural_basis", "共感の神経基盤", "Neural Basis of Empathy", "他者の感情や痛みへの反応に関わる神経メカニズム。"),
            ("NEURO-000084", "social_reward_processing", "社会的報酬処理", "Social Reward Processing", "承認・称賛・所属感など社会的報酬を処理する神経過程。"),
            ("NEURO-000085", "social_pain_network", "社会的痛みネットワーク", "Social Pain Network", "拒絶・孤立・排除など社会的苦痛に反応する神経ネットワーク。"),
            ("NEURO-000086", "trust_neural_basis", "信頼判断の神経基盤", "Neural Basis of Trust", "他者や情報源への信頼判断に関わる神経メカニズム。"),
            ("NEURO-000087", "fairness_processing", "公平性処理", "Fairness Processing", "分配・交換・協力における公平性を評価する神経過程。"),
            ("NEURO-000088", "reputation_neural_processing", "評判処理の神経基盤", "Neural Processing of Reputation", "他者からの評価や社会的地位を処理する神経過程。"),
            ("NEURO-000089", "attachment_neural_system", "愛着神経システム", "Attachment Neural System", "親密さ・安心感・結びつきに関わる神経システム。"),
            ("NEURO-000090", "social_threat_detection", "社会的脅威検知", "Social Threat Detection", "拒絶・批判・評価低下などの社会的脅威を検出する神経過程。")
        ]
    },
    {
        "category": "Neuroscience - Plasticity Development",
        "name_ja": "神経科学・可塑性発達",
        "items": [
            ("NEURO-000091", "neuroplasticity", "神経可塑性", "Neuroplasticity", "経験や学習によって神経結合や脳機能が変化する性質。"),
            ("NEURO-000092", "synaptic_plasticity", "シナプス可塑性", "Synaptic Plasticity", "神経細胞間の結合強度が経験により変化する性質。"),
            ("NEURO-000093", "long_term_potentiation", "長期増強", "Long Term Potentiation", "反復的な神経活動によりシナプス伝達が長期的に強化される現象。"),
            ("NEURO-000094", "long_term_depression", "長期抑圧", "Long Term Depression", "神経活動パターンによりシナプス伝達が長期的に弱まる現象。"),
            ("NEURO-000095", "critical_period", "臨界期", "Critical Period", "特定の経験が神経発達や学習に大きな影響を持つ時期。"),
            ("NEURO-000096", "sensitive_period", "敏感期", "Sensitive Period", "特定の経験に対して学習や発達が起こりやすい時期。"),
            ("NEURO-000097", "experience_dependent_plasticity", "経験依存的可塑性", "Experience Dependent Plasticity", "個別の経験に応じて神経回路が変化する性質。"),
            ("NEURO-000098", "experience_expectant_plasticity", "経験期待的可塑性", "Experience Expectant Plasticity", "一般的に期待される環境入力によって発達する神経可塑性。"),
            ("NEURO-000099", "learning_induced_plasticity", "学習誘導性可塑性", "Learning Induced Plasticity", "学習によって神経活動や結合が変化する過程。"),
            ("NEURO-000100", "recovery_plasticity", "回復可塑性", "Recovery Plasticity", "損傷・負荷・失敗後に機能を補償・再構成する神経可塑性。")
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
        "output_dir": "vol6_neuroscience/neuroscience_051_100",
        "index_filename": "neuroscience_051_100_index.yml",
        "index_content": "\n".join(index_lines) + "\n",
        "items": all_items
    }

    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(json.dumps(pack, ensure_ascii=False, indent=2), encoding="utf-8")

    print(f"Created: {OUT}")
    print(f"Items: {len(all_items)}")


if __name__ == "__main__":
    main()