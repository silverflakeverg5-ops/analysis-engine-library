import json
from pathlib import Path

OUT = Path("data/master_packs/vol19_mapping_rules_001_050.json")

SECTIONS = [
    {
        "category": "Mapping Rules - Signal Mapping",
        "name_ja": "対応ルール・シグナル対応",
        "items": [
            ("MAP-000001", "signal_to_concept_mapping", "シグナル概念対応", "Signal to Concept Mapping", "観測シグナルを関連する知識概念へ対応づけるルール。"),
            ("MAP-000002", "signal_to_behavior_mapping", "シグナル行動対応", "Signal to Behavior Mapping", "観測シグナルを行動パターン項目へ対応づけるルール。"),
            ("MAP-000003", "signal_to_personality_mapping", "シグナル性格対応", "Signal to Personality Mapping", "観測シグナルを性格傾向の推論材料へ対応づけるルール。"),
            ("MAP-000004", "signal_to_state_mapping", "シグナル状態対応", "Signal to State Mapping", "観測シグナルを一時的状態の推論材料へ対応づけるルール。"),
            ("MAP-000005", "signal_to_context_mapping", "シグナル文脈対応", "Signal to Context Mapping", "観測シグナルを時間・場所・課題などの文脈へ対応づけるルール。"),
            ("MAP-000006", "multi_signal_mapping", "複合シグナル対応", "Multi Signal Mapping", "複数シグナルの同時変化を知識項目へ対応づけるルール。"),
            ("MAP-000007", "baseline_deviation_mapping", "ベースライン乖離対応", "Baseline Deviation Mapping", "本人の通常傾向からのズレを推論材料へ対応づけるルール。"),
            ("MAP-000008", "trend_mapping", "時系列傾向対応", "Trend Mapping", "長期的な増減や安定傾向を知識項目へ対応づけるルール。"),
            ("MAP-000009", "anomaly_mapping", "異常値対応", "Anomaly Mapping", "短期的な外れ値や急変を状態変化材料へ対応づけるルール。"),
            ("MAP-000010", "signal_mapping_integration", "シグナル対応統合", "Signal Mapping Integration", "観測シグナルと知識項目の対応づけ全体を管理する枠組み。")
        ]
    },
    {
        "category": "Mapping Rules - Modifier Mapping",
        "name_ja": "対応ルール・補正対応",
        "items": [
            ("MAP-000011", "context_modifier_mapping", "文脈補正対応", "Context Modifier Mapping", "時間・場所・端末・課題文脈に応じて補正要因を対応づけるルール。"),
            ("MAP-000012", "state_modifier_mapping", "状態補正対応", "State Modifier Mapping", "睡眠・疲労・ストレスなどの状態要因を対応づけるルール。"),
            ("MAP-000013", "data_quality_modifier_mapping", "データ品質補正対応", "Data Quality Modifier Mapping", "欠損・ノイズ・サンプル数に応じて補正要因を対応づけるルール。"),
            ("MAP-000014", "individual_modifier_mapping", "個人差補正対応", "Individual Difference Modifier Mapping", "年齢・経験・文化・技能水準に応じて補正要因を対応づけるルール。"),
            ("MAP-000015", "safety_modifier_mapping", "安全補正対応", "Safety Modifier Mapping", "プライバシー・高リスク・未成年などの安全補正を対応づけるルール。"),
            ("MAP-000016", "app_domain_modifier_mapping", "アプリ領域補正対応", "App Domain Modifier Mapping", "診断・ゲーム・秘書・教育など用途別補正を対応づけるルール。"),
            ("MAP-000017", "temporal_modifier_mapping", "時系列補正対応", "Temporal Modifier Mapping", "短期状態・長期傾向・変化点を補正要因へ対応づけるルール。"),
            ("MAP-000018", "social_modifier_mapping", "社会補正対応", "Social Modifier Mapping", "公開性・関係性・権威・集団規範を補正要因へ対応づけるルール。"),
            ("MAP-000019", "modifier_priority_mapping", "補正優先度対応", "Modifier Priority Mapping", "複数補正要因の適用優先度を対応づけるルール。"),
            ("MAP-000020", "modifier_mapping_integration", "補正対応統合", "Modifier Mapping Integration", "補正要因と推論材料の対応づけ全体を管理する枠組み。")
        ]
    },
    {
        "category": "Mapping Rules - Display Mapping",
        "name_ja": "対応ルール・表示対応",
        "items": [
            ("MAP-000021", "result_to_display_mapping", "結果表示対応", "Result to Display Mapping", "推論結果を適切な表示形式へ対応づけるルール。"),
            ("MAP-000022", "confidence_to_display_mapping", "信頼度表示対応", "Confidence to Display Mapping", "信頼度に応じて表示の強さや説明量を変えるルール。"),
            ("MAP-000023", "uncertainty_to_expression_mapping", "不確実性表現対応", "Uncertainty to Expression Mapping", "不確実性が高い場合に慎重な表現へ対応づけるルール。"),
            ("MAP-000024", "safety_to_display_mapping", "安全表示対応", "Safety to Display Mapping", "安全リスクに応じて非断定・支援的表現へ対応づけるルール。"),
            ("MAP-000025", "app_use_case_display_mapping", "用途別表示対応", "App Use Case Display Mapping", "アプリ用途に応じて表示設計を対応づけるルール。"),
            ("MAP-000026", "signal_explanation_mapping", "シグナル説明対応", "Signal Explanation Mapping", "使用シグナルをユーザー向け説明へ対応づけるルール。"),
            ("MAP-000027", "modifier_explanation_mapping", "補正説明対応", "Modifier Explanation Mapping", "補正要因をユーザー向け説明へ対応づけるルール。"),
            ("MAP-000028", "action_suggestion_mapping", "行動提案対応", "Action Suggestion Mapping", "結果や状態に応じて小さな次アクションへ対応づけるルール。"),
            ("MAP-000029", "notification_mapping", "通知対応", "Notification Mapping", "文脈や状態に応じて通知タイミング・内容を対応づけるルール。"),
            ("MAP-000030", "display_mapping_integration", "表示対応統合", "Display Mapping Integration", "推論材料・安全性・用途を表示設計へ接続する枠組み。")
        ]
    },
    {
        "category": "Mapping Rules - App Mapping",
        "name_ja": "対応ルール・アプリ対応",
        "items": [
            ("MAP-000031", "diagnosis_app_mapping", "診断アプリ対応", "Diagnosis App Mapping", "診断アプリで利用する知識・シグナル・表示を対応づけるルール。"),
            ("MAP-000032", "game_app_mapping", "ゲームアプリ対応", "Game App Mapping", "ゲーム行動から取得するシグナルと知識項目を対応づけるルール。"),
            ("MAP-000033", "assistant_app_mapping", "秘書アプリ対応", "Assistant App Mapping", "予定・タスク・通知文脈と知識項目を対応づけるルール。"),
            ("MAP-000034", "education_app_mapping", "教育アプリ対応", "Education App Mapping", "学習ログ・教材・評価と知識項目を対応づけるルール。"),
            ("MAP-000035", "work_support_mapping", "仕事支援対応", "Work Support Mapping", "業務・集中・タスク管理のシグナルを知識項目へ対応づけるルール。"),
            ("MAP-000036", "wellbeing_app_mapping", "ウェルビーイング対応", "Wellbeing App Mapping", "睡眠・疲労・感情・回復系シグナルを知識項目へ対応づけるルール。"),
            ("MAP-000037", "relationship_app_mapping", "人間関係アプリ対応", "Relationship App Mapping", "対人反応や会話シグナルを知識項目へ対応づけるルール。"),
            ("MAP-000038", "personalization_mapping", "個別化対応", "Personalization Mapping", "ユーザー状態や嗜好に応じて個別化材料を対応づけるルール。"),
            ("MAP-000039", "cross_app_mapping", "複数アプリ横断対応", "Cross App Mapping", "複数アプリで共通知識を再利用するための対応ルール。"),
            ("MAP-000040", "app_mapping_integration", "アプリ対応統合", "App Mapping Integration", "アプリ用途と知識DBの接続を統合管理する枠組み。")
        ]
    },
    {
        "category": "Mapping Rules - Integration",
        "name_ja": "対応ルール・統合",
        "items": [
            ("MAP-000041", "mapping_schema", "対応スキーマ", "Mapping Schema", "シグナル・知識・補正・表示の対応関係を表す構造定義。"),
            ("MAP-000042", "mapping_confidence", "対応信頼度", "Mapping Confidence", "対応づけの根拠量や一貫性を示す信頼度概念。"),
            ("MAP-000043", "mapping_priority", "対応優先度", "Mapping Priority", "複数対応候補がある場合の優先順位を管理する概念。"),
            ("MAP-000044", "mapping_conflict_resolution", "対応競合解決", "Mapping Conflict Resolution", "矛盾する対応候補を調整するための管理概念。"),
            ("MAP-000045", "mapping_audit", "対応監査", "Mapping Audit", "対応ルールが安全・一貫・妥当か確認する監査。"),
            ("MAP-000046", "mapping_versioning", "対応ルール版管理", "Mapping Versioning", "対応ルールの変更履歴と互換性を管理する考え方。"),
            ("MAP-000047", "mapping_test_case", "対応テストケース", "Mapping Test Case", "観測入力から期待される対応結果を確認するテスト材料。"),
            ("MAP-000048", "mapping_update_cycle", "対応更新サイクル", "Mapping Update Cycle", "アプリ実装や観測結果に応じて対応ルールを見直す周期。"),
            ("MAP-000049", "mapping_library_boundary", "対応ライブラリ境界", "Mapping Library Boundary", "DBは対応材料を持つが推論処理はアプリ側で行う境界管理。"),
            ("MAP-000050", "mapping_rules_integration", "対応ルール統合", "Mapping Rules Integration", "シグナル・補正・表示・アプリ接続を統合する対応管理枠組み。")
        ]
    }
]


