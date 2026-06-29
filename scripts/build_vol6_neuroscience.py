import json
from pathlib import Path

OUT = Path("data/master_packs/vol6_neuroscience_101_150.json")

SECTIONS = [
    {
        "category": "Neuroscience - Sleep Circadian",
        "name_ja": "神経科学・睡眠概日",
        "items": [
            ("NEURO-000101", "sleep_architecture", "睡眠構造", "Sleep Architecture", "ノンレム睡眠・レム睡眠などから成る睡眠段階の構成。"),
            ("NEURO-000102", "rem_sleep", "レム睡眠", "REM Sleep", "夢見・情動記憶・記憶統合に関わる睡眠段階。"),
            ("NEURO-000103", "non_rem_sleep", "ノンレム睡眠", "Non REM Sleep", "身体回復・記憶固定・脳の休息に関わる睡眠段階。"),
            ("NEURO-000104", "slow_wave_sleep", "徐波睡眠", "Slow Wave Sleep", "深いノンレム睡眠で、記憶固定や回復に関わる睡眠状態。"),
            ("NEURO-000105", "circadian_rhythm", "概日リズム", "Circadian Rhythm", "約24時間周期で睡眠・覚醒・体温・ホルモン分泌などを調整する生体リズム。"),
            ("NEURO-000106", "sleep_pressure", "睡眠圧", "Sleep Pressure", "覚醒時間の長さに応じて高まる眠気や睡眠欲求。"),
            ("NEURO-000107", "chronotype", "クロノタイプ", "Chronotype", "朝型・夜型など、活動しやすい時間帯に関する個人差。"),
            ("NEURO-000108", "sleep_deprivation_effect", "睡眠不足影響", "Sleep Deprivation Effect", "睡眠不足により注意・記憶・感情制御・判断が低下する影響。"),
            ("NEURO-000109", "sleep_memory_consolidation", "睡眠中記憶固定", "Sleep Memory Consolidation", "睡眠中に学習内容や経験記憶が安定化・再編成される過程。"),
            ("NEURO-000110", "circadian_misalignment", "概日リズム不一致", "Circadian Misalignment", "生活時間と体内リズムのずれによって覚醒や認知機能が低下する状態。")
        ]
    },
    {
        "category": "Neuroscience - Interoception Body Signals",
        "name_ja": "神経科学・内受容身体信号",
        "items": [
            ("NEURO-000111", "interoception", "内受容感覚", "Interoception", "心拍・呼吸・空腹・緊張など身体内部状態を感じ取る感覚。"),
            ("NEURO-000112", "heartbeat_perception", "心拍知覚", "Heartbeat Perception", "心拍の変化や身体的覚醒を感知する内受容過程。"),
            ("NEURO-000113", "breathing_regulation", "呼吸調整", "Breathing Regulation", "呼吸の深さや速さを通じて覚醒や情動状態を調整する過程。"),
            ("NEURO-000114", "body_awareness", "身体意識", "Body Awareness", "身体姿勢・緊張・疲労・感覚状態に気づく認知身体過程。"),
            ("NEURO-000115", "somatic_marker", "ソマティックマーカー", "Somatic Marker", "身体反応が意思決定や価値判断の手がかりになる仕組み。"),
            ("NEURO-000116", "autonomic_arousal", "自律神経覚醒", "Autonomic Arousal", "交感神経・副交感神経の活動変化による身体的覚醒状態。"),
            ("NEURO-000117", "heart_rate_variability", "心拍変動", "Heart Rate Variability", "心拍間隔の変動で、ストレス回復や自律神経調整の指標として扱われる。"),
            ("NEURO-000118", "physiological_stress_signal", "生理的ストレス信号", "Physiological Stress Signal", "心拍・呼吸・皮膚反応などに現れるストレス関連の身体信号。"),
            ("NEURO-000119", "fatigue_signal", "疲労信号", "Fatigue Signal", "眠気・反応遅延・筋緊張低下などに現れる疲労関連の身体信号。"),
            ("NEURO-000120", "embodied_cognition", "身体化認知", "Embodied Cognition", "身体状態や身体運動が認知・感情・判断に影響するという考え方。")
        ]
    },
    {
        "category": "Neuroscience - Decision Valuation",
        "name_ja": "神経科学・意思決定価値評価",
        "items": [
            ("NEURO-000121", "valuation_system", "価値評価システム", "Valuation System", "選択肢の価値・報酬・コストを評価する神経システム。"),
            ("NEURO-000122", "subjective_value", "主観的価値", "Subjective Value", "個人が選択肢に対して感じる価値や魅力度。"),
            ("NEURO-000123", "expected_value_computation", "期待価値計算", "Expected Value Computation", "報酬量と確率を統合して選択肢の期待価値を推定する過程。"),
            ("NEURO-000124", "effort_cost_computation", "努力コスト計算", "Effort Cost Computation", "行動に必要な労力や負荷を価値判断に反映する過程。"),
            ("NEURO-000125", "social_value_computation", "社会的価値計算", "Social Value Computation", "承認・信頼・所属・評判など社会的要素を価値判断に反映する過程。"),
            ("NEURO-000126", "uncertainty_processing_neural", "不確実性処理の神経基盤", "Neural Uncertainty Processing", "結果や確率が不明確な状況で選択を調整する神経過程。"),
            ("NEURO-000127", "exploration_exploitation_balance", "探索活用バランス", "Exploration Exploitation Balance", "新しい選択肢を試すか既知の良い選択肢を使うかを調整する過程。"),
            ("NEURO-000128", "action_selection_neural", "行動選択の神経基盤", "Neural Action Selection", "複数の可能な行動から一つを選ぶ神経認知過程。"),
            ("NEURO-000129", "choice_conflict_neural", "選択葛藤の神経基盤", "Neural Choice Conflict", "複数の選択肢が競合する際に生じる神経認知的葛藤。"),
            ("NEURO-000130", "value_updating", "価値更新", "Value Updating", "経験やフィードバックにより選択肢の価値評価を更新する過程。")
        ]
    },
    {
        "category": "Neuroscience - Motor Action",
        "name_ja": "神経科学・運動行動",
        "items": [
            ("NEURO-000131", "motor_cortex", "運動皮質", "Motor Cortex", "随意運動の計画と実行に関わる大脳皮質領域。"),
            ("NEURO-000132", "premotor_cortex", "運動前野", "Premotor Cortex", "運動準備・行動選択・視覚情報に基づく運動制御に関わる領域。"),
            ("NEURO-000133", "supplementary_motor_area", "補足運動野", "Supplementary Motor Area", "系列運動・自発的行動開始・運動計画に関わる領域。"),
            ("NEURO-000134", "cerebellum", "小脳", "Cerebellum", "運動調整・タイミング・誤差学習・予測制御に関わる脳領域。"),
            ("NEURO-000135", "basal_ganglia", "大脳基底核", "Basal Ganglia", "行動選択・習慣・報酬学習・運動開始に関わる神経回路。"),
            ("NEURO-000136", "motor_learning", "運動学習", "Motor Learning", "練習やフィードバックにより運動技能が改善する学習過程。"),
            ("NEURO-000137", "procedural_learning_neural", "手続き学習の神経基盤", "Neural Procedural Learning", "技能や操作手順を習得する神経学習過程。"),
            ("NEURO-000138", "action_planning", "行動計画", "Action Planning", "目標達成のために身体動作や操作手順を準備する神経認知過程。"),
            ("NEURO-000139", "sensorimotor_prediction", "感覚運動予測", "Sensorimotor Prediction", "自分の行動が生む感覚結果を予測する神経過程。"),
            ("NEURO-000140", "motor_inhibition", "運動抑制", "Motor Inhibition", "開始された、または準備された運動反応を停止・抑制する神経機能。")
        ]
    },
    {
        "category": "Neuroscience - Individual Differences",
        "name_ja": "神経科学・個人差",
        "items": [
            ("NEURO-000141", "neural_efficiency", "神経効率性", "Neural Efficiency", "課題遂行に必要な神経資源を効率的に使う性質。"),
            ("NEURO-000142", "trait_anxiety_neural_basis", "特性不安の神経基盤", "Neural Basis of Trait Anxiety", "不安傾向と脅威処理・情動調整に関わる神経基盤。"),
            ("NEURO-000143", "impulsivity_neural_basis", "衝動性の神経基盤", "Neural Basis of Impulsivity", "即時反応・抑制困難・報酬接近に関わる神経基盤。"),
            ("NEURO-000144", "sensation_seeking_neural_basis", "刺激希求の神経基盤", "Neural Basis of Sensation Seeking", "新奇性や強い刺激を求める傾向に関わる神経基盤。"),
            ("NEURO-000145", "resilience_neural_basis", "レジリエンスの神経基盤", "Neural Basis of Resilience", "ストレスや失敗後の回復に関わる神経基盤。"),
            ("NEURO-000146", "empathy_individual_difference", "共感の個人差", "Individual Differences in Empathy", "他者感情への反応や理解の強さに関する神経認知的個人差。"),
            ("NEURO-000147", "reward_sensitivity_difference", "報酬感受性の個人差", "Individual Differences in Reward Sensitivity", "報酬刺激への反応しやすさや接近行動の個人差。"),
            ("NEURO-000148", "stress_reactivity_difference", "ストレス反応性の個人差", "Individual Differences in Stress Reactivity", "負荷や脅威に対する身体・神経反応の個人差。"),
            ("NEURO-000149", "cognitive_control_difference", "認知制御の個人差", "Individual Differences in Cognitive Control", "抑制・切替・目標保持など認知制御の強さに関する個人差。"),
            ("NEURO-000150", "sleep_need_difference", "睡眠必要量の個人差", "Individual Differences in Sleep Need", "十分な回復や認知機能維持に必要な睡眠量の個人差。")
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
        "output_dir": "vol6_neuroscience/neuroscience_101_150",
        "index_filename": "neuroscience_101_150_index.yml",
        "index_content": "\n".join(index_lines) + "\n",
        "items": all_items
    }

    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(json.dumps(pack, ensure_ascii=False, indent=2), encoding="utf-8")

    print(f"Created: {OUT}")
    print(f"Items: {len(all_items)}")


if __name__ == "__main__":
    main()