# Read-Only Knowledge Runtime

## 目的

`analysis_engine`は、Vol1〜Vol41のKnowledge Itemを複数アプリから共通参照するための最小ランタイムです。

このランタイムは次の処理を行いません。

- 人格・能力・状態の推論
- スコアリングや重み付け
- 医療・心理診断
- 適職・相性・危険性の判定
- 利用者データの保存
- Knowledge Itemの変更

推論、Modifier補正、表示文生成は、既存の責任分界どおり各アプリ側で実装します。

## Pythonからの利用

```python
from analysis_engine import KnowledgeLibrary

library = KnowledgeLibrary()

item = library.require("EMO-000001")

result = library.search(
    "感情",
    knowledge_type="emotion_core",
    tags=["CAT:感情コア"],
    limit=20,
)

response = result.to_dict()

matches = library.match_signals(
    ["OBS-000014", "判断潜時"],
    mode="any",
    target_knowledge_types=["decision_strategy"],
    limit=20,
)

bundle = library.interpretation_bundle("DEC-000091")

pipeline = library.application_pipeline(
    ["OBS-000014"],
    target_knowledge_types=["decision_strategy"],
    application_id="APP-000001",
    limit=10,
)

guidance = library.application_guidance("APP-000001")

safety_report = library.safety_contract_report()

contract_report = library.runtime_contract_report()

divination_registry = library.divination_registry()

numerology = library.calculate_numerology(
    "1990-01-01",
    name="Jane Doe",
    target_year=2026,
)

japanese_name = library.calculate_japanese_name(
    "山田",
    "太郎",
    surname_strokes=[3, 5],
    given_strokes=[4, 9],
    stroke_dictionary="modern_glyph_declared_v1",
)

japanese_name_from_dictionary = library.calculate_japanese_name_from_dictionary(
    "山田",
    "太郎",
    stroke_dictionary={"山": 3, "田": 5, "太": 4, "郎": 9},
    stroke_dictionary_id="modern_glyph_dictionary_v1",
)
```

`get`は存在しないIDに`None`を返し、`require`は`ItemNotFoundError`を送出します。

## CLIからの利用

メタデータを確認します。

```bash
python -m analysis_engine --metadata
```

IDで1項目を取得します。

```bash
python -m analysis_engine --id EMO-000001
```

条件を指定して検索します。

```bash
python -m analysis_engine --query 感情 --knowledge-type emotion_core --limit 10
```

Observation Signal IDまたは自由記述Signalを照合します。

```bash
python -m analysis_engine --match-signal OBS-000014 --limit 10
python -m analysis_engine --match-signal "Decision Latency" --target-knowledge-type decision_strategy
```

候補Knowledgeの解釈材料を取得します。

```bash
python -m analysis_engine --bundle-id DEC-000091
```

Signal照合と候補ごとの解釈材料取得を一度に行います。

```bash
python -m analysis_engine --pipeline-signal OBS-000014 --target-knowledge-type decision_strategy --limit 10
```

App Use Caseの表示・安全ガイダンスを取得、またはパイプラインへ添付します。

```bash
python -m analysis_engine --app-guidance-id APP-000001
python -m analysis_engine --pipeline-signal OBS-000014 --app-use-case-id APP-000001 --limit 10
```

公開ランタイム全体の安全契約を監査します。

```bash
python -m analysis_engine --safety-audit
python scripts/audit_runtime_safety.py
```

公開レスポンスのv1互換性を監査します。

```bash
python -m analysis_engine --contract-audit
python scripts/audit_runtime_contract.py
```

対応する占術体系、必要入力、計算基準、安全境界を一括取得します。

```bash
python -m analysis_engine --divination-registry
```

`divination_registry`は、西洋占星術から風水までの詳細10体系を安定した順序で返します。各体系には`knowledge_type`、ID接頭辞、項目数、伝統名、入力種別、必要入力、計算基準、解釈範囲、根拠区分、出典系統が含まれます。これはアプリの入力画面や機能選択を組み立てるための参照情報であり、占断、性格推論、診断、採点、未来予測は行いません。

数秘術の再現可能な算術結果を取得します。

```bash
python -m analysis_engine --numerology-birth-date 1990-01-01
python -m analysis_engine --numerology-birth-date 1990-01-01 --numerology-name "Jane Doe" --numerology-target-year 2026
```

現行方式は`modern_western_digit_sum`です。生年月日からライフパス数・誕生日数・態度数、任意の対象年から個人年数を算出します。ラテン文字氏名を指定した場合はピタゴラス式の1〜9配当で表現数・ソウル数・人格数を算出します。既定では11・22・33を保持し、`--reduce-master-numbers`指定時は一桁まで還元します。

