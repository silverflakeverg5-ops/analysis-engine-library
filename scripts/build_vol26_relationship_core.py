import json
from pathlib import Path


OUT = Path("data/master_packs/vol26_relationship_core_001_100.json")

SECTIONS = [
    ("Foundations", "関係基礎", [
        ("relationship", "関係性", "Relationship", "複数者の継続的な相互作用と結びつき"),
        ("relational_tie", "関係的結合", "Relational Tie", "当事者間をつなぐ社会的または心理的な結合"),
        ("relational_interaction", "関係的相互作用", "Relational Interaction", "互いの行動が相手へ影響する過程"),
        ("interdependence", "相互依存", "Interdependence", "双方の結果や選択が互いに関連する状態"),
        ("relational_reciprocity", "関係的互恵性", "Relational Reciprocity", "働きかけや支援が双方向に交換される性質"),
        ("relational_context", "関係文脈", "Relational Context", "役割・場面・文化など関係解釈の背景"),
        ("relationship_history", "関係履歴", "Relationship History", "過去の相互作用が現在へ与える蓄積"),
        ("relational_expectation", "関係期待", "Relational Expectation", "相手や関係の将来行動に対する見込み"),
        ("relational_norm", "関係規範", "Relational Norm", "関係内で共有または期待される行動基準"),
        ("relationship_quality", "関係品質", "Relationship Quality", "満足・信頼・安定などを統合した関係状態"),
    ]),
    ("Trust", "信頼", [
        ("interpersonal_trust", "対人信頼", "Interpersonal Trust", "相手が期待を大きく損なわないという見込み"),
        ("perceived_reliability", "知覚された信頼性", "Perceived Reliability", "相手が約束や役割を安定して果たすという評価"),
        ("relational_predictability", "関係的予測可能性", "Relational Predictability", "相手の反応を一貫して予測できる度合い"),
        ("perceived_benevolence", "知覚された善意", "Perceived Benevolence", "相手が自分の利益にも配慮するという評価"),
        ("relational_credibility", "関係的信用", "Relational Credibility", "相手の説明や意図を信用できる度合い"),
        ("vulnerability_acceptance", "脆弱性受容", "Vulnerability Acceptance", "不確実性を伴って相手へ委ねることを受け入れる過程"),
        ("trust_calibration", "信頼較正", "Trust Calibration", "根拠に応じて信頼の強さを調整する過程"),
        ("trust_repair", "信頼修復", "Trust Repair", "損なわれた信頼を説明と行動で回復する過程"),
        ("betrayal_sensitivity", "裏切り感受性", "Betrayal Sensitivity", "期待違反や不誠実の兆候へ反応する度合い"),
        ("relational_suspicion", "関係的疑念", "Relational Suspicion", "相手の意図や説明を慎重に疑う状態"),
    ]),
    ("Attachment and Security", "愛着と安心", [
        ("attachment", "愛着", "Attachment", "安心や保護を求める持続的な情緒的結びつき"),
        ("secure_attachment_pattern", "安定型愛着パターン", "Secure Attachment Pattern", "接近と自律を比較的柔軟に両立する関係パターン"),
        ("anxious_attachment_pattern", "不安型愛着パターン", "Anxious Attachment Pattern", "拒絶への懸念と安心確認が増えやすい関係パターン"),
        ("avoidant_attachment_pattern", "回避型愛着パターン", "Avoidant Attachment Pattern", "親密さや依存から距離を取りやすい関係パターン"),
        ("proximity_seeking", "近接希求", "Proximity Seeking", "安心のため相手との距離を縮めようとする行動"),
        ("separation_response", "分離反応", "Separation Response", "離別や連絡断に対して生じる反応"),
        ("reassurance_seeking", "安心確認", "Reassurance Seeking", "関係継続や評価を繰り返し確かめる行動"),
        ("relational_dependency", "関係的依存", "Relational Dependency", "必要な機能や安心を相手へ強く委ねる状態"),
        ("relational_autonomy", "関係内自律", "Relational Autonomy", "関係を保ちながら自己決定を維持する状態"),
        ("relational_security", "関係的安心感", "Relational Security", "関係が継続し尊重されるという感覚"),
    ]),
    ("Intimacy", "親密性", [
        ("intimacy", "親密性", "Intimacy", "理解・信頼・開示を伴う心理的な近さ"),
        ("relational_closeness", "関係的近接感", "Relational Closeness", "相手を自己に近い存在と感じる度合い"),
        ("relational_self_disclosure", "関係的自己開示", "Relational Self Disclosure", "個人的な経験や考えを相手へ共有する行動"),
        ("perceived_responsiveness", "知覚された応答性", "Perceived Responsiveness", "相手が理解し配慮して応じるという評価"),
        ("mutual_understanding", "相互理解", "Mutual Understanding", "双方が互いの意図や立場を理解している状態"),
        ("relational_empathy", "関係的共感", "Relational Empathy", "相手の視点や感情を理解し応答する過程"),
        ("relational_validation", "関係的受容", "Relational Validation", "相手の経験や感情を尊重して認める行動"),
        ("affection_expression", "愛情表現", "Affection Expression", "好意や大切さを伝える言語的・行動的表現"),
        ("privacy_boundary", "プライバシー境界", "Privacy Boundary", "共有する情報と保持する情報を分ける境界"),
        ("emotional_availability", "情緒的利用可能性", "Emotional Availability", "相手の感情的必要へ応じられる状態"),
    ]),
    ("Boundaries", "境界と自律", [
        ("boundary_clarity", "境界明確性", "Boundary Clarity", "許容範囲や役割の境界が明確な度合い"),
        ("relational_consent", "関係的同意", "Relational Consent", "関与や共有について自由意思で合意する過程"),
        ("personal_space", "個人空間", "Personal Space", "身体的・心理的に必要とする距離"),
        ("role_boundary", "役割境界", "Role Boundary", "関係内の責任や期待を区切る境界"),
        ("time_boundary", "時間境界", "Time Boundary", "連絡・支援・共同活動に使う時間の境界"),
        ("digital_boundary", "デジタル境界", "Digital Boundary", "オンライン連絡や情報共有に関する境界"),
        ("boundary_negotiation", "境界交渉", "Boundary Negotiation", "双方の必要に合わせ境界を話し合う過程"),
        ("boundary_violation", "境界侵害", "Boundary Violation", "合意された、または合理的な境界を越える行動"),
        ("autonomy_support", "自律性支援", "Autonomy Support", "相手の選択と自己決定を尊重する働きかけ"),
        ("controlling_behavior", "統制行動", "Controlling Behavior", "相手の選択や行動を過度に制限する働きかけ"),
    ]),
    ("Cooperation and Exchange", "協力と交換", [
        ("relational_cooperation", "関係的協力", "Relational Cooperation", "共通または両立する目標へ共同で行動する過程"),
        ("relational_coordination", "関係的調整", "Relational Coordination", "役割・時間・資源を相互にそろえる過程"),
        ("mutual_aid", "相互扶助", "Mutual Aid", "必要に応じて互いに支援を提供する関係"),
        ("social_exchange", "社会的交換", "Social Exchange", "利益・負担・支援を交換する関係過程"),
        ("relational_equity", "関係的衡平", "Relational Equity", "貢献と結果の釣り合いに関する評価"),
        ("relational_fairness", "関係的公正", "Relational Fairness", "扱いや意思決定が公正であるという評価"),
        ("resource_sharing", "資源共有", "Resource Sharing", "時間・情報・物的資源を分け合う行動"),
        ("relationship_commitment", "関係コミットメント", "Relationship Commitment", "関係を維持しようとする意図"),
        ("relationship_investment", "関係投資", "Relationship Investment", "関係へ投入された時間・努力・共有資源"),
        ("perceived_alternatives", "知覚された代替関係", "Perceived Alternatives", "現在の関係以外に得られる選択肢の評価"),
    ]),
    ("Conflict and Repair", "対立と修復", [
        ("relational_conflict", "関係的対立", "Relational Conflict", "目標・認識・必要が両立しない相互作用"),
        ("relational_disagreement", "関係的不一致", "Relational Disagreement", "意見や判断が一致していない状態"),
        ("conflict_escalation", "対立激化", "Conflict Escalation", "対立の強度や範囲が拡大する過程"),
        ("conflict_avoidance", "対立回避", "Conflict Avoidance", "不一致の表明や処理を避ける行動"),
        ("relational_compromise", "関係的妥協", "Relational Compromise", "双方が譲歩して合意点を作る過程"),
        ("relational_negotiation", "関係的交渉", "Relational Negotiation", "異なる必要や利害を話し合って調整する過程"),
        ("forgiveness", "許し", "Forgiveness", "侵害後の報復動機や敵意を弱める過程"),
        ("relational_apology", "関係的謝罪", "Relational Apology", "責任と影響を認め修復意図を示す行動"),
        ("relationship_repair", "関係修復", "Relationship Repair", "損なわれた理解・信頼・協力を回復する過程"),
        ("relational_rupture", "関係断裂", "Relational Rupture", "信頼や相互作用が大きく損なわれた状態"),
    ]),
    ("Power and Agency", "権力と主体性", [
        ("power_balance", "権力均衡", "Power Balance", "意思決定や資源への影響力が釣り合う度合い"),
        ("relational_dominance", "関係的優位", "Relational Dominance", "一方が相互作用を強く方向づける状態"),
        ("relational_submission", "関係的服従", "Relational Submission", "相手の要求や判断を優先し続ける状態"),
        ("interpersonal_influence", "対人影響", "Interpersonal Influence", "相手の判断や行動を変化させる作用"),
        ("decision_equality", "意思決定対等性", "Decision Equality", "双方が意思決定へ参加できる度合い"),
        ("dependency_asymmetry", "依存非対称", "Dependency Asymmetry", "一方が他方へより強く依存する状態"),
        ("coercion_risk", "強制リスク", "Coercion Risk", "脅しや不利益によって同意を歪める可能性"),
        ("manipulation_risk", "操作リスク", "Manipulation Risk", "情報や感情を利用して選択を不当に誘導する可能性"),
        ("status_difference", "地位差", "Status Difference", "役職・年齢・資源などによる関係上の差"),
        ("relational_agency", "関係的主体性", "Relational Agency", "関係内で自分の意思を表明し選択できる度合い"),
    ]),
    ("Lifecycle", "関係変化", [
        ("relationship_formation", "関係形成", "Relationship Formation", "接触から継続的な結びつきが生まれる過程"),
        ("relationship_maintenance", "関係維持", "Relationship Maintenance", "関係の質と継続を支える行動"),
        ("relationship_deepening", "関係深化", "Relationship Deepening", "信頼・理解・親密性が増す過程"),
        ("relational_distancing", "関係的距離化", "Relational Distancing", "接触や心理的関与を減らす過程"),
        ("relationship_transition", "関係移行", "Relationship Transition", "役割や関係形式が変化する過程"),
        ("relationship_breakup", "関係解消", "Relationship Breakup", "継続していた関係を終了する過程"),
        ("relational_grief", "関係喪失悲嘆", "Relational Grief", "関係の喪失や変化に伴う適応過程"),
        ("relationship_reconnection", "関係再接続", "Relationship Reconnection", "距離化や中断後に交流を再開する過程"),
        ("relationship_resilience", "関係レジリエンス", "Relationship Resilience", "負荷や対立後に関係機能を回復する力"),
        ("relationship_dissolution", "関係消散", "Relationship Dissolution", "相互作用と結びつきが段階的に消える過程"),
    ]),
    ("Observation and Integration", "観測と統合", [
        ("interaction_frequency_signal", "交流頻度シグナル", "Interaction Frequency Signal", "一定期間の接触や共同活動量を捉える観測概念"),
        ("initiation_reciprocity_signal", "開始互恵性シグナル", "Initiation Reciprocity Signal", "双方が交流を開始する比率を捉える観測概念"),
        ("response_consistency_signal", "応答一貫性シグナル", "Response Consistency Signal", "相手への応答の安定性を捉える観測概念"),
        ("support_exchange_signal", "支援交換シグナル", "Support Exchange Signal", "支援の提供と受領を捉える観測概念"),
        ("boundary_response_signal", "境界応答シグナル", "Boundary Response Signal", "境界表明後の尊重や調整を捉える観測概念"),
        ("conflict_recovery_signal", "対立回復シグナル", "Conflict Recovery Signal", "対立後に通常の交流へ戻る過程を捉える観測概念"),
        ("trust_behavior_signal", "信頼行動シグナル", "Trust Behavior Signal", "約束履行や情報共有など信頼関連行動を捉える観測概念"),
        ("relationship_profile", "関係プロファイル", "Relationship Profile", "複数の関係特性を二者・文脈別に整理する枠組み"),
        ("relationship_context_mapping", "関係文脈マッピング", "Relationship Context Mapping", "関係行動を役割・場面・履歴と結びつける枠組み"),
        ("relationship_core_integration", "関係コア統合", "Relationship Core Integration", "相互作用・補正・根拠・安全境界を接続する枠組み"),
    ]),
]


