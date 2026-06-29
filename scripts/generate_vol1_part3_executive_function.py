from pathlib import Path

BASE = Path("data/vol1_core/executive_function")
BASE.mkdir(parents=True, exist_ok=True)

files = {
    "EXE-000001_inhibition.yml": """id: EXE-000001
name_ja: 抑制制御
name_en: Inhibitory Control
category: Executive Function
attribute: Ability
definition_ja: 不適切または不要な反応・衝動・行動を抑える能力。
parent:
  - 実行機能
related:
  - 衝動性
  - 自己制御
  - 選択的注意
tests:
  - Go/No-Go Task
  - Stroop Task
  - Stop Signal Task
observable_data:
  - 誤反応
  - フライング反応
  - キャンセル率
  - 反応抑制失敗率
signal_candidates:
  - 待てずに反応する
  - 不要な操作をしてしまう
  - ルール違反の選択が増える
device_level: スマホ・PCのみ推定可能
modifiers:
  - 疲労
  - ストレス
  - 年齢
  - 報酬
  - 時間制限
evidence: 標準課題あり、ADHD評価・神経心理研究で重要
status: active
""",

    "EXE-000002_cognitive_flexibility.yml": """id: EXE-000002
name_ja: 認知の柔軟性
name_en: Cognitive Flexibility
category: Executive Function
attribute: Ability
definition_ja: 状況やルールの変化に応じて考え方や行動方略を切り替える能力。
parent:
  - 実行機能
related:
  - 注意切替
  - 交替的注意
  - 適応力
tests:
  - WCST
  - Trail Making Test
  - Task Switching Task
observable_data:
  - ルール変更後ミス率
  - 方略変更回数
  - 切替時間
  - 固執反応
signal_candidates:
  - 前のルールに引きずられる
  - 変化後にミスが増える
  - 同じ方法にこだわる
device_level: スマホ・PCのみ推定可能
modifiers:
  - 年齢
  - 疲労
  - ルール複雑性
  - 経験
evidence: 神経心理検査・実行機能研究で重要
status: active
""",

    "EXE-000003_planning.yml": """id: EXE-000003
name_ja: 計画性
name_en: Planning
category: Executive Function
attribute: Ability
definition_ja: 目標達成のために手順・資源・時間配分を事前に組み立てる能力。
parent:
  - 実行機能
related:
  - 優先順位付け
  - 時間管理
  - 問題解決
  - 誠実性
tests:
  - Tower of London
  - Tower of Hanoi
  - BRIEF
observable_data:
  - 初動時間
  - 手戻り回数
  - 資源配分
  - 手順ミス
  - 予定変更回数
signal_candidates:
  - 開始前に時間を使う
  - 途中の手戻りが少ない
  - 資源を先に確保する
device_level: スマホ・PCのみ推定可能
modifiers:
  - 時間制限
  - 課題複雑性
  - 経験
  - 疲労
evidence: 実行機能研究・BRIEF・産業評価で使用
status: active
""",

    "EXE-000004_self_monitoring.yml": """id: EXE-000004
name_ja: 自己モニタリング
name_en: Self-Monitoring
category: Executive Function
attribute: Ability
definition_ja: 自分の行動・ミス・進捗・状態を観察し、必要に応じて修正する能力。
parent:
  - 実行機能
related:
  - メタ認知
  - エラー検出
  - 自己管理
tests:
  - BRIEF
  - Metacognitive Tasks
observable_data:
  - エラー後修正率
  - 確認回数
  - 自己修正回数
  - 進捗確認頻度
signal_candidates:
  - ミス後にすぐ修正する
  - 同じミスを繰り返す
  - 進捗確認が多い
device_level: スマホ・PCのみ推定可能
modifiers:
  - 疲労
  - 経験
  - フィードバック有無
  - 認知負荷
evidence: BRIEF・メタ認知研究で使用
status: active
""",

    "EXE-000005_organization.yml": """id: EXE-000005
name_ja: 組織化能力
name_en: Organization
category: Executive Function
attribute: Ability
definition_ja: 情報・物・手順・資源を整理し、扱いやすい構造にまとめる能力。
parent:
  - 実行機能
related:
  - 計画性
  - 情報整理
  - 優先順位付け
tests:
  - BRIEF
  - Executive Function Rating Scales
observable_data:
  - 分類行動
  - 整理回数
  - 探索時間
  - 手順の一貫性
signal_candidates:
  - 情報を分類して扱う
  - 探し物や確認が多い
  - 手順が散らばる
device_level: スマホ・PCのみ推定可能
modifiers:
  - 情報量
  - 環境の複雑さ
  - 経験
  - 時間制限
evidence: BRIEF・産業評価・教育評価で使用
status: active
""",

    "EXE-000006_task_initiation.yml": """id: EXE-000006
name_ja: 課題開始
name_en: Task Initiation
category: Executive Function
attribute: Ability
definition_ja: 必要な課題や行動を適切なタイミングで開始する能力。
parent:
  - 実行機能
related:
  - 先延ばし
  - 動機づけ
  - 自己管理
tests:
  - BRIEF
  - BDEFS
observable_data:
  - 開始遅延
  - 初動時間
  - 期限直前開始率
  - 未着手率
signal_candidates:
  - 開始までに時間がかかる
  - 期限直前に集中する
  - 簡単な課題でも着手が遅れる
device_level: スマホ・PCのみ推定可能
modifiers:
  - 動機づけ
  - 疲労
  - 報酬
  - 課題難易度
  - 不安
evidence: BRIEF・BDEFS・ADHD評価で使用
status: active
""",

    "executive_function_index.yml": """category: Executive Function
name_ja: 実行機能
items:
  - EXE-000001_inhibition.yml
  - EXE-000002_cognitive_flexibility.yml
  - EXE-000003_planning.yml
  - EXE-000004_self_monitoring.yml
  - EXE-000005_organization.yml
  - EXE-000006_task_initiation.yml
notes:
  - 統合はしない
  - 実行機能は上位概念として扱う
  - 個別項目はRelationで接続する
  - Signalは推定候補として管理する
"""
}

for filename, content in files.items():
    (BASE / filename).write_text(content, encoding="utf-8")

print(f"Generated {len(files)} files in {BASE}")