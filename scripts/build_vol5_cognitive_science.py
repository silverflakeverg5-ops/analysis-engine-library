import json
from pathlib import Path

OUT = Path("data/master_packs/vol5_cognitive_science_051_100.json")

SECTIONS = [
    {
        "category": "Cognitive Science - Problem Solving",
        "name_ja": "認知科学・問題解決",
        "items": [
            ("COGSCI-000051", "problem_solving", "問題解決", "Problem Solving", "目標と現状の差を埋めるために方略を選び実行する認知過程。"),
            ("COGSCI-000052", "means_end_analysis", "手段目的分析", "Means End Analysis", "目標状態と現在状態の差を分析し、必要な手段を選ぶ問題解決方略。"),
            ("COGSCI-000053", "problem_representation", "問題表象", "Problem Representation", "問題の構造・条件・制約を心的に表現する認知過程。"),
            ("COGSCI-000054", "strategy_selection", "方略選択", "Strategy Selection", "課題や状況に応じて有効な解決方法を選ぶ認知過程。"),
            ("COGSCI-000055", "heuristic_search", "ヒューリスティック探索", "Heuristic Search", "完全探索ではなく経験則や近道を使って解を探す認知過程。"),
            ("COGSCI-000056", "insight_problem_solving", "洞察的問題解決", "Insight Problem Solving", "突然の気づきや再構成によって解決に至る問題解決過程。"),
            ("COGSCI-000057", "constraint_relaxation", "制約緩和", "Constraint Relaxation", "固定観念や制約を緩めることで新しい解を見つける認知過程。"),
            ("COGSCI-000058", "analogical_reasoning", "類推推論", "Analogical Reasoning", "既知の事例や構造を別の問題へ対応づけて考える推論過程。"),
            ("COGSCI-000059", "debugging_behavior", "デバッグ的思考", "Debugging Thinking", "誤りの原因を特定し、仮説検証しながら修正する思考過程。"),
            ("COGSCI-000060", "solution_evaluation", "解決策評価", "Solution Evaluation", "導いた解決策の妥当性・効果・リスクを評価する認知過程。")
        ]
    },
    {
        "category": "Cognitive Science - Language",
        "name_ja": "認知科学・言語",
        "items": [
            ("COGSCI-000061", "language_comprehension", "言語理解", "Language Comprehension", "文字や音声として提示された言語情報の意味を理解する認知過程。"),
            ("COGSCI-000062", "reading_comprehension", "読解", "Reading Comprehension", "文章の内容・構造・意図を読み取り理解する認知過程。"),
            ("COGSCI-000063", "semantic_processing", "意味処理", "Semantic Processing", "語句や文の意味を解釈し、既存知識と結びつける認知過程。"),
            ("COGSCI-000064", "pragmatic_understanding", "語用理解", "Pragmatic Understanding", "文脈や相手の意図を踏まえて発話の意味を理解する認知過程。"),
            ("COGSCI-000065", "verbal_fluency", "言語流暢性", "Verbal Fluency", "条件に合う語や表現を素早く生成する認知機能。"),
            ("COGSCI-000066", "narrative_understanding", "物語理解", "Narrative Understanding", "出来事の因果関係や登場人物の意図を含めて物語を理解する認知過程。"),
            ("COGSCI-000067", "instruction_following", "指示理解", "Instruction Following", "言語的な指示を理解し、適切な行動に変換する認知過程。"),
            ("COGSCI-000068", "ambiguity_resolution", "曖昧性解消", "Ambiguity Resolution", "複数の意味や解釈がある情報から、文脈に合う解釈を選ぶ認知過程。"),
            ("COGSCI-000069", "metaphor_understanding", "比喩理解", "Metaphor Understanding", "比喩や象徴表現を、文脈や類似性をもとに理解する認知過程。"),
            ("COGSCI-000070", "dialogue_context_tracking", "対話文脈追跡", "Dialogue Context Tracking", "会話の流れ・前提・相手の意図を追跡しながら理解する認知過程。")
        ]
    },
    {
        "category": "Cognitive Science - Social Cognition",
        "name_ja": "認知科学・社会的認知",
        "items": [
            ("COGSCI-000071", "theory_of_mind", "心の理論", "Theory of Mind", "他者の信念・意図・感情などの心的状態を推測する認知機能。"),
            ("COGSCI-000072", "perspective_taking", "視点取得", "Perspective Taking", "自分とは異なる他者の立場や視点から状況を理解する認知機能。"),
            ("COGSCI-000073", "empathy_processing", "共感処理", "Empathy Processing", "他者の感情状態を理解し、それに反応する認知情動過程。"),
            ("COGSCI-000074", "social_inference", "社会的推論", "Social Inference", "他者の行動や状況から意図・関係・規範を推測する認知過程。"),
            ("COGSCI-000075", "trait_inference", "特性推論", "Trait Inference", "他者の行動から性格や傾向を推測する認知過程。"),
            ("COGSCI-000076", "emotion_recognition", "感情認識", "Emotion Recognition", "表情・声・言語・行動から感情状態を認識する認知機能。"),
            ("COGSCI-000077", "social_norm_processing", "社会規範処理", "Social Norm Processing", "集団や場面における暗黙のルールや期待を理解する認知過程。"),
            ("COGSCI-000078", "reputation_processing", "評判処理", "Reputation Processing", "他者や自分に関する評価・信頼・評判情報を処理する認知過程。"),
            ("COGSCI-000079", "trust_judgment", "信頼判断", "Trust Judgment", "相手や情報源をどの程度信頼できるか判断する認知過程。"),
            ("COGSCI-000080", "cooperation_reasoning", "協力推論", "Cooperation Reasoning", "協力・裏切り・相互利益に関する相手の行動を推測する認知過程。")
        ]
    },
    {
        "category": "Cognitive Science - Metacognition",
        "name_ja": "認知科学・メタ認知",
        "items": [
            ("COGSCI-000081", "metacognition", "メタ認知", "Metacognition", "自分の認知状態・理解度・判断の確かさを把握する認知機能。"),
            ("COGSCI-000082", "confidence_judgment", "確信度判断", "Confidence Judgment", "自分の回答や判断がどの程度正しいか見積もる認知過程。"),
            ("COGSCI-000083", "error_awareness", "エラー自覚", "Error Awareness", "自分の誤りやズレに気づく認知機能。"),
            ("COGSCI-000084", "learning_monitoring", "学習モニタリング", "Learning Monitoring", "自分の理解度や習得状況を確認しながら学習する認知過程。"),
            ("COGSCI-000085", "strategy_monitoring", "方略モニタリング", "Strategy Monitoring", "現在使っている方略が有効かどうか確認する認知過程。"),
            ("COGSCI-000086", "judgment_of_learning", "学習判断", "Judgment of Learning", "あとで思い出せるか、理解できているかを予測するメタ認知判断。"),
            ("COGSCI-000087", "feeling_of_knowing", "既知感", "Feeling of Knowing", "今は思い出せなくても知っていると感じるメタ認知的感覚。"),
            ("COGSCI-000088", "calibration", "キャリブレーション", "Calibration", "自信度と実際の正確性がどの程度一致しているかを示す概念。"),
            ("COGSCI-000089", "self_explanation", "自己説明", "Self Explanation", "自分で理由や仕組みを説明しながら理解を深める学習方略。"),
            ("COGSCI-000090", "reflection", "振り返り", "Reflection", "過去の行動や結果を見直し、理解や改善につなげる認知過程。")
        ]
    },
    {
        "category": "Cognitive Science - Perception",
        "name_ja": "認知科学・知覚",
        "items": [
            ("COGSCI-000091", "visual_perception", "視覚知覚", "Visual Perception", "形・色・動き・位置などの視覚情報を処理する認知機能。"),
            ("COGSCI-000092", "auditory_perception", "聴覚知覚", "Auditory Perception", "音の高さ・強さ・方向・意味を処理する認知機能。"),
            ("COGSCI-000093", "pattern_recognition", "パターン認識", "Pattern Recognition", "情報の中から規則性・構造・まとまりを検出する認知機能。"),
            ("COGSCI-000094", "object_recognition", "物体認識", "Object Recognition", "視覚情報から対象物を識別し意味づける認知機能。"),
            ("COGSCI-000095", "spatial_perception", "空間知覚", "Spatial Perception", "位置関係・距離・方向などの空間情報を把握する認知機能。"),
            ("COGSCI-000096", "temporal_perception", "時間知覚", "Temporal Perception", "時間の長さ・順序・タイミングを感じ取る認知機能。"),
            ("COGSCI-000097", "multisensory_integration", "多感覚統合", "Multisensory Integration", "視覚・聴覚・触覚など複数の感覚情報を統合する認知過程。"),
            ("COGSCI-000098", "perceptual_grouping", "知覚的群化", "Perceptual Grouping", "近接・類似・連続性などに基づいて情報をまとまりとして知覚する過程。"),
            ("COGSCI-000099", "signal_detection", "信号検出", "Signal Detection", "ノイズの中から意味のある刺激や変化を検出する認知過程。"),
            ("COGSCI-000100", "perceptual_learning", "知覚学習", "Perceptual Learning", "経験により知覚判断や識別能力が改善する学習過程。")
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
        "output_dir": "vol5_cognitive_science/cognitive_science_051_100",
        "index_filename": "cognitive_science_051_100_index.yml",
        "index_content": "\n".join(index_lines) + "\n",
        "items": all_items
    }

    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(json.dumps(pack, ensure_ascii=False, indent=2), encoding="utf-8")

    print(f"Created: {OUT}")
    print(f"Items: {len(all_items)}")


if __name__ == "__main__":
    main()