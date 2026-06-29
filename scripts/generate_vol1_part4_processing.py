from pathlib import Path

BASE = Path("data/vol1_core/processing")
BASE.mkdir(parents=True, exist_ok=True)

files = {
    "PRO-000001_processing_speed.yml": """id: PRO-000001
name_ja: 処理速度
name_en: Processing Speed
category: Processing
attribute: Ability
definition_ja: 入力された情報を素早く認識・判断・処理する能力。
parent:
  - 認知機能
related:
  - 注意
  - 反応速度
  - 判断速度
  - ワーキングメモリ
tests:
  - WAIS Coding
  - WAIS Symbol Search
  - WISC Processing Speed Index
observable_data:
  - 作業完了時間
  - 単位時間あたり処理数
  - 正答速度
  - 入力速度
signal_candidates:
  - 単純課題の処理が速い
  - 情報量が増えると処理が遅くなる
  - 速度を上げるとミスが増える
device_level: スマホ・PCのみ推定可能
modifiers:
  - 年齢
  - 疲労
  - 睡眠
  - 視覚負荷
  - 課題難易度
evidence: WAIS・WISCなど標準知能検査で使用
status: active
""",

    "PRO-000002_reaction_speed.yml": """id: PRO-000002
name_ja: 反応速度
name_en: Reaction Speed
category: Processing
attribute: Ability
definition_ja: 刺激に対して反応を開始するまでの速さ。
parent:
  - 処理特性
related:
  - 処理速度
  - 注意
  - 運動制御
tests:
  - Simple Reaction Time Task
  - Choice Reaction Time Task
observable_data:
  - 単純反応時間
  - 選択反応時間
  - 最短反応時間
  - 反応時間ばらつき
signal_candidates:
  - 刺激後すぐ反応する
  - 反応が遅れる
  - 反応速度のばらつきが大きい
device_level: スマホ・PCのみ推定可能
modifiers:
  - 年齢
  - 疲労
  - 覚醒度
  - 眠気
  - 入力デバイス
evidence: 認知心理学・神経心理学・HCIで使用
status: active
""",

    "PRO-000003_decision_speed.yml": """id: PRO-000003
name_ja: 判断速度
name_en: Decision Speed
category: Processing
attribute: Ability
definition_ja: 複数の選択肢や情報から意思決定に至るまでの速さ。
parent:
  - 意思決定
related:
  - 反応速度
  - 処理速度
  - 慎重性
  - リスク判断
tests:
  - Choice Reaction Time Task
  - Decision-Making Tasks
observable_data:
  - 選択までの時間
  - 初回選択時間
  - 比較時間
  - 選択変更回数
signal_candidates:
  - すぐ決める
  - 決定までに時間がかかる
  - 選択肢が増えると急に遅くなる
device_level: スマホ・PCのみ推定可能
modifiers:
  - 選択肢数
  - 情報量
  - リスク
  - 時間制限
  - 疲労
evidence: 意思決定研究・HCI・認知心理学で使用
status: active
""",

    "PRO-000004_information_processing.yml": """id: PRO-000004
name_ja: 情報処理
name_en: Information Processing
category: Processing
attribute: Ability
definition_ja: 情報を受け取り、整理し、意味づけし、必要な行動や判断へつなげる能力。
parent:
  - 認知機能
related:
  - 情報整理
  - 情報統合
  - 注意
  - 推論
observable_data:
  - 情報確認回数
  - 分類行動
  - 正答率
  - 処理時間
  - 再確認率
signal_candidates:
  - 情報量が増えると混乱する
  - 情報を分類して扱う
  - 必要情報を見落とす
device_level: スマホ・PCのみ推定可能
modifiers:
  - 情報量
  - 表示形式
  - 認知負荷
  - 経験
  - 疲労
evidence: 認知心理学・HCI・教育評価で使用
status: active
""",

    "processing_index.yml": """category: Processing
name_ja: 処理
items:
  - PRO-000001_processing_speed.yml
  - PRO-000002_reaction_speed.yml
  - PRO-000003_decision_speed.yml
  - PRO-000004_information_processing.yml
notes:
  - 処理速度、反応速度、判断速度は統合しない
  - 速度と精度のトレードオフを考慮する
  - Signalは候補として管理する
"""
}

for filename, content in files.items():
    (BASE / filename).write_text(content, encoding="utf-8")

print(f"Generated {len(files)} files in {BASE}")