def make_item(item_id, slug, name_ja, name_en, definition_ja, category, parent_ja):
    return {
        "filename": f"{item_id}_{slug}.yml",
        "id": item_id,
        "knowledge_type": "mapping_rule",
        "name_ja": name_ja,
        "name_en": name_en,
        "category": "Mapping Rule",
        "attribute": category.replace("Mapping Rules - ", ""),
        "definition_ja": definition_ja,
        "tags": ["CAT:対応ルール", f"CAT:{parent_ja}", "ATTR:接続設計"],
        "parent": [parent_ja],
        "related": ["観測シグナル", "補正要因", "表示設計"],
        "observable_data": [
            f"{name_ja}入力条件",
            f"{name_ja}対応先",
            f"{name_ja}信頼度",
            f"{name_ja}適用範囲"
        ],
        "signal_candidates": [
            f"{name_ja}を対応ルールとして利用できる",
            "Knowledge DBとアプリ側推論を接続する材料になる"
        ],
        "device_level": "DB管理用",
        "modifiers": ["用途", "信頼度", "安全性", "文脈"],
        "evidence": "情報設計・HCI・知識工学・アプリ設計で使用",
        "status": "active"
    }


def main():
    all_items = []
    index_lines = ["category: Mapping Rule", "name_ja: 対応ルール", "items:"]

    for section in SECTIONS:
        parent_ja = section["name_ja"].replace("対応ルール・", "")
        for raw in section["items"]:
            item = make_item(*raw, category=section["category"], parent_ja=parent_ja)
            all_items.append(item)
            index_lines.append(f"  - {item['filename']}")

    index_lines.extend([
        "notes:",
        "  - 対応ルールはDBとアプリ推論を接続する管理材料として扱う",
        "  - Knowledge DB側ではスコアリングしない",
        "  - アプリ側で対応ルールを参照して推論・表示・補正を行う"
    ])

    pack = {
        "output_dir": "vol19_mapping_rules/mapping_rules_001_050",
        "index_filename": "mapping_rules_001_050_index.yml",
        "index_content": "\n".join(index_lines) + "\n",
        "items": all_items
    }

    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(json.dumps(pack, ensure_ascii=False, indent=2), encoding="utf-8")

    print(f"Created: {OUT}")
    print(f"Items: {len(all_items)}")


if __name__ == "__main__":
    main()