def make_item(item_id, slug, name_ja, name_en, focus, section_en, section_ja):
    return {
        "filename": f"{item_id}_{slug}.yml",
        "id": item_id,
        "knowledge_type": "relationship_core",
        "name_ja": name_ja,
        "name_en": name_en,
        "category": "Relationship Core",
        "attribute": section_en,
        "definition_ja": f"{name_ja}は、{focus}を表す関係概念。一方の人物だけに帰属させて断定しない。",
        "tags": ["CAT:関係性", f"CAT:{section_ja}", "ATTR:関係要因"],
        "parent": [section_ja],
        "related": ["相互作用", "コミュニケーション", "社会的文脈"],
        "observable_data": ["交流頻度", "応答の相互性", "支援と協力の推移", "対立後の修復行動"],
        "signal_candidates": [
            f"{name_ja}と整合する相互作用が複数場面で観測される",
            "役割・履歴・媒体・負荷の変化に伴って関係行動が変化する",
        ],
        "device_level": "同意された会話・共同活動・ゲーム内交流ログから観測可能",
        "modifiers": ["関係履歴", "文化", "役割", "権力差", "媒体", "ストレス", "プライバシー境界"],
        "evidence": "対人関係研究・愛着研究・社会心理学・家族心理学・会話分析を参照",
        "status": "active",
    }


