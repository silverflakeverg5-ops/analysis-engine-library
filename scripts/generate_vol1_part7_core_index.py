from pathlib import Path

BASE = Path("data/vol1_core")
BASE.mkdir(parents=True, exist_ok=True)

files = {
    "core_index.yml": """id: CORE-INDEX-000001
name_ja: Vol.1 Core Index
name_en: Vol.1 Core Index
description_ja: 認知・記憶・実行機能・処理・推論・空間認知に関する中核カテゴリの索引。
status: active
categories:
  attention:
    name_ja: 注意
    path: data/vol1_core/attention/attention_index.yml
  memory:
    name_ja: 記憶
    path: data/vol1_core/memory/memory_index.yml
  executive_function:
    name_ja: 実行機能
    path: data/vol1_core/executive_function/executive_function_index.yml
  processing:
    name_ja: 処理
    path: data/vol1_core/processing/processing_index.yml
  reasoning:
    name_ja: 推論
    path: data/vol1_core/reasoning/reasoning_index.yml
  spatial:
    name_ja: 空間認知
    path: data/vol1_core/spatial/spatial_index.yml
principles:
  - 項目は統合しない
  - 類義語・重複候補はRelationで管理する
  - Signalは推定候補として扱う
  - アプリ種別ではなく観測データと必要機材レベルで管理する
""",

    "README.md": """# Vol.1 Core

Vol.1 Core は、人間分析エンジンの中核となる認知・能力系カテゴリを管理する領域です。

## 含まれるカテゴリ

- Attention（注意）
- Memory（記憶）
- Executive Function（実行機能）
- Processing（処理）
- Reasoning（推論）
- Spatial（空間認知）

## 方針

- 項目は統合しない。
- 類義語・近接概念は Relation で管理する。
- Signal は結論ではなく候補として管理する。
- アプリ種別タグは使わない。
- 必要機材レベルは保持する。
- スマホ・PCのみで取得可能な観測データを優先する。

## 役割

この領域は、ゲーム・AI支援・学習・作業支援・環境診断など、複数アプリで共通利用できる認知能力の基礎辞典として利用する。
"""
}

for filename, content in files.items():
    (BASE / filename).write_text(content, encoding="utf-8")

print(f"Generated {len(files)} files in {BASE}")