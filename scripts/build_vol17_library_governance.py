import json
from pathlib import Path

OUT = Path("data/master_packs/vol17_library_governance_001_050.json")

SECTIONS = [
    {
        "category": "Library Governance - Schema",
        "name_ja": "ライブラリ管理・スキーマ",
        "items": [
            ("GOV-000001", "knowledge_item_schema", "知識項目スキーマ", "Knowledge Item Schema", "知識項目に必要なID・名称・定義・タグ・観測データなどの構造定義。"),
            ("GOV-000002", "required_field_policy", "必須フィールド方針", "Required Field Policy", "各YAML項目に必ず含めるフィールドを管理する方針。"),
            ("GOV-000003", "optional_field_policy", "任意フィールド方針", "Optional Field Policy", "将来拡張用の任意フィールドを安全に追加するための方針。"),
            ("GOV-000004", "field_naming_convention", "フィールド命名規則", "Field Naming Convention", "YAMLやJSON内のフィールド名を一貫させるための規則。"),
            ("GOV-000005", "id_format_policy", "ID形式方針", "ID Format Policy", "知識項目IDの接頭辞・桁数・採番規則を管理する方針。"),
            ("GOV-000006", "filename_policy", "ファイル名方針", "Filename Policy", "YAMLファイル名の形式・重複防止・可読性を管理する方針。"),
            ("GOV-000007", "index_file_policy", "インデックスファイル方針", "Index File Policy", "各カテゴリのindex.ymlに含める内容や構造を管理する方針。"),
            ("GOV-000008", "master_pack_policy", "マスターパック方針", "Master Pack Policy", "Builderが出力するJSONマスターパックの構造と運用方針。"),
            ("GOV-000009", "yaml_generation_policy", "YAML生成方針", "YAML Generation Policy", "master_packからYAMLを生成する手順と品質を管理する方針。"),
            ("GOV-000010", "schema_version_policy", "スキーマ版管理方針", "Schema Version Policy", "スキーマ変更時の互換性・履歴・移行を管理する方針。")
        ]
    },
    {
        "category": "Library Governance - Taxonomy",
        "name_ja": "ライブラリ管理・分類体系",
        "items": [
            ("GOV-000011", "taxonomy_policy", "分類体系方針", "Taxonomy Policy", "知識項目を概念・行動・環境・補正要因などに整理する方針。"),
            ("GOV-000012", "knowledge_type_policy", "knowledge_type方針", "Knowledge Type Policy", "知識種別を一貫して管理するための方針。"),
            ("GOV-000013", "category_policy", "カテゴリ方針", "Category Policy", "大分類カテゴリの付け方と重複を管理する方針。"),
            ("GOV-000014", "attribute_policy", "属性方針", "Attribute Policy", "項目の属性を分類・検索しやすくするための方針。"),
            ("GOV-000015", "tag_policy", "タグ方針", "Tag Policy", "CAT・ATTRなどのタグを一貫して付与するための方針。"),
            ("GOV-000016", "parent_child_policy", "親子関係方針", "Parent Child Policy", "parentフィールドを使って上位概念と下位項目を管理する方針。"),
            ("GOV-000017", "related_item_policy", "関連項目方針", "Related Item Policy", "relatedフィールドで横断参照を管理する方針。"),
            ("GOV-000018", "cross_volume_link_policy", "Vol横断リンク方針", "Cross Volume Link Policy", "複数Vol間の知識項目を関連づける方針。"),
            ("GOV-000019", "duplicate_concept_policy", "概念重複方針", "Duplicate Concept Policy", "似た概念を統合せずタグと関連で扱うための方針。"),
            ("GOV-000020", "taxonomy_extension_policy", "分類拡張方針", "Taxonomy Extension Policy", "将来のVolやカテゴリ追加に対応するための方針。")
        ]
    },
    {
        "category": "Library Governance - Audit",
        "name_ja": "ライブラリ管理・監査",
        "items": [
            ("GOV-000021", "global_audit", "全体監査", "Global Audit", "全YAML項目の必須フィールド・ID重複・構造を確認する監査。"),
            ("GOV-000022", "volume_audit", "Vol別監査", "Volume Audit", "各Vol単位で項目数・構造・カテゴリ整合性を確認する監査。"),
            ("GOV-000023", "required_field_audit", "必須項目監査", "Required Field Audit", "必須フィールドが欠けていないか確認する監査。"),
            ("GOV-000024", "duplicate_id_audit", "ID重複監査", "Duplicate ID Audit", "同一IDが複数ファイルに存在しないか確認する監査。"),
            ("GOV-000025", "filename_id_consistency_audit", "ファイル名ID整合監査", "Filename ID Consistency Audit", "ファイル名とidフィールドが一致しているか確認する監査。"),
            ("GOV-000026", "tag_consistency_audit", "タグ整合監査", "Tag Consistency Audit", "タグ形式や分類タグの一貫性を確認する監査。"),
            ("GOV-000027", "index_reference_audit", "インデックス参照監査", "Index Reference Audit", "index.ymlに記載された項目と実ファイルの整合を確認する監査。"),
            ("GOV-000028", "orphan_item_audit", "孤立項目監査", "Orphan Item Audit", "indexや関連から参照されない項目を確認する監査。"),
            ("GOV-000029", "status_audit", "ステータス監査", "Status Audit", "active・draft・deprecatedなどの状態管理を確認する監査。"),
            ("GOV-000030", "audit_result_logging", "監査結果ログ", "Audit Result Logging", "監査結果を記録し、変更履歴や品質確認に使う管理。")
        ]
    },
    {
        "category": "Library Governance - Lifecycle",
        "name_ja": "ライブラリ管理・ライフサイクル",
        "items": [
            ("GOV-000031", "item_creation_policy", "項目作成方針", "Item Creation Policy", "新しい知識項目を追加する際の基準と手順。"),
            ("GOV-000032", "item_update_policy", "項目更新方針", "Item Update Policy", "既存項目の定義・タグ・関連を更新する際の方針。"),
            ("GOV-000033", "item_deprecation_policy", "項目非推奨方針", "Item Deprecation Policy", "古い項目や低品質項目を削除せず非推奨化する方針。"),
            ("GOV-000034", "item_merge_policy", "項目統合方針", "Item Merge Policy", "重複や近接概念を統合する場合の方針。"),
            ("GOV-000035", "item_split_policy", "項目分割方針", "Item Split Policy", "概念が広すぎる場合に複数項目へ分割する方針。"),
            ("GOV-000036", "backward_compatibility_policy", "後方互換方針", "Backward Compatibility Policy", "既存アプリが参照するIDや構造を壊さないための方針。"),
            ("GOV-000037", "change_log_policy", "変更履歴方針", "Change Log Policy", "知識項目やスキーマ変更を追跡する方針。"),
            ("GOV-000038", "release_policy", "リリース方針", "Release Policy", "一定単位でKnowledge Libraryを更新・配布する方針。"),
            ("GOV-000039", "quality_gate_policy", "品質ゲート方針", "Quality Gate Policy", "監査OKやレビュー完了など次工程へ進む条件を管理する方針。"),
            ("GOV-000040", "maintenance_cycle", "保守サイクル", "Maintenance Cycle", "定期的に項目・根拠・分類・監査を見直す管理サイクル。")
        ]
    },
    {
        "category": "Library Governance - Integration",
        "name_ja": "ライブラリ管理・統合",
        "items": [
            ("GOV-000041", "knowledge_library_boundary", "知識ライブラリ境界", "Knowledge Library Boundary", "Knowledge DBは推論せず材料提供に徹するという境界管理。"),
            ("GOV-000042", "app_side_inference_boundary", "アプリ側推論境界", "App Side Inference Boundary", "推論・スコアリング・表示は各アプリ側で行うという責任境界。"),
            ("GOV-000043", "common_library_reuse", "共通ライブラリ再利用", "Common Library Reuse", "診断・ゲーム・秘書・教育など複数アプリで共通知識を再利用する設計。"),
            ("GOV-000044", "cross_app_consistency", "複数アプリ整合性", "Cross App Consistency", "複数アプリで同じ知識項目を使う際の意味や表示の整合性。"),
            ("GOV-000045", "library_scalability", "ライブラリ拡張性", "Library Scalability", "数千〜一万項目規模へ拡張できる構造と運用性。"),
            ("GOV-000046", "storage_efficiency", "保存効率", "Storage Efficiency", "データ容量を無駄に増やさず管理しやすくする設計。"),
            ("GOV-000047", "builder_workflow_integration", "Builderワークフロー統合", "Builder Workflow Integration", "Builder・master_pack・YAML生成・監査を一連の流れとして管理する枠組み。"),
            ("GOV-000048", "github_workflow_integration", "GitHubワークフロー統合", "GitHub Workflow Integration", "生成・監査・commit・pushを一貫して管理する運用。"),
            ("GOV-000049", "library_quality_integration", "ライブラリ品質統合", "Library Quality Integration", "スキーマ・分類・監査・安全性を統合して品質を保つ枠組み。"),
            ("GOV-000050", "analysis_engine_library_governance", "分析エンジンライブラリ統制", "Analysis Engine Library Governance", "Knowledge Library全体の構造・品質・安全性・運用を統合管理する枠組み。")
        ]
    }
]


