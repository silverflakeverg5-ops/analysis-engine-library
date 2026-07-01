import json
from pathlib import Path

OUT = Path("data/master_packs/vol18_roadmap_001_050.json")

SECTIONS = [
    {
        "category": "Roadmap - Expansion",
        "name_ja": "ロードマップ・拡張",
        "items": [
            ("ROAD-000001", "knowledge_library_expansion", "知識ライブラリ拡張", "Knowledge Library Expansion", "Knowledge Libraryを段階的に拡張していく開発方針。"),
            ("ROAD-000002", "volume_expansion_plan", "Vol拡張計画", "Volume Expansion Plan", "新しいVolを追加して知識領域を広げる計画。"),
            ("ROAD-000003", "item_count_growth_plan", "項目数拡張計画", "Item Count Growth Plan", "3000〜10000項目規模へ拡張するための項目追加計画。"),
            ("ROAD-000004", "core_quality_preservation", "基盤品質維持", "Core Quality Preservation", "項目数を増やしても基本設計と品質を維持する方針。"),
            ("ROAD-000005", "master_pack_scaling", "マスターパック拡張", "Master Pack Scaling", "100〜300項目単位でマスターパックを増やす運用方針。"),
            ("ROAD-000006", "builder_scaling", "Builder拡張", "Builder Scaling", "Builder方式で大量項目を生成・管理する開発方針。"),
            ("ROAD-000007", "audit_scaling", "監査拡張", "Audit Scaling", "項目数増加に対応して監査範囲や精度を強化する方針。"),
            ("ROAD-000008", "tag_expansion", "タグ拡張", "Tag Expansion", "後から検索・逆引きしやすいタグ体系を拡張する方針。"),
            ("ROAD-000009", "cross_link_expansion", "横断リンク拡張", "Cross Link Expansion", "Vol間のrelatedやparentを拡張して知識接続を強化する方針。"),
            ("ROAD-000010", "future_domain_addition", "将来領域追加", "Future Domain Addition", "未整備の知識領域を将来追加するための拡張方針。")
        ]
    },
    {
        "category": "Roadmap - Quality",
        "name_ja": "ロードマップ・品質",
        "items": [
            ("ROAD-000011", "quality_first_policy", "品質優先方針", "Quality First Policy", "単純な項目数増加より分析精度に貢献する知識品質を優先する方針。"),
            ("ROAD-000012", "definition_quality_plan", "定義品質計画", "Definition Quality Plan", "各項目の定義を簡潔かつ実用的に保つ計画。"),
            ("ROAD-000013", "observable_data_quality_plan", "観測データ品質計画", "Observable Data Quality Plan", "観測可能データをアプリ実装に使いやすく整える計画。"),
            ("ROAD-000014", "signal_candidate_quality_plan", "Signal候補品質計画", "Signal Candidate Quality Plan", "Signal候補を推論材料として利用しやすく整備する計画。"),
            ("ROAD-000015", "modifier_quality_plan", "補正要因品質計画", "Modifier Quality Plan", "補正要因を安全で実装しやすく整理する計画。"),
            ("ROAD-000016", "evidence_quality_plan", "根拠品質計画", "Evidence Quality Plan", "根拠種別や適用範囲を整えて信頼性を高める計画。"),
            ("ROAD-000017", "safety_quality_plan", "安全品質計画", "Safety Quality Plan", "断定・偏見・高リスク利用を避ける品質管理計画。"),
            ("ROAD-000018", "consistency_quality_plan", "整合性品質計画", "Consistency Quality Plan", "ID・タグ・カテゴリ・用語の整合性を維持する計画。"),
            ("ROAD-000019", "review_cycle_plan", "レビュー周期計画", "Review Cycle Plan", "定期的に項目・根拠・安全性を見直す計画。"),
            ("ROAD-000020", "quality_roadmap_integration", "品質ロードマップ統合", "Quality Roadmap Integration", "定義・観測・根拠・安全性を統合して品質を高める方針。")
        ]
    },
    {
        "category": "Roadmap - App Integration",
        "name_ja": "ロードマップ・アプリ連携",
        "items": [
            ("ROAD-000021", "diagnosis_app_integration_plan", "診断アプリ連携計画", "Diagnosis App Integration Plan", "診断アプリがKnowledge Libraryを推論材料として使うための計画。"),
            ("ROAD-000022", "game_app_integration_plan", "ゲームアプリ連携計画", "Game App Integration Plan", "ゲーム内行動からシグナルを取得し知識DBと接続する計画。"),
            ("ROAD-000023", "assistant_app_integration_plan", "秘書アプリ連携計画", "Assistant App Integration Plan", "予定・通知・生活文脈とKnowledge Libraryを接続する計画。"),
            ("ROAD-000024", "education_app_integration_plan", "教育アプリ連携計画", "Education App Integration Plan", "学習ログ・教材・フィードバックと知識DBを接続する計画。"),
            ("ROAD-000025", "work_support_integration_plan", "仕事支援連携計画", "Work Support Integration Plan", "タスク・集中・業務文脈とKnowledge Libraryを接続する計画。"),
            ("ROAD-000026", "wellbeing_integration_plan", "ウェルビーイング連携計画", "Wellbeing Integration Plan", "睡眠・疲労・感情・回復支援と知識DBを接続する計画。"),
            ("ROAD-000027", "multi_app_reuse_plan", "複数アプリ再利用計画", "Multi App Reuse Plan", "共通知識DBを複数アプリで再利用する計画。"),
            ("ROAD-000028", "app_side_inference_plan", "アプリ側推論計画", "App Side Inference Plan", "推論・スコアリング・表示を各アプリ側で実装する計画。"),
            ("ROAD-000029", "api_connection_plan", "API接続計画", "API Connection Plan", "Knowledge Libraryをアプリから参照しやすくする接続設計。"),
            ("ROAD-000030", "app_integration_roadmap", "アプリ連携ロードマップ", "App Integration Roadmap", "複数アプリとKnowledge Libraryの連携を段階的に進める計画。")
        ]
    },
    {
        "category": "Roadmap - Operations",
        "name_ja": "ロードマップ・運用",
        "items": [
            ("ROAD-000031", "generation_workflow_plan", "生成ワークフロー計画", "Generation Workflow Plan", "Builder・master_pack・YAML生成を安定運用する計画。"),
            ("ROAD-000032", "audit_workflow_plan", "監査ワークフロー計画", "Audit Workflow Plan", "生成後に監査を実行し品質確認する運用計画。"),
            ("ROAD-000033", "git_workflow_plan", "Git運用計画", "Git Workflow Plan", "変更をcommit・pushして履歴管理する運用計画。"),
            ("ROAD-000034", "release_cycle_plan", "リリースサイクル計画", "Release Cycle Plan", "一定単位でKnowledge Libraryを更新・公開する計画。"),
            ("ROAD-000035", "backup_plan", "バックアップ計画", "Backup Plan", "データ消失を防ぐために保存・復元手段を確保する計画。"),
            ("ROAD-000036", "storage_management_plan", "保存容量管理計画", "Storage Management Plan", "容量を無駄に増やさず管理する運用計画。"),
            ("ROAD-000037", "script_maintenance_plan", "スクリプト保守計画", "Script Maintenance Plan", "Builder・生成・監査スクリプトを保守する計画。"),
            ("ROAD-000038", "documentation_plan", "文書化計画", "Documentation Plan", "構造・手順・方針を文書として残す計画。"),
            ("ROAD-000039", "handoff_plan", "引継ぎ計画", "Handoff Plan", "チャットや作業環境をまたいで進捗を引き継ぐ計画。"),
            ("ROAD-000040", "operation_roadmap_integration", "運用ロードマップ統合", "Operation Roadmap Integration", "生成・監査・Git・文書化を統合して進める運用方針。")
        ]
    },
    {
        "category": "Roadmap - Milestones",
        "name_ja": "ロードマップ・マイルストーン",
        "items": [
            ("ROAD-000041", "foundation_complete_milestone", "基盤完成マイルストーン", "Foundation Complete Milestone", "基本設計・Builder・監査・主要Volが整った状態。"),
            ("ROAD-000042", "one_thousand_items_milestone", "1000項目マイルストーン", "One Thousand Items Milestone", "Knowledge Libraryが1000項目規模に到達した状態。"),
            ("ROAD-000043", "three_thousand_items_milestone", "3000項目マイルストーン", "Three Thousand Items Milestone", "実用的な分析アプリに使える知識量へ到達した状態。"),
            ("ROAD-000044", "ten_thousand_items_milestone", "10000項目マイルストーン", "Ten Thousand Items Milestone", "大規模Knowledge Libraryとして多用途に対応できる状態。"),
            ("ROAD-000045", "first_app_connection_milestone", "初回アプリ接続マイルストーン", "First App Connection Milestone", "最初のアプリがKnowledge Libraryを参照できる状態。"),
            ("ROAD-000046", "signal_mapping_milestone", "シグナル対応付けマイルストーン", "Signal Mapping Milestone", "観測シグナルと知識項目の対応付けが整った状態。"),
            ("ROAD-000047", "modifier_mapping_milestone", "補正対応付けマイルストーン", "Modifier Mapping Milestone", "補正要因と推論材料の対応付けが整った状態。"),
            ("ROAD-000048", "display_mapping_milestone", "表示対応付けマイルストーン", "Display Mapping Milestone", "表示設計と用途・安全性の対応付けが整った状態。"),
            ("ROAD-000049", "safety_review_milestone", "安全レビュー完了マイルストーン", "Safety Review Milestone", "安全倫理・表示・補正がレビュー済みの状態。"),
            ("ROAD-000050", "roadmap_integration", "ロードマップ統合", "Roadmap Integration", "拡張・品質・アプリ連携・運用・マイルストーンを統合管理する枠組み。")
        ]
    }
]