出力には各合計値、還元過程、参照Knowledge ID、採用方式が含まれます。生年月日と氏名の原文はレスポンスへ再掲せず、ランタイム内にも保存しません。算術処理のみを行い、数の象徴解釈、人物推論、診断、採点、将来予測は生成しません。氏名計算は現段階ではラテン文字だけに対応し、未対応文字を黙って読み替えずエラーにします。

漢字・ひらがな・カタカナの日本語氏名から、五格・陰陽配列・三才配置を計算します。

```bash
python -m analysis_engine --japanese-surname 山田 --japanese-given-name 太郎 --japanese-surname-strokes 3,5 --japanese-given-strokes 4,9 --stroke-dictionary modern_glyph_declared_v1
```

画数は字体・字典・流派によって変わるため、ランタイムは漢字から画数を推測しません。呼び出し側が、採用した画数辞典または画数表の識別名と各文字の画数を明示します。文字数と画数列が一致しない場合や、画数根拠が未指定の場合は処理を失敗させます。

アプリがバージョン管理された文字画数辞書を持つ場合は、`calculate_japanese_name_from_dictionary`へ`{"山": 3, "田": 5}`形式の辞書を渡せます。氏名に使われた文字を完全一致で検索し、画数列を自動構成します。`高`と`髙`のような異体字は別文字として扱い、完全一致する登録がない場合は代替字を推測せず処理を失敗させます。

CLIではUTF-8 JSON辞書も読み込めます。

```bash
python -m analysis_engine --japanese-surname 山田 --japanese-given-name 太郎 --stroke-dictionary modern_glyph_dictionary_v1 --stroke-dictionary-file strokes.json
```

JSONのルートは文字をキー、1〜64の整数画数を値とするオブジェクトです。ファイルは5 MB以下、辞書は10万項目以下に制限されます。レスポンスの`stroke_resolution`は、直接画数指定なら`explicit_sequence`、辞書解決なら`dictionary_lookup`です。

既定の`single_character_adjustment=virtual_one`では、一字姓・一字名の天格・地格・外格へ仮数1を加えます。`none`も選択できますが、どちらの場合も採用方式を出力します。計算結果は`NAM-000031`〜`NAM-000040`の五格・陰陽・三才項目へ接続されます。吉凶、命名品質、人格、能力、相性は判定しません。氏名原文はレスポンスへ再掲せず保存もしませんが、監査可能性のため画数列は返します。

## 検索契約

検索では次の条件を利用できます。

- `query`: 大文字小文字を区別しない部分一致
- `category`: 完全一致
- `knowledge_type`: 完全一致
- `tags`: 指定タグをすべて含む項目
- `status`: 完全一致。既定値は`active`
- `offset`: 0以上
- `limit`: 1〜100
- `sort`: `id`、`name_ja`、`name_en`

レスポンスは、ページング情報、Knowledge Item一覧、安全境界を含みます。`inference_performed`と`scoring_performed`は常に`false`です。

## Signal照合契約

`match_signals`は、入力SignalとKnowledge Itemの`name_ja`、`name_en`、`definition_ja`、`observable_data`、`signal_candidates`を決定的に文字列照合します。

- `OBS-` IDを指定した場合は、Observation Signalの日本語名、英語名、観測データ名へ展開します。
- 自由記述を指定した場合は、その語句をそのまま照合します。
- `mode="any"`は入力のいずれか、`mode="all"`はすべてに一致する項目を返します。
- `target_knowledge_types`で照合対象を限定できます。
- 既定ではAPI契約、テスト、文書、Observation Signalなどの運用項目を候補から除外します。
- 結果ごとに、入力、展開語、フィールド、実際に一致した記述を証跡として返します。

この照合は検索処理です。意味的関連性、因果関係、確信度、人物特性を推論せず、数値スコアや順位を生成しません。

## 解釈材料バンドル契約

`interpretation_bundle`は、1つのKnowledge Itemについて次の材料をまとめます。

- 元Knowledge Itemとデータ内の格納場所
- `modifiers`フィールドの原文
- Modifierカタログへ文字列一致した項目と一致証跡
- `evidence`フィールドの原文
- Evidence Sourceカタログへ文字列一致した項目と一致証跡
- 非診断、文脈配慮、不確実性開示、序列化回避、人間確認、Knowledge DB境界の安全基底
- 専用カタログへ解決できなかった原文値

