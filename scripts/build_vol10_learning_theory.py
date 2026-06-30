import json
from pathlib import Path

OUT = Path("data/master_packs/vol10_learning_theory_051_100.json")

SECTIONS = [
    {
        "category": "Learning Theory - Cognitive Load Learning",
        "name_ja": "学習理論・認知負荷学習",
        "items": [
            ("LEARN-000051", "cognitive_load_learning", "認知負荷学習", "Cognitive Load Learning", "学習時の情報処理負荷が理解・記憶・成績に影響する考え方。"),
            ("LEARN-000052", "intrinsic_cognitive_load_learning", "内在的認知負荷", "Intrinsic Cognitive Load", "学習内容そのものの複雑さによって生じる認知負荷。"),
            ("LEARN-000053", "extraneous_cognitive_load_learning", "外在的認知負荷", "Extraneous Cognitive Load", "教材設計や説明の分かりにくさによって余分に生じる認知負荷。"),
            ("LEARN-000054", "germane_cognitive_load_learning", "学習関連認知負荷", "Germane Cognitive Load", "理解やスキーマ形成に有効に使われる認知負荷。"),
            ("LEARN-000055", "split_attention_effect", "注意分割効果", "Split Attention Effect", "関連情報が分散して提示されることで理解負荷が高まる現象。"),
            ("LEARN-000056", "modality_effect", "モダリティ効果", "Modality Effect", "視覚と聴覚など複数チャネルを適切に使うことで学習効率が変化する現象。"),
            ("LEARN-000057", "redundancy_effect", "冗長性効果", "Redundancy Effect", "不要な重複情報がかえって理解や処理を妨げる現象。"),
            ("LEARN-000058", "worked_example_effect", "例題効果", "Worked Example Effect", "解法例を提示することで初学者の学習負荷を下げる効果。"),
            ("LEARN-000059", "expertise_reversal_effect", "熟達度逆転効果", "Expertise Reversal Effect", "初学者に有効な支援が熟達者には不要または妨げになる現象。"),
            ("LEARN-000060", "segmenting_effect", "分節化効果", "Segmenting Effect", "情報を小さなまとまりに分けて提示することで理解しやすくなる効果。")
        ]
    },
    {
        "category": "Learning Theory - Memory Learning",
        "name_ja": "学習理論・記憶学習",
        "items": [
            ("LEARN-000061", "encoding_strategy", "符号化方略", "Encoding Strategy", "情報を記憶しやすい形に変換する学習方略。"),
            ("LEARN-000062", "elaborative_rehearsal", "精緻化リハーサル", "Elaborative Rehearsal", "新しい情報を既存知識と結びつけて深く記憶する方法。"),
            ("LEARN-000063", "maintenance_rehearsal", "維持リハーサル", "Maintenance Rehearsal", "情報を繰り返して一時的に保持する方法。"),
            ("LEARN-000064", "mnemonic_strategy", "記憶術", "Mnemonic Strategy", "語呂・イメージ・場所法などを使って記憶を助ける方法。"),
            ("LEARN-000065", "dual_coding", "二重符号化", "Dual Coding", "言語情報と視覚情報を組み合わせて記憶を強める方法。"),
            ("LEARN-000066", "generation_effect", "生成効果", "Generation Effect", "与えられた情報を読むだけでなく、自分で生成することで記憶が高まりやすい現象。"),
            ("LEARN-000067", "testing_effect", "テスト効果", "Testing Effect", "再学習よりもテストや想起練習によって記憶保持が高まりやすい現象。"),
            ("LEARN-000068", "retrieval_cue", "検索手がかり", "Retrieval Cue", "記憶を思い出す助けとなる文脈・語句・画像などの手がかり。"),
            ("LEARN-000069", "forgetting_curve", "忘却曲線", "Forgetting Curve", "時間経過に伴い記憶保持率が低下する一般的傾向。"),
            ("LEARN-000070", "relearning_effect", "再学習効果", "Relearning Effect", "一度学んだ内容を再び学ぶ時に習得が速くなる現象。")
        ]
    },
    {
        "category": "Learning Theory - Skill Acquisition",
        "name_ja": "学習理論・技能習得",
        "items": [
            ("LEARN-000071", "skill_acquisition", "技能習得", "Skill Acquisition", "練習や経験によって技能が向上し自動化される過程。"),
            ("LEARN-000072", "deliberate_practice", "意図的練習", "Deliberate Practice", "明確な目標・フィードバック・弱点改善を伴う高品質な練習。"),
            ("LEARN-000073", "automaticity", "自動化", "Automaticity", "反復によって意識的負荷が少なく行動できるようになる状態。"),
            ("LEARN-000074", "fluency_development", "流暢性発達", "Fluency Development", "処理や技能が速く正確に実行できるようになる過程。"),
            ("LEARN-000075", "accuracy_speed_tradeoff_learning", "正確性速度トレードオフ学習", "Accuracy Speed Tradeoff Learning", "正確さと速さのバランスを調整しながら技能を改善する過程。"),
            ("LEARN-000076", "practice_variability", "練習変動性", "Practice Variability", "異なる条件や文脈で練習することにより適応力を高める方法。"),
            ("LEARN-000077", "blocked_practice", "ブロック練習", "Blocked Practice", "同じ種類の課題を連続して練習する方法。"),
            ("LEARN-000078", "random_practice", "ランダム練習", "Random Practice", "複数種類の課題をランダムに混ぜて練習する方法。"),
            ("LEARN-000079", "motor_skill_learning", "運動技能学習", "Motor Skill Learning", "身体動作や操作技能が練習によって向上する学習過程。"),
            ("LEARN-000080", "cognitive_skill_learning", "認知技能学習", "Cognitive Skill Learning", "判断・計算・問題解決など認知的技能が習得される過程。")
        ]
    },
    {
        "category": "Learning Theory - Social Collaborative Learning",
        "name_ja": "学習理論・社会協同学習",
        "items": [
            ("LEARN-000081", "collaborative_learning", "協同学習", "Collaborative Learning", "複数人が相互作用しながら理解や成果を高める学習方法。"),
            ("LEARN-000082", "peer_learning", "ピア学習", "Peer Learning", "同じ立場や近いレベルの学習者同士で教え合い学ぶ方法。"),
            ("LEARN-000083", "peer_tutoring", "ピアチュータリング", "Peer Tutoring", "学習者同士が教える側と学ぶ側に分かれて支援する方法。"),
            ("LEARN-000084", "reciprocal_teaching", "相互教授法", "Reciprocal Teaching", "要約・質問・予測・明確化などを交代で行い理解を深める方法。"),
            ("LEARN-000085", "cooperative_learning", "協力学習", "Cooperative Learning", "役割分担や相互依存を設計して集団で学ぶ方法。"),
            ("LEARN-000086", "discussion_learning", "討議学習", "Discussion Learning", "意見交換や議論を通じて理解を深める学習方法。"),
            ("LEARN-000087", "explanation_to_others", "他者説明学習", "Learning by Teaching", "他者に説明することで自分の理解を深める学習方法。"),
            ("LEARN-000088", "socially_shared_regulation", "社会的共有調整", "Socially Shared Regulation", "集団で目標・進捗・方略を共有しながら学習を調整する過程。"),
            ("LEARN-000089", "group_knowledge_building", "集団知識構築", "Group Knowledge Building", "複数人の知識や視点を統合して理解を発展させる過程。"),
            ("LEARN-000090", "learning_community", "学習コミュニティ", "Learning Community", "学習者同士が継続的に支援・共有・成長する集団環境。")
        ]
    },
    {
        "category": "Learning Theory - Assessment Evaluation",
        "name_ja": "学習理論・評価測定",
        "items": [
            ("LEARN-000091", "formative_assessment", "形成的評価", "Formative Assessment", "学習途中で理解度や課題を把握し改善につなげる評価。"),
            ("LEARN-000092", "summative_assessment", "総括的評価", "Summative Assessment", "学習終了時に到達度や成果を確認する評価。"),
            ("LEARN-000093", "diagnostic_assessment", "診断的評価", "Diagnostic Assessment", "学習前や途中で強み・弱み・前提知識を把握する評価。"),
            ("LEARN-000094", "criterion_referenced_assessment", "到達基準評価", "Criterion Referenced Assessment", "定められた基準に対して到達度を評価する方法。"),
            ("LEARN-000095", "norm_referenced_assessment", "相対評価", "Norm Referenced Assessment", "他者との比較に基づいて成績や位置づけを評価する方法。"),
            ("LEARN-000096", "self_assessment", "自己評価", "Self Assessment", "学習者自身が理解度・成果・課題を評価する方法。"),
            ("LEARN-000097", "peer_assessment", "相互評価", "Peer Assessment", "学習者同士が成果や行動を評価し合う方法。"),
            ("LEARN-000098", "rubric_assessment", "ルーブリック評価", "Rubric Assessment", "評価基準と水準を明示して成果を評価する方法。"),
            ("LEARN-000099", "learning_analytics", "ラーニングアナリティクス", "Learning Analytics", "学習ログや成績データを分析して学習支援に活用する方法。"),
            ("LEARN-000100", "competency_based_assessment", "コンピテンシー評価", "Competency Based Assessment", "知識だけでなく実践的能力や行動に基づいて評価する方法。")
        ]
    }
]


