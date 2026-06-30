import json
from pathlib import Path

OUT = Path("data/master_packs/vol8_physiology_051_100.json")

SECTIONS = [
    {
        "category": "Physiology - Nutrition Metabolism",
        "name_ja": "生理・栄養代謝",
        "items": [
            ("PHYS-000051", "blood_glucose_stability", "血糖安定性", "Blood Glucose Stability", "血糖値の上下が集中・眠気・気分・判断に影響する状態。"),
            ("PHYS-000052", "hunger_state", "空腹状態", "Hunger State", "空腹により注意・感情・意思決定が影響を受ける状態。"),
            ("PHYS-000053", "satiety_state", "満腹状態", "Satiety State", "満腹により眠気・集中低下・活動量変化が生じやすい状態。"),
            ("PHYS-000054", "caffeine_effect", "カフェイン影響", "Caffeine Effect", "カフェイン摂取による覚醒・集中・不安・睡眠への影響。"),
            ("PHYS-000055", "alcohol_effect", "アルコール影響", "Alcohol Effect", "飲酒による判断・抑制・睡眠・感情への影響。"),
            ("PHYS-000056", "nutrient_deficit", "栄養不足", "Nutrient Deficit", "必要な栄養素の不足が体調・気分・認知に影響する状態。"),
            ("PHYS-000057", "metabolic_energy", "代謝エネルギー", "Metabolic Energy", "身体と脳の活動を支えるエネルギー利用状態。"),
            ("PHYS-000058", "hydration_balance", "水分バランス", "Hydration Balance", "水分摂取と排出のバランスが身体・認知に影響する状態。"),
            ("PHYS-000059", "meal_quality", "食事品質", "Meal Quality", "食事内容の質がエネルギー・気分・集中に影響する要因。"),
            ("PHYS-000060", "digestive_load", "消化負荷", "Digestive Load", "消化に伴う身体負荷が眠気や集中に影響する状態。")
        ]
    },
    {
        "category": "Physiology - Exercise Movement",
        "name_ja": "生理・運動身体活動",
        "items": [
            ("PHYS-000061", "exercise_frequency", "運動頻度", "Exercise Frequency", "一定期間内に運動や身体活動を行う頻度。"),
            ("PHYS-000062", "exercise_intensity", "運動強度", "Exercise Intensity", "身体活動時にかかる負荷の強さ。"),
            ("PHYS-000063", "aerobic_condition", "有酸素状態", "Aerobic Condition", "持久的活動を支える心肺機能や活動耐性の状態。"),
            ("PHYS-000064", "muscle_strength_condition", "筋力状態", "Muscle Strength Condition", "身体動作や姿勢保持を支える筋力の状態。"),
            ("PHYS-000065", "mobility_condition", "可動性状態", "Mobility Condition", "関節・筋肉・身体動作の動かしやすさ。"),
            ("PHYS-000066", "movement_variability", "身体活動変動", "Movement Variability", "日々の活動量や移動量の変動パターン。"),
            ("PHYS-000067", "sedentary_load", "座位負荷", "Sedentary Load", "長時間座位により身体・集中・疲労へ負荷がかかる状態。"),
            ("PHYS-000068", "movement_breaks", "身体活動休憩", "Movement Breaks", "座位や作業の合間に身体を動かして回復する行動。"),
            ("PHYS-000069", "exercise_recovery", "運動後回復", "Exercise Recovery", "運動後に疲労・筋緊張・エネルギー状態が回復する過程。"),
            ("PHYS-000070", "body_activation", "身体活性化", "Body Activation", "軽い運動や姿勢変化により覚醒・集中が高まる状態。")
        ]
    },
    {
        "category": "Physiology - Sensory Load",
        "name_ja": "生理・感覚負荷",
        "items": [
            ("PHYS-000071", "visual_load", "視覚負荷", "Visual Load", "画面・文字・光・細かい情報処理により視覚系へかかる負荷。"),
            ("PHYS-000072", "auditory_load", "聴覚負荷", "Auditory Load", "音量・騒音・会話・聞き取りにより聴覚系へかかる負荷。"),
            ("PHYS-000073", "sensory_sensitivity", "感覚過敏性", "Sensory Sensitivity", "光・音・匂い・触覚などの刺激に反応しやすい状態。"),
            ("PHYS-000074", "sensory_underresponsiveness", "感覚低反応", "Sensory Underresponsiveness", "感覚刺激への気づきや反応が弱くなりやすい状態。"),
            ("PHYS-000075", "screen_brightness_load", "画面輝度負荷", "Screen Brightness Load", "画面の明るさやコントラストが目や疲労に与える負荷。"),
            ("PHYS-000076", "noise_stress", "騒音ストレス", "Noise Stress", "継続的または突発的な音がストレスや注意低下を引き起こす状態。"),
            ("PHYS-000077", "multisensory_overload", "多感覚過負荷", "Multisensory Overload", "複数の感覚刺激が同時に多く入り処理負荷が高まる状態。"),
            ("PHYS-000078", "sensory_recovery", "感覚回復", "Sensory Recovery", "刺激の少ない環境で感覚負荷や疲労が回復する過程。"),
            ("PHYS-000079", "tactile_comfort", "触覚快適性", "Tactile Comfort", "衣服・椅子・端末などの触覚的快適さが行動に影響する状態。"),
            ("PHYS-000080", "environmental_sensory_fit", "感覚環境適合", "Environmental Sensory Fit", "光・音・温度などの感覚環境が本人に合っている度合い。")
        ]
    },
    {
        "category": "Physiology - Hormonal State",
        "name_ja": "生理・ホルモン状態",
        "items": [
            ("PHYS-000081", "cortisol_rhythm", "コルチゾールリズム", "Cortisol Rhythm", "ストレスや覚醒に関わるコルチゾール分泌の日内変動。"),
            ("PHYS-000082", "melatonin_rhythm", "メラトニンリズム", "Melatonin Rhythm", "睡眠覚醒リズムを支えるメラトニン分泌の変動。"),
            ("PHYS-000083", "sex_hormone_context", "性ホルモン文脈", "Sex Hormone Context", "性ホルモン変動が気分・体調・認知に影響し得る文脈。"),
            ("PHYS-000084", "thyroid_function_context", "甲状腺機能文脈", "Thyroid Function Context", "代謝・活力・気分に関わる甲状腺機能の文脈。"),
            ("PHYS-000085", "adrenal_activation", "副腎活性", "Adrenal Activation", "ストレスや覚醒に伴う副腎系の活性化。"),
            ("PHYS-000086", "hormonal_fluctuation", "ホルモン変動", "Hormonal Fluctuation", "周期・ストレス・生活リズムに伴うホルモン状態の変化。"),
            ("PHYS-000087", "puberty_context", "思春期文脈", "Puberty Context", "成長期のホルモン変化が情動・身体・行動に影響する文脈。"),
            ("PHYS-000088", "menopause_context", "更年期文脈", "Menopause Context", "更年期に伴うホルモン変化が睡眠・気分・体調に影響する文脈。"),
            ("PHYS-000089", "stress_hormone_load", "ストレスホルモン負荷", "Stress Hormone Load", "慢性的ストレスによりホルモン系へ負荷がかかる状態。"),
            ("PHYS-000090", "hormonal_recovery", "ホルモン回復", "Hormonal Recovery", "負荷やリズム乱れの後にホルモン状態が安定へ戻る過程。")
        ]
    },
    {
        "category": "Physiology - Integration",
        "name_ja": "生理・統合",
        "items": [
            ("PHYS-000091", "mind_body_interaction", "心身相互作用", "Mind Body Interaction", "身体状態と認知・感情・行動が相互に影響し合う仕組み。"),
            ("PHYS-000092", "physiological_baseline", "生理的ベースライン", "Physiological Baseline", "通常時の覚醒・疲労・睡眠・体調などの基準状態。"),
            ("PHYS-000093", "physiological_variability", "生理的変動性", "Physiological Variability", "日内・日間で生理状態がどの程度変動するか。"),
            ("PHYS-000094", "physiological_resilience", "生理的レジリエンス", "Physiological Resilience", "負荷後に身体状態が回復・安定する力。"),
            ("PHYS-000095", "physiological_vulnerability", "生理的脆弱性", "Physiological Vulnerability", "睡眠不足・疲労・ストレスなどの影響を受けやすい状態。"),
            ("PHYS-000096", "body_signal_awareness", "身体信号への気づき", "Body Signal Awareness", "疲労・空腹・緊張など身体サインに気づく度合い。"),
            ("PHYS-000097", "behavioral_energy_budget", "行動エネルギー予算", "Behavioral Energy Budget", "一日に使える身体的・精神的エネルギーの配分。"),
            ("PHYS-000098", "load_recovery_balance", "負荷回復バランス", "Load Recovery Balance", "活動負荷と回復機会が釣り合っている度合い。"),
            ("PHYS-000099", "physiological_context_dependency", "生理文脈依存性", "Physiological Context Dependency", "体調やリズムによって行動・判断が変化する性質。"),
            ("PHYS-000100", "physiological_integration", "生理統合", "Physiological Integration", "睡眠・疲労・栄養・ストレス・身体状態が統合して行動に影響する状態。")
        ]
    }
]