def make_item(item_id, slug, name_ja, name_en, definition_ja, category, parent_ja):
    return {
        "filename": f"{item_id}_{slug}.yml",
        "id": item_id,
        "knowledge_type": "library_governance",
        "name_ja": name_ja,
        "name_en": name_en,
        "category": "Library Governance",
        "attribute": category.replace("Library Governance - ", ""),
        "definition_ja": definition_ja,
        "tags": ["CAT:ライブラリ管理", f"CAT:{parent_ja}", "ATTR:管理方針"],
        "parent": [parent_ja],
        "related": ["監査", "スキーマ", "安全設計"],
        "observable_data": [
            f"{name_ja}適用範囲",
            f"{name_ja}管理対象",
            f"{name_ja}監査条件",
            f"{name_ja}更新履歴"
        ],
        "signal_candidates": [
            f"{name_ja}をライブラリ運用方針として利用できる",
            "Knowledge DBの品質・拡張性・保守性を管理する材料になる"
        ],
        "device_level": "DB管理用",
        "modifiers": ["品質", "保守性", "互換性", "拡張性"],
        "evidence": "情報設計・データガバナンス・ナレッジマネジメント・ソフトウェア運用で使用",
        "status": "active"
    }


def main():
    all_items = []
    index_lines = ["category: Library Governance", "name_ja: ライブラリ管理", "items:"]

    for section in SECTIONS:
        parent_ja = section["name_ja"].replace("ライブラリ管理・", "")
        for raw in section["items"]:
            item = make_item(*raw, category=section["category"], parent_ja=parent_ja)
            all_items.append(item)
            index_lines.append(f"  - {item['filename']}")

    index_lines.extend([
        "notes:",
        "  - ライブラリ管理はDB運用と品質維持のための管理材料として扱う",
        "  - Knowledge DB側では推論しない",
        "  - Builder・生成・監査・Git管理の一貫性を重視する"
    ])

    pack = {
        "output_dir": "vol17_library_governance/library_governance_001_050",
        "index_filename": "library_governance_001_050_index.yml",
        "index_content": "\n".join(index_lines) + "\n",
        "items": all_items
    }

    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(json.dumps(pack, ensure_ascii=False, indent=2), encoding="utf-8")

    print(f"Created: {OUT}")
    print(f"Items: {len(all_items)}")


if __name__ == "__main__":
    main()