明示的なID参照が既存スキーマにないため、専用カタログへのリンクは文字列一致した場合だけ追加します。一致しない材料を推測で補完しません。また、Evidence Sourceへのリンクは根拠の強さや対象Knowledgeへの適用可能性を保証しません。

## アプリ連携パイプライン契約

`application_pipeline`は、`match_signals`と`interpretation_bundle`を順に実行し、アプリが利用しやすい単一レスポンスへまとめます。

- Signal入力、照合方式、ページング条件をそのまま監査可能な形で返します。
- 各候補にはフィールド単位の一致証跡と、同じKnowledge IDの解釈材料を付けます。
- 運用項目と材料項目は候補から除外します。
- バンドルを含むレスポンス量を制御するため、`limit`は1〜20、既定値は10です。
- 候補はID順の安定したページングであり、関連度順ではありません。

パイプラインは照合と材料収集だけを行います。人物特性の推論、スコア、確信度、候補順位、根拠強度、適用可能性、結論は生成しません。

## アプリ表示・安全ガイダンス契約

`application_guidance`は、1つの`app_use_case`について次の材料をまとめます。

- App Use Case本体と格納場所
- App Use Caseが持つModifier・Evidence原文と解決状況
- 傾向・可能性・非診断・文脈・非評価・理由・使用Signal・Modifier・Evidence・不確実性・データ限界・ユーザー修正の固定表示基底
- 安全表示対応と用途別表示対応のMapping Rule
- 非診断、文脈配慮、不確実性開示、序列化回避、人間確認、Knowledge DB境界の安全基底

現行YAMLにはApp Use CaseからDisplay Designへの明示的なID参照がありません。そのため、返却する表示設計は全用途共通の固定基底であり、`mapping_status.baseline_only=true`、`app_specific_mapping_resolved=false`として返します。用途固有の表示適合性を推測したり、表示文を生成したりしません。

`application_pipeline`の`application_id`へApp Use Case IDを指定すると、このガイダンスを候補一覧とは別に1回だけ添付します。候補Knowledgeの選択順や照合結果は変えません。

## ランタイム安全契約ゲート

`safety_contract_report`は、代表入力を使って次の公開境界を実際に呼び出し、安全契約を検査します。

- メタデータ
- 検索
- Signal照合
- 解釈材料バンドル
- アプリ表示・安全ガイダンス
- アプリ連携パイプライン
- 占術体系レジストリ
- 数秘術算術アダプター
- 日本語姓名五格アダプター

非推論・非採点・非順位付けフラグ、固定安全基底、固定表示基底、`baseline_only`開示、Signal候補と解釈材料のID整合性を確認します。監査自体も人物データの分析や表示適合性評価を行いません。

`scripts/audit_runtime_safety.py`は不合格が1件でもある場合に終了コード1を返します。`scripts/run_quality_checks.py`にも組み込まれているため、安全契約違反は通常の品質ゲートを失敗させます。

## API互換性スナップショットゲート

`runtime_contract_report`は、次の10レスポンスについてJSONのキー階層と値型から決定的なSHA-256指紋を作り、[08_runtime_api_contract_v1.json](08_runtime_api_contract_v1.json)と比較します。

- メタデータ
- 検索
- Signal照合
- 解釈材料バンドル
- アプリ表示・安全ガイダンス
- アプリ連携パイプライン
- 占術体系レジストリ
- 数秘術算術アダプター
- 日本語姓名五格アダプター
- ランタイム安全契約レポート

Knowledge Itemの名称や定義などの値は指紋に含めません。アプリ統合を壊し得るキー追加・削除、型変更、レスポンス階層変更、エンドポイント欠落だけを検出します。

`scripts/audit_runtime_contract.py`は不一致がある場合に終了コード1を返し、通常の品質ゲートも失敗させます。意図的にAPI契約を変更する場合だけ、次のコマンドで候補スナップショットを表示し、内容とAPIバージョンをレビューしてから固定ファイルを更新します。コマンド自体はファイルを書き換えません。

```bash
python scripts/audit_runtime_contract.py --print-current
```

## 実装上の境界

- 既存YAMLスキーマは変更しません。
- YAMLは起動時に読み込み、メモリ上で読み取り専用インデックス化します。
- ID重複や未対応のYAML構造を検出した場合は、不完全な状態で続行せず起動を失敗させます。
- HTTPサーバ、DB、外部サービス、利用者データ処理は含みません。

## テスト

```bash
python -m unittest discover -s tests -v
```
