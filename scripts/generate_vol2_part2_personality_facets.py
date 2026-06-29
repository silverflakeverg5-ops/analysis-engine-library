from pathlib import Path

BASE = Path("data/vol2_personality/facets")
BASE.mkdir(parents=True, exist_ok=True)

files = {
    "FAC-000001_sociability.yml": """id: FAC-000001
knowledge_type: trait
name_ja: 社交性
name_en: Sociability
category: Personality Facet
attribute: Trait
definition_ja: 他者との交流を好み、対人場面へ関わろうとする傾向。
tags:
  - CAT:性格
  - THEORY:BigFive
  - ATTR:特性
parent:
  - 外向性
related:
  - 会話量
  - 交流傾向
  - 協調性
observable_data:
  - 会話回数
  - 返信頻度
  - 交流選択
signal_candidates:
  - 対人接点を選びやすい
  - 他者への反応が多い
device_level: スマホ・PCのみ推定可能
modifiers:
  - 文化
  - 環境
  - 気分
evidence: Big Five外向性の下位特性として利用
status: active
""",

    "FAC-000002_assertiveness.yml": """id: FAC-000002
knowledge_type: trait
name_ja: 自己主張
name_en: Assertiveness
category: Personality Facet
attribute: Trait
definition_ja: 自分の意見や意図を表明し、状況へ能動的に働きかける傾向。
tags:
  - CAT:性格
  - THEORY:BigFive
  - ATTR:特性
parent:
  - 外向性
related:
  - 主導性
  - 影響力
  - 支配性
observable_data:
  - 提案回数
  - 主導的選択
  - 発言量
signal_candidates:
  - 自分から行動を始める
  - 選択を主導する
device_level: スマホ・PCのみ推定可能
modifiers:
  - 社会環境
  - 文化
  - 評価状況
evidence: 性格特性・対人行動評価で使用
status: active
""",

    "FAC-000003_curiosity.yml": """id: FAC-000003
knowledge_type: trait
name_ja: 好奇心
name_en: Curiosity
category: Personality Facet
attribute: Trait
definition_ja: 新しい情報・経験・選択肢へ関心を持ち、探索しようとする傾向。
tags:
  - CAT:性格
  - THEORY:BigFive
  - ATTR:特性
parent:
  - 開放性
related:
  - 探索志向
  - 学習意欲
  - 新規性志向
observable_data:
  - 新規選択率
  - 探索範囲
  - 情報閲覧数
signal_candidates:
  - 未知の項目を試す
  - 選択肢を広く調べる
device_level: スマホ・PCのみ推定可能
modifiers:
  - 年齢
  - 経験
  - 環境
evidence: 開放性・動機づけ研究で使用
status: active
""",

    "FAC-000004_creativity.yml": """id: FAC-000004
knowledge_type: trait
name_ja: 創造性
name_en: Creativity
category: Personality Facet
attribute: Trait
definition_ja: 新しい発想や独自の組み合わせを生み出す傾向。
tags:
  - CAT:性格
  - CAT:創造性
  - THEORY:BigFive
  - ATTR:特性
parent:
  - 開放性
related:
  - 発想力
  - 柔軟性
  - 独創性
observable_data:
  - 解法の多様性
  - 非定型行動
  - 組み合わせ数
signal_candidates:
  - 通常と異なる方法を試す
  - 複数の解法を生み出す
device_level: スマホ・PCのみ推定可能
modifiers:
  - 経験
  - 教育
  - 環境
  - 制約条件
evidence: 創造性研究・開放性との関連で使用
status: active
""",

    "FAC-000005_self_discipline.yml": """id: FAC-000005
knowledge_type: trait
name_ja: 自己規律
name_en: Self-Discipline
category: Personality Facet
attribute: Trait
definition_ja: 目標やルールに沿って行動を維持し、誘惑や中断に流されにくい傾向。
tags:
  - CAT:性格
  - CAT:自己管理
  - THEORY:BigFive
  - ATTR:特性
parent:
  - 誠実性
related:
  - 抑制制御
  - 継続力
  - 目標管理
observable_data:
  - 継続率
  - 中断率
  - ルール遵守
signal_candidates:
  - 決めた行動を継続する
  - 途中離脱が少ない
device_level: スマホ・PCのみ推定可能
modifiers:
  - 疲労
  - 報酬
  - ストレス
  - 環境
evidence: 誠実性の下位特性として利用
status: active
""",

    "FAC-000006_responsibility.yml": """id: FAC-000006
knowledge_type: trait
name_ja: 責任感
name_en: Responsibility
category: Personality Facet
attribute: Trait
definition_ja: 自分の役割・約束・結果に対して責任を持とうとする傾向。
tags:
  - CAT:性格
  - THEORY:BigFive
  - ATTR:特性
parent:
  - 誠実性
related:
  - 信頼性
  - 期限遵守
  - 当事者意識
observable_data:
  - 期限遵守
  - 課題完了率
  - 約束履行
signal_candidates:
  - 最後まで完了しようとする
  - 自分の担当を優先する
device_level: スマホ・PCのみ推定可能
modifiers:
  - 社会環境
  - 評価状況
  - 疲労
evidence: 性格評価・人材評価で使用
status: active
""",

    "FAC-000007_empathy.yml": """id: FAC-000007
knowledge_type: trait
name_ja: 共感性
name_en: Empathy
category: Personality Facet
attribute: Trait
definition_ja: 他者の感情や立場を理解し、配慮しようとする傾向。
tags:
  - CAT:性格
  - CAT:社会性
  - THEORY:BigFive
  - ATTR:特性
parent:
  - 協調性
related:
  - 他者視点取得
  - 配慮
  - 感情認識
observable_data:
  - 支援選択
  - 共感表現
  - 他者利益選択
signal_candidates:
  - 他者に配慮した選択をする
  - 感情的な文脈へ反応する
device_level: スマホ・PCのみ推定可能
modifiers:
  - 文化
  - 対人環境
  - 疲労
evidence: 協調性・社会認知研究で使用
status: active
""",

    "FAC-000008_risk_tolerance.yml": """id: FAC-000008
knowledge_type: trait
name_ja: リスク許容
name_en: Risk Tolerance
category: Personality Facet
attribute: Trait
definition_ja: 不確実性や損失可能性を含む選択を受け入れやすい傾向。
tags:
  - CAT:性格
  - CAT:意思決定
  - THEORY:行動経済学
  - ATTR:特性
parent:
  - 行動傾向
related:
  - リスク選好
  - 損失回避
  - 挑戦性
observable_data:
  - 高リスク選択率
  - 安全選択率
  - 損失後行動
signal_candidates:
  - 高リターン高リスクを選ぶ
  - 損失後も挑戦する
device_level: スマホ・PCのみ推定可能
modifiers:
  - 年齢
  - 文化
  - 報酬条件
  - 損失経験
evidence: 行動経済学・意思決定研究で使用
status: active
""",

    "personality_facets_index.yml": """category: Personality Facets
name_ja: 性格下位特性
items:
  - FAC-000001_sociability.yml
  - FAC-000002_assertiveness.yml
  - FAC-000003_curiosity.yml
  - FAC-000004_creativity.yml
  - FAC-000005_self_discipline.yml
  - FAC-000006_responsibility.yml
  - FAC-000007_empathy.yml
  - FAC-000008_risk_tolerance.yml
notes:
  - 下位特性は統合しない
  - 上位性格因子との関係はparentとtagsで管理する
  - アプリ種別タグは付けない
"""
}

for filename, content in files.items():
    (BASE / filename).write_text(content, encoding="utf-8")

print(f"Generated {len(files)} files in {BASE}")