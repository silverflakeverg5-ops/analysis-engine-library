from pathlib import Path

BASE = Path("data/vol2_personality")
BASE.mkdir(parents=True, exist_ok=True)

files = {
    "personality_index.yml": """id: VOL2-PERSONALITY-INDEX
name_ja: Vol.2 Personality Index
name_en: Vol.2 Personality Index
description_ja: 性格特性・下位特性・動機・価値観・感情安定性・対人社会性に関する索引。
status: active
categories:
  core:
    name_ja: 性格特性コア
    path: data/vol2_personality/core/personality_core_index.yml
  facets:
    name_ja: 性格下位特性
    path: data/vol2_personality/facets/personality_facets_index.yml
  motivation_values:
    name_ja: 動機・価値観
    path: data/vol2_personality/motivation_values/motivation_values_index.yml
  emotion_stability:
    name_ja: 感情・安定性
    path: data/vol2_personality/emotion_stability/emotion_stability_index.yml
  social_interpersonal:
    name_ja: 対人・社会性
    path: data/vol2_personality/social_interpersonal/social_interpersonal_index.yml
principles:
  - 性格特性は統合しない
  - 理論名はtagsで管理する
  - アプリ種別タグは使わない
  - Signalは候補として扱う
  - 医療診断には使わない
""",

    "README.md": """# Vol.2 Personality

Vol.2 Personality は、性格特性・下位特性・動機・価値観・感情安定性・対人社会性を管理する領域です。

## 含まれるカテゴリ

- Personality Core（性格特性コア）
- Personality Facets（性格下位特性）
- Motivation and Values（動機・価値観）
- Emotion and Stability（感情・安定性）
- Social Interpersonal（対人・社会性）

## 方針

- 性格診断名そのものではなく、分析可能な構成概念として管理する。
- Big Five、HEXACO、行動経済学、組織心理学などは tags で管理する。
- 統合はしない。
- 医療診断や人格の断定には使わない。
- 観測データ、Signal候補、補正要因を保持する。
"""
}

for filename, content in files.items():
    (BASE / filename).write_text(content, encoding="utf-8")

print(f"Generated {len(files)} files in {BASE}")