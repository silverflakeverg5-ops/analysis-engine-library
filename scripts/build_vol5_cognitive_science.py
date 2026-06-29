import json
from pathlib import Path

OUT = Path("data/master_packs/vol5_cognitive_science_101_150.json")

SECTIONS = [
    {
        "category": "Cognitive Science - Memory",
        "name_ja": "認知科学・記憶",
        "items": [
            ("COGSCI-000101", "episodic_memory", "エピソード記憶", "Episodic Memory", "個人的な出来事や経験を時間・場所・文脈とともに保持する記憶システム。"),
            ("COGSCI-000102", "semantic_memory", "意味記憶", "Semantic Memory", "言葉・概念・事実・知識などを保持する記憶システム。"),
            ("COGSCI-000103", "procedural_memory", "手続き記憶", "Procedural Memory", "技能や操作手順など、行動として表れる知識を保持する記憶システム。"),
            ("COGSCI-000104", "short_term_memory", "短期記憶", "Short Term Memory", "短時間だけ情報を保持する記憶機能。"),
            ("COGSCI-000105", "long_term_memory", "長期記憶", "Long Term Memory", "長期間にわたって情報を保持する記憶システム。"),
            ("COGSCI-000106", "encoding", "符号化", "Encoding", "経験や情報を記憶として保存できる形に変換する過程。"),
            ("COGSCI-000107", "retrieval", "検索・想起", "Retrieval", "保存された記憶情報を取り出して利用する過程。"),
            ("COGSCI-000108", "recognition_memory", "再認記憶", "Recognition Memory", "以前に見た・経験した情報かどうかを判断する記憶機能。"),
            ("COGSCI-000109", "recall_memory", "再生記憶", "Recall Memory", "手がかりが少ない状態で記憶内容を思い出す機能。"),
            ("COGSCI-000110", "memory_consolidation", "記憶固定", "Memory Consolidation", "新しい記憶が安定して長期保持されるようになる過程。")
        ]
    },
    {
        "category": "Cognitive Science - Reasoning",
        "name_ja": "認知科学・推論",
        "items": [
            ("COGSCI-000111", "deductive_reasoning", "演繹推論", "Deductive Reasoning", "前提が正しければ結論も必然的に導かれる形式の推論過程。"),
            ("COGSCI-000112", "inductive_reasoning", "帰納推論", "Inductive Reasoning", "複数の事例や観察から一般的な規則や傾向を推測する推論過程。"),
            ("COGSCI-000113", "abductive_reasoning", "仮説推論", "Abductive Reasoning", "観察された結果を説明するもっともらしい原因や仮説を考える推論過程。"),
            ("COGSCI-000114", "causal_reasoning", "因果推論", "Causal Reasoning", "出来事同士の原因と結果の関係を推測する認知過程。"),
            ("COGSCI-000115", "probabilistic_reasoning", "確率推論", "Probabilistic Reasoning", "不確実な情報をもとに発生可能性や期待値を推定する推論過程。"),
            ("COGSCI-000116", "counterfactual_reasoning", "反実仮想推論", "Counterfactual Reasoning", "もし別の行動や条件だったらどうなったかを考える推論過程。"),
            ("COGSCI-000117", "conditional_reasoning", "条件推論", "Conditional Reasoning", "もしAならBという条件関係をもとに結論を導く推論過程。"),
            ("COGSCI-000118", "analogical_mapping", "類推対応づけ", "Analogical Mapping", "異なる対象や状況間の構造的な対応関係を見つける推論過程。"),
            ("COGSCI-000119", "hypothesis_testing", "仮説検証", "Hypothesis Testing", "仮説を立て、証拠や結果によって妥当性を確認する認知過程。"),
            ("COGSCI-000120", "evidence_evaluation", "証拠評価", "Evidence Evaluation", "情報や証拠の信頼性・関連性・強さを評価する認知過程。")
        ]
    },
    {
        "category": "Cognitive Science - Emotion Cognition",
        "name_ja": "認知科学・感情認知",
        "items": [
            ("COGSCI-000121", "emotion_appraisal", "感情評価", "Emotion Appraisal", "出来事や状況を自分にとってどのような意味を持つか評価し感情を生じさせる過程。"),
            ("COGSCI-000122", "emotion_regulation", "感情調整", "Emotion Regulation", "感情の強さ・持続・表出を調整する認知情動過程。"),
            ("COGSCI-000123", "affective_attention", "感情的注意", "Affective Attention", "感情的に重要な刺激へ注意が向きやすくなる認知過程。"),
            ("COGSCI-000124", "mood_congruent_processing", "気分一致処理", "Mood Congruent Processing", "現在の気分と一致する情報が処理・想起されやすくなる認知過程。"),
            ("COGSCI-000125", "emotional_memory", "感情記憶", "Emotional Memory", "感情を伴う経験が記憶に強く残りやすくなる記憶処理。"),
            ("COGSCI-000126", "threat_detection", "脅威検知", "Threat Detection", "危険や損失につながる刺激を検出しやすくする認知機能。"),
            ("COGSCI-000127", "reward_sensitivity", "報酬感受性", "Reward Sensitivity", "報酬や快感につながる刺激へ反応しやすい認知情動特性。"),
            ("COGSCI-000128", "frustration_tolerance", "欲求不満耐性", "Frustration Tolerance", "期待通りに進まない状況で行動や感情を保つ性質。"),
            ("COGSCI-000129", "affective_decision_making", "感情的意思決定", "Affective Decision Making", "感情状態や情動反応が選択や判断に影響する意思決定過程。"),
            ("COGSCI-000130", "emotional_interference", "感情的干渉", "Emotional Interference", "感情刺激が注意・記憶・判断などの認知処理を妨げる現象。")
        ]
    },
    {
        "category": "Cognitive Science - Mental Models",
        "name_ja": "認知科学・メンタルモデル",
        "items": [
            ("COGSCI-000131", "mental_model", "メンタルモデル", "Mental Model", "対象・仕組み・状況について頭の中に形成される理解の枠組み。"),
            ("COGSCI-000132", "schema", "スキーマ", "Schema", "経験に基づいて形成された知識構造や解釈の枠組み。"),
            ("COGSCI-000133", "script_knowledge", "スクリプト知識", "Script Knowledge", "典型的な場面で起きる行動や出来事の順序に関する知識。"),
            ("COGSCI-000134", "conceptual_model", "概念モデル", "Conceptual Model", "システムや対象がどのように機能するかについての概念的理解。"),
            ("COGSCI-000135", "situation_model", "状況モデル", "Situation Model", "物語・会話・場面について人物・時間・因果関係を含めて構築される心的表象。"),
            ("COGSCI-000136", "cognitive_map", "認知地図", "Cognitive Map", "空間・関係・配置について頭の中に形成される地図的表象。"),
            ("COGSCI-000137", "category_learning", "カテゴリ学習", "Category Learning", "対象を共通特徴や規則に基づいて分類できるようになる学習過程。"),
            ("COGSCI-000138", "prototype_processing", "プロトタイプ処理", "Prototype Processing", "カテゴリの典型例に基づいて対象を判断する認知過程。"),
            ("COGSCI-000139", "exemplar_processing", "事例ベース処理", "Exemplar Processing", "過去の具体的事例との類似性に基づいて判断する認知過程。"),
            ("COGSCI-000140", "concept_formation", "概念形成", "Concept Formation", "複数の経験や情報から抽象的な概念を作る認知過程。")
        ]
    },
    {
        "category": "Cognitive Science - Cognitive Load",
        "name_ja": "認知科学・認知負荷",
        "items": [
            ("COGSCI-000141", "cognitive_load", "認知負荷", "Cognitive Load", "情報処理や課題遂行に必要な認知資源の負担量。"),
            ("COGSCI-000142", "intrinsic_load", "内在的負荷", "Intrinsic Load", "課題そのものの複雑さや要素間関係によって生じる認知負荷。"),
            ("COGSCI-000143", "extraneous_load", "外在的負荷", "Extraneous Load", "不適切な表示・説明・環境によって余分に生じる認知負荷。"),
            ("COGSCI-000144", "germane_load", "学習関連負荷", "Germane Load", "理解やスキーマ構築に有効に使われる認知負荷。"),
            ("COGSCI-000145", "dual_task_interference", "二重課題干渉", "Dual Task Interference", "複数課題を同時に行うことで処理効率が低下する現象。"),
            ("COGSCI-000146", "task_demand", "課題要求", "Task Demand", "課題遂行に必要とされる注意・記憶・判断などの要求量。"),
            ("COGSCI-000147", "mental_effort", "心的努力", "Mental Effort", "課題遂行のために主観的・客観的に投入される認知的努力。"),
            ("COGSCI-000148", "processing_capacity", "処理容量", "Processing Capacity", "一定時間内に処理できる情報量や認知的資源の範囲。"),
            ("COGSCI-000149", "cognitive_fatigue", "認知疲労", "Cognitive Fatigue", "継続的な認知活動によって注意・判断・処理速度が低下する状態。"),
            ("COGSCI-000150", "load_management", "負荷管理", "Load Management", "情報量・作業量・休憩・手順を調整して認知負荷を制御する過程。")
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
        "output_dir": "vol5_cognitive_science/cognitive_science_101_150",
        "index_filename": "cognitive_science_101_150_index.yml",
        "index_content": "\n".join(index_lines) + "\n",
        "items": all_items
    }

    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(json.dumps(pack, ensure_ascii=False, indent=2), encoding="utf-8")

    print(f"Created: {OUT}")
    print(f"Items: {len(all_items)}")


if __name__ == "__main__":
    main()