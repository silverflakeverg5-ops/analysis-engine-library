import json
from pathlib import Path

OUT = Path("data/master_packs/vol16_safety_ethics_051_100.json")

SECTIONS = [
    {
        "category": "Safety Ethics - Consent Control",
        "name_ja": "安全倫理・同意制御",
        "items": [
            ("SAFE-000051", "explicit_consent", "明示的同意", "Explicit Consent", "データ利用や推論表示についてユーザーが明確に同意する仕組み。"),
            ("SAFE-000052", "granular_consent", "細分化同意", "Granular Consent", "データ種別・用途・表示範囲ごとに同意を分けて管理する考え方。"),
            ("SAFE-000053", "withdrawal_of_consent", "同意撤回", "Withdrawal of Consent", "ユーザーがいつでも同意を取り消せる仕組み。"),
            ("SAFE-000054", "consent_refresh", "同意再確認", "Consent Refresh", "時間経過や用途変更時に同意を再確認する設計。"),
            ("SAFE-000055", "informed_consent_display", "説明付き同意表示", "Informed Consent Display", "何に使われるかを理解できる形で同意を求める表示設計。"),
            ("SAFE-000056", "default_privacy_protection", "初期プライバシー保護", "Default Privacy Protection", "初期設定で過剰なデータ利用を避ける安全設計。"),
            ("SAFE-000057", "optional_data_use", "任意データ利用", "Optional Data Use", "追加データ提供を必須にせず任意で扱う設計。"),
            ("SAFE-000058", "consent_scope_clarity", "同意範囲明確化", "Consent Scope Clarity", "ユーザーが何に同意しているか明確にする管理概念。"),
            ("SAFE-000059", "consent_log_management", "同意ログ管理", "Consent Log Management", "同意・撤回・変更履歴を管理する仕組み。"),
            ("SAFE-000060", "consent_control_integration", "同意制御統合", "Consent Control Integration", "同意取得・撤回・範囲管理を統合して扱う枠組み。")
        ]
    },
    {
        "category": "Safety Ethics - Transparency",
        "name_ja": "安全倫理・透明性",
        "items": [
            ("SAFE-000061", "data_transparency", "データ透明性", "Data Transparency", "どのデータがどの目的で使われたか分かるようにする考え方。"),
            ("SAFE-000062", "inference_transparency", "推論透明性", "Inference Transparency", "推論結果がどの材料から作られたか説明可能にする考え方。"),
            ("SAFE-000063", "limitation_transparency", "限界透明性", "Limitation Transparency", "推論や表示の限界を明示する安全設計。"),
            ("SAFE-000064", "uncertainty_transparency", "不確実性透明性", "Uncertainty Transparency", "結果の確信度や曖昧さをユーザーに示す考え方。"),
            ("SAFE-000065", "model_boundary_transparency", "モデル境界透明性", "Model Boundary Transparency", "システムができることとできないことを明確にする設計。"),
            ("SAFE-000066", "data_source_display", "データソース表示", "Data Source Display", "使用したデータ源をユーザーに示す表示設計。"),
            ("SAFE-000067", "reason_code_display", "理由コード表示", "Reason Code Display", "推論に使われた主要理由を簡潔に示す表示設計。"),
            ("SAFE-000068", "audit_trail_visibility", "監査経路可視化", "Audit Trail Visibility", "データ利用や表示判断の履歴を確認できる状態。"),
            ("SAFE-000069", "user_facing_explanation", "ユーザー向け説明", "User Facing Explanation", "技術的詳細を平易な言葉で説明する設計。"),
            ("SAFE-000070", "transparency_integration", "透明性統合", "Transparency Integration", "データ・推論・限界・同意を統合して説明する枠組み。")
        ]
    },
    {
        "category": "Safety Ethics - User Control",
        "name_ja": "安全倫理・ユーザー制御",
        "items": [
            ("SAFE-000071", "user_editable_profile", "ユーザー編集可能プロフィール", "User Editable Profile", "ユーザーが自分に関する推論前提を確認・修正できる設計。"),
            ("SAFE-000072", "result_correction", "結果修正", "Result Correction", "ユーザーが推論結果に対して違う・近いなどの修正を返せる仕組み。"),
            ("SAFE-000073", "preference_control", "嗜好制御", "Preference Control", "通知・表示・提案の好みをユーザーが調整できる仕組み。"),
            ("SAFE-000074", "personalization_toggle", "個別化オンオフ", "Personalization Toggle", "個別化機能をユーザーが有効化・無効化できる設計。"),
            ("SAFE-000075", "data_delete_control", "データ削除制御", "Data Delete Control", "ユーザーが自分のデータ削除を行える仕組み。"),
            ("SAFE-000076", "data_export_control", "データ確認制御", "Data Export Control", "ユーザーが自分のデータを確認・取得できる仕組み。"),
            ("SAFE-000077", "notification_control", "通知制御", "Notification Control", "通知頻度・種類・時間帯をユーザーが調整できる設計。"),
            ("SAFE-000078", "analysis_pause_control", "分析停止制御", "Analysis Pause Control", "一時的に分析や観測利用を停止できる仕組み。"),
            ("SAFE-000079", "user_override", "ユーザー上書き", "User Override", "システム推論よりユーザー修正を優先できる設計。"),
            ("SAFE-000080", "user_control_integration", "ユーザー制御統合", "User Control Integration", "修正・停止・削除・個別化制御を統合して扱う枠組み。")
        ]
    },
    {
        "category": "Safety Ethics - Audit Governance",
        "name_ja": "安全倫理・監査統制",
        "items": [
            ("SAFE-000081", "knowledge_item_audit", "知識項目監査", "Knowledge Item Audit", "知識項目の定義・根拠・安全性を確認する管理過程。"),
            ("SAFE-000082", "bias_audit", "バイアス監査", "Bias Audit", "知識・データ・表示に含まれる偏りを確認する過程。"),
            ("SAFE-000083", "privacy_audit", "プライバシー監査", "Privacy Audit", "データ利用や表示がプライバシーを侵害しないか確認する過程。"),
            ("SAFE-000084", "display_safety_audit", "表示安全監査", "Display Safety Audit", "結果表示が断定的・不安誘発的・不公平でないか確認する過程。"),
            ("SAFE-000085", "high_risk_review", "高リスクレビュー", "High Risk Review", "重大判断や機微領域に関わる用途を追加確認する過程。"),
            ("SAFE-000086", "versioned_safety_policy", "安全方針バージョン管理", "Versioned Safety Policy", "安全方針や表示方針の変更履歴を管理する考え方。"),
            ("SAFE-000087", "incident_review", "インシデントレビュー", "Incident Review", "不適切表示や有害影響が起きた場合に原因と対策を確認する過程。"),
            ("SAFE-000088", "human_in_the_loop_review", "人間参加レビュー", "Human in the Loop Review", "必要時に人間が推論や表示の妥当性を確認する仕組み。"),
            ("SAFE-000089", "governance_documentation", "統制文書化", "Governance Documentation", "安全ルール・責任範囲・監査結果を文書化する管理。"),
            ("SAFE-000090", "audit_governance_integration", "監査統制統合", "Audit Governance Integration", "監査・レビュー・文書化・改善を統合して管理する枠組み。")
        ]
    },
    {
        "category": "Safety Ethics - Deployment Boundaries",
        "name_ja": "安全倫理・運用境界",
        "items": [
            ("SAFE-000091", "entertainment_boundary", "エンタメ用途境界", "Entertainment Boundary", "診断風コンテンツを娯楽として扱うための境界設計。"),
            ("SAFE-000092", "education_boundary", "教育用途境界", "Education Boundary", "学習支援を成績断定や能力固定化に使わないための境界設計。"),
            ("SAFE-000093", "workplace_boundary", "職場用途境界", "Workplace Boundary", "職場支援を人事評価や選別に直結させないための境界設計。"),
            ("SAFE-000094", "wellbeing_boundary", "ウェルビーイング境界", "Wellbeing Boundary", "健康支援を医療診断や治療判断にしないための境界設計。"),
            ("SAFE-000095", "relationship_boundary_safety", "関係性用途境界", "Relationship Boundary Safety", "相性や関係推定を断定や排除に使わないための境界設計。"),
            ("SAFE-000096", "minor_use_boundary", "未成年利用境界", "Minor Use Boundary", "未成年向け用途で表示・データ利用・提案を慎重化する境界設計。"),
            ("SAFE-000097", "commercial_use_boundary", "商用利用境界", "Commercial Use Boundary", "収益化や推薦が操作的誘導にならないよう制限する境界設計。"),
            ("SAFE-000098", "third_party_sharing_boundary", "第三者共有境界", "Third Party Sharing Boundary", "推論結果や個人データを第三者へ共有する際の制限概念。"),
            ("SAFE-000099", "deployment_context_review", "運用文脈レビュー", "Deployment Context Review", "実際のアプリ運用文脈が安全範囲内か確認する過程。"),
            ("SAFE-000100", "safety_boundary_integration", "安全境界統合", "Safety Boundary Integration", "用途・対象・データ・表示の境界を統合して管理する枠組み。")
        ]
    }
]


