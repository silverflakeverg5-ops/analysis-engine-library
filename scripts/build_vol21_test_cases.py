import json
from pathlib import Path

OUT = Path("data/master_packs/vol21_test_cases_001_050.json")

SECTIONS = [
    {
        "category": "Test Cases - Data Audit",
        "name_ja": "テストケース・データ監査",
        "items": [
            ("TEST-000001", "required_fields_test", "必須フィールドテスト", "Required Fields Test", "全YAMLに必須フィールドが存在するか確認するテスト。"),
            ("TEST-000002", "duplicate_id_test", "ID重複テスト", "Duplicate ID Test", "同じIDが複数項目に存在しないか確認するテスト。"),
            ("TEST-000003", "filename_id_match_test", "ファイル名ID一致テスト", "Filename ID Match Test", "ファイル名のID部分とidフィールドが一致するか確認するテスト。"),
            ("TEST-000004", "yaml_parse_test", "YAML解析テスト", "YAML Parse Test", "YAMLファイルが正しく読み込める構造か確認するテスト。"),
            ("TEST-000005", "index_reference_test", "インデックス参照テスト", "Index Reference Test", "index.ymlに記載された項目ファイルが存在するか確認するテスト。"),
            ("TEST-000006", "orphan_file_test", "孤立ファイルテスト", "Orphan File Test", "どのindexからも参照されない項目ファイルを確認するテスト。"),
            ("TEST-000007", "status_value_test", "ステータス値テスト", "Status Value Test", "statusフィールドが許可値であるか確認するテスト。"),
            ("TEST-000008", "knowledge_type_test", "knowledge_typeテスト", "Knowledge Type Test", "knowledge_typeが定義済み種別に収まっているか確認するテスト。"),
            ("TEST-000009", "empty_field_test", "空フィールドテスト", "Empty Field Test", "必須フィールドが空欄になっていないか確認するテスト。"),
            ("TEST-000010", "global_audit_test", "全体監査テスト", "Global Audit Test", "全データに対して基本監査をまとめて実行するテスト。")
        ]
    },
    {
        "category": "Test Cases - Schema",
        "name_ja": "テストケース・スキーマ",
        "items": [
            ("TEST-000011", "schema_contract_test", "スキーマ契約テスト", "Schema Contract Test", "知識項目が定義済みスキーマに従っているか確認するテスト。"),
            ("TEST-000012", "field_type_test", "フィールド型テスト", "Field Type Test", "文字列・配列などフィールド型が想定通りか確認するテスト。"),
            ("TEST-000013", "array_field_test", "配列フィールドテスト", "Array Field Test", "tags・parent・relatedなどが配列として管理されているか確認するテスト。"),
            ("TEST-000014", "string_field_test", "文字列フィールドテスト", "String Field Test", "nameやdefinitionなどが文字列として管理されているか確認するテスト。"),
            ("TEST-000015", "id_format_test", "ID形式テスト", "ID Format Test", "IDが接頭辞と桁数のルールに従っているか確認するテスト。"),
            ("TEST-000016", "filename_format_test", "ファイル名形式テスト", "Filename Format Test", "ファイル名がIDとslugを含む形式になっているか確認するテスト。"),
            ("TEST-000017", "tag_format_test", "タグ形式テスト", "Tag Format Test", "CATやATTRなどのタグ形式が一貫しているか確認するテスト。"),
            ("TEST-000018", "device_level_test", "device_levelテスト", "Device Level Test", "device_levelが用途に合った表現になっているか確認するテスト。"),
            ("TEST-000019", "evidence_field_test", "根拠フィールドテスト", "Evidence Field Test", "evidenceが空でなく、根拠種別を示しているか確認するテスト。"),
            ("TEST-000020", "schema_integration_test", "スキーマ統合テスト", "Schema Integration Test", "フィールド・型・ID・タグの整合性を統合確認するテスト。")
        ]
    },
    {
        "category": "Test Cases - Generation",
        "name_ja": "テストケース・生成",
        "items": [
            ("TEST-000021", "master_pack_json_test", "マスターパックJSONテスト", "Master Pack JSON Test", "master_pack JSONが正しく読み込めるか確認するテスト。"),
            ("TEST-000022", "master_pack_required_key_test", "マスターパック必須キー確認", "Master Pack Required Key Test", "output_dir・index_filename・itemsなどの必須キーを確認するテスト。"),
            ("TEST-000023", "yaml_generation_test", "YAML生成テスト", "YAML Generation Test", "master_packからYAMLファイルが生成されるか確認するテスト。"),
            ("TEST-000024", "index_generation_test", "インデックス生成テスト", "Index Generation Test", "index.ymlが正しく生成されるか確認するテスト。"),
            ("TEST-000025", "output_dir_creation_test", "出力フォルダ生成テスト", "Output Directory Creation Test", "指定された出力フォルダが作成されるか確認するテスト。"),
            ("TEST-000026", "generated_item_count_test", "生成項目数テスト", "Generated Item Count Test", "master_packのitems数と生成ファイル数が一致するか確認するテスト。"),
            ("TEST-000027", "overwrite_behavior_test", "上書き挙動テスト", "Overwrite Behavior Test", "同じmaster_packを再実行しても安全に上書きできるか確認するテスト。"),
            ("TEST-000028", "encoding_test", "文字コードテスト", "Encoding Test", "日本語を含むJSON・YAMLがUTF-8で正しく扱えるか確認するテスト。"),
            ("TEST-000029", "builder_output_test", "Builder出力テスト", "Builder Output Test", "Builderスクリプトが期待するmaster_packを出力するか確認するテスト。"),
            ("TEST-000030", "generation_pipeline_test", "生成パイプラインテスト", "Generation Pipeline Test", "BuilderからYAML生成までの一連の流れを確認するテスト。")
        ]
    },
    {
        "category": "Test Cases - API Contract",
        "name_ja": "テストケース・API契約",
        "items": [
            ("TEST-000031", "api_item_response_test", "API項目応答テスト", "API Item Response Test", "単一知識項目のAPI応答が契約通りか確認するテスト。"),
            ("TEST-000032", "api_list_response_test", "API一覧応答テスト", "API List Response Test", "複数項目取得APIの応答構造を確認するテスト。"),
            ("TEST-000033", "api_search_filter_test", "API検索絞込テスト", "API Search Filter Test", "タグ・カテゴリ・attributeによる検索結果を確認するテスト。"),
            ("TEST-000034", "api_pagination_test", "APIページングテスト", "API Pagination Test", "limit・offsetなどページング仕様を確認するテスト。"),
            ("TEST-000035", "api_error_response_test", "APIエラー応答テスト", "API Error Response Test", "存在しないIDや不正クエリへの応答を確認するテスト。"),
            ("TEST-000036", "api_no_inference_test", "API非推論テスト", "API No Inference Test", "APIがスコアや診断結果を返していないか確認するテスト。"),
            ("TEST-000037", "api_safety_note_test", "API安全注記テスト", "API Safety Note Test", "必要な安全注記や境界情報が返るか確認するテスト。"),
            ("TEST-000038", "api_version_test", "API版管理テスト", "API Version Test", "API版・スキーマ版・ライブラリ版が取得できるか確認するテスト。"),
            ("TEST-000039", "api_backward_compatibility_test", "API後方互換テスト", "API Backward Compatibility Test", "既存アプリ参照を壊さないか確認するテスト。"),
            ("TEST-000040", "api_contract_integration_test", "API契約統合テスト", "API Contract Integration Test", "検索・応答・安全・版管理を統合確認するテスト。")
        ]
    },
    {
        "category": "Test Cases - Safety",
        "name_ja": "テストケース・安全",
        "items": [
            ("TEST-000041", "non_diagnostic_display_test", "非診断表示テスト", "Non Diagnostic Display Test", "診断・断定として表示されないか確認するテスト。"),
            ("TEST-000042", "no_ranking_output_test", "順位出力禁止テスト", "No Ranking Output Test", "人や能力を優劣順位で出力しないか確認するテスト。"),
            ("TEST-000043", "privacy_sensitive_test", "プライバシー配慮テスト", "Privacy Sensitive Test", "機微情報を過度に露出しないか確認するテスト。"),
            ("TEST-000044", "minor_safety_test", "未成年安全テスト", "Minor Safety Test", "未成年文脈で慎重な表示や制御が行われるか確認するテスト。"),
            ("TEST-000045", "high_stakes_guardrail_test", "高リスクガードレールテスト", "High Stakes Guardrail Test", "重大判断用途への直接利用を防ぐか確認するテスト。"),
            ("TEST-000046", "uncertainty_expression_test", "不確実性表現テスト", "Uncertainty Expression Test", "不確実性が適切に表示されるか確認するテスト。"),
            ("TEST-000047", "supportive_tone_test", "支援的トーンテスト", "Supportive Tone Test", "評価的・攻撃的ではなく支援的表現になっているか確認するテスト。"),
            ("TEST-000048", "manipulation_risk_test", "操作リスクテスト", "Manipulation Risk Test", "ユーザーを過度に誘導する表現になっていないか確認するテスト。"),
            ("TEST-000049", "user_control_test", "ユーザー制御テスト", "User Control Test", "修正・停止・削除・同意撤回の導線を確認するテスト。"),
            ("TEST-000050", "safety_test_integration", "安全テスト統合", "Safety Test Integration", "非診断・ privacy・公平性・高リスク制御を統合確認するテスト。")
        ]
    }
]


