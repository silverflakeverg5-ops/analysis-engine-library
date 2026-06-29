from pathlib import Path

BASE = Path("data/vol1_core/memory")
BASE.mkdir(parents=True, exist_ok=True)

files = {
    "MEM-000001_working_memory.yml": """id: MEM-000001
name_ja: ワーキングメモリ
name_en: Working Memory
category: Memory
attribute: Ability
definition_ja: 短時間の情報を保持しながら、同時に処理・更新する能力。
parent:
  - 記憶
  - 実行機能
related:
  - 注意
  - 推論
  - 学習
  - 処理速度
tests:
  - WAIS Digit Span
  - Letter Number Sequencing
  - N-back
  - Corsi Block
observable_data:
  - 保持数
  - 再確認回数
  - 記憶エラー率
  - 更新遅延
signal_candidates:
  - 途中で情報を忘れる
  - 確認回数が増える
  - 同時管理数が増えるとミスが増える
device_level: スマホ・PCのみ推定可能
modifiers:
  - 年齢
  - 睡眠
  - 疲労
  - ストレス
  - 認知負荷
evidence: 標準検査あり、知能検査・実行機能研究で重要
status: active
""",

    "MEM-000002_short_term_memory.yml": """id: MEM-000002
name_ja: 短期記憶
name_en: Short-Term Memory
category: Memory
attribute: Ability
definition_ja: 短時間だけ情報を保持する能力。
parent:
  - 記憶
related:
  - ワーキングメモリ
  - 即時記憶
tests:
  - Digit Span
  - Memory Span Task
observable_data:
  - 保持成功率
  - 保持時間
  - 即時再生エラー
signal_candidates:
  - 直前情報を忘れる
  - 短い間隔でも再確認する
device_level: スマホ・PCのみ推定可能
modifiers:
  - 年齢
  - 疲労
  - 注意
evidence: 標準検査あり、認知心理学で研究多数
status: active
""",

    "MEM-000003_long_term_memory.yml": """id: MEM-000003
name_ja: 長期記憶
name_en: Long-Term Memory
category: Memory
attribute: Ability
definition_ja: 長期間にわたり情報を保持し、必要に応じて想起する能力。
parent:
  - 記憶
related:
  - 意味記憶
  - エピソード記憶
  - 手続き記憶
tests:
  - WMS
  - RAVLT
  - CVLT
observable_data:
  - 遅延再生率
  - 再認率
  - 再学習速度
signal_candidates:
  - 過去情報を正しく思い出せる
  - 再学習が早い
device_level: スマホ・PCのみ推定可能
modifiers:
  - 年齢
  - 睡眠
  - 感情
  - 反復
evidence: 神経心理検査・認知心理学で重要
status: active
""",

    "MEM-000004_episodic_memory.yml": """id: MEM-000004
name_ja: エピソード記憶
name_en: Episodic Memory
category: Memory
attribute: Ability
definition_ja: いつ・どこで・何が起きたかという経験や出来事に関する記憶。
parent:
  - 長期記憶
related:
  - 自伝的記憶
  - 文脈記憶
tests:
  - WMS
  - Story Recall
observable_data:
  - 出来事再生率
  - 文脈情報の保持
  - 時系列再現
signal_candidates:
  - 出来事の順序を取り違える
  - 場所や時点の記憶が曖昧
device_level: スマホ・PCのみ推定可能
modifiers:
  - 年齢
  - 感情
  - 睡眠
evidence: 認知心理学・神経心理学で研究多数
status: active
""",

    "MEM-000005_semantic_memory.yml": """id: MEM-000005
name_ja: 意味記憶
name_en: Semantic Memory
category: Memory
attribute: Ability
definition_ja: 言葉、概念、知識、事実に関する記憶。
parent:
  - 長期記憶
related:
  - 知識
  - 語彙
  - 一般知識
tests:
  - Vocabulary
  - Information
  - Naming Task
observable_data:
  - 知識正答率
  - 語彙使用数
  - 概念理解
signal_candidates:
  - 用語理解が早い
  - 知識問題に強い
device_level: スマホ・PCのみ推定可能
modifiers:
  - 教育
  - 経験
  - 年齢
evidence: 知能検査・神経心理検査で使用
status: active
""",

    "MEM-000006_procedural_memory.yml": """id: MEM-000006
name_ja: 手続き記憶
name_en: Procedural Memory
category: Memory
attribute: Ability
definition_ja: 技能や手順を身体的・自動的に実行するための記憶。
parent:
  - 長期記憶
related:
  - 運動学習
  - 習慣
  - スキル習得
tests:
  - Serial Reaction Time Task
  - Motor Learning Task
observable_data:
  - 操作習熟速度
  - 手順ミス率
  - 反復後の自動化
signal_candidates:
  - 繰り返しで操作が滑らかになる
  - 手順確認が減る
device_level: スマホ・PCのみ推定可能
modifiers:
  - 練習
  - 経験
  - 疲労
evidence: 認知心理学・神経心理学で研究多数
status: active
""",

    "MEM-000007_visual_memory.yml": """id: MEM-000007
name_ja: 視覚記憶
name_en: Visual Memory
category: Memory
attribute: Ability
definition_ja: 図形、位置、色、形など視覚情報を保持・再生する能力。
parent:
  - 記憶
related:
  - 空間記憶
  - 視空間認知
  - パターン認識
tests:
  - Rey Complex Figure
  - Corsi Block
observable_data:
  - 図形再現率
  - 位置記憶率
  - 視覚情報の再認率
signal_candidates:
  - 見た配置を覚えている
  - 似た図形を取り違える
device_level: スマホ・PCのみ推定可能
modifiers:
  - 年齢
  - 注意
  - 疲労
evidence: 神経心理検査で使用
status: active
""",

    "memory_index.yml": """category: Memory
name_ja: 記憶
items:
  - MEM-000001_working_memory.yml
  - MEM-000002_short_term_memory.yml
  - MEM-000003_long_term_memory.yml
  - MEM-000004_episodic_memory.yml
  - MEM-000005_semantic_memory.yml
  - MEM-000006_procedural_memory.yml
  - MEM-000007_visual_memory.yml
notes:
  - 統合はしない
  - 類義語・重複候補はRelationで管理
  - アプリ種別ではなく観測データとSignalで管理
"""
}

for filename, content in files.items():
    (BASE / filename).write_text(content, encoding="utf-8")

print(f"Generated {len(files)} files in {BASE}")