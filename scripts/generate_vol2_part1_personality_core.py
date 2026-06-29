from pathlib import Path

BASE = Path("data/vol2_personality/core")
BASE.mkdir(parents=True, exist_ok=True)

files = {
    "PER-000001_extraversion.yml": """id: PER-000001
knowledge_type: trait
name_ja: 外向性
name_en: Extraversion
category: Personality
attribute: Trait
definition_ja: 社交性、活動性、刺激への反応性、外界への関心の強さに関する性格特性。
tags:
  - CAT:性格
  - THEORY:BigFive
  - THEORY:HEXACO
  - ATTR:特性
parent:
  - 性格特性
related:
  - 社交性
  - 活動性
  - 刺激希求
  - ポジティブ感情
observable_data:
  - 会話量
  - 反応頻度
  - 選択行動
  - 交流行動
signal_candidates:
  - 他者との接点を選びやすい
  - 外部刺激への反応が多い
  - 活動量が高い
device_level: スマホ・PCのみ推定可能
modifiers:
  - 文化
  - 年齢
  - 環境
  - 状態
evidence: Big Five、HEXACOで主要因子
status: active
""",

    "PER-000002_agreeableness.yml": """id: PER-000002
knowledge_type: trait
name_ja: 協調性
name_en: Agreeableness
category: Personality
attribute: Trait
definition_ja: 他者への配慮、信頼、協力、対立回避などに関する性格特性。
tags:
  - CAT:性格
  - THEORY:BigFive
  - THEORY:HEXACO
  - ATTR:特性
parent:
  - 性格特性
related:
  - 共感性
  - 協力性
  - 信頼
  - 調和志向
observable_data:
  - 協力選択
  - 返信内容
  - 支援行動
  - 対立回避行動
signal_candidates:
  - 協力的な選択をしやすい
  - 他者利益を考慮する
  - 対立場面で調整を選ぶ
device_level: スマホ・PCのみ推定可能
modifiers:
  - 文化
  - 対人環境
  - ストレス
evidence: Big Five、HEXACOで主要因子
status: active
""",

    "PER-000003_conscientiousness.yml": """id: PER-000003
knowledge_type: trait
name_ja: 誠実性
name_en: Conscientiousness
category: Personality
attribute: Trait
definition_ja: 計画性、責任感、自己管理、継続力、規律性に関する性格特性。
tags:
  - CAT:性格
  - THEORY:BigFive
  - THEORY:HEXACO
  - ATTR:特性
parent:
  - 性格特性
related:
  - 計画性
  - 自己管理
  - 責任感
  - 継続力
  - 抑制制御
observable_data:
  - 期限遵守
  - 継続率
  - 計画行動
  - 手順遵守
signal_candidates:
  - 事前に計画する
  - 途中で投げ出しにくい
  - ルールや手順を守る
device_level: スマホ・PCのみ推定可能
modifiers:
  - 年齢
  - 文化
  - 職業経験
  - 疲労
evidence: Big Five、HEXACOで主要因子
status: active
""",

    "PER-000004_neuroticism.yml": """id: PER-000004
knowledge_type: trait
name_ja: 神経症傾向
name_en: Neuroticism
category: Personality
attribute: Trait
definition_ja: 不安、情緒的反応性、ストレス感受性、気分の揺れやすさに関する性格特性。
tags:
  - CAT:性格
  - THEORY:BigFive
  - ATTR:特性
parent:
  - 性格特性
related:
  - 不安
  - ストレス感受性
  - 感情調整
  - 情緒安定性
observable_data:
  - 反応変動
  - 回避選択
  - 中断率
  - ストレス下のミス変化
signal_candidates:
  - 負荷が高い場面で行動が揺れる
  - 失敗後に慎重化する
  - 不確実場面を避ける
device_level: スマホ・PCのみ推定可能
modifiers:
  - 睡眠
  - 疲労
  - ストレス
  - 環境
evidence: Big Fiveで主要因子
status: active
""",

    "PER-000005_emotional_stability.yml": """id: PER-000005
knowledge_type: trait
name_ja: 情緒安定性
name_en: Emotional Stability
category: Personality
attribute: Trait
definition_ja: 感情の揺れにくさ、ストレス下での安定性、落ち着きに関する性格特性。
tags:
  - CAT:性格
  - THEORY:BigFive
  - ATTR:特性
parent:
  - 性格特性
related:
  - 神経症傾向
  - 感情調整
  - ストレス耐性
observable_data:
  - 負荷時のミス変化
  - 反応の一貫性
  - 再挑戦率
  - 回復時間
signal_candidates:
  - 失敗後も行動が安定する
  - 高負荷でも反応が大きく崩れない
device_level: スマホ・PCのみ推定可能
modifiers:
  - 睡眠
  - 疲労
  - ストレス
  - 環境
evidence: Big Fiveの神経症傾向の反対概念として広く使用
status: active
""",

    "PER-000006_openness.yml": """id: PER-000006
knowledge_type: trait
name_ja: 開放性
name_en: Openness to Experience
category: Personality
attribute: Trait
definition_ja: 好奇心、想像力、創造性、新しい経験への関心に関する性格特性。
tags:
  - CAT:性格
  - THEORY:BigFive
  - THEORY:HEXACO
  - ATTR:特性
parent:
  - 性格特性
related:
  - 好奇心
  - 創造性
  - 探索志向
  - 柔軟性
observable_data:
  - 探索行動
  - 新規選択率
  - 試行錯誤
  - 多様な選択
signal_candidates:
  - 未知の選択肢を試す
  - 既存パターンから外れた行動を取る
  - 探索範囲が広い
device_level: スマホ・PCのみ推定可能
modifiers:
  - 年齢
  - 文化
  - 教育
  - 経験
evidence: Big Five、HEXACOで主要因子
status: active
""",

    "PER-000007_honesty_humility.yml": """id: PER-000007
knowledge_type: trait
name_ja: 誠実・謙虚さ
name_en: Honesty-Humility
category: Personality
attribute: Trait
definition_ja: 公平性、誠実さ、謙虚さ、利己的利益への抑制に関する性格特性。
tags:
  - CAT:性格
  - THEORY:HEXACO
  - ATTR:特性
parent:
  - 性格特性
related:
  - 公平性
  - 謙虚さ
  - 倫理観
  - 欲望抑制
observable_data:
  - 公平選択
  - 利他的選択
  - ルール遵守
  - 不正回避
signal_candidates:
  - 自分だけが得をする選択を避ける
  - 公平な配分を選ぶ
  - ルール外の有利行動を避ける
device_level: スマホ・PCのみ推定可能
modifiers:
  - 文化
  - 報酬条件
  - 社会環境
evidence: HEXACOで主要因子
status: active
""",

    "personality_core_index.yml": """category: Personality Core
name_ja: 性格特性コア
items:
  - PER-000001_extraversion.yml
  - PER-000002_agreeableness.yml
  - PER-000003_conscientiousness.yml
  - PER-000004_neuroticism.yml
  - PER-000005_emotional_stability.yml
  - PER-000006_openness.yml
  - PER-000007_honesty_humility.yml
notes:
  - 性格特性は統合しない
  - Big Five、HEXACOなどの理論タグで管理する
  - 診断名ではなく観測データとSignal候補を保持する
  - アプリ種別タグは付けない
"""
}

for filename, content in files.items():
    (BASE / filename).write_text(content, encoding="utf-8")

print(f"Generated {len(files)} files in {BASE}")