def make_item(item_id, slug, name_ja, name_en, definition_ja, category, parent_ja):
    return {
        "filename": f"{item_id}_{slug}.yml",
        "id": item_id,
        "knowledge_type": "test_case",
        "name_ja": name_ja,
        "name_en": name_en,
        "category": "Test Case",
        "attribute": category.replace("Test Cases - ", ""),
        "definition_ja": definition_ja,
        "tags": ["CAT:テストケース", f"CAT:{parent_ja}", "ATTR:品質確認"],
        "parent": [parent_ja],
        "related": ["監査", "API契約", "安全設計"],
        "observable_data": [
            f"{name_ja}入力条件",
            f"{name_ja}期待結果",
            f"{name_ja}失敗条件",
            f"{name_ja}確認対象"
        ],
        "signal_candidates": [
            f"{name_ja}を品質確認テストとして利用できる",
            "Knowledge Libraryの監査・API・安全性を確認する材料になる"
        ],
        "device_level": "DB管理用",
        "modifiers": ["品質", "安全性", "互換性", "監査範囲"],
        "evidence": "ソフトウェアテスト・QA・データ監査・安全設計で使用",
        "status": "active"
    }


def main():
    all_items = []
    index_lines = ["category: Test Case", "name_ja: テストケース", "items:"]

    for section in SECTIONS:
        parent_ja = section["name_ja"].replace("テストケース・", "")
        for raw in section["items"]:
            item = make_item(*raw, category=section["category"], parent_ja=parent_ja)
            all_items.append(item)
            index_lines.append(f"  - {item['filename']}")

    index_lines.extend([
        "notes:",
        "  - テストケースはDB品質確認とアプリ接続検証の材料として扱う",
        "  - Knowledge DB側では推論しない",
        "  - 監査・API・安全性・表示の検証に利用する"
    ])

    pack = {
        "output_dir": "vol21_test_cases/test_cases_001_050",
        "index_filename": "test_cases_001_050_index.yml",
        "index_content": "\n".join(index_lines) + "\n",
        "items": all_items
    }

    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(json.dumps(pack, ensure_ascii=False, indent=2), encoding="utf-8")

    print(f"Created: {OUT}")
    print(f"Items: {len(all_items)}")


if __name__ == "__main__":
    main()