from pathlib import Path

BASE = Path("data/vol2_personality/social_interpersonal")
BASE.mkdir(parents=True, exist_ok=True)

files = {
    "SOC-000001_empathy.yml": """id: SOC-000001
knowledge_type: trait
name_ja: 共感性
name_en: Empathy
category: Social Interpersonal
attribute: Trait
definition_ja: 他者の感情や立場を理解し、配慮しようとする傾向。
tags:
  - CAT:社会性
  - CAT:性格
  - ATTR:特性
parent:
  - 協調性
related:
  - 他者視点取得
  - 感情認識
  - 配慮
observable_data:
  - 支援選択
  - 共感表現
  - 他者利益選択
signal_candidates:
  - 他者に配慮した選択をする
  - 感情的文脈へ反応する
device_level: スマホ・PCのみ推定可能
modifiers:
  - 文化
  - 対人環境
  - 疲労
evidence: 社会心理学・性格心理学で使用
status: active
""",

    "SOC-000002_cooperation.yml": """id: SOC-000002
knowledge_type: trait
name_ja: 協力性
name_en: Cooperation
category: Social Interpersonal
attribute: Trait
definition_ja: 他者と協力し、共同目標の達成に向けて行動する傾向。
tags:
  - CAT:社会性
  - ATTR:特性
parent:
  - 協調性
related:
  - チームワーク
  - 情報共有
  - 支援行動
observable_data:
  - 協力選択
  - 役割分担
  - 支援行動
signal_candidates:
  - 単独利益より共同利益を選ぶ
  - 他者の行動に合わせる
device_level: スマホ・PCのみ推定可能
modifiers:
  - チーム環境
  - 報酬設計
  - 文化
evidence: 社会心理学・組織行動学で使用
status: active
""",

    "SOC-000003_trustworthiness.yml": """id: SOC-000003
knowledge_type: trait
name_ja: 信頼性
name_en: Trustworthiness
category: Social Interpersonal
attribute: Trait
definition_ja: 約束、ルール、役割を安定して守り、他者から信頼されやすい傾向。
tags:
  - CAT:社会性
  - CAT:性格
  - ATTR:特性
parent:
  - 誠実性
related:
  - 責任感
  - 期限遵守
  - 誠実・謙虚さ
observable_data:
  - 約束履行
  - 期限遵守
  - ルール遵守
signal_candidates:
  - 一貫して約束を守る
  - 役割を最後まで遂行する
device_level: スマホ・PCのみ推定可能
modifiers:
  - 疲労
  - 評価状況
  - 社会環境
evidence: 性格評価・人材評価で使用
status: active
""",

    "SOC-000004_altruism.yml": """id: SOC-000004
knowledge_type: trait
name_ja: 利他性
name_en: Altruism
category: Social Interpersonal
attribute: Trait
definition_ja: 自分の利益だけでなく、他者の利益や支援を重視する傾向。
tags:
  - CAT:社会性
  - CAT:性格
  - ATTR:特性
parent:
  - 協調性
related:
  - 共感性
  - 支援行動
  - 公平性
observable_data:
  - 他者利益選択
  - 支援行動
  - 公平配分
signal_candidates:
  - 自分の得より他者支援を選ぶ
  - 不利でも公平な選択をする
device_level: スマホ・PCのみ推定可能
modifiers:
  - 文化
  - 報酬条件
  - 対人関係
evidence: 社会心理学・行動経済学で使用
status: active
""",

    "SOC-000005_competitiveness.yml": """id: SOC-000005
knowledge_type: trait
name_ja: 競争性
name_en: Competitiveness
category: Social Interpersonal
attribute: Trait
definition_ja: 他者との比較、勝敗、順位、成果競争に動機づけられやすい傾向。
tags:
  - CAT:社会性
  - CAT:動機
  - ATTR:特性
parent:
  - 対人傾向
related:
  - 達成動機
  - 挑戦性
  - 支配性
observable_data:
  - 競争選択
  - ランキング反応
  - 勝敗後行動
signal_candidates:
  - 他者比較があると行動量が増える
  - 勝敗後に再挑戦する
device_level: スマホ・PCのみ推定可能
modifiers:
  - 報酬
  - 評価状況
  - 文化
evidence: 社会心理学・スポーツ心理学・組織心理学で使用
status: active
""",

    "SOC-000006_harmony_orientation.yml": """id: SOC-000006
knowledge_type: trait
name_ja: 調和志向
name_en: Harmony Orientation
category: Social Interpersonal
attribute: Trait
definition_ja: 対立を避け、周囲との関係性や安定した雰囲気を重視する傾向。
tags:
  - CAT:社会性
  - CAT:価値観
  - ATTR:特性
parent:
  - 協調性
related:
  - 対立回避
  - 配慮
  - 協力性
observable_data:
  - 対立回避選択
  - 調整行動
  - 妥協選択
signal_candidates:
  - 衝突を避ける選択をする
  - 関係維持を優先する
device_level: スマホ・PCのみ推定可能
modifiers:
  - 文化
  - チーム環境
  - 評価状況
evidence: 社会心理学・組織行動学で使用
status: active
""",

    "SOC-000007_leadership.yml": """id: SOC-000007
knowledge_type: trait
name_ja: リーダーシップ
name_en: Leadership
category: Social Interpersonal
attribute: Trait
definition_ja: 目標達成や集団行動に向けて、他者を方向づけたり支援したりする傾向。
tags:
  - CAT:社会性
  - CAT:組織行動
  - ATTR:特性
parent:
  - 対人能力
related:
  - 主導性
  - 意思決定
  - 情報共有
observable_data:
  - 提案回数
  - 役割取得
  - 方針提示
signal_candidates:
  - 自分から方針を示す
  - 他者の行動を調整する
device_level: スマホ・PCのみ推定可能
modifiers:
  - チーム構成
  - 評価状況
  - 経験
evidence: 産業・組織心理学で使用
status: active
""",

    "SOC-000008_followership.yml": """id: SOC-000008
knowledge_type: trait
name_ja: フォロワーシップ
name_en: Followership
category: Social Interpersonal
attribute: Trait
definition_ja: 集団やリーダーを支え、役割を理解して協力的に行動する傾向。
tags:
  - CAT:社会性
  - CAT:組織行動
  - ATTR:特性
parent:
  - 対人能力
related:
  - 協力性
  - 役割理解
  - 支援行動
observable_data:
  - 支援行動
  - 役割遵守
  - 情報共有
signal_candidates:
  - 他者の方針を補助する
  - 必要な役割を自発的に担う
device_level: スマホ・PCのみ推定可能
modifiers:
  - チーム環境
  - 役割明確性
  - 文化
evidence: 組織行動学・チーム研究で使用
status: active
""",

    "social_interpersonal_index.yml": """category: Social Interpersonal
name_ja: 対人・社会性
items:
  - SOC-000001_empathy.yml
  - SOC-000002_cooperation.yml
  - SOC-000003_trustworthiness.yml
  - SOC-000004_altruism.yml
  - SOC-000005_competitiveness.yml
  - SOC-000006_harmony_orientation.yml
  - SOC-000007_leadership.yml
  - SOC-000008_followership.yml
notes:
  - 対人特性は統合しない
  - 人間向け診断文ではなく、観測データとSignal候補を保持する
  - アプリ種別タグは付けない
"""
}

for filename, content in files.items():
    (BASE / filename).write_text(content, encoding="utf-8")

print(f"Generated {len(files)} files in {BASE}")