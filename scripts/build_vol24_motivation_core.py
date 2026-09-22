import json
from pathlib import Path


OUT = Path("data/master_packs/vol24_motivation_core_001_100.json")

SECTIONS = [
    ("Basic Processes", "基本過程", [
        ("motivation", "動機づけ", "Motivation", "行動を開始し方向づけ維持する過程"),
        ("motive", "動機", "Motive", "特定の行動へ向かわせる内的な理由"),
        ("drive", "動因", "Drive", "不足や緊張を低減しようとする力"),
        ("goal", "目標", "Goal", "行動が目指す将来の状態"),
        ("incentive", "誘因", "Incentive", "行動を引き出す外的な魅力や条件"),
        ("need", "欲求", "Need", "充足を求める心理的または身体的必要"),
        ("desire", "願望", "Desire", "ある結果や状態を望む主観的な強さ"),
        ("behavioral_intention", "行動意図", "Behavioral Intention", "行動を実行しようとする意思"),
        ("effort", "努力投入", "Effort", "目標達成へ投入する資源や負荷"),
        ("persistence", "持続性", "Persistence", "障害があっても行動を続ける傾向"),
    ]),
    ("Approach and Avoidance", "接近と回避", [
        ("approach_motivation", "接近動機", "Approach Motivation", "望ましい結果へ近づこうとする力"),
        ("avoidance_motivation", "回避動機", "Avoidance Motivation", "望ましくない結果から離れようとする力"),
        ("promotion_focus", "促進焦点", "Promotion Focus", "成長や獲得を重視する自己調整"),
        ("prevention_focus", "予防焦点", "Prevention Focus", "安全や損失防止を重視する自己調整"),
        ("gain_seeking", "利得追求", "Gain Seeking", "利益や好結果を得ようとする方向性"),
        ("loss_avoidance", "損失回避動機", "Loss Avoidance", "損失や悪化を防ごうとする方向性"),
        ("challenge_approach", "挑戦接近", "Challenge Approach", "難しい課題を成長機会として選ぶ方向性"),
        ("threat_avoidance", "脅威回避", "Threat Avoidance", "危険や評価低下を避ける方向性"),
        ("exploration_motivation", "探索動機", "Exploration Motivation", "未知の選択肢や情報を調べようとする力"),
        ("withdrawal_motivation", "撤退動機", "Withdrawal Motivation", "負荷の高い対象から距離を取ろうとする力"),
    ]),
    ("Self Determination", "自己決定", [
        ("intrinsic_motivation", "内発的動機づけ", "Intrinsic Motivation", "活動そのものの興味や楽しさによる動機"),
        ("extrinsic_motivation", "外発的動機づけ", "Extrinsic Motivation", "報酬や評価など外的結果による動機"),
        ("autonomy_need", "自律性欲求", "Autonomy Need", "自分で選び決めたいという心理的欲求"),
        ("competence_need", "有能感欲求", "Competence Need", "能力を発揮し上達したいという心理的欲求"),
        ("relatedness_need", "関係性欲求", "Relatedness Need", "他者とつながり受容されたいという心理的欲求"),
        ("identified_regulation", "同一化的調整", "Identified Regulation", "価値を自分で認めて行動する調整"),
        ("integrated_regulation", "統合的調整", "Integrated Regulation", "行動価値を自己の一部として統合した調整"),
        ("introjected_regulation", "取り入れ的調整", "Introjected Regulation", "罪悪感や自尊心維持に押される調整"),
        ("external_regulation", "外的調整", "External Regulation", "報酬や罰など外部統制による調整"),
        ("amotivation", "無動機", "Amotivation", "行動と結果の結びつきや意欲が弱い状態"),
    ]),
    ("Achievement", "達成", [
        ("achievement_motivation", "達成動機", "Achievement Motivation", "基準を満たし成果を上げようとする力"),
        ("mastery_goal", "熟達目標", "Mastery Goal", "理解や技能向上を目指す目標志向"),
        ("performance_approach_goal", "遂行接近目標", "Performance Approach Goal", "他者より良い成績を目指す目標志向"),
        ("performance_avoidance_goal", "遂行回避目標", "Performance Avoidance Goal", "能力不足の露呈を避ける目標志向"),
        ("task_orientation", "課題志向", "Task Orientation", "課題の達成や改善を基準にする方向性"),
        ("ego_orientation", "自我志向", "Ego Orientation", "他者との比較を基準にする方向性"),
        ("motivational_self_efficacy", "動機的自己効力感", "Motivational Self Efficacy", "必要な行動を実行できるという見込み"),
        ("outcome_expectancy", "結果期待", "Outcome Expectancy", "行動が望む結果につながるという期待"),
        ("task_value", "課題価値", "Task Value", "課題を重要または有用とみなす評価"),
        ("goal_commitment", "目標コミットメント", "Goal Commitment", "選んだ目標を維持しようとする強さ"),
    ]),
    ("Reward", "報酬", [
        ("reward_sensitivity", "報酬感受性", "Reward Sensitivity", "報酬の手がかりへ反応する度合い"),
        ("punishment_sensitivity", "罰感受性", "Punishment Sensitivity", "罰や否定的結果の手がかりへ反応する度合い"),
        ("incentive_salience", "誘因顕著性", "Incentive Salience", "報酬対象が注意と欲求を引きつける強さ"),
        ("reward_anticipation", "報酬予期", "Reward Anticipation", "将来の報酬を予想して生じる動機"),
        ("reward_learning", "報酬学習", "Reward Learning", "結果に応じて選択価値を更新する過程"),
        ("delayed_gratification", "満足遅延", "Delayed Gratification", "大きな将来報酬のため即時報酬を待つ傾向"),
        ("effort_discounting", "努力割引", "Effort Discounting", "必要努力が大きいほど報酬価値を低く見る傾向"),
        ("temporal_discounting", "時間割引", "Temporal Discounting", "受け取りが遅いほど報酬価値を低く見る傾向"),
        ("goal_gradient", "目標勾配", "Goal Gradient", "目標へ近づくほど行動が加速する傾向"),
        ("reward_satiation", "報酬飽和", "Reward Satiation", "反復した報酬の動機づけ効果が弱まる状態"),
    ]),
    ("Persistence and Regulation", "持続と調整", [
        ("grit", "グリット", "Grit", "長期目標へ情熱と努力を維持する傾向"),
        ("perseverance", "忍耐的持続", "Perseverance", "困難の中でも試行を続ける傾向"),
        ("tenacity", "粘り強さ", "Tenacity", "抵抗があっても目標から離れにくい傾向"),
        ("self_control_motivation", "自己統制動機", "Self Control Motivation", "短期衝動を抑え長期目標を守る力"),
        ("implementation_intention", "実行意図", "Implementation Intention", "状況と行動を事前に結びつける計画"),
        ("action_initiation", "行動開始", "Action Initiation", "意図を実際の最初の行動へ移す過程"),
        ("goal_reengagement", "目標再関与", "Goal Reengagement", "代替目標へ再び努力を向ける過程"),
        ("goal_disengagement", "目標離脱", "Goal Disengagement", "達成困難な目標から努力を引き上げる過程"),
        ("recovery_motivation", "回復動機", "Recovery Motivation", "低下した活動や状態を戻そうとする力"),
        ("habit_support", "習慣支援動機", "Habit Support", "反復しやすい条件によって継続を支える作用"),
    ]),
    ("Social Motives", "社会的動機", [
        ("affiliation_motivation", "親和動機", "Affiliation Motivation", "他者と良好な関係を持とうとする力"),
        ("belonging_motivation", "所属動機", "Belonging Motivation", "集団の一員として受容されようとする力"),
        ("approval_motivation", "承認動機", "Approval Motivation", "他者から肯定的評価を得ようとする力"),
        ("status_motivation", "地位動機", "Status Motivation", "集団内の地位や影響力を高めようとする力"),
        ("power_motivation", "権力動機", "Power Motivation", "他者や結果へ影響を及ぼそうとする力"),
        ("dominance_motivation", "優位動機", "Dominance Motivation", "相対的な主導権を得ようとする力"),
        ("care_motivation", "ケア動機", "Care Motivation", "他者を守り支援しようとする力"),
        ("altruistic_motivation", "利他的動機", "Altruistic Motivation", "自分の直接利益を越えて他者へ貢献する力"),
        ("reciprocity_motivation", "互恵動機", "Reciprocity Motivation", "受けた行為へ応え交換関係を保とうとする力"),
        ("recognition_motivation", "認知獲得動機", "Recognition Motivation", "成果や存在を他者に認められようとする力"),
    ]),
    ("Values and Meaning", "価値と意味", [
        ("value_congruence", "価値整合", "Value Congruence", "行動と本人の価値観が一致する度合い"),
        ("meaning_motivation", "意味動機", "Meaning Motivation", "活動に意味や一貫性を見いだそうとする力"),
        ("purpose_motivation", "目的動機", "Purpose Motivation", "長期的な目的へ行動を結びつける力"),
        ("identity_motivation", "同一性動機", "Identity Motivation", "自己像と整合する行動を選ぼうとする力"),
        ("moral_motivation", "道徳的動機", "Moral Motivation", "倫理的基準に沿って行動しようとする力"),
        ("growth_motivation", "成長動機", "Growth Motivation", "能力や理解を広げようとする力"),
        ("security_motivation", "安全動機", "Security Motivation", "安定と予測可能性を確保しようとする力"),
        ("novelty_motivation", "新奇動機", "Novelty Motivation", "新しい刺激や経験を求めようとする力"),
        ("stability_motivation", "安定維持動機", "Stability Motivation", "現在の秩序や状態を保とうとする力"),
        ("contribution_motivation", "貢献動機", "Contribution Motivation", "他者や共同体へ価値を提供しようとする力"),
    ]),
    ("Context and Dynamics", "文脈と変動", [
        ("context_dependent_motivation", "文脈依存動機", "Context Dependent Motivation", "状況や課題に応じて変わる動機"),
        ("state_motivation", "状態動機", "State Motivation", "短期的な状況によって生じる動機状態"),
        ("trait_motivation", "特性的動機", "Trait Motivation", "複数場面で比較的安定して現れる動機傾向"),
        ("motivational_intensity", "動機強度", "Motivational Intensity", "行動を駆動する力の強さ"),
        ("motivational_conflict", "動機葛藤", "Motivational Conflict", "複数の動機が競合する状態"),
        ("motivational_ambivalence", "動機的両価性", "Motivational Ambivalence", "接近と回避が同時に存在する状態"),
        ("motivational_fatigue", "動機疲労", "Motivational Fatigue", "継続負荷によって意欲が低下した状態"),
        ("motivational_recovery", "動機回復", "Motivational Recovery", "低下した意欲が再び戻る過程"),
        ("environmental_motivation_support", "環境的動機支援", "Environmental Motivation Support", "環境条件が自発性や継続を支える作用"),
        ("barrier_sensitivity", "障壁感受性", "Barrier Sensitivity", "手間や困難によって意欲が低下する度合い"),
    ]),
    ("Observation and Integration", "観測と統合", [
        ("choice_preference_signal", "選択選好シグナル", "Choice Preference Signal", "反復選択から動機候補を捉える観測概念"),
        ("effort_investment_signal", "努力投入シグナル", "Effort Investment Signal", "投入時間や試行量から動機候補を捉える観測概念"),
        ("persistence_signal", "持続シグナル", "Persistence Signal", "継続期間や中断耐性から動機候補を捉える観測概念"),
        ("retry_signal", "再試行シグナル", "Retry Signal", "失敗後の再試行から動機候補を捉える観測概念"),
        ("abandonment_signal", "離脱シグナル", "Abandonment Signal", "中断や放棄の文脈から動機候補を捉える観測概念"),
        ("optional_engagement_signal", "任意参加シグナル", "Optional Engagement Signal", "強制されない参加から自発性候補を捉える観測概念"),
        ("reward_response_signal", "報酬反応シグナル", "Reward Response Signal", "報酬前後の行動差から動機候補を捉える観測概念"),
        ("difficulty_response_signal", "難度反応シグナル", "Difficulty Response Signal", "難度変化への反応から動機候補を捉える観測概念"),
        ("motivation_profile", "動機プロファイル", "Motivation Profile", "複数の動機候補を文脈別に整理する枠組み"),
        ("motivation_core_integration", "動機コア統合", "Motivation Core Integration", "動機・観測・補正・根拠を安全に接続する枠組み"),
    ]),
]


