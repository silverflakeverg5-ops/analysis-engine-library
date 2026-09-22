"""Build the Vol30 Culture and Context master pack (CUL-000001..000100)."""

from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "data" / "master_packs" / "vol30_culture_context_001_100.json"


SECTIONS = [
    ("Cultural Foundations", "文化的基盤", [
        ("cultural_context", "文化的文脈", "Cultural Context", "共有された意味・慣行・制度が行動解釈の背景となること"),
        ("within_group_variation", "集団内多様性", "Within-Group Variation", "同じ集団内にも大きな個人差・地域差・世代差があること"),
        ("cultural_dynamism", "文化的動態性", "Cultural Dynamism", "規範や慣行が交流・技術・世代・出来事により変化すること"),
        ("multi_level_culture", "多層文化", "Multi-Level Culture", "国・地域・組織・家族・専門領域など複数層が同時に影響すること"),
        ("cultural_learning", "文化学習", "Cultural Learning", "観察・参加・説明・反応を通じて意味や慣行を学ぶ過程"),
        ("enculturation", "文化化", "Enculturation", "生活する共同体の規範や実践へ継続的に参加する過程"),
        ("cultural_script", "文化的スクリプト", "Cultural Script", "特定場面で期待される行動の共有された筋書き"),
        ("cultural_schema", "文化的スキーマ", "Cultural Schema", "経験の解釈や予測に用いられる共有知識の枠組み"),
        ("situational_cultural_activation", "文化的枠組みの状況活性", "Situational Cultural Activation", "場面・相手・言語に応じて異なる文化的枠組みが前面に出ること"),
        ("cultural_humility", "文化的謙虚さ", "Cultural Humility", "自分の理解の限界を認め本人や共同体から継続して学ぶ姿勢"),
    ]),
    ("Values Norms and Practices", "価値・規範・慣行", [
        ("norm_awareness", "規範認識", "Norm Awareness", "場面で共有される期待や許容範囲を把握する過程"),
        ("descriptive_norm", "記述的規範", "Descriptive Norm", "周囲の人が実際に行っている行動が判断の手掛かりとなること"),
        ("injunctive_norm", "命令的規範", "Injunctive Norm", "何をすべきか・避けるべきかという期待が行動へ影響すること"),
        ("value_priority_context", "価値優先文脈", "Value Priority Context", "場面に応じて複数の価値の優先順位が変わること"),
        ("duty_rights_balance", "義務権利均衡", "Duty-Rights Balance", "関係上の義務と個人の権利を調整する枠組み"),
        ("harmony_expression", "調和表現", "Harmony Expression", "関係維持や対立回避の価値が表現方法へ反映されること"),
        ("achievement_meaning", "達成意味づけ", "Achievement Meaning", "達成が個人・家族・集団・社会のどこへ結びつけられるかという文脈"),
        ("reciprocity_norm_context", "互恵規範文脈", "Reciprocity Norm Context", "与える・受け取る・返す行為の時期や形に共有期待があること"),
        ("fairness_norm_interpretation", "公正規範解釈", "Fairness Norm Interpretation", "平等・必要・貢献・手続きなど公正基準の重みが文脈で異なること"),
        ("norm_change", "規範変化", "Norm Change", "世代・制度・接触・出来事により共有期待が更新される過程"),
    ]),
    ("Communication and Meaning", "伝達と意味", [
        ("contextual_meaning", "文脈依存意味", "Contextual Meaning", "同じ語や行為の意味が関係・場面・共有知識により変わること"),
        ("directness_norm", "直接性規範", "Directness Norm", "要望や不同意をどの程度明示するかに関する共有期待"),
        ("indirectness_norm", "間接性規範", "Indirectness Norm", "含意・婉曲・関係手掛かりを用いることに関する共有期待"),
        ("politeness_convention", "礼貌慣習", "Politeness Convention", "敬意や配慮を表す語彙・形式・順序に関する慣習"),
        ("silence_meaning", "沈黙の文化的意味", "Cultural Meaning of Silence", "沈黙が熟考・敬意・不同意・不参加など異なる意味を持ちうること"),
        ("turn_taking_norm", "発話交替規範", "Turn-Taking Norm", "発話の重なり・間・順番に関する共有期待"),
        ("emotion_expression_norm", "感情表出規範", "Emotion Expression Norm", "感情を誰にどの場面でどの程度示すかに関する期待"),
        ("nonverbal_convention", "非言語慣習", "Nonverbal Convention", "視線・身振り・距離・声量などの意味が文脈で異なること"),
        ("code_switching_context", "コード切替文脈", "Code-Switching Context", "相手・目的・所属に応じて言語や話し方を切り替えること"),
        ("translation_equivalence_risk", "翻訳等価性リスク", "Translation Equivalence Risk", "直訳では概念・強度・含意が一致しない可能性があること"),
    ]),
    ("Self Relations and Belonging", "自己・関係・所属", [
        ("independent_self_construal", "独立的自己観文脈", "Independent Self-Construal Context", "自己を固有の選好や目標との関係で捉えやすい文脈"),
        ("interdependent_self_construal", "協調的自己観文脈", "Interdependent Self-Construal Context", "自己を関係・役割・所属とのつながりで捉えやすい文脈"),
        ("relational_self", "関係的自己", "Relational Self", "特定の相手との関係が自己理解や行動の手掛かりとなること"),
        ("family_obligation_context", "家族義務文脈", "Family Obligation Context", "家族への責任や相互支援の範囲が生活判断へ影響すること"),
        ("in_group_boundary", "内集団境界", "In-Group Boundary", "誰を身近な共同体として扱うかの境界が文脈で変わること"),
        ("outgroup_contact", "集団間接触", "Intergroup Contact", "異なる集団との接触条件が理解・信頼・協力へ影響すること"),
        ("belonging_practice", "所属実践", "Belonging Practice", "儀礼・言語・参加・相互支援を通じて所属を表すこと"),
        ("reputation_concern_context", "評判配慮文脈", "Reputation Concern Context", "周囲からの評価が選択や自己表現へ影響すること"),
        ("face_management", "フェイス管理", "Face Management", "本人や他者の社会的評価・尊厳を保つため表現を調整すること"),
        ("autonomy_relatedness_balance", "自律関係性均衡", "Autonomy-Relatedness Balance", "自己決定と関係維持を対立させず状況に応じて調整すること"),
    ]),
    ("Authority Status and Institutions", "権威・地位・制度", [
        ("authority_legitimacy_context", "権威正当性文脈", "Authority Legitimacy Context", "権限がどの根拠で正当と受け止められるかという文脈"),
        ("hierarchy_norm", "階層規範", "Hierarchy Norm", "役職・年次・専門性などによる役割差を扱う共有期待"),
        ("egalitarian_norm", "平等主義規範", "Egalitarian Norm", "地位差を抑え対等な参加を重視する共有期待"),
        ("status_display_convention", "地位表示慣習", "Status Display Convention", "敬称・席順・服装・発言順などで地位を示す慣習"),
        ("role_deference", "役割敬譲", "Role Deference", "特定の役割へ判断や発言機会を譲ることに関する期待"),
        ("institutional_trust_context", "制度信頼文脈", "Institutional Trust Context", "行政・教育・医療・企業などへの経験が制度利用へ影響すること"),
        ("rule_formality", "規則形式性", "Rule Formality", "明文化された規則と状況的な取り決めの重みが異なること"),
        ("informal_network_use", "非公式ネットワーク利用", "Informal Network Use", "人間関係を通じた情報・調整・支援が制度利用を補うこと"),
        ("leadership_expectation_context", "リーダー期待文脈", "Leadership Expectation Context", "指示・参加・保護・専門性などリーダーに求める役割が異なること"),
        ("participation_voice_norm", "参加発言規範", "Participation and Voice Norm", "意思決定へ誰がどのように意見を表すかに関する期待"),
    ]),
    ("Time Space and Uncertainty", "時間・空間・不確実性", [
        ("clock_time_norm", "時計時間規範", "Clock-Time Norm", "時刻・所要時間・順序を基準に活動を調整する慣行"),
        ("event_time_norm", "出来事時間規範", "Event-Time Norm", "出来事の進行や関係上の区切りを基準に活動を移す慣行"),
        ("punctuality_context", "時間厳守文脈", "Punctuality Context", "到着や締切の許容幅と意味が場面・関係により異なること"),
        ("future_orientation_context", "未来志向文脈", "Future Orientation Context", "将来の結果や準備を現在の判断へ重く反映する文脈"),
        ("present_orientation_context", "現在志向文脈", "Present Orientation Context", "現在の必要・経験・関係を判断へ重く反映する文脈"),
        ("long_term_continuity", "長期連続性", "Long-Term Continuity", "世代・組織・共同体の継続を長期判断へ含めること"),
        ("personal_space_norm", "対人距離規範", "Personal Space Norm", "身体的距離や接触の適切さが関係・場面で異なること"),
        ("privacy_boundary_norm", "プライバシー境界規範", "Privacy Boundary Norm", "個人・家族・集団で共有してよい情報の境界が異なること"),
        ("uncertainty_management_norm", "不確実性管理規範", "Uncertainty Management Norm", "曖昧さを規則・相談・試行・保留などで扱う慣行"),
        ("planning_flexibility_context", "計画柔軟性文脈", "Planning Flexibility Context", "計画の固定度と状況対応の望ましい配分が異なること"),
    ]),
    ("Identity Migration and Acculturation", "文化的アイデンティティと移行", [
        ("multicultural_identity", "多文化的アイデンティティ", "Multicultural Identity", "複数の文化的所属を自己理解へ位置づけること"),
        ("bicultural_integration", "二文化統合", "Bicultural Integration", "二つの文化的枠組みを両立・切替・統合して扱うこと"),
        ("heritage_culture_maintenance", "継承文化維持", "Heritage Culture Maintenance", "家族や共同体から受け継いだ言語・慣行・価値を保つこと"),
        ("host_culture_participation", "受入文化参加", "Host Culture Participation", "移住・移動先の制度・関係・慣行へ参加すること"),
        ("acculturation_pathway", "文化適応経路", "Acculturation Pathway", "複数文化への関与の仕方が時間や領域により変化する過程"),
        ("cultural_identity_salience", "文化的同一性顕在性", "Cultural Identity Salience", "特定場面で文化的所属が自己理解の前面に出る度合い"),
        ("language_identity_context", "言語アイデンティティ文脈", "Language Identity Context", "使用言語が所属感・自己表現・関係へ結びつくこと"),
        ("migration_transition_context", "移住移行文脈", "Migration Transition Context", "移動に伴う制度・言語・関係・役割の再構成が行動へ影響すること"),
        ("discrimination_context", "差別経験文脈", "Discrimination Context", "偏見や排除への経験が安全感・表現・参加へ影響しうること"),
        ("identity_negotiation", "文化的同一性交渉", "Cultural Identity Negotiation", "相手や制度との関係で所属・呼称・表現を調整する過程"),
    ]),
    ("Learning Work and Digital Culture", "学習・仕事・デジタル文化", [
        ("learning_participation_norm", "学習参加規範", "Learning Participation Norm", "質問・発言・協働・自習の望ましい形に関する期待"),
        ("teacher_learner_role", "教師学習者役割文脈", "Teacher-Learner Role Context", "教える側と学ぶ側の権限・責任・距離に関する期待"),
        ("error_expression_norm", "誤り表明規範", "Error Expression Norm", "間違いや不確実さを誰にどのように示すかに関する期待"),
        ("feedback_norm_context", "フィードバック規範文脈", "Feedback Norm Context", "評価・批判・称賛を伝え受け取る形式に関する期待"),
        ("work_coordination_norm", "仕事調整規範", "Work Coordination Norm", "報告・相談・委任・期限調整の方法に関する共有慣行"),
        ("work_life_boundary_norm", "仕事生活境界規範", "Work-Life Boundary Norm", "勤務時間外の連絡や私生活共有の適切さに関する期待"),
        ("digital_etiquette", "デジタル礼儀", "Digital Etiquette", "返信速度・既読・通知・公開範囲などオンライン行動の共有期待"),
        ("platform_subculture", "プラットフォーム下位文化", "Platform Subculture", "特定サービス内の語彙・規範・役割・参加様式"),
        ("gaming_culture_context", "ゲーム文化文脈", "Gaming Culture Context", "ゲームジャンル・コミュニティ・競技性に伴う共有慣行"),
        ("online_offline_norm_shift", "オンライン・オフライン規範切替", "Online-Offline Norm Shift", "媒体や匿名性に応じて表現・距離・責任の期待が変わること"),
    ]),
    ("Fairness and Localization", "公平性とローカライズ", [
        ("measurement_invariance", "測定不変性", "Measurement Invariance", "異なる集団で指標が同じ概念と尺度を測っているか検証すること"),
        ("construct_equivalence", "構成概念等価性", "Construct Equivalence", "扱う概念が各文化文脈で同等の意味と範囲を持つか確かめること"),
        ("language_localization", "言語ローカライズ", "Language Localization", "語彙だけでなく含意・例・敬意・読みやすさを地域向けに調整すること"),
        ("response_style_context", "回答様式文脈", "Response Style Context", "極端反応・中間反応・同意傾向などが尺度回答へ影響しうること"),
        ("reference_group_effect", "参照集団効果", "Reference Group Effect", "自己評価が比較対象とする周囲の基準により変わること"),
        ("stereotype_threat_context", "ステレオタイプ脅威文脈", "Stereotype Threat Context", "否定的固定観念への懸念が課題行動や回答へ影響しうること"),
        ("sampling_representativeness", "標本代表性", "Sampling Representativeness", "データが対象となる言語・地域・集団・利用条件を十分に含むか確かめること"),
        ("cultural_bias_audit", "文化的バイアス監査", "Cultural Bias Audit", "誤差・欠測・判定差・不利益が文化文脈で偏っていないか点検すること"),
        ("local_stakeholder_review", "地域関係者レビュー", "Local Stakeholder Review", "対象文脈を知る当事者・専門家・運用者が意味と影響を確認すること"),
        ("cross_cultural_validation", "文化横断検証", "Cross-Cultural Validation", "翻訳・測定・モデル・表示を複数文脈で独立に検証すること"),
    ]),
    ("Observation and Integration", "観測と統合", [
        ("self_reported_cultural_context", "自己申告文化文脈", "Self-Reported Cultural Context", "本人が任意に示した言語・所属・慣行・生活文脈を扱う観測概念"),
        ("language_choice_signal", "言語選択シグナル", "Language Choice Signal", "場面や相手に応じた言語・表現形式の選択を捉える観測概念"),
        ("norm_shift_signal", "規範切替シグナル", "Norm Shift Signal", "集団・媒体・役割の変化に伴う行動様式の切替を捉える観測概念"),
        ("audience_adaptation_signal", "聞き手適応シグナル", "Audience Adaptation Signal", "相手に応じた説明・礼儀・直接性の調整を捉える観測概念"),
        ("context_switching_signal", "文脈切替シグナル", "Context Switching Signal", "異なる文化的場面を移る際の表現・役割・規範の切替を捉える観測概念"),
        ("cultural_practice_signal", "文化的実践シグナル", "Cultural Practice Signal", "本人が明示した慣行への参加や選択を時系列で捉える観測概念"),
        ("multi_context_consistency", "多文脈一貫性", "Multi-Context Consistency", "複数場面で維持される行動と場面別に変わる行動を分ける枠組み"),
        ("within_person_cultural_variation", "個人内文化変動", "Within-Person Cultural Variation", "同一人物の言語・相手・役割による変化を捉える枠組み"),
        ("culture_context_profile", "文化文脈プロファイル", "Culture Context Profile", "本人申告と複数場面の文脈情報を固定類型化せず整理する枠組み"),
        ("culture_context_integration", "文化文脈統合", "Culture Context Integration", "観測・本人申告・補正・公平性検証を安全に接続する統合枠組み"),
    ]),
]


