from pathlib import Path

BASE = Path("data/vol2_personality/emotion_stability")
BASE.mkdir(parents=True, exist_ok=True)

files = {
    "EMO-000001_emotion_regulation.yml": """id: EMO-000001
knowledge_type: trait
name_ja: 感情調整
name_en: Emotion Regulation
category: Emotion
attribute: Trait
definition_ja: 感情の強さや表出、持続時間を状況に応じて調整する傾向・能力。
tags:
  - CAT:感情
  - CAT:自己管理
  - ATTR:特性
parent:
  - 感情
related:
  - 情緒安定性
  - ストレス耐性
  - 自己制御
observable_data:
  - 失敗後行動
  - 反応変動
  - 回復時間
  - 中断率
signal_candidates:
  - 失敗後に行動が乱れる
  - 高負荷後に回復する
  - 感情的場面で選択が変化する
device_level: スマホ・PCのみ推定可能
modifiers:
  - 睡眠
  - 疲労
  - ストレス
  - 環境
evidence: 感情心理学・臨床心理学・自己制御研究で使用
status: active
""",

    "EMO-000002_stress_sensitivity.yml": """id: EMO-000002
knowledge_type: trait
name_ja: ストレス感受性
name_en: Stress Sensitivity
category: Emotion
attribute: Trait
definition_ja: 心理的・環境的負荷に対して反応しやすい傾向。
tags:
  - CAT:感情
  - CAT:ストレス
  - ATTR:特性
parent:
  - 神経症傾向
related:
  - 不安
  - 疲労
  - 情緒安定性
observable_data:
  - 負荷時ミス率
  - 回避選択
  - 反応時間変動
  - 離脱率
signal_candidates:
  - 負荷が高い場面でミスが増える
  - 不確実な状況を避ける
  - 圧迫条件で行動が揺れる
device_level: スマホ・PCのみ推定可能
modifiers:
  - 睡眠
  - 疲労
  - 騒音
  - 時間制限
evidence: Big Five神経症傾向・ストレス研究で使用
status: active
""",

    "EMO-000003_anxiety_proneness.yml": """id: EMO-000003
knowledge_type: trait
name_ja: 不安傾向
name_en: Anxiety Proneness
category: Emotion
attribute: Trait
definition_ja: 不確実性、失敗、評価、危険に対して不安を感じやすい傾向。
tags:
  - CAT:感情
  - CAT:ストレス
  - ATTR:特性
parent:
  - 神経症傾向
related:
  - 回避傾向
  - 安全志向
  - ストレス感受性
observable_data:
  - 回避選択
  - 確認回数
  - 決定遅延
  - 安全選択率
signal_candidates:
  - 何度も確認する
  - リスクのある選択を避ける
  - 決定まで時間がかかる
device_level: スマホ・PCのみ推定可能
modifiers:
  - 環境不安
  - 評価状況
  - 睡眠
  - 疲労
evidence: 性格心理学・臨床心理学で使用
status: active
""",

    "EMO-000004_resilience.yml": """id: EMO-000004
knowledge_type: trait
name_ja: レジリエンス
name_en: Resilience
category: Emotion
attribute: Trait
definition_ja: 失敗、負荷、ストレス、不利な状況から回復し、行動を再開・継続する傾向。
tags:
  - CAT:感情
  - CAT:適応
  - ATTR:特性
parent:
  - 適応力
related:
  - 回復力
  - 継続力
  - ストレス耐性
observable_data:
  - 再挑戦率
  - 回復時間
  - 失敗後改善率
  - 継続率
signal_candidates:
  - 失敗後に再挑戦する
  - 一時的に崩れても戻る
  - 負荷後も継続する
device_level: スマホ・PCのみ推定可能
modifiers:
  - 支援環境
  - 睡眠
  - 疲労
  - 成功経験
evidence: ストレス研究・教育心理学・産業心理学で使用
status: active
""",

    "EMO-000005_frustration_tolerance.yml": """id: EMO-000005
knowledge_type: trait
name_ja: フラストレーション耐性
name_en: Frustration Tolerance
category: Emotion
attribute: Trait
definition_ja: 思い通りに進まない状況や失敗に対して、行動を維持する傾向。
tags:
  - CAT:感情
  - CAT:自己制御
  - ATTR:特性
parent:
  - ストレス耐性
related:
  - 忍耐力
  - 感情調整
  - 継続力
observable_data:
  - 失敗後継続率
  - 中断率
  - 再挑戦までの時間
  - 操作の乱れ
signal_candidates:
  - 失敗が続くと離脱する
  - 難局でも継続する
  - ミス後に操作が荒くなる
device_level: スマホ・PCのみ推定可能
modifiers:
  - 疲労
  - 難易度
  - 報酬
  - 時間制限
evidence: 感情調整・自己制御研究で使用
status: active
""",

    "emotion_stability_index.yml": """category: Emotion and Stability
name_ja: 感情・安定性
items:
  - EMO-000001_emotion_regulation.yml
  - EMO-000002_stress_sensitivity.yml
  - EMO-000003_anxiety_proneness.yml
  - EMO-000004_resilience.yml
  - EMO-000005_frustration_tolerance.yml
notes:
  - 感情状態と感情特性は統合しない
  - 医療診断には使わない
  - Signalは候補として扱う
  - アプリ種別タグは付けない
"""
}

for filename, content in files.items():
    (BASE / filename).write_text(content, encoding="utf-8")

print(f"Generated {len(files)} files in {BASE}")