"""Build the Vol29 Development and Life Stage master pack (DEV-000001..000100)."""

from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "data" / "master_packs" / "vol29_development_001_100.json"


SECTIONS = [
    ("Lifespan Foundations", "生涯発達基盤", [
        ("developmental_change", "発達的変化", "Developmental Change", "時間・経験・環境に伴って行動や方略が変化する過程"),
        ("individual_variability", "発達個人差", "Individual Variability", "変化の時期・速度・方向が個人ごとに異なること"),
        ("multidirectionality", "発達多方向性", "Multidirectionality", "ある側面の成長と別側面の維持・変化が同時に起こりうること"),
        ("contextual_plasticity", "文脈的可塑性", "Contextual Plasticity", "支援・練習・環境変更に応じて方略が変わりうること"),
        ("cumulative_experience", "累積経験", "Cumulative Experience", "過去の経験が後の選択や学習へ積み重なって影響すること"),
        ("cohort_context", "コホート文脈", "Cohort Context", "同時代の教育・技術・社会経験が行動文脈を形づくること"),
        ("historical_context", "歴史的文脈", "Historical Context", "社会的出来事や制度変化が発達経路へ影響すること"),
        ("timing_of_experience", "経験時機", "Timing of Experience", "経験する時期によって意味や影響が異なりうること"),
        ("continuity_discontinuity", "連続性と非連続性", "Continuity and Discontinuity", "段階的変化と転機による変化の両方を扱うこと"),
        ("person_environment_transaction", "人間環境相互作用", "Person-Environment Transaction", "本人の行動と環境反応が相互に発達経路を作ること"),
    ]),
    ("Learning and Skill Growth", "学習と技能成長", [
        ("foundational_skill_growth", "基礎技能成長", "Foundational Skill Growth", "反復経験を通じて基礎的な技能が形成・更新される過程"),
        ("guided_participation", "導かれた参加", "Guided Participation", "他者と活動へ参加しながら役割や技能を学ぶ過程"),
        ("scaffolding_response", "足場かけ応答", "Scaffolding Response", "一時的な支援を使って未習熟な課題へ取り組む過程"),
        ("practice_adaptation", "練習適応", "Practice Adaptation", "成果や難易度に応じて練習方法を調整する過程"),
        ("strategy_development", "方略発達", "Strategy Development", "経験に応じて課題解決の方法を増やし選び分ける過程"),
        ("metacognitive_growth", "メタ認知成長", "Metacognitive Growth", "自分の理解・誤り・学習方法を捉え直す過程"),
        ("expertise_progression", "熟達進行", "Expertise Progression", "領域経験により知識構造と判断方略が変化する過程"),
        ("transfer_growth", "転移能力成長", "Transfer Growth", "学んだ知識や技能を新しい場面へ適用できる範囲が広がる過程"),
        ("feedback_use_development", "フィードバック活用発達", "Feedback Use Development", "結果や助言を次の試行へ反映する方法が変化する過程"),
        ("lifelong_learning_orientation", "生涯学習志向", "Lifelong Learning Orientation", "生活段階を通じて新しい知識や技能へ関わり続ける傾向"),
    ]),
    ("Self-Regulation and Autonomy", "自己調整と自律", [
        ("co_regulation", "共同調整", "Co-Regulation", "他者の支援を利用しながら行動や感情を調整する過程"),
        ("self_regulation_growth", "自己調整成長", "Self-Regulation Growth", "目標に合わせて注意・感情・行動を調整する方法が増える過程"),
        ("impulse_management_growth", "衝動管理成長", "Impulse Management Growth", "即時反応と長期目標を状況に応じて調整する過程"),
        ("emotion_regulation_growth", "感情調整成長", "Emotion Regulation Growth", "感情を理解し表現・回復方法を選べる範囲が変化する過程"),
        ("attention_regulation_growth", "注意調整成長", "Attention Regulation Growth", "課題や環境に応じて注意を向け直す方略が変化する過程"),
        ("planning_independence", "計画自立性", "Planning Independence", "支援の量を調整しながら自ら計画を立てる過程"),
        ("responsibility_assumption", "責任引受け", "Responsibility Assumption", "役割に伴う課題や結果への責任範囲を広げる過程"),
        ("help_seeking_independence", "自律的援助要請", "Independent Help Seeking", "必要な支援を自ら判断して適切な相手へ求める過程"),
        ("autonomy_support_response", "自律支援応答", "Autonomy Support Response", "選択機会や理由説明のある支援を活用する過程"),
        ("dependency_autonomy_balance", "依存自律均衡", "Dependency-Autonomy Balance", "自力で行う範囲と他者に頼る範囲を調整する過程"),
    ]),
    ("Identity and Values", "アイデンティティと価値", [
        ("self_concept_development", "自己概念発達", "Self-Concept Development", "経験や他者との関係から自分についての理解を更新する過程"),
        ("identity_exploration", "アイデンティティ探索", "Identity Exploration", "自分に合う役割・価値・所属の可能性を試す過程"),
        ("identity_commitment", "アイデンティティ確立", "Identity Commitment", "検討した役割や価値へ一定の関与を形成する過程"),
        ("value_clarification_development", "価値明確化発達", "Value Clarification Development", "経験を通じて大切にする基準を言語化し直す過程"),
        ("role_identity_integration", "役割同一性統合", "Role Identity Integration", "複数の社会的役割を自己理解の中で調整する過程"),
        ("narrative_identity_development", "物語的自己発達", "Narrative Identity Development", "過去・現在・将来の経験を自己の物語として結び直す過程"),
        ("possible_self_construction", "可能自己構築", "Possible Self Construction", "将来なりうる自分や避けたい自分を思い描く過程"),
        ("belonging_identity", "所属同一性", "Belonging Identity", "集団や地域への所属を自己理解へ位置づける過程"),
        ("identity_transition", "アイデンティティ移行", "Identity Transition", "生活変化に応じて自己理解や役割の位置づけを更新する過程"),
        ("identity_flexibility", "アイデンティティ柔軟性", "Identity Flexibility", "一貫性を保ちながら新しい経験に合わせて自己理解を修正する過程"),
    ]),
    ("Social and Relationship Growth", "社会性と関係成長", [
        ("trust_development", "信頼形成発達", "Trust Development", "反復的な相互作用を通じて信頼の置き方を学ぶ過程"),
        ("reciprocity_growth", "互恵性成長", "Reciprocity Growth", "与える・受け取る・返す関係を状況に応じて調整する過程"),
        ("perspective_taking_growth", "視点取得成長", "Perspective Taking Growth", "他者の知識・感情・立場を考慮する範囲が広がる過程"),
        ("friendship_development", "友人関係発達", "Friendship Development", "親密さ・共有・相互支援を伴う友人関係を築き直す過程"),
        ("intimacy_development", "親密性発達", "Intimacy Development", "安全な自己開示と相互理解を調整する過程"),
        ("boundary_development", "対人境界発達", "Boundary Development", "自他の権利・負担・プライバシーの境界を調整する過程"),
        ("conflict_skill_growth", "葛藤技能成長", "Conflict Skill Growth", "不一致を表現・交渉・修復する方法を増やす過程"),
        ("social_role_learning", "社会的役割学習", "Social Role Learning", "集団内の期待や責任を経験から学ぶ過程"),
        ("community_participation_growth", "共同体参加成長", "Community Participation Growth", "地域や集団での参加方法と責任範囲を変化させる過程"),
        ("support_network_development", "支援ネットワーク発達", "Support Network Development", "必要な支援を得られる関係を形成・維持・更新する過程"),
    ]),
    ("Roles and Life Transitions", "役割と生活移行", [
        ("transition_anticipation", "移行予期", "Transition Anticipation", "今後の生活変化を見越して情報や資源を準備する過程"),
        ("role_entry", "役割参入", "Role Entry", "新しい役割の規範・技能・関係を学ぶ過程"),
        ("role_exit", "役割離脱", "Role Exit", "終えた役割から責任・習慣・自己理解を切り替える過程"),
        ("role_conflict_transition", "役割葛藤移行", "Role Conflict Transition", "複数役割の要求が衝突する時に優先順位を組み替える過程"),
        ("routine_reconstruction", "生活習慣再構成", "Routine Reconstruction", "環境や役割の変化に合わせて日課を作り直す過程"),
        ("relocation_adaptation", "転居適応", "Relocation Adaptation", "居住環境の変化に応じて関係・習慣・資源利用を再構成する過程"),
        ("education_transition", "教育移行", "Education Transition", "学習環境や教育段階の変化へ適応する過程"),
        ("work_transition", "仕事移行", "Work Transition", "就業・転職・退職などに伴い技能・役割・生活を調整する過程"),
        ("relationship_transition", "関係移行", "Relationship Transition", "関係の開始・変化・終了に応じて期待と境界を更新する過程"),
        ("caregiving_transition", "ケア役割移行", "Caregiving Transition", "養育・介護・支援役割の開始や変化へ適応する過程"),
    ]),
    ("Purpose Work and Contribution", "目的・仕事・貢献", [
        ("interest_pathway_development", "興味経路発達", "Interest Pathway Development", "接触・試行・経験を通じて関心分野が形成される過程"),
        ("competence_pathway", "有能感経路", "Competence Pathway", "技能の獲得と周囲の反応から得意分野の理解を更新する過程"),
        ("vocational_exploration", "職業探索", "Vocational Exploration", "仕事や活動領域の可能性を調べ試す過程"),
        ("career_identity", "キャリア同一性", "Career Identity", "仕事・学習・生活役割を自己理解へ位置づける過程"),
        ("goal_horizon_change", "目標時間軸変化", "Goal Horizon Change", "生活文脈に応じて短期と長期の目標配分を変える過程"),
        ("purpose_development", "目的意識発達", "Purpose Development", "自分にとって意味があり他者や社会にもつながる方向性を形成する過程"),
        ("generativity_expression", "次世代貢献表現", "Generativity Expression", "知識・支援・資源を次の世代や共同体へ渡す過程"),
        ("mentoring_role", "メンタリング役割", "Mentoring Role", "経験を共有し他者の成長を支援する役割を担う過程"),
        ("contribution_orientation", "貢献志向", "Contribution Orientation", "活動が他者・組織・社会へ与える価値を考慮する過程"),
        ("role_mastery", "役割熟達", "Role Mastery", "役割経験を通じて判断・技能・協働方法を洗練する過程"),
    ]),
    ("Adaptation and Resilience", "適応とレジリエンス", [
        ("change_readiness_development", "変化準備性発達", "Change Readiness Development", "変化に備えて情報・技能・支援を整える方法が増える過程"),
        ("coping_repertoire_growth", "対処レパートリー成長", "Coping Repertoire Growth", "負担へ対処する方法を増やし使い分ける過程"),
        ("recovery_learning", "回復学習", "Recovery Learning", "疲労やストレス後の経験から回復条件を学ぶ過程"),
        ("resource_mobilization", "資源動員", "Resource Mobilization", "変化に必要な知識・時間・支援・制度を利用する過程"),
        ("support_use_adaptation", "支援利用適応", "Support Use Adaptation", "状況変化に合わせて支援の種類や利用方法を変える過程"),
        ("meaning_making_after_change", "変化後意味形成", "Meaning Making After Change", "大きな変化を自己理解や将来像へ位置づけ直す過程"),
        ("setback_reappraisal", "挫折再評価", "Setback Reappraisal", "期待外の結果を別の視点から評価し次の行動へつなげる過程"),
        ("adaptation_pacing", "適応速度調整", "Adaptation Pacing", "負担と資源に合わせて変化への取り組み速度を調整する過程"),
        ("stability_change_balance", "安定変化均衡", "Stability-Change Balance", "維持したい要素と変える要素を選び分ける過程"),
        ("resilience_development_context", "レジリエンス発達文脈", "Resilience Development Context", "回復や適応が個人だけでなく環境・関係・資源との相互作用で変わること"),
    ]),
    ("Later Life and Aging Context", "加齢と後期生活文脈", [
        ("experience_based_compensation", "経験基盤補償", "Experience-Based Compensation", "経験や道具を使って変化した機能や状況を補う過程"),
        ("selective_goal_focus", "選択的目標集中", "Selective Goal Focus", "限られた時間や資源を重要な目標へ集中する過程"),
        ("resource_prioritization", "資源優先配分", "Resource Prioritization", "体力・時間・注意を価値の高い活動へ配分する過程"),
        ("routine_continuity", "生活連続性", "Routine Continuity", "変化の中でも本人にとって重要な習慣や役割を維持する過程"),
        ("technology_adaptation_across_life", "生涯技術適応", "Technology Adaptation Across Life", "経験や利用目的に応じて新しい技術の使い方を学ぶ過程"),
        ("health_context_adaptation", "健康文脈適応", "Health Context Adaptation", "健康状態や利用可能な支援に合わせて活動方法を調整する過程"),
        ("social_network_selectivity", "社会関係選択性", "Social Network Selectivity", "関係の質・目的・負担に応じて交流を選択する過程"),
        ("life_review", "人生回顧", "Life Review", "過去の経験を振り返り意味やつながりを再構成する過程"),
        ("legacy_orientation", "レガシー志向", "Legacy Orientation", "知識・作品・関係・価値を将来へ残すことに関わる過程"),
        ("age_stereotype_resistance", "年齢ステレオタイプ抵抗", "Age Stereotype Resistance", "年齢に基づく固定的期待と本人の実際の能力や希望を分ける過程"),
    ]),
    ("Observation and Integration", "観測と統合", [
        ("longitudinal_change_signal", "縦断変化シグナル", "Longitudinal Change Signal", "同意済みの複数時点データから変化と安定を捉える観測概念"),
        ("skill_trajectory_signal", "技能軌跡シグナル", "Skill Trajectory Signal", "試行・支援・成果の時系列から技能変化を捉える観測概念"),
        ("role_transition_signal", "役割移行シグナル", "Role Transition Signal", "明示された役割変更前後の行動文脈を捉える観測概念"),
        ("autonomy_change_signal", "自律変化シグナル", "Autonomy Change Signal", "支援利用と独立遂行の配分変化を捉える観測概念"),
        ("identity_expression_change_signal", "自己表現変化シグナル", "Identity Expression Change Signal", "明示的な自己記述・目標・役割表現の変化を捉える観測概念"),
        ("relationship_pattern_change_signal", "関係パターン変化シグナル", "Relationship Pattern Change Signal", "同意された交流データから関係行動の変化を捉える観測概念"),
        ("developmental_context_dependency", "発達文脈依存性", "Developmental Context Dependency", "環境・機会・役割・健康状態により変化の意味が異なること"),
        ("cohort_context_modifier", "コホート文脈補正", "Cohort Context Modifier", "時代・教育・技術経験の違いを比較時に補正する枠組み"),
        ("developmental_profile", "発達文脈プロファイル", "Developmental Context Profile", "複数時点の変化と生活文脈を領域別に整理する枠組み"),
        ("developmental_integration", "発達情報統合", "Developmental Information Integration", "観測・補正・本人申告・根拠を安全に接続する統合枠組み"),
    ]),
]


