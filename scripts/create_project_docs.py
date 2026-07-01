from pathlib import Path

DOCS = Path("docs")
DOCS.mkdir(exist_ok=True)

README = """# Analysis Engine Library

人間分析用の Knowledge Library。

## 基本方針

- DB側では推論しない
- 推論・スコアリング・表示はアプリ側で行う
- DBは概念・定義・タグ・観測可能データ・Signal候補・補正要因・根拠を保持する
- YAMLを知識項目として管理する
- Builderからmaster_pack JSONを生成し、そこからYAMLを生成する

## 基本コマンド

```bash
python scripts/run_quality_checks.py