def make_item(item_id, slug, name_ja, name_en, focus, section_en, section_ja):
    return {
        "filename": f"{item_id}_{slug}.yml",
        "id": item_id,
        "knowledge_type": "motivation_core",
        "name_ja": name_ja,
        "name_en": name_en,
        "category": "Motivation Core",
        "attribute": section_en,
        "definition_ja": f"{name_ja}は、{focus}を表す動機づけ概念。単独で人格や特性を断定しない。",
        "tags": ["CAT:動機づけ", f"CAT:{section_ja}", "ATTR:動機要因"],
        "parent": [section_ja],
        "related": ["行動観測", "目標選択", "文脈依存性"],
        "observable_data": ["選択頻度", "開始までの時間", "努力投入量", "継続と離脱の推移"],
        "signal_candidates": [
            f"{name_ja}と整合する選択や努力が複数場面で観測される",
            "報酬・難度・時間制約の変化に伴って行動量が変化する",
        ],
        "device_level": "スマートフォン・PC・ゲーム機の行動ログから観測可能",
        "modifiers": ["疲労", "睡眠", "ストレス", "報酬設計", "課題難度", "社会的文脈"],
        "evidence": "動機づけ心理学・自己決定理論・目標理論・行動科学の研究を参照",
        "status": "active",
    }