def make_item(item_id, slug, name_ja, name_en, focus, section_en, section_ja):
    return {
        "filename": f"{item_id}_{slug}.yml",
        "id": item_id,
        "knowledge_type": "development_core",
        "name_ja": name_ja,
        "name_en": name_en,
        "category": "Development and Life Stage",
        "attribute": section_en,
        "definition_ja": f"{name_ja}は、{focus}を表す生涯発達概念。年齢や段階だけから能力・成熟度・人格を断定しない。",
        "tags": ["CAT:発達・ライフステージ", f"CAT:{section_ja}", "ATTR:発達文脈"],
        "parent": [section_ja],
        "related": ["生涯発達", "生活文脈", "時系列観測"],
        "observable_data": ["本人同意に基づく複数時点の行動記録", "明示回答された役割・目標・生活変化", "学習・支援利用・成果の時系列", "本人が選択した振り返り記録"],
        "signal_candidates": [
            f"{name_ja}と整合する変化または安定が複数時点で観測される",
            "環境・機会・文化・健康・役割の変化に伴って行動パターンが変化する",
        ],
        "device_level": "同意済みの縦断イベントログと明示的な自己申告から観測し、行動ログだけで年齢や発達段階を推定しない",
        "modifiers": ["文化・地域", "教育・経験機会", "社会経済的資源", "健康・障害・神経多様性", "家族・支援関係", "生活役割", "コホート・時代", "重大な生活変化"],
        "evidence": "生涯発達心理学・教育心理学・社会心理学・老年学・ライフコース研究・HCI研究を参照",
        "status": "active",
    }


