from pathlib import Path

BASE = Path("data/vol1_core/spatial")
BASE.mkdir(parents=True, exist_ok=True)

files = {
    "SPA-000001_spatial_recognition.yml": """id: SPA-000001
name_ja: 空間認識
name_en: Spatial Recognition
category: Spatial
attribute: Ability
definition_ja: 物体の位置、距離、方向、配置など空間的な関係を把握する能力。
parent:
  - 視空間認知
related:
  - 視覚認知
  - 空間記憶
  - 方向感覚
tests:
  - Block Design
  - Rey Complex Figure
  - Visual Spatial Tasks
observable_data:
  - 位置把握率
  - 配置再現率
  - 距離判断誤差
  - 空間配置ミス
signal_candidates:
  - 位置関係を取り違える
  - 配置を正確に再現する
  - 距離感の判断に迷う
device_level: スマホ・PCのみ推定可能
modifiers:
  - 年齢
  - 経験
  - 視覚負荷
  - 画面サイズ
evidence: 知能検査・神経心理検査で使用
status: active
""",

    "SPA-000002_mental_rotation.yml": """id: SPA-000002
name_ja: 心的回転
name_en: Mental Rotation
category: Spatial
attribute: Ability
definition_ja: 図形や物体を頭の中で回転させ、向きや形の一致を判断する能力。
parent:
  - 視空間認知
related:
  - 空間認識
  - 図形認識
  - 抽象推論
tests:
  - Mental Rotation Task
  - Block Design
observable_data:
  - 回転判断正答率
  - 回転判断時間
  - 角度差による反応変化
signal_candidates:
  - 図形の向きが変わると判断が遅くなる
  - 回転角度が大きいほどミスが増える
device_level: スマホ・PCのみ推定可能
modifiers:
  - 経験
  - 年齢
  - 教育
  - 疲労
evidence: 認知心理学・空間能力研究で使用
status: active
""",

    "SPA-000003_navigation.yml": """id: SPA-000003
name_ja: ナビゲーション能力
name_en: Navigation Ability
category: Spatial
attribute: Ability
definition_ja: 現在地、目的地、経路、方向を理解し、空間内を移動・探索する能力。
parent:
  - 空間認知
related:
  - 方向感覚
  - 経路記憶
  - 空間探索
observable_data:
  - 経路選択
  - 迷い回数
  - 往復回数
  - 最短経路率
  - 探索範囲
signal_candidates:
  - 同じ場所を何度も通る
  - 目的地まで遠回りする
  - 地図や配置を使って効率化する
device_level: スマホ・PCのみ推定可能
modifiers:
  - 経験
  - 地図情報
  - 環境複雑性
  - 疲労
evidence: 空間認知研究・HCI・ゲーム研究で使用
status: active
""",

    "SPA-000004_spatial_memory.yml": """id: SPA-000004
name_ja: 空間記憶
name_en: Spatial Memory
category: Spatial
attribute: Ability
definition_ja: 物体や場所の位置、配置、経路など空間情報を記憶する能力。
parent:
  - 記憶
  - 空間認知
related:
  - 視覚記憶
  - 経路記憶
  - ナビゲーション能力
tests:
  - Corsi Block
  - Spatial Memory Task
observable_data:
  - 位置再現率
  - 経路再現率
  - 配置記憶率
signal_candidates:
  - 一度見た位置を覚えている
  - 配置を取り違える
  - 経路を再現できる
device_level: スマホ・PCのみ推定可能
modifiers:
  - 年齢
  - 注意
  - 経験
  - 疲労
evidence: 神経心理検査・認知心理学で使用
status: active
""",

    "spatial_index.yml": """category: Spatial
name_ja: 空間認知
items:
  - SPA-000001_spatial_recognition.yml
  - SPA-000002_mental_rotation.yml
  - SPA-000003_navigation.yml
  - SPA-000004_spatial_memory.yml
notes:
  - 空間認識、心的回転、ナビゲーション、空間記憶は統合しない
  - 位置・経路・配置・図形操作に関するRelationを後で追加する
  - Signalは候補として管理する
"""
}

for filename, content in files.items():
    (BASE / filename).write_text(content, encoding="utf-8")

print(f"Generated {len(files)} files in {BASE}")