import json
from pathlib import Path

OUT = Path("data/master_packs/vol16_safety_ethics_001_050.json")

SECTIONS = [
    {
        "category": "Safety Ethics - Core",
        "name_ja": "安全倫理・基本",
        "items": [
            ("SAFE-000001", "non_diagnostic_principle", "非診断原則", "Non Diagnostic Principle", "人間分析結果を医療診断・性格断定・能力判定として扱わない原則。"),
            ("SAFE-000002", "probabilistic_expression_principle", "確率的表現原則", "Probabilistic Expression Principle", "結果を断定せず、可能性・傾向・推測として表現する原則。"),
            ("SAFE-000003", "user_autonomy_principle", "ユーザー自律原則", "User Autonomy Principle", "ユーザー自身の判断や選択を尊重する原則。"),
            ("SAFE-000004", "do_no_harm_principle", "危害回避原則", "Do No Harm Principle", "分析・表示・提案によって心理的・社会的害を与えないようにする原則。"),
            ("SAFE-000005", "supportive_use_principle", "支援目的原則", "Supportive Use Principle", "知識DBを評価や選別ではなく支援や自己理解に使う原則。"),
            ("SAFE-000006", "context_sensitive_principle", "文脈配慮原則", "Context Sensitive Principle", "観測結果を文脈・状態・環境と切り離して解釈しない原則。"),
            ("SAFE-000007", "uncertainty_disclosure_principle", "不確実性開示原則", "Uncertainty Disclosure Principle", "推論の不確実性や限界を表示する原則。"),
            ("SAFE-000008", "no_ranking_principle", "序列化回避原則", "No Ranking Principle", "人を優劣や順位で評価しないための原則。"),
            ("SAFE-000009", "human_review_principle", "人間確認原則", "Human Review Principle", "高リスク領域では自動推論だけで完結させない原則。"),
            ("SAFE-000010", "knowledge_db_boundary_principle", "知識DB境界原則", "Knowledge DB Boundary Principle", "Knowledge DBは推論せず、アプリ側に材料だけを提供する原則。")
        ]
    },
    {
        "category": "Safety Ethics - Privacy",
        "name_ja": "安全倫理・プライバシー",
        "items": [
            ("SAFE-000011", "data_minimization", "データ最小化", "Data Minimization", "目的に必要な範囲のデータだけを扱う原則。"),
            ("SAFE-000012", "purpose_limitation", "目的制限", "Purpose Limitation", "取得したデータを明示された目的の範囲内で利用する原則。"),
            ("SAFE-000013", "consent_management", "同意管理", "Consent Management", "データ利用・個別化・推論表示への同意を管理する仕組み。"),
            ("SAFE-000014", "sensitive_data_handling", "機微情報管理", "Sensitive Data Handling", "健康・人間関係・個人属性など慎重に扱うべき情報を保護する考え方。"),
            ("SAFE-000015", "privacy_by_design", "プライバシー・バイ・デザイン", "Privacy by Design", "設計段階からプライバシー保護を組み込む考え方。"),
            ("SAFE-000016", "user_data_control", "ユーザーデータ制御", "User Data Control", "ユーザーがデータ確認・修正・削除・停止を行える設計。"),
            ("SAFE-000017", "data_retention_limit", "データ保持制限", "Data Retention Limit", "不要になったデータを長期間保持しないための管理原則。"),
            ("SAFE-000018", "anonymization_principle", "匿名化原則", "Anonymization Principle", "個人を直接特定しにくくする処理や管理の考え方。"),
            ("SAFE-000019", "pseudonymization_principle", "仮名化原則", "Pseudonymization Principle", "識別情報を分離し、再識別リスクを下げる管理方法。"),
            ("SAFE-000020", "privacy_risk_review", "プライバシーリスク確認", "Privacy Risk Review", "データ利用や推論表示がプライバシーリスクを持たないか確認する過程。")
        ]
    },
    {
        "category": "Safety Ethics - Fairness",
        "name_ja": "安全倫理・公平性",
        "items": [
            ("SAFE-000021", "fairness_principle", "公平性原則", "Fairness Principle", "属性・環境・データ量の違いにより不当な扱いが生じないようにする原則。"),
            ("SAFE-000022", "bias_awareness", "バイアス認識", "Bias Awareness", "データ・設計・表示に含まれる偏りの可能性を認識すること。"),
            ("SAFE-000023", "stereotype_avoidance", "ステレオタイプ回避", "Stereotype Avoidance", "集団属性に基づく固定的な解釈や表示を避ける原則。"),
            ("SAFE-000024", "cultural_fairness", "文化的公平性", "Cultural Fairness", "文化差や表現様式の違いを考慮して解釈する考え方。"),
            ("SAFE-000025", "accessibility_fairness", "アクセシビリティ公平性", "Accessibility Fairness", "身体的・認知的・技術的制約がある人にも不利益を与えない設計。"),
            ("SAFE-000026", "data_coverage_fairness", "データカバレッジ公平性", "Data Coverage Fairness", "観測データ量や種類の差による不公平を抑える考え方。"),
            ("SAFE-000027", "language_fairness", "言語公平性", "Language Fairness", "言語能力や表現差による誤解釈を避ける考え方。"),
            ("SAFE-000028", "minor_user_fairness", "未成年公平性", "Minor User Fairness", "未成年ユーザーに対して不適切な評価や誘導を避ける考え方。"),
            ("SAFE-000029", "socioeconomic_context_fairness", "社会経済文脈公平性", "Socioeconomic Context Fairness", "経済状況や利用環境の違いを考慮して解釈する考え方。"),
            ("SAFE-000030", "fairness_audit", "公平性監査", "Fairness Audit", "知識項目や表示が不公平な影響を持たないか確認する管理過程。")
        ]
    },
    {
        "category": "Safety Ethics - Risk Control",
        "name_ja": "安全倫理・リスク制御",
        "items": [
            ("SAFE-000031", "high_stakes_use_limit", "高リスク用途制限", "High Stakes Use Limit", "雇用・進路・医療など重大判断への直接利用を制限する考え方。"),
            ("SAFE-000032", "mental_health_boundary", "メンタルヘルス境界", "Mental Health Boundary", "心理的困難を診断せず、必要時は専門支援へつなぐ境界設計。"),
            ("SAFE-000033", "manipulation_avoidance", "操作的誘導回避", "Manipulation Avoidance", "ユーザーの弱さや状態を利用して行動を誘導しない原則。"),
            ("SAFE-000034", "dependency_prevention", "依存予防", "Dependency Prevention", "アプリや推論結果への過度な依存を避ける設計。"),
            ("SAFE-000035", "over_personalization_risk", "過剰個別化リスク", "Over Personalization Risk", "過度に踏み込んだ個別化が不快感や不信を生むリスク。"),
            ("SAFE-000036", "self_fulfilling_risk", "自己成就リスク", "Self Fulfilling Risk", "表示された傾向が本人の自己理解や行動を固定化するリスク。"),
            ("SAFE-000037", "labeling_risk", "ラベリングリスク", "Labeling Risk", "ユーザーに固定的なラベルを付けることで生じる心理的・社会的リスク。"),
            ("SAFE-000038", "social_comparison_risk", "社会的比較リスク", "Social Comparison Risk", "他者比較によって不安・劣等感・過剰競争が生じるリスク。"),
            ("SAFE-000039", "distress_escalation_control", "苦痛悪化制御", "Distress Escalation Control", "表示や通知が苦痛を強めないよう制御する考え方。"),
            ("SAFE-000040", "risk_escalation_path", "リスク時エスカレーション導線", "Risk Escalation Path", "高リスク兆候がある場合に安全な支援導線へつなぐ設計。")
        ]
    },
    {
        "category": "Safety Ethics - Integration",
        "name_ja": "安全倫理・統合",
        "items": [
            ("SAFE-000041", "safety_guardrail", "安全ガードレール", "Safety Guardrail", "推論・表示・提案が安全範囲を超えないようにする統合的制御。"),
            ("SAFE-000042", "ethical_review_process", "倫理レビュー過程", "Ethical Review Process", "知識項目やアプリ利用が倫理的に妥当か確認する過程。"),
            ("SAFE-000043", "safety_modifier_stack", "安全補正スタック", "Safety Modifier Stack", "プライバシー・公平性・高リスク性など複数補正を重ねる考え方。"),
            ("SAFE-000044", "safe_output_policy", "安全出力方針", "Safe Output Policy", "結果表示や提案を安全に整えるための方針。"),
            ("SAFE-000045", "user_trust_protection", "ユーザー信頼保護", "User Trust Protection", "透明性・同意・説明可能性により信頼を守る考え方。"),
            ("SAFE-000046", "harm_monitoring", "有害影響モニタリング", "Harm Monitoring", "表示や提案がユーザーに悪影響を与えていないか確認する過程。"),
            ("SAFE-000047", "safe_iteration", "安全な改善反復", "Safe Iteration", "ユーザー反応や監査結果をもとに安全性を改善し続ける過程。"),
            ("SAFE-000048", "boundary_documentation", "境界文書化", "Boundary Documentation", "知識DBとアプリ推論の責任範囲を明確に残す管理。"),
            ("SAFE-000049", "safety_audit_signal", "安全監査シグナル", "Safety Audit Signal", "安全性確認が必要な知識項目や表示を検出する材料。"),
            ("SAFE-000050", "safety_ethics_integration", "安全倫理統合", "Safety Ethics Integration", "プライバシー・公平性・非断定・高リスク制御を統合する枠組み。")
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
        "output_dir": "vol16_safety_ethics/safety_ethics_001_050",
        "index_filename": "safety_ethics_001_050_index.yml",
        "index_content": "\n".join(index_lines) + "\n",
        "items": all_items
    }

    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(json.dumps(pack, ensure_ascii=False, indent=2), encoding="utf-8")

    print(f"Created: {OUT}")
    print(f"Items: {len(all_items)}")


if __name__ == "__main__":
    main()