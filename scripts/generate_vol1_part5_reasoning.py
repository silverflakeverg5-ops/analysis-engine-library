from pathlib import Path

BASE = Path("data/vol1_core/reasoning")
BASE.mkdir(parents=True, exist_ok=True)

files = {
    "REA-000001_deductive_reasoning.yml": """id: REA-000001
name_ja: 演繹推論
name_en: Deductive Reasoning
category: Reasoning
attribute: Ability
definition_ja: 一般的なルールや前提から、論理的に結論を導く能力。
parent:
  - 推論
related:
  - 論理思考
  - ルール理解
  - 問題解決
tests:
  - Logical Reasoning Task
  - Syllogism Task
observable_data:
  - ルール適用率
  - 論理ミス
  - 条件分岐の正答率
signal_candidates:
  - ルールに沿って安定して判断する
  - 条件が増えると誤判断が増える
device_level: スマホ・PCのみ推定可能
modifiers:
  - ルール複雑性
  - ワーキングメモリ
  - 疲労
evidence: 認知心理学・知能検査で使用
status: active
""",

    "REA-000002_inductive_reasoning.yml": """id: REA-000002
name_ja: 帰納推論
name_en: Inductive Reasoning
category: Reasoning
attribute: Ability
definition_ja: 複数の事例やパターンから、一般的な規則や傾向を見つける能力。
parent:
  - 推論
related:
  - パターン認識
  - 学習
  - 抽象推論
tests:
  - Raven Progressive Matrices
  - Pattern Reasoning Task
observable_data:
  - パターン発見率
  - ルール習得速度
  - 試行錯誤回数
signal_candidates:
  - 少ない試行で規則を見つける
  - 似たパターンへ応用する
device_level: スマホ・PCのみ推定可能
modifiers:
  - 経験
  - 課題複雑性
  - 注意
evidence: 知能検査・認知心理学で重要
status: active
""",

    "REA-000003_causal_reasoning.yml": """id: REA-000003
name_ja: 因果推論
name_en: Causal Reasoning
category: Reasoning
attribute: Ability
definition_ja: ある出来事や結果の原因、または原因から結果を推測する能力。
parent:
  - 推論
related:
  - 仮説構築
  - 問題解決
  - 結果予測
observable_data:
  - 原因特定率
  - 仮説修正回数
  - 結果予測精度
signal_candidates:
  - 失敗後に原因を探す
  - 結果から条件を推測する
  - 関係のない要因を原因と見なす
device_level: スマホ・PCのみ推定可能
modifiers:
  - 情報量
  - 経験
  - 認知バイアス
evidence: 認知心理学・科学的思考研究で使用
status: active
""",

    "REA-000004_abstract_reasoning.yml": """id: REA-000004
name_ja: 抽象推論
name_en: Abstract Reasoning
category: Reasoning
attribute: Ability
definition_ja: 具体的な情報から共通構造や抽象的な規則を見つける能力。
parent:
  - 推論
related:
  - 流動性知能
  - パターン認識
  - 概念形成
tests:
  - Raven Progressive Matrices
  - Matrix Reasoning
observable_data:
  - 図形規則発見率
  - 概念分類率
  - 未知課題の正答率
signal_candidates:
  - 初見の規則を発見する
  - 表面的に違う問題の共通点を見つける
device_level: スマホ・PCのみ推定可能
modifiers:
  - 年齢
  - 教育
  - 疲労
evidence: 知能検査・流動性推理で重要
status: active
""",

    "REA-000005_analogical_reasoning.yml": """id: REA-000005
name_ja: 類推
name_en: Analogical Reasoning
category: Reasoning
attribute: Ability
definition_ja: ある対象や状況の関係性を、別の対象や状況へ当てはめて理解する能力。
parent:
  - 推論
related:
  - 転移学習
  - 抽象推論
  - 比較判断
observable_data:
  - 類似関係発見率
  - 応用成功率
  - 既知パターンの転用率
signal_candidates:
  - 過去の経験を別課題へ応用する
  - 類似点から解法を導く
device_level: スマホ・PCのみ推定可能
modifiers:
  - 経験
  - 知識量
  - 課題類似性
evidence: 認知心理学・教育心理学で使用
status: active
""",

    "reasoning_index.yml": """category: Reasoning
name_ja: 推論
items:
  - REA-000001_deductive_reasoning.yml
  - REA-000002_inductive_reasoning.yml
  - REA-000003_causal_reasoning.yml
  - REA-000004_abstract_reasoning.yml
  - REA-000005_analogical_reasoning.yml
notes:
  - 各推論形式は統合しない
  - 流動性知能や問題解決とのRelationを後で追加する
  - Signalは候補として管理する
"""
}

for filename, content in files.items():
    (BASE / filename).write_text(content, encoding="utf-8")

print(f"Generated {len(files)} files in {BASE}")