def main():
    items = []
    index_lines = ["category: Motivation Core", "name_ja: 動機づけコア", "items:"]
    number = 1
    for section_en, section_ja, definitions in SECTIONS:
        for slug, name_ja, name_en, focus in definitions:
            item_id = f"MOT-{number:06d}"
            item = make_item(item_id, slug, name_ja, name_en, focus, section_en, section_ja)
            items.append(item)
            index_lines.append(f"  - {item['filename']}")
            number += 1

    if len(items) != 100:
        raise ValueError(f"Expected 100 items, got {len(items)}")

    index_lines.extend([
        "notes:",
        "  - 動機づけコアは推論材料であり、人格や性格を単独で断定しない",
        "  - 単一シグナルではなく複数場面・時間変化・Modifierを組み合わせる",
        "  - アプリ側で目的に応じた重み付けと安全な表示を行う",
    ])
    pack = {
        "output_dir": "vol24_motivation_core/motivation_core_001_100",
        "index_filename": "motivation_core_001_100_index.yml",
        "index_content": "\n".join(index_lines) + "\n",
        "items": items,
    }
    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(json.dumps(pack, ensure_ascii=False, indent=2), encoding="utf-8")
    print(f"Created: {OUT}")
    print(f"Items: {len(items)}")


if __name__ == "__main__":
    main()
