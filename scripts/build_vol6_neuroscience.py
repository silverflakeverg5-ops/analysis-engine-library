import json
from pathlib import Path

OUT = Path("data/master_packs/vol6_neuroscience_001_050.json")

SECTIONS = [
    {
        "category": "Neuroscience - Brain Systems",
        "name_ja": "神経科学・脳システム",
        "items": [
            ("NEURO-000001", "prefrontal_cortex", "前頭前野", "Prefrontal Cortex", "計画・判断・抑制・ワーキングメモリなど高次認知機能に関わる脳領域。"),
            ("NEURO-000002", "dorsolateral_prefrontal_cortex", "背外側前頭前野", "Dorsolateral Prefrontal Cortex", "ワーキングメモリ・認知制御・計画に関わる前頭前野領域。"),
            ("NEURO-000003", "ventromedial_prefrontal_cortex", "腹内側前頭前野", "Ventromedial Prefrontal Cortex", "価値判断・感情的意思決定・自己関連処理に関わる前頭前野領域。"),
            ("NEURO-000004", "orbitofrontal_cortex", "眼窩前頭皮質", "Orbitofrontal Cortex", "報酬価値・罰・選択肢評価の更新に関わる脳領域。"),
            ("NEURO-000005", "anterior_cingulate_cortex", "前部帯状皮質", "Anterior Cingulate Cortex", "葛藤検出・エラー検出・注意制御に関わる脳領域。"),
            ("NEURO-000006", "amygdala", "扁桃体", "Amygdala", "恐怖・脅威・情動的価値づけに関わる脳領域。"),
            ("NEURO-000007", "hippocampus", "海馬", "Hippocampus", "エピソード記憶・空間記憶・記憶固定に関わる脳領域。"),
            ("NEURO-000008", "striatum", "線条体", "Striatum", "報酬学習・習慣形成・行動選択に関わる脳領域。"),
            ("NEURO-000009", "insula", "島皮質", "Insula", "身体感覚・内受容感覚・嫌悪・リスク認知に関わる脳領域。"),
            ("NEURO-000010", "parietal_cortex", "頭頂皮質", "Parietal Cortex", "空間処理・注意・数量処理などに関わる脳領域。")
        ]
    },
    {
        "category": "Neuroscience - Neural Networks",
        "name_ja": "神経科学・脳ネットワーク",
        "items": [
            ("NEURO-000011", "default_mode_network", "デフォルトモードネットワーク", "Default Mode Network", "自己関連思考・内省・過去未来シミュレーションに関わる脳ネットワーク。"),
            ("NEURO-000012", "central_executive_network", "中央実行ネットワーク", "Central Executive Network", "目標志向的思考・ワーキングメモリ・認知制御に関わる脳ネットワーク。"),
            ("NEURO-000013", "salience_network", "サリエンスネットワーク", "Salience Network", "重要刺激の検出と注意切替に関わる脳ネットワーク。"),
            ("NEURO-000014", "dorsal_attention_network", "背側注意ネットワーク", "Dorsal Attention Network", "目的に基づく注意の方向づけに関わる脳ネットワーク。"),
            ("NEURO-000015", "ventral_attention_network", "腹側注意ネットワーク", "Ventral Attention Network", "予期しない重要刺激への注意切替に関わる脳ネットワーク。"),
            ("NEURO-000016", "reward_network", "報酬ネットワーク", "Reward Network", "報酬予測・快感・接近行動に関わる神経ネットワーク。"),
            ("NEURO-000017", "limbic_system", "辺縁系", "Limbic System", "情動・記憶・動機づけに関わる脳領域群。"),
            ("NEURO-000018", "frontoparietal_network", "前頭頭頂ネットワーク", "Frontoparietal Network", "柔軟な認知制御や課題遂行に関わる脳ネットワーク。"),
            ("NEURO-000019", "sensorimotor_network", "感覚運動ネットワーク", "Sensorimotor Network", "身体運動と感覚処理に関わる脳ネットワーク。"),
            ("NEURO-000020", "social_brain_network", "社会脳ネットワーク", "Social Brain Network", "他者理解・共感・社会的判断に関わる脳ネットワーク。")
        ]
    },
    {
        "category": "Neuroscience - Neurotransmitters",
        "name_ja": "神経科学・神経伝達物質",
        "items": [
            ("NEURO-000021", "dopamine", "ドーパミン", "Dopamine", "報酬予測・動機づけ・学習・行動選択に関わる神経伝達物質。"),
            ("NEURO-000022", "serotonin", "セロトニン", "Serotonin", "気分・衝動性・睡眠・満足感などに関わる神経伝達物質。"),
            ("NEURO-000023", "noradrenaline", "ノルアドレナリン", "Noradrenaline", "覚醒・注意・ストレス反応に関わる神経伝達物質。"),
            ("NEURO-000024", "acetylcholine", "アセチルコリン", "Acetylcholine", "注意・学習・記憶・覚醒に関わる神経伝達物質。"),
            ("NEURO-000025", "gaba", "GABA", "GABA", "神経活動の抑制に関わり、不安・興奮・制御に影響する神経伝達物質。"),
            ("NEURO-000026", "glutamate", "グルタミン酸", "Glutamate", "興奮性神経伝達や学習・記憶の可塑性に関わる神経伝達物質。"),
            ("NEURO-000027", "oxytocin", "オキシトシン", "Oxytocin", "社会的結びつき・信頼・親和行動に関わる神経ペプチド。"),
            ("NEURO-000028", "endorphin", "エンドルフィン", "Endorphin", "快感・痛みの緩和・報酬感に関わる内因性オピオイド。"),
            ("NEURO-000029", "cortisol", "コルチゾール", "Cortisol", "ストレス反応・覚醒・代謝調整に関わるホルモン。"),
            ("NEURO-000030", "melatonin", "メラトニン", "Melatonin", "睡眠覚醒リズムや概日リズムの調整に関わるホルモン。")
        ]
    },
    {
        "category": "Neuroscience - Reward Learning",
        "name_ja": "神経科学・報酬学習",
        "items": [
            ("NEURO-000031", "reward_prediction_error", "報酬予測誤差", "Reward Prediction Error", "期待した報酬と実際の報酬との差に基づいて学習を更新する信号。"),
            ("NEURO-000032", "reinforcement_signal", "強化信号", "Reinforcement Signal", "行動結果に基づいて将来の行動選択を変えるための神経信号。"),
            ("NEURO-000033", "approach_system", "接近システム", "Approach System", "報酬や望ましい対象へ近づく行動を促す神経行動システム。"),
            ("NEURO-000034", "avoidance_system", "回避システム", "Avoidance System", "脅威や損失を避ける行動を促す神経行動システム。"),
            ("NEURO-000035", "habit_loop", "習慣ループ", "Habit Loop", "手がかり・行動・報酬の反復によって形成される習慣的行動の循環。"),
            ("NEURO-000036", "cue_reactivity", "手がかり反応性", "Cue Reactivity", "報酬や習慣に結びついた刺激に対して反応しやすくなる性質。"),
            ("NEURO-000037", "incentive_salience", "誘因顕著性", "Incentive Salience", "報酬に関連する手がかりが注意や接近行動を引きつける性質。"),
            ("NEURO-000038", "delay_discounting_neural_basis", "遅延割引の神経基盤", "Neural Basis of Delay Discounting", "即時報酬と将来報酬の選択に関わる神経メカニズム。"),
            ("NEURO-000039", "risk_reward_tradeoff", "リスク報酬トレードオフ", "Risk Reward Tradeoff", "リスクと報酬のバランスを評価する神経認知過程。"),
            ("NEURO-000040", "motivation_energy_allocation", "動機づけとエネルギー配分", "Motivational Energy Allocation", "報酬期待や価値に応じて努力量を配分する神経認知過程。")
        ]
    },
    {
        "category": "Neuroscience - Stress Emotion",
        "name_ja": "神経科学・ストレス情動",
        "items": [
            ("NEURO-000041", "stress_response_system", "ストレス反応系", "Stress Response System", "脅威や負荷に対して身体と脳を動員する反応システム。"),
            ("NEURO-000042", "hpa_axis", "HPA軸", "HPA Axis", "視床下部・下垂体・副腎から成るストレス応答システム。"),
            ("NEURO-000043", "sympathetic_activation", "交感神経活性化", "Sympathetic Activation", "緊張・覚醒・闘争逃走反応に関わる自律神経の活性化。"),
            ("NEURO-000044", "parasympathetic_recovery", "副交感神経回復", "Parasympathetic Recovery", "休息・回復・鎮静に関わる自律神経の働き。"),
            ("NEURO-000045", "emotion_regulation_network", "感情調整ネットワーク", "Emotion Regulation Network", "前頭前野と辺縁系などが関わる感情調整の神経ネットワーク。"),
            ("NEURO-000046", "fear_conditioning", "恐怖条件づけ", "Fear Conditioning", "中立刺激が恐怖や脅威と結びつく学習過程。"),
            ("NEURO-000047", "extinction_learning", "消去学習", "Extinction Learning", "以前に学習した恐怖や反応が安全経験によって弱まる学習過程。"),
            ("NEURO-000048", "threat_bias_neural_basis", "脅威バイアスの神経基盤", "Neural Basis of Threat Bias", "脅威刺激へ注意や反応が偏る神経メカニズム。"),
            ("NEURO-000049", "emotional_arousal", "情動覚醒", "Emotional Arousal", "感情刺激によって身体・注意・記憶が活性化する状態。"),
            ("NEURO-000050", "allostatic_load", "アロスタティック負荷", "Allostatic Load", "慢性的なストレス適応によって身体脳システムに蓄積する負担。")
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
        "output_dir": "vol6_neuroscience/neuroscience_001_050",
        "index_filename": "neuroscience_001_050_index.yml",
        "index_content": "\n".join(index_lines) + "\n",
        "items": all_items
    }

    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(json.dumps(pack, ensure_ascii=False, indent=2), encoding="utf-8")

    print(f"Created: {OUT}")
    print(f"Items: {len(all_items)}")


if __name__ == "__main__":
    main()