def make_item(item_id, slug, name_ja, name_en, focus, section_en, section_ja):
    return {
        "filename": f"{item_id}_{slug}.yml",
        "id": item_id,
        "knowledge_type": "culture_context",
        "name_ja": name_ja,
        "name_en": name_en,
        "category": "Culture and Context",
        "attribute": section_en,
        "definition_ja": f"{name_ja}は、{focus}を表す文化文脈概念。国籍・民族・言語・地域だけから人格や能力を断定しない。",
        "tags": ["CAT:文化・文脈", f"CAT:{section_ja}", "ATTR:文脈補正"],
        "parent": [section_ja],
        "related": ["文化背景補正", "社会的文脈", "公平性"],
        "observable_data": ["本人が任意に申告した言語・所属・生活文脈", "同意済みの場面・相手・役割情報", "複数文脈における表現と選択の変化", "翻訳版・地域版ごとの欠測と回答分布"],
        "signal_candidates": [
            f"{name_ja}と整合する文脈差が同一人物の複数場面で観測される",
            "言語・相手・役割・媒体・制度の変化に伴って行動の意味または表現が変化する",
        ],
        "device_level": "本人同意に基づく文脈情報と明示申告を利用し、行動ログから国籍・民族・宗教・移民状態を推定しない",
        "modifiers": ["本人が選択した文化的所属", "使用言語と習熟度", "地域・制度", "家族・組織・共同体", "世代・コホート", "移動・移住経験", "相手との関係と権力差", "媒体・プラットフォーム"],
        "evidence": "文化心理学・文化人類学・社会言語学・異文化コミュニケーション・測定論・HCI研究を参照",
        "status": "active",
    }