def make_item(item_id, slug, name_ja, name_en, definition_ja, category, parent_ja):
    return {
        "filename": f"{item_id}_{slug}.yml",
        "id": item_id,
        "knowledge_type": "roadmap",
        "name_ja": name_ja,
        "name_en": name_en,
        "category": "Roadmap",
        "attribute": category.replace("Roadmap - ", ""),
        "definition_ja": definition_ja,
        "tags": ["CAT:ロードマップ", f"CAT:{parent_ja}", "ATTR:開発計画"],
        "parent": [parent_ja],
        "related": ["ライブラリ管理", "アプリ用途", "監査"],
        "observable_data": [
            f"{name_ja}進捗",
            f"{name_ja}対象範囲",
            f"{name_ja}完了条件",
            f"{name_ja}依存関係"
        ],
        "signal_candidates": [
            f"{name_ja}を開発計画として利用できる",
            "Knowledge Libraryの拡張・品質・運用を管理する材料になる"
        ],
        "device_level": "DB管理用",
        "modifiers": ["優先度", "進捗", "依存関係", "品質"],
        "evidence": "プロジェクト管理・ナレッジマネジメント・ソフトウェア開発運用で使用",
        "status": "active"
    }


def main():
    all_items = []
    index_lines = ["category: Roadmap", "name_ja: ロードマップ", "items:"]

    for section in SECTIONS:
        parent_ja = section["name_ja"].replace("ロードマップ・", "")
        for raw in section["items"]:
            item = make_item(*raw, category=section["category"], parent_ja=parent_ja)
            all_items.append(item)
            index_lines.append(f"  - {item['filename']}")

    index_lines.extend([
        "notes:",
        "  - ロードマップは開発計画と管理材料として扱う",
        "  - Knowledge DB側では推論しない",
        "  - 今後の拡張・品質管理・アプリ接続に利用する"
    ])

    pack = {
        "output_dir": "vol18_roadmap/roadmap_001_050",
        "index_filename": "roadmap_001_050_index.yml",
        "index_content": "\n".join(index_lines) + "\n",
        "items": all_items
    }

    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(json.dumps(pack, ensure_ascii=False, indent=2), encoding="utf-8")

    print(f"Created: {OUT}")
    print(f"Items: {len(all_items)}")


if __name__ == "__main__":
    main()