def main():
    items = []
    index_lines = ["category: Development and Life Stage", "name_ja: 発達・ライフステージ", "items:"]
    number = 1
    for section_en, section_ja, definitions in SECTIONS:
        for slug, name_ja, name_en, focus in definitions:
            item_id = f"DEV-{number:06d}"
            item = make_item(item_id, slug, name_ja, name_en, focus, section_en, section_ja)
            items.append(item)
            index_lines.append(f"  - {item['filename']}")
            number += 1
    if len(items) != 100:
        raise ValueError(f"Expected 100 items, got {len(items)}")
    index_lines.extend([
        "notes:",
        "  - 年齢・世代・発達段階だけから能力、成熟度、人格、健康状態を断定しない",
        "  - 発達は多方向で個人差が大きく、文化・機会・健康・役割・時代のModifierを必ず考慮する",
        "  - 行動ログから年齢や敏感な生活段階を推定せず、本人の同意と明示申告を優先する",
        "  - 採用・教育選抜・保険・医療など高影響領域の自動判定には直接利用しない",
    ])
    pack = {
        "output_dir": "vol29_development/development_001_100",
        "index_filename": "development_001_100_index.yml",
        "index_content": "\n".join(index_lines) + "\n",
        "items": items,
    }
    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(json.dumps(pack, ensure_ascii=False, indent=2), encoding="utf-8")
    print(f"Created: {OUT}")
    print(f"Items: {len(items)}")


if __name__ == "__main__":
    main()