def make_item(item_id, slug, name_ja, name_en, definition_ja, category, parent_ja):
    return {
        "filename": f"{item_id}_{slug}.yml",
        "id": item_id,
        "knowledge_type": "safety_ethics",
        "name_ja": name_ja,
        "name_en": name_en,
        "category": "Safety Ethics",
        "attribute": category.replace("Safety Ethics - ", ""),
        "definition_ja": definition_ja,
        "tags": ["CAT:安全倫理", f"CAT:{parent_ja}", "ATTR:安全設計"],
        "parent": [parent_ja],
        "related": ["補正要因", "表示設計", "アプリ用途"],
        "observable_data": [
            f"{name_ja}適用条件",
            f"{name_ja}リスク兆候",
            f"{name_ja}制御対象",
            f"{name_ja}監査項目"
        ],
        "signal_candidates": [
            f"{name_ja}が必要な文脈が観測される",
            "アプリ側で推論・表示・提案を安全に制御する材料になる"
        ],
        "device_level": "DB管理用",
        "modifiers": ["安全性", "プライバシー", "公平性", "高リスク性"],
        "evidence": "AI安全性・UX倫理・プライバシー設計・リスクコミュニケーションで使用",
        "status": "active"
    }


def main():
    all_items = []
    index_lines = ["category: Safety Ethics", "name_ja: 安全倫理", "items:"]

    for section in SECTIONS:
        parent_ja = section["name_ja"].replace("安全倫理・", "")
        for raw in section["items"]:
            item = make_item(*raw, category=section["category"], parent_ja=parent_ja)
            all_items.append(item)
            index_lines.append(f"  - {item['filename']}")

    index_lines.extend([
        "notes:",
        "  - 安全倫理は推論結果ではなく制御材料として扱う",
        "  - Knowledge DB側ではスコアリングしない",
        "  - アプリ側で安全性・表現・同意・リスク制御に利用する"
    ])

    pack = {
        "output_dir": "vol16_safety_ethics/safety_ethics_051_100",
        "index_filename": "safety_ethics_051_100_index.yml",
        "index_content": "\n".join(index_lines) + "\n",
        "items": all_items
    }

    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(json.dumps(pack, ensure_ascii=False, indent=2), encoding="utf-8")

    print(f"Created: {OUT}")
    print(f"Items: {len(all_items)}")


if __name__ == "__main__":
    main()