def main():
    items = []
    index_lines = ["category: Culture and Context", "name_ja: 文化・文脈", "items:"]
    number = 1
    for section_en, section_ja, definitions in SECTIONS:
        for slug, name_ja, name_en, focus in definitions:
            item_id = f"CUL-{number:06d}"
            item = make_item(item_id, slug, name_ja, name_en, focus, section_en, section_ja)
            items.append(item)
            index_lines.append(f"  - {item['filename']}")
            number += 1
    if len(items) != 100:
        raise ValueError(f"Expected 100 items, got {len(items)}")
    index_lines.extend([
        "notes:",
        "  - 文化を国籍・民族・言語・地域と一対一対応させず、集団内差と個人内変動を優先する",
        "  - 行動ログから国籍、民族、宗教、移民状態などの機微属性を推定しない",
        "  - 本人の任意申告、地域関係者レビュー、測定不変性、公平性監査を組み合わせる",
        "  - 採用・教育選抜・保険・金融・法執行など高影響領域の自動判定には直接利用しない",
    ])
    pack = {
        "output_dir": "vol30_culture_context/culture_context_001_100",
        "index_filename": "culture_context_001_100_index.yml",
        "index_content": "\n".join(index_lines) + "\n",
        "items": items,
    }
    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(json.dumps(pack, ensure_ascii=False, indent=2), encoding="utf-8")
    print(f"Created: {OUT}")
    print(f"Items: {len(items)}")


if __name__ == "__main__":
    main()
