import json
from pathlib import Path

OUT = Path("data/master_packs/vol22_documentation_051_100.json")

SECTIONS = [
    {
        "category": "Documentation - Operations",
        "name_ja": "文書化・運用",
        "items": [
            ("DOC-000051", "daily_operation_doc", "日常運用文書", "Daily Operation Documentation", "通常作業で行う生成・監査・Git反映の手順を説明する文書。"),
            ("DOC-000052", "release_operation_doc", "リリース運用文書", "Release Operation Documentation", "一定単位でKnowledge Libraryを更新・反映する手順を説明する文書。"),
            ("DOC-000053", "backup_operation_doc", "バックアップ運用文書", "Backup Operation Documentation", "データ消失を避けるためのバックアップ方針を説明する文書。"),
            ("DOC-000054", "restore_operation_doc", "復元運用文書", "Restore Operation Documentation", "誤削除や破損時に復元する手順を説明する文書。"),
            ("DOC-000055", "storage_operation_doc", "保存容量運用文書", "Storage Operation Documentation", "容量増加を管理し、不要データを整理する手順を説明する文書。"),
            ("DOC-000056", "audit_operation_doc", "監査運用文書", "Audit Operation Documentation", "監査の実行タイミング・結果確認・修正方法を説明する文書。"),
            ("DOC-000057", "branch_operation_doc", "ブランチ運用文書", "Branch Operation Documentation", "mainや作業ブランチの使い分けを説明する文書。"),
            ("DOC-000058", "commit_operation_doc", "コミット運用文書", "Commit Operation Documentation", "変更単位・コミットメッセージ・push手順を説明する文書。"),
            ("DOC-000059", "cleanup_operation_doc", "クリーンアップ運用文書", "Cleanup Operation Documentation", "誤作成ファイルや不要ファイルを整理する手順を説明する文書。"),
            ("DOC-000060", "operations_documentation_integration", "運用文書統合", "Operations Documentation Integration", "日常運用・監査・Git・保守文書を統合管理する枠組み。")
        ]
    },
    {
        "category": "Documentation - App Integration",
        "name_ja": "文書化・アプリ連携",
        "items": [
            ("DOC-000061", "app_integration_overview_doc", "アプリ連携概要文書", "App Integration Overview Documentation", "Knowledge Libraryを各アプリで利用する考え方を説明する文書。"),
            ("DOC-000062", "diagnosis_app_integration_doc", "診断アプリ連携文書", "Diagnosis App Integration Documentation", "診断アプリでのDB参照・推論・表示の流れを説明する文書。"),
            ("DOC-000063", "game_app_integration_doc", "ゲームアプリ連携文書", "Game App Integration Documentation", "ゲーム内行動シグナルとDB接続の方法を説明する文書。"),
            ("DOC-000064", "assistant_app_integration_doc", "秘書アプリ連携文書", "Assistant App Integration Documentation", "予定・通知・生活文脈とDB接続の方法を説明する文書。"),
            ("DOC-000065", "education_app_integration_doc", "教育アプリ連携文書", "Education App Integration Documentation", "学習ログ・教材・フィードバックとDB接続の方法を説明する文書。"),
            ("DOC-000066", "work_support_integration_doc", "仕事支援連携文書", "Work Support Integration Documentation", "業務・集中・タスク文脈とDB接続の方法を説明する文書。"),
            ("DOC-000067", "wellbeing_integration_doc", "ウェルビーイング連携文書", "Wellbeing Integration Documentation", "睡眠・疲労・感情・回復支援とDB接続の方法を説明する文書。"),
            ("DOC-000068", "multi_app_reuse_doc", "複数アプリ再利用文書", "Multi App Reuse Documentation", "共通知識DBを複数アプリで再利用する設計を説明する文書。"),
            ("DOC-000069", "app_side_inference_doc", "アプリ側推論文書", "App Side Inference Documentation", "推論・スコアリング・表示をアプリ側で実装する方針を説明する文書。"),
            ("DOC-000070", "app_integration_documentation", "アプリ連携文書統合", "App Integration Documentation", "アプリ連携に関する文書群を統合管理する枠組み。")
        ]
    },
    {
        "category": "Documentation - Mapping",
        "name_ja": "文書化・対応ルール",
        "items": [
            ("DOC-000071", "mapping_rule_overview_doc", "対応ルール概要文書", "Mapping Rule Overview Documentation", "観測シグナル・補正・表示・用途の対応ルールを説明する文書。"),
            ("DOC-000072", "signal_mapping_doc", "Signal対応文書", "Signal Mapping Documentation", "観測シグナルを知識項目へ対応づける考え方を説明する文書。"),
            ("DOC-000073", "modifier_mapping_doc", "補正対応文書", "Modifier Mapping Documentation", "文脈・状態・データ品質に応じた補正対応を説明する文書。"),
            ("DOC-000074", "display_mapping_doc", "表示対応文書", "Display Mapping Documentation", "推論材料を表示設計へ接続する考え方を説明する文書。"),
            ("DOC-000075", "safety_mapping_doc", "安全対応文書", "Safety Mapping Documentation", "高リスク文脈を安全制御へ接続する考え方を説明する文書。"),
            ("DOC-000076", "evidence_mapping_doc", "根拠対応文書", "Evidence Mapping Documentation", "知識項目と根拠種別・根拠強度の接続を説明する文書。"),
            ("DOC-000077", "concept_linking_doc", "概念接続文書", "Concept Linking Documentation", "親子・関連・近接概念の接続方針を説明する文書。"),
            ("DOC-000078", "mapping_conflict_doc", "対応競合文書", "Mapping Conflict Documentation", "複数対応候補が矛盾する場合の扱いを説明する文書。"),
            ("DOC-000079", "mapping_audit_doc", "対応監査文書", "Mapping Audit Documentation", "対応ルールの妥当性・安全性・整合性を確認する手順文書。"),
            ("DOC-000080", "mapping_documentation_integration", "対応ルール文書統合", "Mapping Documentation Integration", "対応ルール文書を統合管理する枠組み。")
        ]
    },
    {
        "category": "Documentation - Testing QA",
        "name_ja": "文書化・テストQA",
        "items": [
            ("DOC-000081", "test_strategy_doc", "テスト戦略文書", "Test Strategy Documentation", "データ監査・API・表示・安全テストの全体方針を説明する文書。"),
            ("DOC-000082", "data_audit_test_doc", "データ監査テスト文書", "Data Audit Test Documentation", "必須フィールド・ID・YAML構造を確認するテスト手順文書。"),
            ("DOC-000083", "schema_test_doc", "スキーマテスト文書", "Schema Test Documentation", "フィールド型・ID形式・タグ形式を確認する手順文書。"),
            ("DOC-000084", "generation_test_doc", "生成テスト文書", "Generation Test Documentation", "BuilderからYAML生成までを確認するテスト文書。"),
            ("DOC-000085", "api_test_doc", "APIテスト文書", "API Test Documentation", "API応答・検索・安全境界を確認するテスト文書。"),
            ("DOC-000086", "display_test_doc", "表示テスト文書", "Display Test Documentation", "非断定・説明・提案・透明性表示を確認するテスト文書。"),
            ("DOC-000087", "safety_test_doc", "安全テスト文書", "Safety Test Documentation", "プライバシー・高リスク・未成年・操作リスクを確認するテスト文書。"),
            ("DOC-000088", "integration_test_doc", "統合テスト文書", "Integration Test Documentation", "生成・API・表示・安全性を横断確認するテスト文書。"),
            ("DOC-000089", "quality_gate_doc", "品質ゲート文書", "Quality Gate Documentation", "次工程へ進むための監査OK条件や確認項目を説明する文書。"),
            ("DOC-000090", "testing_documentation_integration", "テスト文書統合", "Testing Documentation Integration", "テスト・QA関連文書を統合管理する枠組み。")
        ]
    },
    {
        "category": "Documentation - Integration",
        "name_ja": "文書化・統合",
        "items": [
            ("DOC-000091", "readme_documentation", "README文書", "README Documentation", "リポジトリの目的・使い方・基本コマンドを説明する入口文書。"),
            ("DOC-000092", "contributing_documentation", "CONTRIBUTING文書", "CONTRIBUTING Documentation", "項目追加・修正・監査・Git運用の貢献手順を説明する文書。"),
            ("DOC-000093", "changelog_documentation", "CHANGELOG文書", "CHANGELOG Documentation", "変更履歴・追加Vol・修正内容を記録する文書。"),
            ("DOC-000094", "release_notes_documentation", "リリースノート文書", "Release Notes Documentation", "リリースごとの追加内容・注意点を説明する文書。"),
            ("DOC-000095", "governance_documentation", "ガバナンス文書", "Governance Documentation", "ライブラリ管理・安全・監査・責任範囲を説明する文書。"),
            ("DOC-000096", "architecture_decision_record", "設計判断記録", "Architecture Decision Record", "重要な設計判断と理由を記録する文書。"),
            ("DOC-000097", "faq_documentation", "FAQ文書", "FAQ Documentation", "よくある疑問や作業ミスへの回答を整理する文書。"),
            ("DOC-000098", "troubleshooting_documentation", "トラブルシューティング文書", "Troubleshooting Documentation", "エラーや誤操作時の対処法を整理する文書。"),
            ("DOC-000099", "documentation_audit", "文書監査", "Documentation Audit", "文書が最新で正確か確認する管理過程。"),
            ("DOC-000100", "documentation_system_integration", "文書化システム統合", "Documentation System Integration", "プロジェクト・開発・API・安全・テスト文書を統合管理する枠組み。")
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
        "output_dir": "vol22_documentation/documentation_051_100",
        "index_filename": "documentation_051_100_index.yml",
        "index_content": "\n".join(index_lines) + "\n",
        "items": all_items
    }

    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(json.dumps(pack, ensure_ascii=False, indent=2), encoding="utf-8")

    print(f"Created: {OUT}")
    print(f"Items: {len(all_items)}")


if __name__ == "__main__":
    main()