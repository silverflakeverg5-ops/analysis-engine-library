import json
from pathlib import Path

OUT = Path("data/master_packs/vol19_mapping_rules_051_100.json")

SECTIONS = [
    {
        "category": "Mapping Rules - Concept Linking",
        "name_ja": "対応ルール・概念接続",
        "items": [
            ("MAP-000051", "concept_to_concept_mapping", "概念間対応", "Concept to Concept Mapping", "関連する知識概念同士を対応づけるルール。"),
            ("MAP-000052", "concept_to_observable_mapping", "概念観測対応", "Concept to Observable Mapping", "知識概念を観測可能データへ対応づけるルール。"),
            ("MAP-000053", "concept_to_modifier_mapping", "概念補正対応", "Concept to Modifier Mapping", "知識概念に必要な補正要因を対応づけるルール。"),
            ("MAP-000054", "concept_to_evidence_mapping", "概念根拠対応", "Concept to Evidence Mapping", "知識概念を根拠種別や研究領域へ対応づけるルール。"),
            ("MAP-000055", "concept_to_app_use_case_mapping", "概念用途対応", "Concept to App Use Case Mapping", "知識概念を利用可能なアプリ用途へ対応づけるルール。"),
            ("MAP-000056", "parent_child_mapping", "親子概念対応", "Parent Child Mapping", "上位概念と下位概念の関係を対応づけるルール。"),
            ("MAP-000057", "related_concept_mapping", "関連概念対応", "Related Concept Mapping", "横断的に関連する概念同士を対応づけるルール。"),
            ("MAP-000058", "near_duplicate_mapping", "近接概念対応", "Near Duplicate Mapping", "似ているが統合しない概念同士を関連として扱うルール。"),
            ("MAP-000059", "concept_scope_mapping", "概念範囲対応", "Concept Scope Mapping", "概念の適用範囲や限界条件を対応づけるルール。"),
            ("MAP-000060", "concept_linking_integration", "概念接続統合", "Concept Linking Integration", "知識概念同士の接続を統合管理する枠組み。")
        ]
    },
    {
        "category": "Mapping Rules - Evidence Mapping",
        "name_ja": "対応ルール・根拠対応",
        "items": [
            ("MAP-000061", "evidence_strength_mapping", "根拠強度対応", "Evidence Strength Mapping", "知識項目に対する根拠の強さを対応づけるルール。"),
            ("MAP-000062", "evidence_type_mapping", "根拠種別対応", "Evidence Type Mapping", "研究設計・データ種別・測定根拠を知識項目へ対応づけるルール。"),
            ("MAP-000063", "evidence_quality_mapping", "根拠品質対応", "Evidence Quality Mapping", "信頼性・妥当性・再現性を知識項目へ対応づけるルール。"),
            ("MAP-000064", "evidence_limitation_mapping", "根拠限界対応", "Evidence Limitation Mapping", "根拠の適用範囲や限界を知識項目へ対応づけるルール。"),
            ("MAP-000065", "evidence_update_mapping", "根拠更新対応", "Evidence Update Mapping", "根拠の更新必要性や見直し周期を対応づけるルール。"),
            ("MAP-000066", "evidence_domain_mapping", "根拠領域対応", "Evidence Domain Mapping", "心理学・認知科学・神経科学などの根拠領域を対応づけるルール。"),
            ("MAP-000067", "evidence_to_display_mapping", "根拠表示対応", "Evidence to Display Mapping", "根拠の強さや種類を表示設計へ対応づけるルール。"),
            ("MAP-000068", "evidence_to_confidence_mapping", "根拠信頼度対応", "Evidence to Confidence Mapping", "根拠品質を推論信頼度の材料へ対応づけるルール。"),
            ("MAP-000069", "evidence_to_safety_mapping", "根拠安全対応", "Evidence to Safety Mapping", "根拠が弱い場合に安全表現や慎重表示へ対応づけるルール。"),
            ("MAP-000070", "evidence_mapping_integration", "根拠対応統合", "Evidence Mapping Integration", "根拠情報と知識項目・表示・信頼度を統合する枠組み。")
        ]
    },
    {
        "category": "Mapping Rules - Safety Mapping",
        "name_ja": "対応ルール・安全対応",
        "items": [
            ("MAP-000071", "risk_to_guardrail_mapping", "リスクガードレール対応", "Risk to Guardrail Mapping", "観測されたリスクを安全ガードレールへ対応づけるルール。"),
            ("MAP-000072", "sensitive_context_mapping", "機微文脈対応", "Sensitive Context Mapping", "健康・未成年・人間関係など慎重文脈を安全制御へ対応づけるルール。"),
            ("MAP-000073", "privacy_risk_mapping", "プライバシーリスク対応", "Privacy Risk Mapping", "個人情報や機微情報の扱いを安全制御へ対応づけるルール。"),
            ("MAP-000074", "high_stakes_mapping", "高リスク用途対応", "High Stakes Mapping", "重大判断に関わる用途を慎重表示や利用制限へ対応づけるルール。"),
            ("MAP-000075", "minor_safety_mapping", "未成年安全対応", "Minor Safety Mapping", "未成年利用文脈を安全表示・同意・制限へ対応づけるルール。"),
            ("MAP-000076", "distress_safety_mapping", "苦痛安全対応", "Distress Safety Mapping", "強い苦痛表現を安全導線や慎重応答へ対応づけるルール。"),
            ("MAP-000077", "non_diagnostic_mapping", "非診断対応", "Non Diagnostic Mapping", "診断的に見える結果を非診断表現へ対応づけるルール。"),
            ("MAP-000078", "labeling_risk_mapping", "ラベリングリスク対応", "Labeling Risk Mapping", "固定的ラベル化を避ける表示や補正へ対応づけるルール。"),
            ("MAP-000079", "manipulation_risk_mapping", "操作リスク対応", "Manipulation Risk Mapping", "過度な誘導や依存を避ける制御へ対応づけるルール。"),
            ("MAP-000080", "safety_mapping_integration", "安全対応統合", "Safety Mapping Integration", "リスク・用途・表示・補正を安全制御へ統合する枠組み。")
        ]
    },
    {
        "category": "Mapping Rules - Data Pipeline Mapping",
        "name_ja": "対応ルール・データ処理対応",
        "items": [
            ("MAP-000081", "raw_data_to_signal_mapping", "生データシグナル対応", "Raw Data to Signal Mapping", "操作ログや入力データを観測シグナルへ変換する対応ルール。"),
            ("MAP-000082", "signal_to_feature_mapping", "シグナル特徴量対応", "Signal to Feature Mapping", "観測シグナルをアプリ側特徴量へ対応づけるルール。"),
            ("MAP-000083", "feature_to_inference_material_mapping", "特徴量推論材料対応", "Feature to Inference Material Mapping", "特徴量を推論材料として使える形へ対応づけるルール。"),
            ("MAP-000084", "baseline_calculation_mapping", "ベースライン算出対応", "Baseline Calculation Mapping", "本人通常傾向を算出するための対応ルール。"),
            ("MAP-000085", "normalization_mapping", "正規化対応", "Normalization Mapping", "端末差・個人差・単位差をそろえるための対応ルール。"),
            ("MAP-000086", "aggregation_window_mapping", "集計期間対応", "Aggregation Window Mapping", "日次・週次・月次など集計期間を対応づけるルール。"),
            ("MAP-000087", "missing_data_handling_mapping", "欠損処理対応", "Missing Data Handling Mapping", "欠損データを補正・除外・低信頼化する対応ルール。"),
            ("MAP-000088", "outlier_handling_mapping", "外れ値処理対応", "Outlier Handling Mapping", "外れ値を検出し推論材料として扱うか調整するルール。"),
            ("MAP-000089", "data_quality_to_confidence_mapping", "データ品質信頼度対応", "Data Quality to Confidence Mapping", "データ品質を推論信頼度へ反映する対応ルール。"),
            ("MAP-000090", "data_pipeline_mapping_integration", "データ処理対応統合", "Data Pipeline Mapping Integration", "生データから推論材料までの対応を統合管理する枠組み。")
        ]
    },
    {
        "category": "Mapping Rules - Governance Mapping",
        "name_ja": "対応ルール・管理対応",
        "items": [
            ("MAP-000091", "mapping_to_audit_mapping", "対応監査接続", "Mapping to Audit Mapping", "対応ルールを監査対象へ接続する管理ルール。"),
            ("MAP-000092", "mapping_to_schema_mapping", "対応スキーマ接続", "Mapping to Schema Mapping", "対応ルールをスキーマ項目や必須フィールドへ接続する管理ルール。"),
            ("MAP-000093", "mapping_to_version_mapping", "対応版管理接続", "Mapping to Version Mapping", "対応ルール変更をバージョン管理へ接続するルール。"),
            ("MAP-000094", "mapping_to_release_mapping", "対応リリース接続", "Mapping to Release Mapping", "対応ルールをリリース単位や変更履歴へ接続する管理ルール。"),
            ("MAP-000095", "mapping_to_documentation_mapping", "対応文書化接続", "Mapping to Documentation Mapping", "対応ルールを説明資料や仕様へ接続する管理ルール。"),
            ("MAP-000096", "mapping_to_test_mapping", "対応テスト接続", "Mapping to Test Mapping", "対応ルールをテストケースや検証条件へ接続する管理ルール。"),
            ("MAP-000097", "mapping_to_app_contract_mapping", "対応アプリ契約接続", "Mapping to App Contract Mapping", "アプリ側が参照する対応ルールの入出力契約を管理するルール。"),
            ("MAP-000098", "mapping_to_library_boundary_mapping", "対応境界接続", "Mapping to Library Boundary Mapping", "DB側材料提供とアプリ側推論の境界を対応ルールに反映する管理。"),
            ("MAP-000099", "mapping_to_quality_gate_mapping", "対応品質ゲート接続", "Mapping to Quality Gate Mapping", "対応ルールの品質確認条件を管理するルール。"),
            ("MAP-000100", "governance_mapping_integration", "管理対応統合", "Governance Mapping Integration", "対応ルールの監査・版管理・テスト・文書化を統合する枠組み。")
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
        "output_dir": "vol19_mapping_rules/mapping_rules_051_100",
        "index_filename": "mapping_rules_051_100_index.yml",
        "index_content": "\n".join(index_lines) + "\n",
        "items": all_items
    }

    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(json.dumps(pack, ensure_ascii=False, indent=2), encoding="utf-8")

    print(f"Created: {OUT}")
    print(f"Items: {len(all_items)}")


if __name__ == "__main__":
    main()