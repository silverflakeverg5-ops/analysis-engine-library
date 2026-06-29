import json
from pathlib import Path

OUT = Path("data/master_packs/vol4_cognitive_bias_extra_061_120.json")

SECTIONS = [
    {
        "category": "Cognitive Bias - Learning Reasoning Bias",
        "name_ja": "認知バイアス・学習推論バイアス",
        "items": [
            ("BIAS-000061", "belief_perseverance", "信念固執", "Belief Perseverance", "反証情報が提示されても、既存の信念や判断を維持しやすい傾向。"),
            ("BIAS-000062", "belief_bias", "信念バイアス", "Belief Bias", "論理的妥当性よりも、結論がもっともらしいかどうかで推論を評価しやすい傾向。"),
            ("BIAS-000063", "representativeness_heuristic", "代表性ヒューリスティック", "Representativeness Heuristic", "対象が典型例にどれだけ似ているかをもとに、確率や分類を判断しやすい傾向。"),
            ("BIAS-000064", "illusion_of_explanatory_depth", "説明深度の錯覚", "Illusion of Explanatory Depth", "自分が物事の仕組みを実際以上に理解していると感じやすい傾向。"),
            ("BIAS-000065", "knowledge_illusion", "知識の錯覚", "Knowledge Illusion", "外部情報や他者の知識に頼っているにもかかわらず、自分が知っていると感じやすい傾向。"),
            ("BIAS-000066", "curse_of_knowledge", "知識の呪い", "Curse of Knowledge", "自分が知っている情報を、他者も当然理解していると見なしやすい傾向。"),
            ("BIAS-000067", "fluency_effect", "流暢性効果", "Fluency Effect", "理解しやすい・処理しやすい情報を、正確・信頼できると判断しやすい傾向。"),
            ("BIAS-000068", "mere_exposure_effect", "単純接触効果", "Mere Exposure Effect", "繰り返し接触した対象に対して好意や親近感を持ちやすい傾向。"),
            ("BIAS-000069", "explanatory_coherence_bias", "説明一貫性バイアス", "Explanatory Coherence Bias", "一貫した説明や物語としてまとまる情報を、妥当だと判断しやすい傾向。"),
            ("BIAS-000070", "causal_oversimplification", "原因単純化バイアス", "Causal Oversimplification", "複雑な出来事を、少数の単純な原因で説明しようとしやすい傾向。"),
        ],
    },
    {
        "category": "Cognitive Bias - Self Evaluation Bias",
        "name_ja": "認知バイアス・自己評価バイアス",
        "items": [
            ("BIAS-000071", "dunning_kruger_effect", "ダニング＝クルーガー効果", "Dunning-Kruger Effect", "能力や知識が不足している領域で、自分の能力を過大評価しやすい傾向。"),
            ("BIAS-000072", "impostor_bias", "インポスター傾向", "Impostor Bias", "成果があっても自分の能力ではなく偶然や周囲のおかげだと感じやすい傾向。"),
            ("BIAS-000073", "spotlight_effect", "スポットライト効果", "Spotlight Effect", "自分の行動や失敗が、実際以上に他者から注目されていると感じやすい傾向。"),
            ("BIAS-000074", "transparency_illusion", "透明性の錯覚", "Illusion of Transparency", "自分の感情や考えが、実際以上に他者へ伝わっていると感じやすい傾向。"),
            ("BIAS-000075", "better_than_average_effect", "平均以上効果", "Better-than-Average Effect", "自分の能力・判断・道徳性を平均以上だと見積もりやすい傾向。"),
            ("BIAS-000076", "defensive_attribution", "防衛的帰属", "Defensive Attribution", "悪い出来事を自分から遠ざける形で原因を解釈し、自尊感情を守ろうとする傾向。"),
            ("BIAS-000077", "impact_bias", "インパクトバイアス", "Impact Bias", "将来の出来事が自分の感情に与える影響の強さや持続時間を過大評価しやすい傾向。"),
            ("BIAS-000078", "affective_forecasting_error", "感情予測誤差", "Affective Forecasting Error", "将来の自分の感情状態を正確に予測しにくい傾向。"),
            ("BIAS-000079", "projection_bias", "投影バイアス", "Projection Bias", "現在の好みや感情状態が、将来も続くと見積もりやすい傾向。"),
            ("BIAS-000080", "egocentric_bias", "自己中心性バイアス", "Egocentric Bias", "出来事や関係性を、自分の視点や貢献を中心に解釈しやすい傾向。"),
        ],
    },
    {
        "category": "Cognitive Bias - Time Planning Bias",
        "name_ja": "認知バイアス・時間計画バイアス",
        "items": [
            ("BIAS-000081", "planning_fallacy", "計画錯誤", "Planning Fallacy", "作業に必要な時間・労力・障害を過小評価し、計画を楽観的に見積もりやすい傾向。"),
            ("BIAS-000082", "time_saving_bias", "時間節約バイアス", "Time Saving Bias", "速度や効率の変化が実際の所要時間に与える影響を誤って見積もりやすい傾向。"),
            ("BIAS-000083", "procrastination_bias", "先延ばしバイアス", "Procrastination Bias", "重要だが負荷のある行動を、短期的な快適さのために後回しにしやすい傾向。"),
            ("BIAS-000084", "deadline_effect", "締切効果", "Deadline Effect", "締切が近づくまで行動開始や集中が高まりにくい傾向。"),
            ("BIAS-000085", "duration_neglect", "持続時間無視", "Duration Neglect", "経験の長さよりもピークや終了時の印象で評価しやすい傾向。"),
            ("BIAS-000086", "delay_discounting_bias", "遅延割引バイアス", "Delay Discounting Bias", "将来得られる大きな報酬より、すぐ得られる小さな報酬を選びやすい傾向。"),
            ("BIAS-000087", "fresh_start_effect", "フレッシュスタート効果", "Fresh Start Effect", "区切りのよい時点で、新しい目標や行動を始めやすくなる傾向。"),
            ("BIAS-000088", "completion_bias", "完了バイアス", "Completion Bias", "重要度よりも、すぐ完了できる小さなタスクを優先しやすい傾向。"),
            ("BIAS-000089", "switching_cost_neglect", "切替コスト無視", "Switching Cost Neglect", "タスク切替に伴う時間・注意・疲労のコストを過小評価しやすい傾向。"),
            ("BIAS-000090", "future_self_discontinuity", "未来自己の断絶", "Future Self Discontinuity", "将来の自分を現在の自分と切り離して感じ、長期的な選択を軽視しやすい傾向。"),
        ],
    },
    {
        "category": "Cognitive Bias - Information Processing Bias",
        "name_ja": "認知バイアス・情報処理バイアス",
        "items": [
            ("BIAS-000091", "information_bias", "情報バイアス", "Information Bias", "判断に必要でない情報でも、多く集めるほど良い判断ができると感じやすい傾向。"),
            ("BIAS-000092", "recency_frequency_bias", "直近頻度バイアス", "Recency Frequency Bias", "直近で頻繁に見た情報を、全体でも多い・重要だと判断しやすい傾向。"),
            ("BIAS-000093", "search_satisficing", "探索満足化", "Search Satisficing", "十分に良さそうな情報を見つけた時点で探索を止めやすい傾向。"),
            ("BIAS-000094", "information_overload_effect", "情報過負荷効果", "Information Overload Effect", "情報量が多すぎることで、判断精度や選択満足度が低下しやすい状態。"),
            ("BIAS-000095", "source_credibility_bias", "情報源信頼バイアス", "Source Credibility Bias", "情報内容よりも、発信者・媒体・肩書きの印象で信頼性を判断しやすい傾向。"),
            ("BIAS-000096", "repetition_truth_effect", "反復真実効果", "Illusory Truth Effect", "繰り返し見聞きした情報を、真実らしいと感じやすい傾向。"),
            ("BIAS-000097", "medium_bias", "媒体バイアス", "Medium Bias", "同じ内容でも、提示媒体や形式によって信頼性や重要性の評価が変わりやすい傾向。"),
            ("BIAS-000098", "visual_dominance_bias", "視覚優位バイアス", "Visual Dominance Bias", "文章や数値よりも、画像・グラフ・見た目の印象を強く重視しやすい傾向。"),
            ("BIAS-000099", "complexity_bias", "複雑性バイアス", "Complexity Bias", "単純な説明よりも、複雑で専門的に見える説明を高度だと感じやすい傾向。"),
            ("BIAS-000100", "simplicity_bias", "単純化バイアス", "Simplicity Bias", "複雑な情報を単純な分類や短い説明に置き換えて理解しようとしやすい傾向。"),
        ],
    },
    {
        "category": "Cognitive Bias - Moral Norm Bias",
        "name_ja": "認知バイアス・道徳規範バイアス",
        "items": [
            ("BIAS-000101", "moral_licensing", "モラルライセンシング", "Moral Licensing", "良い行動をした後に、多少望ましくない行動を正当化しやすくなる傾向。"),
            ("BIAS-000102", "moral_credential_effect", "道徳的資格効果", "Moral Credential Effect", "過去の良い行動や立場を根拠に、現在の判断の偏りを見えにくくする傾向。"),
            ("BIAS-000103", "just_world_bias", "公正世界仮説バイアス", "Just World Bias", "人は自分に見合った結果を受けていると考え、不運や被害を本人要因で説明しやすい傾向。"),
            ("BIAS-000104", "victim_blaming_bias", "被害者非難バイアス", "Victim Blaming Bias", "悪い出来事の被害者に対して、原因や責任を過度に帰属しやすい傾向。"),
            ("BIAS-000105", "purity_bias", "純粋性バイアス", "Purity Bias", "清潔・純粋・汚れなどの感覚的印象が、道徳判断に影響しやすい傾向。"),
            ("BIAS-000106", "ingroup_moral_bias", "内集団道徳バイアス", "Ingroup Moral Bias", "同じ集団の行動を、外集団より道徳的・正当だと評価しやすい傾向。"),
            ("BIAS-000107", "intentionality_bias", "意図性バイアス", "Intentionality Bias", "偶然や過失による出来事にも、意図や悪意を読み取りやすい傾向。"),
            ("BIAS-000108", "outcome_bias", "結果バイアス", "Outcome Bias", "判断や行動の質を、その過程ではなく結果の良し悪しで評価しやすい傾向。"),
            ("BIAS-000109", "omission_bias", "不作為バイアス", "Omission Bias", "行動して悪い結果を生むことを、何もしないで悪い結果になることより強く避けやすい傾向。"),
            ("BIAS-000110", "rule_based_bias", "ルール依存バイアス", "Rule-Based Bias", "状況や目的よりも、既存のルールや形式への適合を過度に重視しやすい傾向。"),
        ],
    },
    {
        "category": "Cognitive Bias - Digital App Response Bias",
        "name_ja": "認知バイアス・デジタル反応バイアス",
        "items": [
            ("BIAS-000111", "notification_salience_bias", "通知顕著性バイアス", "Notification Salience Bias", "通知やアラートの表示に注意が引き寄せられ、優先順位が変わりやすい傾向。"),
            ("BIAS-000112", "streak_bias", "連続記録バイアス", "Streak Bias", "連続記録や継続日数を失うことを避けるため、行動を継続しやすい傾向。"),
            ("BIAS-000113", "badge_reward_bias", "バッジ報酬バイアス", "Badge Reward Bias", "バッジ・称号・実績などの記号的報酬により、行動選択が影響されやすい傾向。"),
            ("BIAS-000114", "ranking_bias", "ランキングバイアス", "Ranking Bias", "ランキング上位の対象を、実際以上に価値が高いと判断しやすい傾向。"),
            ("BIAS-000115", "review_score_bias", "レビュー評価バイアス", "Review Score Bias", "レビュー数や星評価に判断が引き寄せられ、内容比較が浅くなりやすい傾向。"),
            ("BIAS-000116", "scarcity_urgency_bias", "希少性緊急バイアス", "Scarcity Urgency Bias", "数量限定・期限付き表示により、必要性以上に選択や購入を急ぎやすい傾向。"),
            ("BIAS-000117", "progress_bar_bias", "進捗バー効果", "Progress Bar Bias", "進捗表示によって、完了まで行動を続けやすくなる傾向。"),
            ("BIAS-000118", "autoplay_bias", "自動再生バイアス", "Autoplay Bias", "自動で次の行動が始まる設計により、停止判断が遅れやすい傾向。"),
            ("BIAS-000119", "infinite_scroll_bias", "無限スクロールバイアス", "Infinite Scroll Bias", "明確な終点がない表示により、探索や閲覧を継続しやすい傾向。"),
            ("BIAS-000120", "personalization_bias", "パーソナライズバイアス", "Personalization Bias", "自分向けに調整された情報を、実際以上に関連性・信頼性が高いと感じやすい傾向。"),
        ],
    },
]