def main():
    items = []
    index_lines = ["category: Relationship Core", "name_ja: 関係性コア", "items:"]
    number = 1
    for section_en, section_ja, definitions in SECTIONS:
        for slug, name_ja, name_en, focus in definitions:
            item_id = f"REL-{number:06d}"
            item = make_item(item_id, slug, name_ja, name_en, focus, section_en, section_ja)
            items.append(item)
            index_lines.append(f"  - {item['filename']}")
            number += 1
    if len(items) != 100:
        raise ValueError(f"Expected 100 items, got {len(items)}")
    index_lines.extend([
        "notes:",
        "  - 関係性コアは二者以上の相互作用を扱い、一方の人格や価値を断定しない",
        "  - 愛着・依存・対立などは診断名として扱わず、文脈依存の候補として扱う",
        "  - 私的関係データは明示的同意・最小収集・削除可能性を前提とする",
    ])
    pack = {
        "output_dir": "vol26_relationship_core/relationship_core_001_100",
        "index_filename": "relationship_core_001_100_index.yml",
        "index_content": "\n".join(index_lines) + "\n",
        "items": items,
    }
    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(json.dumps(pack, ensure_ascii=False, indent=2), encoding="utf-8")
    print(f"Created: {OUT}")
    print(f"Items: {len(items)}")


if __name__ == "__main__":
    main()
