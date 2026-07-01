import json
from pathlib import Path

OUT = Path("data/master_packs/vol20_api_contracts_001_050.json")

SECTIONS = [
    {
        "category": "API Contracts - Core",
        "name_ja": "API契約・基本",
        "items": [
            ("API-000001", "knowledge_api_contract", "知識API契約", "Knowledge API Contract", "アプリがKnowledge Libraryを参照するための入出力仕様。"),
            ("API-000002", "read_only_api_principle", "読み取り専用API原則", "Read Only API Principle", "Knowledge DBをアプリ側から直接変更せず参照専用にする原則。"),
            ("API-000003", "app_side_inference_contract", "アプリ側推論契約", "App Side Inference Contract", "推論・スコアリング・表示はアプリ側で行うというAPI責任範囲。"),
            ("API-000004", "knowledge_item_response", "知識項目レスポンス", "Knowledge Item Response", "単一知識項目を取得するレスポンス構造。"),
            ("API-000005", "knowledge_list_response", "知識一覧レスポンス", "Knowledge List Response", "条件に合う知識項目一覧を返すレスポンス構造。"),
            ("API-000006", "search_query_contract", "検索クエリ契約", "Search Query Contract", "タグ・カテゴリ・ID・キーワードで検索するための入力仕様。"),
            ("API-000007", "filter_contract", "フィルター契約", "Filter Contract", "knowledge_type・category・attribute・statusなどで絞り込む仕様。"),
            ("API-000008", "pagination_contract", "ページング契約", "Pagination Contract", "大量項目を分割取得するためのlimit・offset等の仕様。"),
            ("API-000009", "sort_contract", "並び順契約", "Sort Contract", "ID・カテゴリ・名称・更新日などで並び替える仕様。"),
            ("API-000010", "api_contract_integration", "API契約統合", "API Contract Integration", "Knowledge Library参照APIの基本仕様を統合管理する枠組み。")
        ]
    },
    {
        "category": "API Contracts - Item Fields",
        "name_ja": "API契約・項目フィールド",
        "items": [
            ("API-000011", "id_field_contract", "IDフィールド契約", "ID Field Contract", "知識項目IDを返すためのフィールド仕様。"),
            ("API-000012", "name_field_contract", "名称フィールド契約", "Name Field Contract", "日本語名・英語名を返すためのフィールド仕様。"),
            ("API-000013", "definition_field_contract", "定義フィールド契約", "Definition Field Contract", "定義文を返すためのフィールド仕様。"),
            ("API-000014", "category_field_contract", "カテゴリフィールド契約", "Category Field Contract", "カテゴリ情報を返すためのフィールド仕様。"),
            ("API-000015", "attribute_field_contract", "属性フィールド契約", "Attribute Field Contract", "属性情報を返すためのフィールド仕様。"),
            ("API-000016", "tag_field_contract", "タグフィールド契約", "Tag Field Contract", "検索・分類用タグを返すためのフィールド仕様。"),
            ("API-000017", "parent_field_contract", "親項目フィールド契約", "Parent Field Contract", "上位概念や親カテゴリを返すためのフィールド仕様。"),
            ("API-000018", "related_field_contract", "関連項目フィールド契約", "Related Field Contract", "関連概念や横断参照を返すためのフィールド仕様。"),
            ("API-000019", "status_field_contract", "ステータスフィールド契約", "Status Field Contract", "active・draft・deprecatedなどの状態を返す仕様。"),
            ("API-000020", "field_contract_integration", "フィールド契約統合", "Field Contract Integration", "知識項目フィールド仕様を統合管理する枠組み。")
        ]
    },
    {
        "category": "API Contracts - Signal Access",
        "name_ja": "API契約・シグナル参照",
        "items": [
            ("API-000021", "observable_data_access", "観測データ参照", "Observable Data Access", "知識項目に紐づく観測可能データ候補を取得する仕様。"),
            ("API-000022", "signal_candidate_access", "Signal候補参照", "Signal Candidate Access", "推論材料となるSignal候補を取得する仕様。"),
            ("API-000023", "signal_by_app_use_case", "用途別Signal参照", "Signal by App Use Case", "アプリ用途に応じて関連Signal候補を取得する仕様。"),
            ("API-000024", "signal_by_knowledge_type", "知識種別別Signal参照", "Signal by Knowledge Type", "知識種別ごとにSignal候補を取得する仕様。"),
            ("API-000025", "signal_mapping_access", "Signal対応参照", "Signal Mapping Access", "観測シグナルと知識項目の対応ルールを取得する仕様。"),
            ("API-000026", "baseline_signal_access", "ベースラインSignal参照", "Baseline Signal Access", "本人通常傾向と比較するためのSignal候補を取得する仕様。"),
            ("API-000027", "state_change_signal_access", "状態変化Signal参照", "State Change Signal Access", "状態変化に関わるSignal候補を取得する仕様。"),
            ("API-000028", "safety_signal_access", "安全Signal参照", "Safety Signal Access", "安全確認や慎重表示に関わるSignal候補を取得する仕様。"),
            ("API-000029", "signal_metadata_access", "Signalメタデータ参照", "Signal Metadata Access", "Signalの用途・限界・補正条件などを取得する仕様。"),
            ("API-000030", "signal_access_integration", "Signal参照統合", "Signal Access Integration", "観測シグナル参照仕様を統合管理する枠組み。")
        ]
    },
    {
        "category": "API Contracts - Modifier Display",
        "name_ja": "API契約・補正表示",
        "items": [
            ("API-000031", "modifier_access", "補正要因参照", "Modifier Access", "知識項目に関係する補正要因を取得する仕様。"),
            ("API-000032", "modifier_mapping_access", "補正対応参照", "Modifier Mapping Access", "文脈・状態・安全性に応じた補正ルールを取得する仕様。"),
            ("API-000033", "display_design_access", "表示設計参照", "Display Design Access", "結果表示や説明に使う表示設計項目を取得する仕様。"),
            ("API-000034", "safe_expression_access", "安全表現参照", "Safe Expression Access", "非断定・支援的表現の表示設計を取得する仕様。"),
            ("API-000035", "explanation_template_access", "説明テンプレート参照", "Explanation Template Access", "理由説明や根拠表示に使うテンプレートを取得する仕様。"),
            ("API-000036", "notification_design_access", "通知設計参照", "Notification Design Access", "通知タイミングや通知表現に関する項目を取得する仕様。"),
            ("API-000037", "app_use_case_access", "アプリ用途参照", "App Use Case Access", "利用文脈や用途別設計項目を取得する仕様。"),
            ("API-000038", "safety_ethics_access", "安全倫理参照", "Safety Ethics Access", "安全倫理・境界・制御項目を取得する仕様。"),
            ("API-000039", "evidence_source_access", "根拠ソース参照", "Evidence Source Access", "根拠種別や品質管理項目を取得する仕様。"),
            ("API-000040", "modifier_display_access_integration", "補正表示参照統合", "Modifier Display Access Integration", "補正・表示・安全・根拠の参照仕様を統合管理する枠組み。")
        ]
    },
    {
        "category": "API Contracts - Versioning Operations",
        "name_ja": "API契約・版管理運用",
        "items": [
            ("API-000041", "api_version_contract", "APIバージョン契約", "API Version Contract", "API仕様のバージョンを管理する契約。"),
            ("API-000042", "schema_version_response", "スキーマバージョン応答", "Schema Version Response", "現在のスキーマ版を返すレスポンス仕様。"),
            ("API-000043", "library_version_response", "ライブラリバージョン応答", "Library Version Response", "Knowledge Libraryの版や更新状態を返す仕様。"),
            ("API-000044", "deprecated_item_response", "非推奨項目応答", "Deprecated Item Response", "非推奨項目の扱いと代替項目を返す仕様。"),
            ("API-000045", "error_response_contract", "エラー応答契約", "Error Response Contract", "存在しないIDや不正クエリへのエラー応答仕様。"),
            ("API-000046", "rate_limit_contract", "レート制限契約", "Rate Limit Contract", "API利用頻度や制限を管理する仕様。"),
            ("API-000047", "cache_policy_contract", "キャッシュ方針契約", "Cache Policy Contract", "参照結果をキャッシュする際の方針。"),
            ("API-000048", "backward_compatibility_contract", "後方互換契約", "Backward Compatibility Contract", "既存アプリを壊さずAPI変更するための契約。"),
            ("API-000049", "api_audit_contract", "API監査契約", "API Audit Contract", "API出力がスキーマと安全方針に合うか確認する契約。"),
            ("API-000050", "api_operations_integration", "API運用統合", "API Operations Integration", "版管理・互換性・監査・運用を統合する枠組み。")
        ]
    }
]


