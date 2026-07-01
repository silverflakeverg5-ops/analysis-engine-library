import json
from pathlib import Path

OUT = Path("data/master_packs/vol22_documentation_001_050.json")

SECTIONS = [
    {
        "category": "Documentation - Project",
        "name_ja": "文書化・プロジェクト",
        "items": [
            ("DOC-000001", "project_overview_doc", "プロジェクト概要文書", "Project Overview Documentation", "Knowledge Libraryの目的・範囲・基本方針を説明する文書。"),
            ("DOC-000002", "architecture_doc", "アーキテクチャ文書", "Architecture Documentation", "Knowledge DB・Builder・YAML生成・アプリ側推論の構成を説明する文書。"),
            ("DOC-000003", "folder_structure_doc", "フォルダ構成文書", "Folder Structure Documentation", "data・scripts・master_packsなどの役割を説明する文書。"),
            ("DOC-000004", "workflow_doc", "作業手順文書", "Workflow Documentation", "Builder作成から生成・監査・Git反映までの手順を説明する文書。"),
            ("DOC-000005", "handoff_doc", "引継ぎ文書", "Handoff Documentation", "別チャットや別作業者へ進捗を引き継ぐための文書。"),
            ("DOC-000006", "progress_doc", "進捗文書", "Progress Documentation", "各Volの完成状況・項目数・未着手領域を記録する文書。"),
            ("DOC-000007", "design_principle_doc", "設計原則文書", "Design Principle Documentation", "統合しない・タグ管理・アプリ側推論などの設計原則を残す文書。"),
            ("DOC-000008", "scope_boundary_doc", "範囲境界文書", "Scope Boundary Documentation", "DB側とアプリ側の責任範囲を明確にする文書。"),
            ("DOC-000009", "terminology_doc", "用語集文書", "Terminology Documentation", "プロジェクト内で使う用語と意味を整理する文書。"),
            ("DOC-000010", "documentation_integration", "文書化統合", "Documentation Integration", "プロジェクト文書を体系的に管理する枠組み。")
        ]
    },
    {
        "category": "Documentation - Developer Guide",
        "name_ja": "文書化・開発者ガイド",
        "items": [
            ("DOC-000011", "developer_setup_doc", "開発環境セットアップ文書", "Developer Setup Documentation", "Codespacesやローカル環境で作業を始めるための文書。"),
            ("DOC-000012", "builder_creation_doc", "Builder作成文書", "Builder Creation Documentation", "Builderスクリプトの作成・上書き・実行方法を説明する文書。"),
            ("DOC-000013", "master_pack_doc", "master_pack仕様文書", "Master Pack Documentation", "master_pack JSONの構造と使い方を説明する文書。"),
            ("DOC-000014", "yaml_generation_doc", "YAML生成文書", "YAML Generation Documentation", "generate_from_master.pyの使い方を説明する文書。"),
            ("DOC-000015", "audit_command_doc", "監査コマンド文書", "Audit Command Documentation", "audit_all_data.pyなど監査コマンドの使い方を説明する文書。"),
            ("DOC-000016", "git_command_doc", "Gitコマンド文書", "Git Command Documentation", "git add・commit・pushの実行手順を説明する文書。"),
            ("DOC-000017", "error_recovery_doc", "エラー復旧文書", "Error Recovery Documentation", "生成・監査・Gitでエラーが出た時の復旧手順を説明する文書。"),
            ("DOC-000018", "overwrite_policy_doc", "上書き方針文書", "Overwrite Policy Documentation", "Builderを上書きして使う運用方針を説明する文書。"),
            ("DOC-000019", "command_sequence_doc", "コマンド順序文書", "Command Sequence Documentation", "実行順序を間違えないための手順文書。"),
            ("DOC-000020", "developer_guide_integration", "開発者ガイド統合", "Developer Guide Integration", "開発者向け手順を統合管理する枠組み。")
        ]
    },
    {
        "category": "Documentation - Data Dictionary",
        "name_ja": "文書化・データ辞書",
        "items": [
            ("DOC-000021", "field_dictionary_doc", "フィールド辞書文書", "Field Dictionary Documentation", "id・name・category・tagsなど各フィールドの意味を説明する文書。"),
            ("DOC-000022", "knowledge_type_dictionary_doc", "knowledge_type辞書文書", "Knowledge Type Dictionary Documentation", "knowledge_typeの種類と使い分けを説明する文書。"),
            ("DOC-000023", "category_dictionary_doc", "カテゴリ辞書文書", "Category Dictionary Documentation", "カテゴリ体系と分類基準を説明する文書。"),
            ("DOC-000024", "tag_dictionary_doc", "タグ辞書文書", "Tag Dictionary Documentation", "CAT・ATTRなどタグ体系を説明する文書。"),
            ("DOC-000025", "status_dictionary_doc", "ステータス辞書文書", "Status Dictionary Documentation", "active・draft・deprecatedなどの状態管理を説明する文書。"),
            ("DOC-000026", "device_level_dictionary_doc", "device_level辞書文書", "Device Level Dictionary Documentation", "観測可能性やDB管理用の区分を説明する文書。"),
            ("DOC-000027", "observable_data_doc", "observable_data文書", "Observable Data Documentation", "観測可能データ候補の意味と使い方を説明する文書。"),
            ("DOC-000028", "signal_candidates_doc", "signal_candidates文書", "Signal Candidates Documentation", "Signal候補の意味とアプリ側利用方法を説明する文書。"),
            ("DOC-000029", "modifiers_field_doc", "modifiersフィールド文書", "Modifiers Field Documentation", "補正要因フィールドの意味と扱いを説明する文書。"),
            ("DOC-000030", "data_dictionary_integration", "データ辞書統合", "Data Dictionary Integration", "フィールド・分類・タグ辞書を統合管理する枠組み。")
        ]
    },
    {
        "category": "Documentation - API",
        "name_ja": "文書化・API",
        "items": [
            ("DOC-000031", "api_overview_doc", "API概要文書", "API Overview Documentation", "Knowledge Library APIの目的と基本仕様を説明する文書。"),
            ("DOC-000032", "api_endpoint_doc", "APIエンドポイント文書", "API Endpoint Documentation", "検索・ID取得・一括出力などのエンドポイントを説明する文書。"),
            ("DOC-000033", "api_request_doc", "APIリクエスト文書", "API Request Documentation", "リクエストパラメータや検索条件を説明する文書。"),
            ("DOC-000034", "api_response_doc", "APIレスポンス文書", "API Response Documentation", "API応答形式と各フィールドを説明する文書。"),
            ("DOC-000035", "api_error_doc", "APIエラー文書", "API Error Documentation", "エラーコード・原因・対処を説明する文書。"),
            ("DOC-000036", "api_version_doc", "APIバージョン文書", "API Version Documentation", "API版管理と互換性を説明する文書。"),
            ("DOC-000037", "api_safety_boundary_doc", "API安全境界文書", "API Safety Boundary Documentation", "APIが推論結果を返さない境界を説明する文書。"),
            ("DOC-000038", "api_example_doc", "API利用例文書", "API Example Documentation", "アプリ側からの参照例を説明する文書。"),
            ("DOC-000039", "api_client_doc", "APIクライアント文書", "API Client Documentation", "アプリ側クライアントの実装方針を説明する文書。"),
            ("DOC-000040", "api_documentation_integration", "API文書化統合", "API Documentation Integration", "API関連文書を統合管理する枠組み。")
        ]
    },
    {
        "category": "Documentation - Safety",
        "name_ja": "文書化・安全",
        "items": [
            ("DOC-000041", "safety_policy_doc", "安全方針文書", "Safety Policy Documentation", "非診断・非断定・支援目的など安全方針を説明する文書。"),
            ("DOC-000042", "privacy_policy_doc", "プライバシー方針文書", "Privacy Policy Documentation", "データ最小化・同意・削除などの方針を説明する文書。"),
            ("DOC-000043", "fairness_policy_doc", "公平性方針文書", "Fairness Policy Documentation", "不公平や偏見を避けるための方針を説明する文書。"),
            ("DOC-000044", "high_risk_boundary_doc", "高リスク境界文書", "High Risk Boundary Documentation", "医療・雇用・進路など重大判断への利用境界を説明する文書。"),
            ("DOC-000045", "minor_safety_doc", "未成年安全文書", "Minor Safety Documentation", "未成年利用時の注意点や制御を説明する文書。"),
            ("DOC-000046", "display_safety_doc", "表示安全文書", "Display Safety Documentation", "断定を避ける表示・支援的トーンを説明する文書。"),
            ("DOC-000047", "consent_doc", "同意管理文書", "Consent Documentation", "データ利用や個別化の同意管理を説明する文書。"),
            ("DOC-000048", "audit_policy_doc", "監査方針文書", "Audit Policy Documentation", "安全・品質・APIの監査方針を説明する文書。"),
            ("DOC-000049", "incident_response_doc", "インシデント対応文書", "Incident Response Documentation", "不適切表示やデータ問題が起きた時の対応を説明する文書。"),
            ("DOC-000050", "safety_documentation_integration", "安全文書化統合", "Safety Documentation Integration", "安全方針・プライバシー・監査文書を統合管理する枠組み。")
        ]
    }
]


