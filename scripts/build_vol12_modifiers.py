import json
from pathlib import Path

OUT = Path("data/master_packs/vol12_modifiers_001_050.json")

SECTIONS = [
    {
        "category": "Modifiers - Context Correction",
        "name_ja": "補正要因・文脈補正",
        "items": [
            ("MOD-000001", "time_of_day_modifier", "時間帯補正", "Time of Day Modifier", "時間帯による注意・覚醒・行動変化を補正する要因。"),
            ("MOD-000002", "weekday_weekend_modifier", "平日休日補正", "Weekday Weekend Modifier", "平日と休日で行動リズムや利用傾向が変わることを補正する要因。"),
            ("MOD-000003", "location_context_modifier", "場所文脈補正", "Location Context Modifier", "自宅・職場・学校・移動中など場所文脈による行動差を補正する要因。"),
            ("MOD-000004", "device_context_modifier", "端末文脈補正", "Device Context Modifier", "スマホ・PC・タブレットなど端末差による操作や反応の違いを補正する要因。"),
            ("MOD-000005", "task_context_modifier", "課題文脈補正", "Task Context Modifier", "課題の種類・難易度・目的による行動差を補正する要因。"),
            ("MOD-000006", "social_context_modifier", "社会文脈補正", "Social Context Modifier", "単独・対人・集団・公開場面による行動差を補正する要因。"),
            ("MOD-000007", "notification_context_modifier", "通知文脈補正", "Notification Context Modifier", "通知の有無や頻度による注意・利用行動の変化を補正する要因。"),
            ("MOD-000008", "environment_noise_modifier", "環境ノイズ補正", "Environment Noise Modifier", "騒音・混雑・外乱による反応や成績の変化を補正する要因。"),
            ("MOD-000009", "recent_event_modifier", "直近イベント補正", "Recent Event Modifier", "直近の成功・失敗・予定・生活変化による状態変化を補正する要因。"),
            ("MOD-000010", "baseline_context_modifier", "ベースライン文脈補正", "Baseline Context Modifier", "本人の通常傾向と観測時文脈の差を補正する要因。")
        ]
    },
    {
        "category": "Modifiers - State Correction",
        "name_ja": "補正要因・状態補正",
        "items": [
            ("MOD-000011", "fatigue_modifier", "疲労補正", "Fatigue Modifier", "疲労による反応遅延・エラー増加・継続率低下を補正する要因。"),
            ("MOD-000012", "sleep_modifier", "睡眠補正", "Sleep Modifier", "睡眠不足・睡眠質・睡眠リズムによる状態差を補正する要因。"),
            ("MOD-000013", "stress_modifier", "ストレス補正", "Stress Modifier", "急性または慢性ストレスによる感情・判断・行動変化を補正する要因。"),
            ("MOD-000014", "arousal_modifier", "覚醒水準補正", "Arousal Modifier", "過覚醒・低覚醒による反応や集中の変化を補正する要因。"),
            ("MOD-000015", "mood_modifier", "気分補正", "Mood Modifier", "現在気分による評価・記憶・選択の偏りを補正する要因。"),
            ("MOD-000016", "health_condition_modifier", "体調補正", "Health Condition Modifier", "痛み・不調・服薬・体調変化による行動差を補正する要因。"),
            ("MOD-000017", "cognitive_load_modifier", "認知負荷補正", "Cognitive Load Modifier", "情報量や同時処理による認知負荷の影響を補正する要因。"),
            ("MOD-000018", "emotional_intensity_modifier", "感情強度補正", "Emotional Intensity Modifier", "強い感情状態による判断・表現・行動変化を補正する要因。"),
            ("MOD-000019", "motivation_level_modifier", "動機水準補正", "Motivation Level Modifier", "意欲や報酬期待の違いによる行動量差を補正する要因。"),
            ("MOD-000020", "recovery_state_modifier", "回復状態補正", "Recovery State Modifier", "負荷後の回復度による反応・集中・継続率の差を補正する要因。")
        ]
    },
    {
        "category": "Modifiers - Data Quality Correction",
        "name_ja": "補正要因・データ品質補正",
        "items": [
            ("MOD-000021", "missing_data_modifier", "欠損データ補正", "Missing Data Modifier", "観測データ欠損による推論信頼度低下を補正する要因。"),
            ("MOD-000022", "sample_size_modifier", "サンプル数補正", "Sample Size Modifier", "観測回数や期間の不足による不確実性を補正する要因。"),
            ("MOD-000023", "measurement_noise_modifier", "測定ノイズ補正", "Measurement Noise Modifier", "端末差・入力ミス・通信不安定などによる測定ノイズを補正する要因。"),
            ("MOD-000024", "outlier_modifier", "外れ値補正", "Outlier Modifier", "一時的な極端値を過大評価しないための補正要因。"),
            ("MOD-000025", "duplicate_event_modifier", "重複イベント補正", "Duplicate Event Modifier", "同一行動や近接イベントの重複記録を補正する要因。"),
            ("MOD-000026", "sensor_reliability_modifier", "センサー信頼性補正", "Sensor Reliability Modifier", "端末・センサー・ログ取得元の信頼性を反映する補正要因。"),
            ("MOD-000027", "self_report_bias_modifier", "自己報告バイアス補正", "Self Report Bias Modifier", "自己申告と行動ログの差や回答バイアスを補正する要因。"),
            ("MOD-000028", "short_term_variability_modifier", "短期変動補正", "Short Term Variability Modifier", "短期間の揺れを長期傾向と誤認しないための補正要因。"),
            ("MOD-000029", "longitudinal_stability_modifier", "長期安定性補正", "Longitudinal Stability Modifier", "長期観測で安定している傾向を重視する補正要因。"),
            ("MOD-000030", "confidence_score_modifier", "信頼度スコア補正", "Confidence Score Modifier", "推論材料としての信頼度を調整する補正要因。")
        ]
    },
    {
        "category": "Modifiers - Individual Difference Correction",
        "name_ja": "補正要因・個人差補正",
        "items": [
            ("MOD-000031", "age_modifier", "年齢補正", "Age Modifier", "年齢や発達段階による行動・認知・生活文脈の違いを補正する要因。"),
            ("MOD-000032", "experience_level_modifier", "経験値補正", "Experience Level Modifier", "課題やアプリへの慣れによる反応・成績差を補正する要因。"),
            ("MOD-000033", "skill_level_modifier", "技能水準補正", "Skill Level Modifier", "技能や知識の水準による成績差を補正する要因。"),
            ("MOD-000034", "language_proficiency_modifier", "言語習熟度補正", "Language Proficiency Modifier", "言語理解や入力能力による反応差を補正する要因。"),
            ("MOD-000035", "accessibility_need_modifier", "アクセシビリティ補正", "Accessibility Need Modifier", "身体的・認知的制約や支援必要性による行動差を補正する要因。"),
            ("MOD-000036", "cultural_background_modifier", "文化背景補正", "Cultural Background Modifier", "文化・規範・表現様式による回答や行動差を補正する要因。"),
            ("MOD-000037", "person_baseline_modifier", "個人ベースライン補正", "Person Baseline Modifier", "一般平均との差ではなく本人の通常傾向との差を重視する補正要因。"),
            ("MOD-000038", "preference_modifier", "嗜好補正", "Preference Modifier", "個人の好みや関心による選択偏りを補正する要因。"),
            ("MOD-000039", "life_stage_modifier", "ライフステージ補正", "Life Stage Modifier", "学生・社会人・子育て・介護など生活段階による差を補正する要因。"),
            ("MOD-000040", "role_context_modifier", "役割文脈補正", "Role Context Modifier", "家庭・職場・学校などで担う役割による行動差を補正する要因。")
        ]
    },
    {
        "category": "Modifiers - Ethical Safety Correction",
        "name_ja": "補正要因・倫理安全補正",
        "items": [
            ("MOD-000041", "privacy_sensitivity_modifier", "プライバシー感度補正", "Privacy Sensitivity Modifier", "個人情報や機微情報を含む場合に扱いを慎重化する補正要因。"),
            ("MOD-000042", "health_sensitivity_modifier", "健康感度補正", "Health Sensitivity Modifier", "健康・体調・医療に関わる情報を慎重に扱う補正要因。"),
            ("MOD-000043", "minor_context_modifier", "未成年文脈補正", "Minor Context Modifier", "未成年に関わる推論や表示を慎重化する補正要因。"),
            ("MOD-000044", "high_stakes_modifier", "高リスク判断補正", "High Stakes Modifier", "進路・雇用・健康など重大判断に使う場合の慎重化要因。"),
            ("MOD-000045", "distress_safety_modifier", "苦痛安全補正", "Distress Safety Modifier", "強い苦痛や危機的表現がある場合に安全側へ調整する補正要因。"),
            ("MOD-000046", "stigma_risk_modifier", "スティグマリスク補正", "Stigma Risk Modifier", "診断的・断定的・偏見的表示を避けるための補正要因。"),
            ("MOD-000047", "manipulation_risk_modifier", "操作リスク補正", "Manipulation Risk Modifier", "ユーザーの脆弱性を利用した誘導を避ける補正要因。"),
            ("MOD-000048", "over_personalization_modifier", "過剰個別化補正", "Over Personalization Modifier", "過度に踏み込んだ推論や表示を抑える補正要因。"),
            ("MOD-000049", "consent_context_modifier", "同意文脈補正", "Consent Context Modifier", "データ利用や推論表示に関する同意状態を反映する補正要因。"),
            ("MOD-000050", "safe_expression_modifier", "安全表現補正", "Safe Expression Modifier", "断定や評価ではなく、可能性・傾向・支援的表現へ調整する補正要因。")
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
        "output_dir": "vol12_modifiers/modifiers_001_050",
        "index_filename": "modifiers_001_050_index.yml",
        "index_content": "\n".join(index_lines) + "\n",
        "items": all_items
    }

    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(json.dumps(pack, ensure_ascii=False, indent=2), encoding="utf-8")

    print(f"Created: {OUT}")
    print(f"Items: {len(all_items)}")


if __name__ == "__main__":
    main()