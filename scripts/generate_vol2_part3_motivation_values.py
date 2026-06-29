from pathlib import Path

BASE = Path("data/vol2_personality/motivation_values")
BASE.mkdir(parents=True, exist_ok=True)

files = {
    "MOT-000001_achievement_motivation.yml": """id: MOT-000001
knowledge_type: trait
name_ja: 達成動機
name_en: Achievement Motivation
category: Motivation
attribute: Trait
definition_ja: 目標達成、成果、成長に向けて努力しようとする傾向。
tags:
  - CAT:動機
  - CAT:性格
  - ATTR:特性
parent:
  - 動機づけ
related:
  - 達成志向
  - 継続力
  - 自己効力感
observable_data:
  - 目標設定
  - 再挑戦率
  - 難易度選択
  - 完了率
signal_candidates:
  - 難しい課題を選ぶ
  - 失敗後も再挑戦する
  - 目標達成まで継続する
device_level: スマホ・PCのみ推定可能
modifiers:
  - 報酬
  - 評価状況
  - 疲労
  - 成功経験
evidence: 動機づけ心理学・教育心理学で使用
status: active
""",

    "MOT-000002_intrinsic_motivation.yml": """id: MOT-000002
knowledge_type: trait
name_ja: 内発的動機
name_en: Intrinsic Motivation
category: Motivation
attribute: Trait
definition_ja: 外部報酬ではなく、活動そのものへの興味や楽しさによって行動する傾向。
tags:
  - CAT:動機
  - ATTR:特性
parent:
  - 動機づけ
related:
  - 好奇心
  - 没入
  - 自律性
observable_data:
  - 自発的開始
  - 継続時間
  - 報酬なし継続
  - 探索行動
signal_candidates:
  - 報酬がなくても続ける
  - 自分から試す
  - 興味対象に時間を使う
device_level: スマホ・PCのみ推定可能
modifiers:
  - 自律性
  - 環境
  - 興味
  - 成功体験
evidence: 自己決定理論・教育心理学で重要
status: active
""",

    "MOT-000003_extrinsic_motivation.yml": """id: MOT-000003
knowledge_type: trait
name_ja: 外発的動機
name_en: Extrinsic Motivation
category: Motivation
attribute: Trait
definition_ja: 報酬、評価、罰、承認など外部要因によって行動する傾向。
tags:
  - CAT:動機
  - ATTR:特性
parent:
  - 動機づけ
related:
  - 報酬感受性
  - 承認欲求
  - 評価反応
observable_data:
  - 報酬条件下の行動増加
  - 評価場面での反応
  - 達成報酬への反応
signal_candidates:
  - 報酬がある時に行動が増える
  - 評価される場面で努力量が変わる
device_level: スマホ・PCのみ推定可能
modifiers:
  - 報酬設計
  - 評価状況
  - 文化
evidence: 動機づけ心理学・行動科学で使用
status: active
""",

    "MOT-000004_autonomy.yml": """id: MOT-000004
knowledge_type: trait
name_ja: 自律性
name_en: Autonomy
category: Motivation
attribute: Trait
definition_ja: 自分で選択し、自分の意思で行動したいとする傾向。
tags:
  - CAT:動機
  - CAT:価値観
  - ATTR:特性
parent:
  - 動機づけ
related:
  - 内発的動機
  - 自己決定
  - 主体性
observable_data:
  - 自由選択率
  - 自発的行動
  - 指示なし行動
signal_candidates:
  - 自分で選べる状況で行動が増える
  - 強制条件で継続率が下がる
device_level: スマホ・PCのみ推定可能
modifiers:
  - 環境
  - 文化
  - 制約条件
evidence: 自己決定理論で主要概念
status: active
""",

    "VAL-000001_security_value.yml": """id: VAL-000001
knowledge_type: value
name_ja: 安全志向
name_en: Security Orientation
category: Values
attribute: Value
definition_ja: 安定、安全、予測可能性を重視する価値傾向。
tags:
  - CAT:価値観
  - CAT:意思決定
  - ATTR:価値観
parent:
  - 価値観
related:
  - リスク回避
  - 安定志向
  - 損失回避
observable_data:
  - 安全選択率
  - リスク回避率
  - 余裕資源確保
signal_candidates:
  - 安全策を選びやすい
  - 不確実な選択を避ける
device_level: スマホ・PCのみ推定可能
modifiers:
  - 年齢
  - 文化
  - 損失経験
  - 環境不安
evidence: 価値観研究・意思決定研究で使用
status: active
""",

    "VAL-000002_growth_value.yml": """id: VAL-000002
knowledge_type: value
name_ja: 成長志向
name_en: Growth Orientation
category: Values
attribute: Value
definition_ja: 学習、改善、自己成長、能力向上を重視する価値傾向。
tags:
  - CAT:価値観
  - CAT:学習
  - ATTR:価値観
parent:
  - 価値観
related:
  - 達成動機
  - 学習意欲
  - 挑戦志向
observable_data:
  - 学習継続
  - 改善行動
  - 難易度上昇選択
signal_candidates:
  - 改善のために繰り返す
  - 新しい課題へ進む
device_level: スマホ・PCのみ推定可能
modifiers:
  - 成功体験
  - 環境
  - フィードバック
evidence: 教育心理学・キャリア心理学で使用
status: active
""",

    "motivation_values_index.yml": """category: Motivation and Values
name_ja: 動機・価値観
items:
  - MOT-000001_achievement_motivation.yml
  - MOT-000002_intrinsic_motivation.yml
  - MOT-000003_extrinsic_motivation.yml
  - MOT-000004_autonomy.yml
  - VAL-000001_security_value.yml
  - VAL-000002_growth_value.yml
notes:
  - 動機と価値観は統合しない
  - 状態ではなく比較的安定した傾向として管理する
  - アプリ種別タグは付けない
"""
}

for filename, content in files.items():
    (BASE / filename).write_text(content, encoding="utf-8")

print(f"Generated {len(files)} files in {BASE}")