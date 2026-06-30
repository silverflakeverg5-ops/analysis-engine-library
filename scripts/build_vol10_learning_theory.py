import json
from pathlib import Path

OUT = Path("data/master_packs/vol10_learning_theory_101_150.json")

SECTIONS = [
    {
        "category": "Learning Theory - Digital Learning",
        "name_ja": "学習理論・デジタル学習",
        "items": [
            ("LEARN-000101", "e_learning", "Eラーニング", "E Learning", "デジタル教材やオンライン環境を用いて行う学習。"),
            ("LEARN-000102", "mobile_learning", "モバイル学習", "Mobile Learning", "スマホやタブレットなど携帯端末を使って行う学習。"),
            ("LEARN-000103", "microlearning", "マイクロラーニング", "Microlearning", "短時間・小単位の教材や課題で学ぶ方法。"),
            ("LEARN-000104", "blended_learning", "ブレンド型学習", "Blended Learning", "対面学習とオンライン学習を組み合わせた学習設計。"),
            ("LEARN-000105", "flipped_learning", "反転学習", "Flipped Learning", "事前学習と授業・演習を組み合わせて理解を深める学習方法。"),
            ("LEARN-000106", "asynchronous_learning", "非同期学習", "Asynchronous Learning", "学習者が自分のタイミングで進めるオンライン学習。"),
            ("LEARN-000107", "synchronous_online_learning", "同期オンライン学習", "Synchronous Online Learning", "リアルタイムで行うオンライン授業や共同学習。"),
            ("LEARN-000108", "learning_platform_engagement", "学習プラットフォーム関与", "Learning Platform Engagement", "学習システム上でのログイン・閲覧・課題提出などの関与度。"),
            ("LEARN-000109", "digital_learning_distraction", "デジタル学習誘惑", "Digital Learning Distraction", "通知・別アプリ・動画などがデジタル学習を妨げる要因。"),
            ("LEARN-000110", "online_learning_self_management", "オンライン学習自己管理", "Online Learning Self Management", "オンライン学習で時間・進捗・集中を自分で管理する行動。")
        ]
    },
    {
        "category": "Learning Theory - Gamified Learning",
        "name_ja": "学習理論・ゲーミファイド学習",
        "items": [
            ("LEARN-000111", "gamification_learning", "ゲーミフィケーション学習", "Gamification Learning", "ポイント・バッジ・ランキングなどゲーム要素を使った学習設計。"),
            ("LEARN-000112", "point_system_learning", "ポイント制学習", "Point System Learning", "学習行動や成果にポイントを付与する設計。"),
            ("LEARN-000113", "badge_learning", "バッジ学習", "Badge Learning", "達成や技能獲得をバッジで可視化する学習設計。"),
            ("LEARN-000114", "leaderboard_learning", "ランキング学習", "Leaderboard Learning", "順位表示によって競争や動機づけを促す学習設計。"),
            ("LEARN-000115", "streak_learning", "連続記録学習", "Streak Learning", "継続日数や連続達成を可視化して学習継続を促す設計。"),
            ("LEARN-000116", "quest_based_learning", "クエスト型学習", "Quest Based Learning", "課題をクエスト形式で提示し、段階的に達成させる学習設計。"),
            ("LEARN-000117", "level_progression_learning", "レベル進行学習", "Level Progression Learning", "難易度や内容をレベル形式で段階的に進める学習方法。"),
            ("LEARN-000118", "challenge_reward_learning", "挑戦報酬学習", "Challenge Reward Learning", "挑戦課題と報酬を組み合わせて学習行動を促す設計。"),
            ("LEARN-000119", "game_feedback_loop_learning", "ゲーム型フィードバックループ学習", "Game Feedback Loop Learning", "行動・結果・報酬・再挑戦の循環で学習を促す設計。"),
            ("LEARN-000120", "playful_learning", "遊びを通じた学習", "Playful Learning", "遊びや探索を通じて自然に理解や技能を獲得する学習。")
        ]
    },
    {
        "category": "Learning Theory - Error Learning",
        "name_ja": "学習理論・エラー学習",
        "items": [
            ("LEARN-000121", "error_based_learning", "エラー基盤学習", "Error Based Learning", "誤りを手がかりに理解や技能を改善する学習過程。"),
            ("LEARN-000122", "productive_failure", "生産的失敗", "Productive Failure", "先に失敗や試行錯誤を経験することで後の理解を深める学習方法。"),
            ("LEARN-000123", "mistake_analysis", "ミス分析", "Mistake Analysis", "誤答や失敗の原因を分析して改善につなげる学習行動。"),
            ("LEARN-000124", "error_correction_learning", "エラー修正学習", "Error Correction Learning", "誤りを修正しながら正しい理解や手順を身につける学習。"),
            ("LEARN-000125", "misconception_correction", "誤概念修正", "Misconception Correction", "誤った理解や思い込みを正しい概念へ修正する学習過程。"),
            ("LEARN-000126", "debugging_learning", "デバッグ学習", "Debugging Learning", "原因特定と修正を通じて問題解決力を高める学習。"),
            ("LEARN-000127", "near_miss_learning", "ニアミス学習", "Near Miss Learning", "惜しい失敗や部分的成功を手がかりに改善する学習。"),
            ("LEARN-000128", "failure_reflection", "失敗振り返り", "Failure Reflection", "失敗後に原因・方略・次の行動を振り返る学習行動。"),
            ("LEARN-000129", "resilience_learning", "レジリエンス学習", "Resilience Learning", "失敗や困難から回復し、次の挑戦へつなげる学習過程。"),
            ("LEARN-000130", "adaptive_error_feedback", "適応的エラーフィードバック", "Adaptive Error Feedback", "誤りの種類や学習者状態に合わせて返す修正支援。")
        ]
    },
    {
        "category": "Learning Theory - Expertise Development",
        "name_ja": "学習理論・熟達化",
        "items": [
            ("LEARN-000131", "expertise_development", "熟達化", "Expertise Development", "長期的な練習と経験により高度な技能や判断力が形成される過程。"),
            ("LEARN-000132", "novice_expert_difference", "初心者熟達者差", "Novice Expert Difference", "初心者と熟達者の知識構造・注意・判断の違い。"),
            ("LEARN-000133", "domain_knowledge", "領域知識", "Domain Knowledge", "特定分野に関する専門的知識や経験。"),
            ("LEARN-000134", "pattern_chunking_expertise", "熟達者のパターンチャンク化", "Expert Pattern Chunking", "熟達者が複雑な情報を意味あるまとまりとして処理する能力。"),
            ("LEARN-000135", "expert_intuition", "熟達者直感", "Expert Intuition", "豊富な経験に基づいて素早く妥当な判断を行う能力。"),
            ("LEARN-000136", "deliberate_practice_cycle", "意図的練習サイクル", "Deliberate Practice Cycle", "目標設定・練習・フィードバック・修正を繰り返す熟達化サイクル。"),
            ("LEARN-000137", "performance_plateau", "成績停滞", "Performance Plateau", "練習を続けても成績向上が一時的に鈍化する状態。"),
            ("LEARN-000138", "expert_feedback", "熟達者フィードバック", "Expert Feedback", "熟達者から得られる具体的で高品質な改善情報。"),
            ("LEARN-000139", "mental_model_refinement", "メンタルモデル精緻化", "Mental Model Refinement", "経験や説明により対象理解の枠組みをより正確にする過程。"),
            ("LEARN-000140", "adaptive_expertise", "適応的熟達", "Adaptive Expertise", "既存技能を新しい状況に柔軟に応用できる熟達状態。")
        ]
    },
    {
        "category": "Learning Theory - Integration",
        "name_ja": "学習理論・統合",
        "items": [
            ("LEARN-000141", "learning_behavior_integration", "学習行動統合", "Learning Behavior Integration", "動機づけ・方略・環境・フィードバックを統合して学習行動を理解する枠組み。"),
            ("LEARN-000142", "learning_context_integration", "学習文脈統合", "Learning Context Integration", "教材・環境・支援・本人状態が統合して学習に影響する状態。"),
            ("LEARN-000143", "cognitive_affective_learning_integration", "認知感情学習統合", "Cognitive Affective Learning Integration", "理解・記憶・感情・動機が相互作用して学習に影響する枠組み。"),
            ("LEARN-000144", "social_learning_integration_theory", "社会的学習統合", "Social Learning Integration", "観察・協同・フィードバック・規範が学習を形成する統合的視点。"),
            ("LEARN-000145", "digital_learning_integration", "デジタル学習統合", "Digital Learning Integration", "オンライン環境・ログ・教材・支援を統合して学習を支える設計。"),
            ("LEARN-000146", "self_regulation_integration", "自己調整統合", "Self Regulation Integration", "目標設定・計画・モニタリング・修正を統合する学習過程。"),
            ("LEARN-000147", "feedback_learning_integration", "フィードバック学習統合", "Feedback Learning Integration", "結果・遂行・修正情報が学習改善に与える影響を統合する枠組み。"),
            ("LEARN-000148", "transfer_learning_integration", "転移学習統合", "Transfer Learning Integration", "学んだ知識や技能を別場面へ応用する統合的過程。"),
            ("LEARN-000149", "lifelong_learning", "生涯学習", "Lifelong Learning", "人生を通じて知識・技能・態度を継続的に更新する学習。"),
            ("LEARN-000150", "human_learning_integration", "人間学習統合", "Human Learning Integration", "認知・感情・社会・環境・生理を統合して人間の学習を理解する枠組み。")
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
        "output_dir": "vol10_learning_theory/learning_theory_101_150",
        "index_filename": "learning_theory_101_150_index.yml",
        "index_content": "\n".join(index_lines) + "\n",
        "items": all_items
    }

    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(json.dumps(pack, ensure_ascii=False, indent=2), encoding="utf-8")

    print(f"Created: {OUT}")
    print(f"Items: {len(all_items)}")


if __name__ == "__main__":
    main()