def make_item(item_id, slug, name_ja, name_en, definition_ja, category, parent_ja):
    filename = f"{item_id}_{slug}.yml"
    return {
        "filename": filename,
        "id": item_id,
        "knowledge_type": "cognitive_bias",
        "name_ja": name_ja,
        "name_en": name_en,
        "category": "Cognitive Bias",
        "attribute": category.replace("Cognitive Bias - ", ""),
        "definition_ja": definition_ja,
        "tags": [
            "CAT:認知バイアス",
            f"CAT:{parent_ja}",
            "ATTR:判断偏り"
        ],
        "parent": [parent_ja],
        "related": [
            "意思決定",
            "情報処理",
            "行動観測"
        ],
        "observable_data": [
            f"{name_ja}関連選択率",
            f"{name_ja}関連反応時間",
            f"{name_ja}関連行動変化",
            "フィードバック後修正率"
        ],
        "signal_candidates": [
            f"{name_ja}に関連する判断の偏りが観測される",
            "条件変更後も同じ判断傾向が続く"
        ],
        "device_level": "スマホ・PCのみ推定可能",
        "modifiers": [
            "情報量",
            "時間圧",
            "疲労",
            "自信"
        ],
        "evidence": "認知心理学・行動経済学・HCI研究で使用",
        "status": "active"
    }


def main():
    all_items = []
    index_lines = [
        "category: Cognitive Bias Extra",
        "name_ja: 認知バイアス追加パック",
        "items:"
    ]

    for section in SECTIONS:
        parent_ja = section["name_ja"].replace("認知バイアス・", "")
        for raw in section["items"]:
            item = make_item(*raw, category=section["category"], parent_ja=parent_ja)
            all_items.append(item)
            index_lines.append(f"  - {item['filename']}")

    index_lines.extend([
        "notes:",
        "  - 認知バイアスは診断結果ではなく推論材料として扱う",
        "  - 観測可能データとSignal候補を中心に管理する",
        "  - アプリ側でスコアリング・推論・表示を行う"
    ])

    pack = {
        "output_dir": "vol4_cognitive_bias/cognitive_bias_extra_061_120",
        "index_filename": "cognitive_bias_extra_061_120_index.yml",
        "index_content": "\n".join(index_lines) + "\n",
        "items": all_items
    }

    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(json.dumps(pack, ensure_ascii=False, indent=2), encoding="utf-8")

    print(f"Created: {OUT}")
    print(f"Items: {len(all_items)}")


if __name__ == "__main__":
    main()