def make_item(item_id, slug, name_ja, name_en, definition_ja, category, parent_ja):
    return {
        "filename": f"{item_id}_{slug}.yml",
        "id": item_id,
        "knowledge_type": "documentation",
        "name_ja": name_ja,
        "name_en": name_en,
        "category": "Documentation",
        "attribute": category.replace("Documentation - ", ""),
        "definition_ja": definition_ja,
        "tags": ["CAT:文書化", f"CAT:{parent_ja}", "ATTR:説明資料"],
        "parent": [parent_ja],
        "related": ["ライブラリ管理", "API契約", "安全設計"],
        "observable_data": [
            f"{name_ja}対象範囲",
            f"{name_ja}読者",
            f"{name_ja}更新条件",
            f"{name_ja}参照先"
        ],
        "signal_candidates": [
            f"{name_ja}を説明資料として利用できる",
            "Knowledge Libraryの保守・引継ぎ・安全運用を支える材料になる"
        ],
        "device_level": "DB管理用",
        "modifiers": ["読者", "更新頻度", "安全性", "保守性"],
        "evidence": "ドキュメンテーション・ソフトウェア運用・ナレッジマネジメントで使用",
        "status": "active"
    }


def main():
    all_items = []
    index_lines = ["category: Documentation", "name_ja: 文書化", "items:"]

    for section in SECTIONS:
        parent_ja = section["name_ja"].replace("文書化・", "")
        for raw in section["items"]:
            item = make_item(*raw, category=section["category"], parent_ja=parent_ja)
            all_items.append(item)
            index_lines.append(f"  - {item['filename']}")

    index_lines.extend([
        "notes:",
        "  - 文書化は運用・引継ぎ・安全確認の材料として扱う",
        "  - Knowledge DB側では推論しない",
        "  - 開発者・アプリ実装者・管理者が参照できる形を目指す"
    ])

    pack = {
        "output_dir": "vol22_documentation/documentation_001_050",
        "index_filename": "documentation_001_050_index.yml",
        "index_content": "\n".join(index_lines) + "\n",
        "items": all_items
    }

    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(json.dumps(pack, ensure_ascii=False, indent=2), encoding="utf-8")

    print(f"Created: {OUT}")
    print(f"Items: {len(all_items)}")


if __name__ == "__main__":
    main()