def make_item(item_id, slug, name_ja, name_en, definition_ja, category, parent_ja):
    return {
        "filename": f"{item_id}_{slug}.yml",
        "id": item_id,
        "knowledge_type": "learning_theory",
        "name_ja": name_ja,
        "name_en": name_en,
        "category": "Learning Theory",
        "attribute": category.replace("Learning Theory - ", ""),
        "definition_ja": definition_ja,
        "tags": ["CAT:学習理論", f"CAT:{parent_ja}", "ATTR:学習要因"],
        "parent": [parent_ja],
        "related": ["認知科学", "行動観測", "教育環境"],
        "observable_data": [
            f"{name_ja}関連正答率",
            f"{name_ja}関連継続率",
            f"{name_ja}関連改善率",
            f"{name_ja}関連反応時間"
        ],
        "signal_candidates": [
            f"{name_ja}が学習行動や成績変化に影響している可能性がある",
            "学習条件の変化に応じて行動パターンが変化する"
        ],
        "device_level": "スマホ・PCのみ推定可能",
        "modifiers": ["難易度", "フィードバック", "疲労", "動機づけ"],
        "evidence": "教育心理学・学習科学・認知科学・HCI研究で使用",
        "status": "active"
    }


def main():
    all_items = []
    index_lines = ["category: Learning Theory", "name_ja: 学習理論", "items:"]

    for section in SECTIONS:
        parent_ja = section["name_ja"].replace("学習理論・", "")
        for raw in section["items"]:
            item = make_item(*raw, category=section["category"], parent_ja=parent_ja)
            all_items.append(item)
            index_lines.append(f"  - {item['filename']}")

    index_lines.extend([
        "notes:",
        "  - 学習理論は学力判定ではなく推論材料として扱う",
        "  - 観測可能データとSignal候補を中心に管理する",
        "  - アプリ側でスコアリング・推論・表示を行う"
    ])

    pack = {
        "output_dir": "vol10_learning_theory/learning_theory_051_100",
        "index_filename": "learning_theory_051_100_index.yml",
        "index_content": "\n".join(index_lines) + "\n",
        "items": all_items
    }

    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(json.dumps(pack, ensure_ascii=False, indent=2), encoding="utf-8")

    print(f"Created: {OUT}")
    print(f"Items: {len(all_items)}")


if __name__ == "__main__":
    main()