def make_item(item_id, slug, name_ja, name_en, definition_ja, category, parent_ja):
    return {
        "filename": f"{item_id}_{slug}.yml",
        "id": item_id,
        "knowledge_type": "api_contract",
        "name_ja": name_ja,
        "name_en": name_en,
        "category": "API Contract",
        "attribute": category.replace("API Contracts - ", ""),
        "definition_ja": definition_ja,
        "tags": ["CAT:API契約", f"CAT:{parent_ja}", "ATTR:接続仕様"],
        "parent": [parent_ja],
        "related": ["対応ルール", "ライブラリ管理", "アプリ用途"],
        "observable_data": [
            f"{name_ja}入力仕様",
            f"{name_ja}出力仕様",
            f"{name_ja}適用範囲",
            f"{name_ja}互換性条件"
        ],
        "signal_candidates": [
            f"{name_ja}をAPI接続仕様として利用できる",
            "Knowledge DBとアプリを安全に接続する材料になる"
        ],
        "device_level": "DB管理用",
        "modifiers": ["互換性", "安全性", "用途", "版管理"],
        "evidence": "API設計・ソフトウェア設計・データガバナンス・HCIで使用",
        "status": "active"
    }


def main():
    all_items = []
    index_lines = ["category: API Contract", "name_ja: API契約", "items:"]

    for section in SECTIONS:
        parent_ja = section["name_ja"].replace("API契約・", "")
        for raw in section["items"]:
            item = make_item(*raw, category=section["category"], parent_ja=parent_ja)
            all_items.append(item)
            index_lines.append(f"  - {item['filename']}")

    index_lines.extend([
        "notes:",
        "  - API契約はDBとアプリの接続仕様として扱う",
        "  - Knowledge DB側では推論しない",
        "  - アプリ側で取得データを使って推論・表示・補正を行う"
    ])

    pack = {
        "output_dir": "vol20_api_contracts/api_contracts_001_050",
        "index_filename": "api_contracts_001_050_index.yml",
        "index_content": "\n".join(index_lines) + "\n",
        "items": all_items
    }

    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(json.dumps(pack, ensure_ascii=False, indent=2), encoding="utf-8")

    print(f"Created: {OUT}")
    print(f"Items: {len(all_items)}")


if __name__ == "__main__":
    main()