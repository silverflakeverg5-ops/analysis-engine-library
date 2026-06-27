from pathlib import Path

BASE = Path("data/vol1_core/attention")
BASE.mkdir(parents=True, exist_ok=True)

files = {
    "ATT-000001_sustained_attention.yml": """id: ATT-000001
name_ja: 持続的注意
name_en: Sustained Attention
category: Attention
attribute: Ability
definition_ja: 一定時間にわたり注意を維持し、課題や刺激に集中し続ける能力。
parent:
  - 注意
related:
  - 集中
  - 疲労
  - 覚醒
  - ワーキングメモリ
tests:
  - CPT
  - SART
  - TOVA
  - TEA
observable_data:
  - 反応時間
  - 反応時間ばらつき
  - 見逃し
  - 誤反応
  - 作業継続時間
signal_candidates:
  - 反応時間が徐々に遅くなる
  - 見逃しが増える
  - 一定時間後にミスが増える
device_level: スマホ・PCのみ推定可能
modifiers:
  - 睡眠
  - 疲労
  - 年齢
  - ストレス
  - 騒音
evidence: 標準検査あり、研究多数
status: active
""",

    "ATT-000002_selective_attention.yml": """id: ATT-000002
name_ja: 選択的注意
name_en: Selective Attention
category: Attention
attribute: Ability
definition_ja: 複数の刺激や情報の中から、必要なものを選び出して注意を向ける能力。
parent:
  - 注意
related:
  - 抑制制御
  - 視覚探索
  - 認知負荷
tests:
  - Stroop Task
  - Flanker Task
  - Visual Search Task
observable_data:
  - 誤選択率
  - 見落とし率
  - 探索時間
  - 妨害刺激時の反応低下
signal_candidates:
  - 不要情報に反応する
  - 重要情報を見落とす
  - 似た刺激を取り違える
device_level: スマホ・PCのみ推定可能
modifiers:
  - 情報量
  - 画面密度
  - 疲労
  - 年齢
evidence: 認知心理学・神経心理評価で使用
status: active
""",

    "ATT-000003_divided_attention.yml": """id: ATT-000003
name_ja: 分割的注意
name_en: Divided Attention
category: Attention
attribute: Ability
definition_ja: 複数の対象や課題へ同時に注意を配分する能力。
parent:
  - 注意
related:
  - マルチタスク
  - ワーキングメモリ
  - 認知負荷
tests:
  - Dual Task
  - TEA
observable_data:
  - 同時課題成功率
  - 切替遅延
  - 片方の課題のミス増加
signal_candidates:
  - 同時処理で精度が落ちる
  - 一方の対象を忘れる
  - 操作が途切れる
device_level: スマホ・PCのみ推定可能
modifiers:
  - 課題数
  - 疲労
  - 経験
  - ストレス
evidence: 認知心理学・神経心理評価で使用
status: active
""",

    "ATT-000004_alternating_attention.yml": """id: ATT-000004
name_ja: 交替的注意
name_en: Alternating Attention
category: Attention
attribute: Ability
definition_ja: 異なる課題や対象の間で注意を切り替える能力。
parent:
  - 注意
related:
  - 認知の柔軟性
  - 注意切替
  - 課題切替
tests:
  - Trail Making Test
  - Task Switching Task
observable_data:
  - 切替時間
  - 切替後ミス率
  - ルール変更後の反応遅延
signal_candidates:
  - ルール変更後にミスが増える
  - 前のルールに引きずられる
  - 切替に時間がかかる
device_level: スマホ・PCのみ推定可能
modifiers:
  - ルール複雑性
  - 年齢
  - 疲労
evidence: 神経心理評価で使用
status: active
""",

    "ATT-000005_focused_attention.yml": """id: ATT-000005
name_ja: 焦点化注意
name_en: Focused Attention
category: Attention
attribute: Ability
definition_ja: 特定の対象に注意を集中させる能力。
parent:
  - 注意
related:
  - 選択的注意
  - 集中
  - 視覚探索
tests:
  - Visual Search Task
  - Attention Task
observable_data:
  - 対象発見時間
  - 誤反応
  - 視線・操作の集中度
signal_candidates:
  - 対象外へ反応する
  - 探索が散らばる
  - 対象発見が遅い
device_level: スマホ・PCのみ推定可能
modifiers:
  - 画面密度
  - 妨害刺激
  - 疲労
evidence: 認知心理学で研究多数
status: active
""",

    "attention_index.yml": """category: Attention
name_ja: 注意
items:
  - ATT-000001_sustained_attention.yml
  - ATT-000002_selective_attention.yml
  - ATT-000003_divided_attention.yml
  - ATT-000004_alternating_attention.yml
  - ATT-000005_focused_attention.yml
notes:
  - 統合はしない
  - 類義語・重複候補は関連として管理
  - アプリ種別ではなく観測データとSignalで管理
"""
}

for filename, content in files.items():
    (BASE / filename).write_text(content, encoding="utf-8")

print(f"Generated {len(files)} files in {BASE}")
