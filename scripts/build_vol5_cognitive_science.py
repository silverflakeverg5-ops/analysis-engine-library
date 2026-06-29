import json
from pathlib import Path

OUT = Path("data/master_packs/vol5_cognitive_science_001_050.json")

SECTIONS = [
    {
        "category": "Cognitive Science - Attention",
        "name_ja": "認知科学・注意",
        "items": [
            ("COGSCI-000001", "selective_attention", "選択的注意", "Selective Attention", "複数の情報の中から特定の対象に注意資源を向ける認知機能。"),
            ("COGSCI-000002", "sustained_attention", "持続的注意", "Sustained Attention", "一定時間にわたり注意を維持し続ける認知機能。"),
            ("COGSCI-000003", "divided_attention", "分割注意", "Divided Attention", "複数の対象や課題に注意を分配する認知機能。"),
            ("COGSCI-000004", "attentional_control", "注意制御", "Attentional Control", "目的に応じて注意の向き先や強度を調整する認知機能。"),
            ("COGSCI-000005", "attentional_shift", "注意切替", "Attentional Shift", "一つの対象や課題から別の対象へ注意を移す認知機能。"),
            ("COGSCI-000006", "visual_attention", "視覚的注意", "Visual Attention", "視覚情報の中から重要な対象を選択・処理する認知機能。"),
            ("COGSCI-000007", "auditory_attention", "聴覚的注意", "Auditory Attention", "音声や環境音の中から重要な情報を選択・処理する認知機能。"),
            ("COGSCI-000008", "attention_span", "注意持続幅", "Attention Span", "一度に注意を維持できる時間的・容量的範囲。"),
            ("COGSCI-000009", "distractor_resistance", "妨害刺激耐性", "Distractor Resistance", "無関係な刺激に注意を奪われにくくする認知的性質。"),
            ("COGSCI-000010", "focus_recovery", "集中回復", "Focus Recovery", "中断や妨害後に元の課題へ注意を戻す認知的機能。")
        ]
    },
    {
        "category": "Cognitive Science - Working Memory",
        "name_ja": "認知科学・ワーキングメモリ",
        "items": [
            ("COGSCI-000011", "working_memory", "ワーキングメモリ", "Working Memory", "一時的に情報を保持しながら操作・判断に利用する認知機能。"),
            ("COGSCI-000012", "verbal_working_memory", "言語性ワーキングメモリ", "Verbal Working Memory", "言語情報を一時保持し、理解や推論に使う認知機能。"),
            ("COGSCI-000013", "visuospatial_working_memory", "視空間ワーキングメモリ", "Visuospatial Working Memory", "位置・形・空間関係などを一時保持する認知機能。"),
            ("COGSCI-000014", "memory_updating", "記憶更新", "Memory Updating", "保持中の情報を新しい情報に置き換えたり更新する認知機能。"),
            ("COGSCI-000015", "chunking", "チャンク化", "Chunking", "複数の情報をまとまりとして整理し、処理負荷を下げる認知方略。"),
            ("COGSCI-000016", "rehearsal", "リハーサル", "Rehearsal", "情報を繰り返し想起・確認して保持する認知方略。"),
            ("COGSCI-000017", "memory_load", "記憶負荷", "Memory Load", "一時的に保持・処理する情報量によって生じる認知的負荷。"),
            ("COGSCI-000018", "interference_control", "干渉制御", "Interference Control", "不要な情報が記憶処理を妨げる影響を抑える認知機能。"),
            ("COGSCI-000019", "serial_order_memory", "系列順序記憶", "Serial Order Memory", "情報の順番や並びを保持する認知機能。"),
            ("COGSCI-000020", "mental_manipulation", "心的操作", "Mental Manipulation", "頭の中で情報を変換・並べ替え・比較する認知処理。")
        ]
    },
    {
        "category": "Cognitive Science - Executive Function",
        "name_ja": "認知科学・実行機能",
        "items": [
            ("COGSCI-000021", "executive_function", "実行機能", "Executive Function", "目標達成のために思考・行動・注意を制御する高次認知機能。"),
            ("COGSCI-000022", "inhibitory_control", "抑制制御", "Inhibitory Control", "衝動的反応や不要な行動を抑える認知機能。"),
            ("COGSCI-000023", "cognitive_flexibility", "認知的柔軟性", "Cognitive Flexibility", "状況変化に応じて考え方や方略を切り替える認知機能。"),
            ("COGSCI-000024", "task_switching", "タスク切替", "Task Switching", "複数の課題やルール間を切り替えて処理する認知機能。"),
            ("COGSCI-000025", "planning_function", "計画機能", "Planning Function", "目標達成のために手順・順序・資源配分を組み立てる認知機能。"),
            ("COGSCI-000026", "monitoring_function", "モニタリング機能", "Monitoring Function", "自分の行動や進捗を確認し、必要に応じて修正する認知機能。"),
            ("COGSCI-000027", "error_monitoring", "エラーモニタリング", "Error Monitoring", "ミスやズレを検出し、修正につなげる認知機能。"),
            ("COGSCI-000028", "goal_maintenance", "目標保持", "Goal Maintenance", "現在の目標やルールを維持しながら行動する認知機能。"),
            ("COGSCI-000029", "self_regulation", "自己調整", "Self Regulation", "感情・注意・行動を目標に合わせて調整する機能。"),
            ("COGSCI-000030", "response_selection", "反応選択", "Response Selection", "複数の可能な反応の中から状況に合う行動を選ぶ認知処理。")
        ]
    },
    {
        "category": "Cognitive Science - Learning",
        "name_ja": "認知科学・学習",
        "items": [
            ("COGSCI-000031", "reinforcement_learning", "強化学習", "Reinforcement Learning", "報酬や罰のフィードバックを通じて行動選択を調整する学習過程。"),
            ("COGSCI-000032", "observational_learning", "観察学習", "Observational Learning", "他者の行動や結果を観察して学ぶ学習過程。"),
            ("COGSCI-000033", "implicit_learning", "潜在学習", "Implicit Learning", "明示的に意識せず、経験を通じて規則や傾向を獲得する学習過程。"),
            ("COGSCI-000034", "explicit_learning", "明示的学習", "Explicit Learning", "意識的に情報やルールを理解しようとする学習過程。"),
            ("COGSCI-000035", "trial_and_error_learning", "試行錯誤学習", "Trial and Error Learning", "試行と失敗を繰り返しながら有効な行動を探索する学習過程。"),
            ("COGSCI-000036", "feedback_learning_process", "フィードバック学習過程", "Feedback Learning Process", "結果や評価をもとに次の判断や行動を修正する学習過程。"),
            ("COGSCI-000037", "habit_learning", "習慣学習", "Habit Learning", "反復により行動が自動化される学習過程。"),
            ("COGSCI-000038", "rule_acquisition", "ルール獲得", "Rule Acquisition", "経験や説明から行動規則や判断基準を獲得する過程。"),
            ("COGSCI-000039", "transfer_of_learning", "学習転移", "Transfer of Learning", "ある場面で学んだ知識や技能を別の場面へ応用する過程。"),
            ("COGSCI-000040", "metacognitive_learning", "メタ認知的学習", "Metacognitive Learning", "自分の理解度や学習方法を把握しながら学ぶ過程。")
        ]
    },
    {
        "category": "Cognitive Science - Decision Making",
        "name_ja": "認知科学・意思決定",
        "items": [
            ("COGSCI-000041", "decision_making", "意思決定", "Decision Making", "複数の選択肢から目的や価値に基づいて行動を選ぶ認知過程。"),
            ("COGSCI-000042", "risk_decision", "リスク下の意思決定", "Decision Under Risk", "結果確率がある程度分かる状況で選択を行う認知過程。"),
            ("COGSCI-000043", "uncertainty_decision", "不確実性下の意思決定", "Decision Under Uncertainty", "結果や確率が不明確な状況で選択を行う認知過程。"),
            ("COGSCI-000044", "value_based_decision", "価値ベース意思決定", "Value Based Decision Making", "選択肢の価値や報酬期待に基づいて判断する認知過程。"),
            ("COGSCI-000045", "cost_benefit_analysis", "費用便益判断", "Cost Benefit Analysis", "得られる利益と必要なコストを比較して判断する認知過程。"),
            ("COGSCI-000046", "deliberative_decision", "熟慮的意思決定", "Deliberative Decision Making", "情報を比較検討しながら時間をかけて判断する認知過程。"),
            ("COGSCI-000047", "intuitive_decision", "直感的意思決定", "Intuitive Decision Making", "明示的な分析よりも経験や感覚に基づいて素早く判断する認知過程。"),
            ("COGSCI-000048", "preference_construction", "選好形成", "Preference Construction", "選択場面や文脈の中で好みや価値判断が形成される過程。"),
            ("COGSCI-000049", "choice_consistency", "選択一貫性", "Choice Consistency", "状況が変わっても選択基準や判断傾向が保たれる性質。"),
            ("COGSCI-000050", "decision_conflict", "意思決定葛藤", "Decision Conflict", "複数の選択肢や価値が競合し、判断が難しくなる状態。")
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
        "tags": [
            "CAT:認知科学",
            f"CAT:{parent_ja}",
            "ATTR:認知機能"
        ],
        "parent": [parent_ja],
        "related": [
            "認知能力",
            "行動観測",
            "認知バイアス"
        ],
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
        "modifiers": [
            "疲労",
            "注意",
            "ストレス",
            "課題難易度"
        ],
        "evidence": "認知科学・認知心理学・HCI研究で使用",
        "status": "active"
    }


def main():
    all_items = []
    index_lines = [
        "category: Cognitive Science",
        "name_ja: 認知科学",
        "items:"
    ]

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
        "output_dir": "vol5_cognitive_science/cognitive_science_001_050",
        "index_filename": "cognitive_science_001_050_index.yml",
        "index_content": "\n".join(index_lines) + "\n",
        "items": all_items
    }

    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(json.dumps(pack, ensure_ascii=False, indent=2), encoding="utf-8")

    print(f"Created: {OUT}")
    print(f"Items: {len(all_items)}")


if __name__ == "__main__":
    main()