import json
from pathlib import Path

OUT = Path("data/master_packs/vol20_api_contracts_051_100.json")

SECTIONS = [
    {
        "category": "API Contracts - Search",
        "name_ja": "API契約・検索",
        "items": [
            ("API-000051", "id_lookup_endpoint", "ID検索エンドポイント", "ID Lookup Endpoint", "知識項目IDから単一項目を取得するAPI仕様。"),
            ("API-000052", "tag_search_endpoint", "タグ検索エンドポイント", "Tag Search Endpoint", "タグを条件に知識項目を検索するAPI仕様。"),
            ("API-000053", "category_search_endpoint", "カテゴリ検索エンドポイント", "Category Search Endpoint", "カテゴリを条件に知識項目を検索するAPI仕様。"),
            ("API-000054", "attribute_search_endpoint", "属性検索エンドポイント", "Attribute Search Endpoint", "attributeを条件に知識項目を検索するAPI仕様。"),
            ("API-000055", "keyword_search_endpoint", "キーワード検索エンドポイント", "Keyword Search Endpoint", "名称・定義・タグを対象にキーワード検索するAPI仕様。"),
            ("API-000056", "related_items_endpoint", "関連項目取得エンドポイント", "Related Items Endpoint", "relatedに基づいて関連知識項目を取得するAPI仕様。"),
            ("API-000057", "parent_items_endpoint", "親項目取得エンドポイント", "Parent Items Endpoint", "parent情報から上位概念を取得するAPI仕様。"),
            ("API-000058", "children_items_endpoint", "子項目取得エンドポイント", "Children Items Endpoint", "親概念に紐づく下位項目を取得するAPI仕様。"),
            ("API-000059", "cross_volume_search_endpoint", "Vol横断検索エンドポイント", "Cross Volume Search Endpoint", "複数Volを横断して知識項目を検索するAPI仕様。"),
            ("API-000060", "search_endpoint_integration", "検索エンドポイント統合", "Search Endpoint Integration", "ID・タグ・カテゴリ・関連項目検索を統合管理するAPI仕様。")
        ]
    },
    {
        "category": "API Contracts - Response Safety",
        "name_ja": "API契約・応答安全",
        "items": [
            ("API-000061", "safe_response_contract", "安全応答契約", "Safe Response Contract", "API応答が診断・断定・不適切表示を直接返さないための仕様。"),
            ("API-000062", "non_inference_response", "非推論応答", "Non Inference Response", "Knowledge DBが推論結果ではなく材料のみ返す応答仕様。"),
            ("API-000063", "no_score_response_contract", "スコア非返却契約", "No Score Response Contract", "DB APIが性格スコアや適性スコアを返さないための仕様。"),
            ("API-000064", "no_ranking_response_contract", "順位非返却契約", "No Ranking Response Contract", "DB APIが人や項目を優劣順位として返さないための仕様。"),
            ("API-000065", "sensitive_field_guard", "機微フィールド保護", "Sensitive Field Guard", "機微情報に関わる項目を慎重に返すための応答制御仕様。"),
            ("API-000066", "safety_note_response", "安全注記応答", "Safety Note Response", "安全上の注意や利用境界をAPI応答に含める仕様。"),
            ("API-000067", "limitation_response", "限界情報応答", "Limitation Response", "知識項目の限界や適用範囲を返すAPI仕様。"),
            ("API-000068", "display_boundary_response", "表示境界応答", "Display Boundary Response", "アプリ側表示で注意すべき境界条件を返す仕様。"),
            ("API-000069", "high_risk_warning_response", "高リスク注意応答", "High Risk Warning Response", "高リスク用途に関係する項目で注意情報を返す仕様。"),
            ("API-000070", "response_safety_integration", "応答安全統合", "Response Safety Integration", "非推論・非診断・安全注記を統合した応答仕様。")
        ]
    },
    {
        "category": "API Contracts - Bulk Export",
        "name_ja": "API契約・一括出力",
        "items": [
            ("API-000071", "bulk_export_contract", "一括出力契約", "Bulk Export Contract", "複数知識項目をまとめて取得するAPI仕様。"),
            ("API-000072", "volume_export_contract", "Vol単位出力契約", "Volume Export Contract", "特定Vol全体を取得するAPI仕様。"),
            ("API-000073", "category_export_contract", "カテゴリ単位出力契約", "Category Export Contract", "カテゴリ単位で知識項目を取得するAPI仕様。"),
            ("API-000074", "tag_export_contract", "タグ単位出力契約", "Tag Export Contract", "指定タグに該当する項目を一括取得するAPI仕様。"),
            ("API-000075", "diff_export_contract", "差分出力契約", "Diff Export Contract", "前回版から変更された項目だけを取得するAPI仕様。"),
            ("API-000076", "full_library_export_contract", "全ライブラリ出力契約", "Full Library Export Contract", "Knowledge Library全体を取得するAPI仕様。"),
            ("API-000077", "compressed_export_contract", "圧縮出力契約", "Compressed Export Contract", "大量データを圧縮して取得するAPI仕様。"),
            ("API-000078", "export_manifest_contract", "出力マニフェスト契約", "Export Manifest Contract", "出力対象・件数・版・生成日時を示す仕様。"),
            ("API-000079", "export_integrity_check", "出力整合性確認", "Export Integrity Check", "一括出力データの欠損や破損を確認する仕様。"),
            ("API-000080", "bulk_export_integration", "一括出力統合", "Bulk Export Integration", "Vol・カテゴリ・タグ・差分出力を統合管理するAPI仕様。")
        ]
    },
    {
        "category": "API Contracts - App Client",
        "name_ja": "API契約・アプリクライアント",
        "items": [
            ("API-000081", "client_app_registration", "アプリ登録契約", "Client App Registration", "Knowledge Libraryを参照するアプリを登録・識別する仕様。"),
            ("API-000082", "client_capability_contract", "クライアント機能契約", "Client Capability Contract", "アプリ側が利用可能な機能や表示能力を示す仕様。"),
            ("API-000083", "client_use_case_declaration", "用途宣言契約", "Client Use Case Declaration", "アプリが診断・教育・秘書など利用目的を宣言する仕様。"),
            ("API-000084", "client_safety_profile", "クライアント安全プロファイル", "Client Safety Profile", "アプリ側の安全設計や制限を示す仕様。"),
            ("API-000085", "client_version_contract", "クライアント版契約", "Client Version Contract", "アプリ版とAPI版の互換性を管理する仕様。"),
            ("API-000086", "client_cache_contract", "クライアントキャッシュ契約", "Client Cache Contract", "アプリ側で取得データをキャッシュする際の仕様。"),
            ("API-000087", "client_update_notification", "クライアント更新通知", "Client Update Notification", "Library更新時にアプリ側へ更新必要性を伝える仕様。"),
            ("API-000088", "client_error_handling", "クライアントエラー処理", "Client Error Handling", "API取得失敗時にアプリ側で安全に処理する仕様。"),
            ("API-000089", "client_fallback_contract", "クライアントフォールバック契約", "Client Fallback Contract", "API未取得時に既存データや安全表示へ戻す仕様。"),
            ("API-000090", "client_contract_integration", "クライアント契約統合", "Client Contract Integration", "アプリ登録・用途宣言・互換性・安全性を統合管理する仕様。")
        ]
    },
    {
        "category": "API Contracts - Integration",
        "name_ja": "API契約・統合",
        "items": [
            ("API-000091", "api_schema_manifest", "APIスキーママニフェスト", "API Schema Manifest", "APIで返されるフィールド・型・版を一覧管理する仕様。"),
            ("API-000092", "api_contract_audit", "API契約監査", "API Contract Audit", "API契約がスキーマ・安全境界・互換性を満たすか確認する監査。"),
            ("API-000093", "api_test_case_contract", "APIテストケース契約", "API Test Case Contract", "API応答が期待仕様を満たすか確認するテスト仕様。"),
            ("API-000094", "api_mock_response_contract", "APIモック応答契約", "API Mock Response Contract", "アプリ開発時に使う仮API応答の仕様。"),
            ("API-000095", "api_documentation_contract", "API文書化契約", "API Documentation Contract", "API仕様を開発者が理解できる形で文書化する方針。"),
            ("API-000096", "api_change_management", "API変更管理", "API Change Management", "API仕様変更の影響・告知・移行を管理する方針。"),
            ("API-000097", "api_security_boundary", "API安全境界", "API Security Boundary", "APIが返す情報範囲とアプリ側責任範囲を分ける境界設計。"),
            ("API-000098", "api_observability", "API観測性", "API Observability", "API利用状況・エラー・応答時間を監視するための設計。"),
            ("API-000099", "api_release_gate", "APIリリースゲート", "API Release Gate", "API仕様を公開する前に満たすべき品質条件。"),
            ("API-000100", "api_contracts_integration", "API契約統合", "API Contracts Integration", "検索・応答安全・一括出力・クライアント契約を統合管理する枠組み。")
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
        "output_dir": "vol20_api_contracts/api_contracts_051_100",
        "index_filename": "api_contracts_051_100_index.yml",
        "index_content": "\n".join(index_lines) + "\n",
        "items": all_items
    }

    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(json.dumps(pack, ensure_ascii=False, indent=2), encoding="utf-8")

    print(f"Created: {OUT}")
    print(f"Items: {len(all_items)}")


if __name__ == "__main__":
    main()