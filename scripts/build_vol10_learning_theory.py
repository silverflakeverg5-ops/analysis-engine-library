import json
from pathlib import Path

OUT = Path("data/master_packs/vol10_learning_theory_001_050.json")

SECTIONS = [
    {
        "category": "Learning Theory - Core Learning",
        "name_ja": "学習理論・基本学習",
        "items": [
            ("LEARN-000001", "learning", "学習", "Learning", "経験や練習によって知識・技能・行動が変化する過程。"),
            ("LEARN-000002", "acquisition", "獲得", "Acquisition", "新しい知識・技能・反応を身につける過程。"),
            ("LEARN-000003", "retention", "保持", "Retention", "学習した内容を一定期間維持する過程。"),
            ("LEARN-000004", "retrieval_practice", "検索練習", "Retrieval Practice", "思い出す練習によって記憶保持と理解を強める学習方法。"),
            ("LEARN-000005", "spacing_effect", "分散学習効果", "Spacing Effect", "学習を時間的に分散することで保持が高まりやすい現象。"),
            ("LEARN-000006", "interleaving", "交互学習", "Interleaving", "複数の課題や内容を混ぜて学ぶことで識別や応用を高める方法。"),
            ("LEARN-000007", "overlearning", "過剰学習", "Overlearning", "一度できるようになった後も練習を続けて習熟を安定させる方法。"),
            ("LEARN-000008", "distributed_practice", "分散練習", "Distributed Practice", "練習を複数回に分けて行い、学習効率と保持を高める方法。"),
            ("LEARN-000009", "massed_practice", "集中練習", "Massed Practice", "短時間にまとめて繰り返し練習する学習方法。"),
            ("LEARN-000010", "transfer", "転移", "Transfer", "ある場面で学んだ知識や技能を別の場面へ応用すること。")
        ]
    },
    {
        "category": "Learning Theory - Feedback",
        "name_ja": "学習理論・フィードバック",
        "items": [
            ("LEARN-000011", "feedback", "フィードバック", "Feedback", "行動や成果に対して返される評価・結果・改善情報。"),
            ("LEARN-000012", "immediate_feedback", "即時フィードバック", "Immediate Feedback", "行動や回答の直後に返されるフィードバック。"),
            ("LEARN-000013", "delayed_feedback", "遅延フィードバック", "Delayed Feedback", "一定時間後に返されるフィードバック。"),
            ("LEARN-000014", "corrective_feedback", "修正フィードバック", "Corrective Feedback", "誤りの内容や正しい方向を示すフィードバック。"),
            ("LEARN-000015", "elaborated_feedback", "精緻化フィードバック", "Elaborated Feedback", "正誤だけでなく理由や考え方を含むフィードバック。"),
            ("LEARN-000016", "knowledge_of_results", "結果知識", "Knowledge of Results", "結果が正しかったか、どの程度達成できたかを示す情報。"),
            ("LEARN-000017", "knowledge_of_performance", "遂行知識", "Knowledge of Performance", "どのように行動・処理したかに関するフィードバック。"),
            ("LEARN-000018", "feedback_timing", "フィードバックタイミング", "Feedback Timing", "フィードバックを返す時点が学習に与える影響。"),
            ("LEARN-000019", "feedback_frequency", "フィードバック頻度", "Feedback Frequency", "フィードバックがどれくらい頻繁に返されるか。"),
            ("LEARN-000020", "feedback_clarity", "フィードバック明確性", "Feedback Clarity", "フィードバック内容が具体的で理解しやすい度合い。")
        ]
    },
    {
        "category": "Learning Theory - Motivation Learning",
        "name_ja": "学習理論・学習動機",
        "items": [
            ("LEARN-000021", "learning_motivation", "学習動機", "Learning Motivation", "学ぼうとする意欲や行動開始を支える動機づけ。"),
            ("LEARN-000022", "mastery_goal", "熟達目標", "Mastery Goal", "能力向上や理解の深化を重視する学習目標。"),
            ("LEARN-000023", "performance_goal", "遂行目標", "Performance Goal", "他者評価や成績で能力を示すことを重視する学習目標。"),
            ("LEARN-000024", "approach_goal", "接近目標", "Approach Goal", "成功や達成へ近づくことを重視する目標志向。"),
            ("LEARN-000025", "avoidance_goal", "回避目標", "Avoidance Goal", "失敗や低評価を避けることを重視する目標志向。"),
            ("LEARN-000026", "self_efficacy_learning", "学習自己効力感", "Learning Self Efficacy", "自分は学習課題を達成できるという見込み。"),
            ("LEARN-000027", "expectancy_value", "期待価値", "Expectancy Value", "成功できる見込みと課題の価値が動機づけを左右する考え方。"),
            ("LEARN-000028", "interest_development", "興味発達", "Interest Development", "一時的な関心が継続的な興味へ変化する過程。"),
            ("LEARN-000029", "learning_autonomy", "学習自律性", "Learning Autonomy", "自分で学習内容や方法を選び調整できる度合い。"),
            ("LEARN-000030", "learning_persistence", "学習継続", "Learning Persistence", "困難や時間経過があっても学習を続ける行動。")
        ]
    },
    {
        "category": "Learning Theory - Self Regulated Learning",
        "name_ja": "学習理論・自己調整学習",
        "items": [
            ("LEARN-000031", "self_regulated_learning", "自己調整学習", "Self Regulated Learning", "目標設定・方略選択・進捗確認・修正を自分で行う学習。"),
            ("LEARN-000032", "learning_goal_setting", "学習目標設定", "Learning Goal Setting", "学習で達成したい状態や成果を定める行動。"),
            ("LEARN-000033", "learning_planning", "学習計画", "Learning Planning", "学習内容・順序・時間配分を事前に整理する行動。"),
            ("LEARN-000034", "learning_monitoring", "学習モニタリング", "Learning Monitoring", "理解度・進捗・ミスを確認しながら学ぶ行動。"),
            ("LEARN-000035", "strategy_adjustment", "学習方略調整", "Strategy Adjustment", "学習方法が有効かを見直し、必要に応じて変更する行動。"),
            ("LEARN-000036", "help_seeking_learning", "学習援助要請", "Help Seeking in Learning", "分からない時に説明・ヒント・支援を求める学習行動。"),
            ("LEARN-000037", "self_explanation_learning", "自己説明学習", "Self Explanation Learning", "自分で理由や仕組みを説明しながら理解を深める学習方略。"),
            ("LEARN-000038", "reflection_learning", "振り返り学習", "Reflective Learning", "学習後に結果や方法を振り返り改善につなげる行動。"),
            ("LEARN-000039", "metacognitive_strategy", "メタ認知方略", "Metacognitive Strategy", "自分の理解や記憶を確認しながら学習を調整する方略。"),
            ("LEARN-000040", "learning_time_management", "学習時間管理", "Learning Time Management", "学習時間・休憩・締切を調整する行動。")
        ]
    },
    {
        "category": "Learning Theory - Instruction Design",
        "name_ja": "学習理論・教授設計",
        "items": [
            ("LEARN-000041", "instructional_design", "教授設計", "Instructional Design", "学習目標に合わせて教材・課題・支援を設計する考え方。"),
            ("LEARN-000042", "scaffolding", "足場かけ", "Scaffolding", "学習者の現在の力に合わせて支援を提供し、徐々に減らす方法。"),
            ("LEARN-000043", "worked_example", "例題学習", "Worked Example", "解法の手順が示された例を使って理解を促す学習方法。"),
            ("LEARN-000044", "guided_discovery", "ガイド付き発見学習", "Guided Discovery", "支援を受けながら自分で規則や解法を見つける学習方法。"),
            ("LEARN-000045", "direct_instruction", "直接教授", "Direct Instruction", "明確な説明・手順・練習を通じて学習を進める教授方法。"),
            ("LEARN-000046", "inquiry_learning", "探究学習", "Inquiry Learning", "問いを立て、調査・実験・考察を通じて理解を深める学習方法。"),
            ("LEARN-000047", "problem_based_learning", "問題基盤型学習", "Problem Based Learning", "現実的な問題解決を通じて知識や技能を学ぶ方法。"),
            ("LEARN-000048", "project_based_learning", "プロジェクト型学習", "Project Based Learning", "成果物や長期課題の制作を通じて学ぶ方法。"),
            ("LEARN-000049", "adaptive_learning", "適応学習", "Adaptive Learning", "学習者の状態や成績に合わせて内容や難易度を調整する学習設計。"),
            ("LEARN-000050", "personalized_learning", "個別最適化学習", "Personalized Learning", "学習者の特性・進度・興味に合わせて学習内容を調整する方法。")
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
        "output_dir": "vol10_learning_theory/learning_theory_001_050",
        "index_filename": "learning_theory_001_050_index.yml",
        "index_content": "\n".join(index_lines) + "\n",
        "items": all_items
    }

    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(json.dumps(pack, ensure_ascii=False, indent=2), encoding="utf-8")

    print(f"Created: {OUT}")
    print(f"Items: {len(all_items)}")


if __name__ == "__main__":
    main()