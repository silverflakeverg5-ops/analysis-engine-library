import json
from pathlib import Path

OUT = Path("data/master_packs/vol8_physiology_001_050.json")

SECTIONS = [
    {
        "category": "Physiology - Sleep",
        "name_ja": "生理・睡眠",
        "items": [
            ("PHYS-000001", "sleep_duration", "睡眠時間", "Sleep Duration", "一晩または一定期間における総睡眠時間。"),
            ("PHYS-000002", "sleep_quality", "睡眠の質", "Sleep Quality", "睡眠の深さ・中途覚醒・回復感などを含む主観的・客観的な睡眠状態。"),
            ("PHYS-000003", "sleep_regularness", "睡眠規則性", "Sleep Regularness", "就寝・起床時刻が安定している度合い。"),
            ("PHYS-000004", "sleep_latency", "入眠潜時", "Sleep Latency", "寝ようとしてから眠りに入るまでの時間。"),
            ("PHYS-000005", "night_waking", "中途覚醒", "Night Waking", "睡眠中に目が覚める頻度や時間。"),
            ("PHYS-000006", "daytime_sleepiness", "日中眠気", "Daytime Sleepiness", "日中に眠気や覚醒低下が生じる状態。"),
            ("PHYS-000007", "sleep_debt", "睡眠負債", "Sleep Debt", "必要睡眠量に対して不足した睡眠が蓄積した状態。"),
            ("PHYS-000008", "circadian_stability", "概日安定性", "Circadian Stability", "体内時計と生活リズムが安定している度合い。"),
            ("PHYS-000009", "chronotype_tendency", "朝型夜型傾向", "Chronotype Tendency", "活動しやすい時間帯が朝寄りか夜寄りかに関する生理的傾向。"),
            ("PHYS-000010", "sleep_recovery", "睡眠回復", "Sleep Recovery", "睡眠によって疲労・注意低下・情動負荷が回復する過程。")
        ]
    },
    {
        "category": "Physiology - Fatigue",
        "name_ja": "生理・疲労",
        "items": [
            ("PHYS-000011", "physical_fatigue", "身体疲労", "Physical Fatigue", "身体活動や姿勢維持によって生じる身体的な疲労状態。"),
            ("PHYS-000012", "mental_fatigue", "精神疲労", "Mental Fatigue", "長時間の認知活動や判断によって注意・意欲・処理効率が低下する状態。"),
            ("PHYS-000013", "fatigue_accumulation", "疲労蓄積", "Fatigue Accumulation", "休息不足や負荷継続により疲労が積み重なる状態。"),
            ("PHYS-000014", "recovery_rate", "回復速度", "Recovery Rate", "疲労やストレスから通常状態へ戻る速さ。"),
            ("PHYS-000015", "energy_level", "エネルギー水準", "Energy Level", "活動・集中・行動開始に使える主観的または生理的な活力量。"),
            ("PHYS-000016", "vigor", "活力", "Vigor", "身体的・精神的に活動へ向かえる強さや前向きさ。"),
            ("PHYS-000017", "burnout_risk_state", "燃え尽きリスク状態", "Burnout Risk State", "慢性的な負荷により意欲低下・疲弊・距離感が強まりやすい状態。"),
            ("PHYS-000018", "rest_deficit", "休息不足", "Rest Deficit", "睡眠以外の休憩・回復時間が不足している状態。"),
            ("PHYS-000019", "overexertion", "過活動", "Overexertion", "必要以上に活動や努力を続け、回復を上回る負荷がかかる状態。"),
            ("PHYS-000020", "fatigue_sensitivity", "疲労感受性", "Fatigue Sensitivity", "同じ負荷に対して疲労を感じやすい度合い。")
        ]
    },
    {
        "category": "Physiology - Stress Arousal",
        "name_ja": "生理・ストレス覚醒",
        "items": [
            ("PHYS-000021", "acute_stress_response", "急性ストレス反応", "Acute Stress Response", "短期的な負荷や脅威に対して生じる身体・認知・情動反応。"),
            ("PHYS-000022", "chronic_stress_state", "慢性ストレス状態", "Chronic Stress State", "長期的に負荷が続き、心身の調整負担が高まった状態。"),
            ("PHYS-000023", "arousal_level", "覚醒水準", "Arousal Level", "眠気から緊張までを含む心身の活性化度合い。"),
            ("PHYS-000024", "hyperarousal", "過覚醒", "Hyperarousal", "緊張や警戒が高まり、休息や睡眠に入りにくい状態。"),
            ("PHYS-000025", "underarousal", "低覚醒", "Underarousal", "眠気・無気力・反応低下が生じやすい低活性状態。"),
            ("PHYS-000026", "stress_recovery", "ストレス回復", "Stress Recovery", "ストレス反応後に身体・感情・注意状態が通常に戻る過程。"),
            ("PHYS-000027", "autonomic_balance", "自律神経バランス", "Autonomic Balance", "交感神経と副交感神経の活動バランス。"),
            ("PHYS-000028", "tension_state", "緊張状態", "Tension State", "筋緊張・呼吸変化・注意固定などを伴う心身の緊張。"),
            ("PHYS-000029", "relaxation_state", "リラックス状態", "Relaxation State", "心身の緊張が低下し、回復や安定に向かう状態。"),
            ("PHYS-000030", "stress_tolerance", "ストレス耐性", "Stress Tolerance", "負荷や圧力があっても行動・感情・判断を維持できる度合い。")
        ]
    },
    {
        "category": "Physiology - Body Rhythm",
        "name_ja": "生理・身体リズム",
        "items": [
            ("PHYS-000031", "daily_activity_rhythm", "日内活動リズム", "Daily Activity Rhythm", "一日の中で活動量や覚醒度が変化するリズム。"),
            ("PHYS-000032", "meal_timing", "食事タイミング", "Meal Timing", "食事を取る時刻や間隔の規則性。"),
            ("PHYS-000033", "hydration_state", "水分状態", "Hydration State", "水分摂取や脱水傾向に関する身体状態。"),
            ("PHYS-000034", "body_temperature_rhythm", "体温リズム", "Body Temperature Rhythm", "一日の中で体温が変化する生理的リズム。"),
            ("PHYS-000035", "menstrual_cycle_context", "月経周期文脈", "Menstrual Cycle Context", "月経周期に伴う体調・気分・集中状態の変化に関する文脈。"),
            ("PHYS-000036", "seasonal_physiological_change", "季節性生理変化", "Seasonal Physiological Change", "季節や日照時間の変化に伴う睡眠・気分・活動量の変化。"),
            ("PHYS-000037", "jet_lag_state", "時差ぼけ状態", "Jet Lag State", "体内時計と現地時間のずれにより認知・睡眠・体調が乱れる状態。"),
            ("PHYS-000038", "shift_work_rhythm", "交代勤務リズム", "Shift Work Rhythm", "勤務時間の変動によって睡眠や概日リズムが乱れやすい状態。"),
            ("PHYS-000039", "weekend_social_jetlag", "社会的時差ぼけ", "Social Jetlag", "平日と休日の睡眠時間帯のずれによって生じるリズムの不一致。"),
            ("PHYS-000040", "recovery_rhythm", "回復リズム", "Recovery Rhythm", "活動と休息がどのような周期で繰り返されるかに関する生理的パターン。")
        ]
    },
    {
        "category": "Physiology - Physical Condition",
        "name_ja": "生理・体調",
        "items": [
            ("PHYS-000041", "pain_state", "痛み状態", "Pain State", "身体の痛みが注意・感情・行動に影響している状態。"),
            ("PHYS-000042", "headache_state", "頭痛状態", "Headache State", "頭痛により集中・判断・気分が影響を受ける状態。"),
            ("PHYS-000043", "digestive_condition", "消化状態", "Digestive Condition", "空腹・満腹・胃腸不調などが行動や集中に影響する状態。"),
            ("PHYS-000044", "muscle_tension", "筋緊張", "Muscle Tension", "肩・首・背中などの筋肉が緊張している状態。"),
            ("PHYS-000045", "posture_condition", "姿勢状態", "Posture Condition", "姿勢や身体配置が疲労・集中・気分に影響する状態。"),
            ("PHYS-000046", "visual_strain", "眼精疲労", "Visual Strain", "画面利用や視覚負荷により目や注意が疲労している状態。"),
            ("PHYS-000047", "hearing_load", "聴覚負荷", "Hearing Load", "騒音や聞き取り負荷により注意や疲労が影響を受ける状態。"),
            ("PHYS-000048", "illness_state", "体調不良状態", "Illness State", "風邪・発熱・不調などにより認知や行動が低下しやすい状態。"),
            ("PHYS-000049", "medication_context", "服薬文脈", "Medication Context", "薬の使用が眠気・集中・気分・身体状態に影響し得る文脈。"),
            ("PHYS-000050", "physical_condition_integration", "体調統合", "Physical Condition Integration", "睡眠・疲労・痛み・覚醒など複数の体調要因が統合して行動に影響する状態。")
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
        "output_dir": "vol8_physiology/physiology_001_050",
        "index_filename": "physiology_001_050_index.yml",
        "index_content": "\n".join(index_lines) + "\n",
        "items": all_items
    }

    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(json.dumps(pack, ensure_ascii=False, indent=2), encoding="utf-8")

    print(f"Created: {OUT}")
    print(f"Items: {len(all_items)}")


if __name__ == "__main__":
    main()