def make_item(item_id, slug, name_ja, name_en, definition_ja, category, parent_ja):
    return {
        "filename": f"{item_id}_{slug}.yml",
        "id": item_id,
        "knowledge_type": "physiology_factor",
        "name_ja": name_ja,
        "name_en": name_en,
        "category": "Physiology",
        "attribute": category.replace("Physiology - ", ""),
        "definition_ja": definition_ja,
        "tags": ["CAT:生理", f"CAT:{parent_ja}", "ATTR:補正要因"],
        "parent": [parent_ja],
        "related": ["神経科学", "行動観測", "環境要因"],
        "observable_data": [
            f"{name_ja}関連反応時間",
            f"{name_ja}関連行動変化",
            f"{name_ja}関連継続率",
            f"{name_ja}関連ストレス反応"
        ],
        "signal_candidates": [
            f"{name_ja}が注意・感情・判断・行動に影響している可能性がある",
            "体調条件の変化に応じて行動パターンが変化する"
        ],
        "device_level": "スマホ・PCのみ推定可能",
        "modifiers": ["年齢", "睡眠", "疲労", "生活状況"],
        "evidence": "生理心理学・健康心理学・睡眠研究・HCI研究で使用",
        "status": "active"
    }


def main():
    all_items = []
    index_lines = ["category: Physiology", "name_ja: 生理", "items:"]

    for section in SECTIONS:
        parent_ja = section["name_ja"].replace("生理・", "")
        for raw in section["items"]:
            item = make_item(*raw, category=section["category"], parent_ja=parent_ja)
            all_items.append(item)
            index_lines.append(f"  - {item['filename']}")

    index_lines.extend([
        "notes:",
        "  - 生理要因は医療診断ではなく補正要因として扱う",
        "  - 観測可能データとSignal候補を中心に管理する",
        "  - アプリ側でスコアリング・推論・表示を行う"
    ])

    pack = {
        "output_dir": "vol8_physiology/physiology_051_100",
        "index_filename": "physiology_051_100_index.yml",
        "index_content": "\n".join(index_lines) + "\n",
        "items": all_items
    }

    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(json.dumps(pack, ensure_ascii=False, indent=2), encoding="utf-8")

    print(f"Created: {OUT}")
    print(f"Items: {len(all_items)}")


if __name__ == "__main__":
    main()