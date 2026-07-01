import json
from pathlib import Path

OUT = Path("data/master_packs/vol21_test_cases_051_100.json")

SECTIONS = [
    {
        "category": "Test Cases - Mapping",
        "name_ja": "テストケース・対応ルール",
        "items": [
            ("TEST-000051", "signal_mapping_test", "Signal対応テスト", "Signal Mapping Test", "観測シグナルが適切な知識項目へ対応づけられるか確認するテスト。"),
            ("TEST-000052", "modifier_mapping_test", "補正対応テスト", "Modifier Mapping Test", "文脈や状態に応じて適切な補正要因が対応づけられるか確認するテスト。"),
            ("TEST-000053", "display_mapping_test", "表示対応テスト", "Display Mapping Test", "推論材料が適切な表示設計へ対応づけられるか確認するテスト。"),
            ("TEST-000054", "app_mapping_test", "アプリ対応テスト", "App Mapping Test", "アプリ用途に応じて利用する知識項目が適切に選ばれるか確認するテスト。"),
            ("TEST-000055", "evidence_mapping_test", "根拠対応テスト", "Evidence Mapping Test", "知識項目が適切な根拠種別へ対応づけられるか確認するテスト。"),
            ("TEST-000056", "safety_mapping_test", "安全対応テスト", "Safety Mapping Test", "リスク文脈が安全制御や慎重表示へ対応づけられるか確認するテスト。"),
            ("TEST-000057", "concept_linking_test", "概念接続テスト", "Concept Linking Test", "関連概念・親子概念・近接概念の接続が妥当か確認するテスト。"),
            ("TEST-000058", "mapping_conflict_test", "対応競合テスト", "Mapping Conflict Test", "複数の対応候補が矛盾する場合に検出できるか確認するテスト。"),
            ("TEST-000059", "mapping_priority_test", "対応優先度テスト", "Mapping Priority Test", "複数対応候補の優先順位が適切に扱われるか確認するテスト。"),
            ("TEST-000060", "mapping_integration_test", "対応統合テスト", "Mapping Integration Test", "シグナル・補正・表示・安全対応が一貫して接続されるか確認するテスト。")
        ]
    },
    {
        "category": "Test Cases - Display",
        "name_ja": "テストケース・表示",
        "items": [
            ("TEST-000061", "tendency_expression_test", "傾向表現テスト", "Tendency Expression Test", "結果が断定ではなく傾向として表示されるか確認するテスト。"),
            ("TEST-000062", "possibility_expression_test", "可能性表現テスト", "Possibility Expression Test", "推論結果が可能性・推測として表示されるか確認するテスト。"),
            ("TEST-000063", "confidence_display_test", "信頼度表示テスト", "Confidence Display Test", "信頼度や根拠量が適切に表示されるか確認するテスト。"),
            ("TEST-000064", "context_display_test", "文脈表示テスト", "Context Display Test", "時間・場所・状態などの文脈が結果と一緒に表示されるか確認するテスト。"),
            ("TEST-000065", "explanation_display_test", "説明表示テスト", "Explanation Display Test", "使用シグナル・補正・根拠が説明されるか確認するテスト。"),
            ("TEST-000066", "alternative_explanation_test", "代替説明テスト", "Alternative Explanation Test", "一つの解釈に固定せず別の可能性も示されるか確認するテスト。"),
            ("TEST-000067", "action_suggestion_test", "行動提案テスト", "Action Suggestion Test", "次にできる小さな行動が安全に提案されるか確認するテスト。"),
            ("TEST-000068", "notification_display_test", "通知表示テスト", "Notification Display Test", "通知文言・頻度・タイミングが適切か確認するテスト。"),
            ("TEST-000069", "data_transparency_display_test", "データ透明性表示テスト", "Data Transparency Display Test", "使用データ・データ量・同意状態が確認できるか確認するテスト。"),
            ("TEST-000070", "display_integration_test", "表示統合テスト", "Display Integration Test", "結果・説明・安全性・提案が一貫して表示されるか確認するテスト。")
        ]
    },
    {
        "category": "Test Cases - App Integration",
        "name_ja": "テストケース・アプリ連携",
        "items": [
            ("TEST-000071", "diagnosis_app_integration_test", "診断アプリ連携テスト", "Diagnosis App Integration Test", "診断アプリがDBを推論材料として安全に参照できるか確認するテスト。"),
            ("TEST-000072", "game_app_integration_test", "ゲームアプリ連携テスト", "Game App Integration Test", "ゲーム行動シグナルと知識項目の接続を確認するテスト。"),
            ("TEST-000073", "assistant_app_integration_test", "秘書アプリ連携テスト", "Assistant App Integration Test", "予定・通知・タスク文脈と知識項目の接続を確認するテスト。"),
            ("TEST-000074", "education_app_integration_test", "教育アプリ連携テスト", "Education App Integration Test", "学習ログ・成績・フィードバックと知識項目の接続を確認するテスト。"),
            ("TEST-000075", "work_support_integration_test", "仕事支援連携テスト", "Work Support Integration Test", "タスク・集中・業務文脈と知識項目の接続を確認するテスト。"),
            ("TEST-000076", "wellbeing_integration_test", "ウェルビーイング連携テスト", "Wellbeing Integration Test", "睡眠・疲労・感情・回復シグナルとの接続を確認するテスト。"),
            ("TEST-000077", "relationship_app_integration_test", "人間関係アプリ連携テスト", "Relationship App Integration Test", "会話・対人反応・関係性シグナルとの接続を確認するテスト。"),
            ("TEST-000078", "personalization_integration_test", "個別化連携テスト", "Personalization Integration Test", "ユーザー文脈に応じた個別化材料取得を確認するテスト。"),
            ("TEST-000079", "multi_app_reuse_test", "複数アプリ再利用テスト", "Multi App Reuse Test", "同じ知識項目を複数アプリで一貫して参照できるか確認するテスト。"),
            ("TEST-000080", "app_integration_boundary_test", "アプリ連携境界テスト", "App Integration Boundary Test", "DB側が推論せずアプリ側で推論する境界が守られるか確認するテスト。")
        ]
    },
    {
        "category": "Test Cases - Operations",
        "name_ja": "テストケース・運用",
        "items": [
            ("TEST-000081", "git_status_clean_test", "Gitクリーン状態テスト", "Git Status Clean Test", "作業後に未追跡・未コミットの変更が残っていないか確認するテスト。"),
            ("TEST-000082", "commit_message_test", "コミットメッセージテスト", "Commit Message Test", "変更内容に合ったコミットメッセージになっているか確認するテスト。"),
            ("TEST-000083", "push_completion_test", "push完了テスト", "Push Completion Test", "ローカル変更がリモートへ反映されているか確認するテスト。"),
            ("TEST-000084", "builder_script_location_test", "Builder配置テスト", "Builder Script Location Test", "Builderスクリプトがscripts配下に正しく配置されているか確認するテスト。"),
            ("TEST-000085", "master_pack_location_test", "マスターパック配置テスト", "Master Pack Location Test", "生成JSONがdata/master_packs配下に保存されているか確認するテスト。"),
            ("TEST-000086", "generated_yaml_location_test", "生成YAML配置テスト", "Generated YAML Location Test", "生成YAMLが対応Vol配下に保存されているか確認するテスト。"),
            ("TEST-000087", "command_sequence_test", "コマンド順序テスト", "Command Sequence Test", "Builder実行・YAML生成・監査・commit・pushの順序を確認するテスト。"),
            ("TEST-000088", "accidental_file_test", "誤作成ファイルテスト", "Accidental File Test", "誤ってコマンド文字列がファイル名として作成されていないか確認するテスト。"),
            ("TEST-000089", "repository_sync_test", "リポジトリ同期テスト", "Repository Sync Test", "ローカルとorigin/mainが一致しているか確認するテスト。"),
            ("TEST-000090", "operations_integration_test", "運用統合テスト", "Operations Integration Test", "生成・監査・Git管理が一貫して完了するか確認するテスト。")
        ]
    },
    {
        "category": "Test Cases - Integration",
        "name_ja": "テストケース・統合",
        "items": [
            ("TEST-000091", "end_to_end_generation_test", "E2E生成テスト", "End to End Generation Test", "BuilderからYAML生成、監査まで一連の処理を確認するテスト。"),
            ("TEST-000092", "end_to_end_api_test", "E2E APIテスト", "End to End API Test", "知識項目取得からアプリ側利用までの流れを確認するテスト。"),
            ("TEST-000093", "end_to_end_display_test", "E2E表示テスト", "End to End Display Test", "取得材料から安全な表示までの流れを確認するテスト。"),
            ("TEST-000094", "end_to_end_safety_test", "E2E安全テスト", "End to End Safety Test", "高リスク文脈で安全補正や慎重表示が働くか確認するテスト。"),
            ("TEST-000095", "cross_volume_consistency_test", "Vol横断整合テスト", "Cross Volume Consistency Test", "複数Vol間でカテゴリ・タグ・関連が一貫しているか確認するテスト。"),
            ("TEST-000096", "large_scale_library_test", "大規模ライブラリテスト", "Large Scale Library Test", "項目数増加後も生成・検索・監査が破綻しないか確認するテスト。"),
            ("TEST-000097", "backward_compatibility_integration_test", "後方互換統合テスト", "Backward Compatibility Integration Test", "既存ID・構造・API参照が維持されるか確認するテスト。"),
            ("TEST-000098", "quality_gate_integration_test", "品質ゲート統合テスト", "Quality Gate Integration Test", "監査・安全・API・表示の条件を満たしてから進めるか確認するテスト。"),
            ("TEST-000099", "release_readiness_test", "リリース準備テスト", "Release Readiness Test", "公開やアプリ接続前に必要条件が満たされているか確認するテスト。"),
            ("TEST-000100", "test_case_integration", "テストケース統合", "Test Case Integration", "データ監査・API・表示・安全・運用テストを統合管理する枠組み。")
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
        "output_dir": "vol21_test_cases/test_cases_051_100",
        "index_filename": "test_cases_051_100_index.yml",
        "index_content": "\n".join(index_lines) + "\n",
        "items": all_items
    }

    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(json.dumps(pack, ensure_ascii=False, indent=2), encoding="utf-8")

    print(f"Created: {OUT}")
    print(f"Items: {len(all_items)}")


if __name__ == "__main__":
    main()