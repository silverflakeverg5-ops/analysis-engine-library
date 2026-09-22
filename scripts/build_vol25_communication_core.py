import json
from pathlib import Path


OUT = Path("data/master_packs/vol25_communication_core_001_100.json")

SECTIONS = [
    ("Foundations", "基礎", [
        ("communication", "コミュニケーション", "Communication", "情報や意味を相互に伝え調整する過程"),
        ("message", "メッセージ", "Message", "伝達される内容と意図のまとまり"),
        ("sender_role", "送信者役割", "Sender Role", "情報を表現して届ける側の機能"),
        ("receiver_role", "受信者役割", "Receiver Role", "情報を受け取り解釈する側の機能"),
        ("communication_channel", "伝達チャネル", "Communication Channel", "対面・音声・文字など伝達に使う経路"),
        ("communication_feedback", "伝達フィードバック", "Communication Feedback", "理解や反応を相手へ返す過程"),
        ("communication_context", "伝達文脈", "Communication Context", "意味の解釈に影響する状況や関係"),
        ("communication_noise", "伝達ノイズ", "Communication Noise", "送受信や理解を妨げる要因"),
        ("shared_meaning", "共有意味", "Shared Meaning", "参加者間で意味理解がそろった状態"),
        ("communication_goal", "伝達目標", "Communication Goal", "会話や表現によって達成したい結果"),
    ]),
    ("Expression", "表現", [
        ("verbal_expression", "言語表現", "Verbal Expression", "言葉を用いて内容や意図を表す行動"),
        ("lexical_choice", "語彙選択", "Lexical Choice", "目的や相手に応じて言葉を選ぶ過程"),
        ("sentence_complexity", "文複雑性", "Sentence Complexity", "文の長さや構造が持つ複雑さ"),
        ("explanation_style", "説明スタイル", "Explanation Style", "情報を順序づけて説明する方法"),
        ("narrative_expression", "物語的表現", "Narrative Expression", "出来事を時間や因果の流れで伝える方法"),
        ("question_asking", "質問行動", "Question Asking", "不足情報や相手の考えを尋ねる行動"),
        ("assertive_expression", "主張表現", "Assertive Expression", "自分の意見や必要を明確に伝える行動"),
        ("self_disclosure", "自己開示", "Self Disclosure", "自分の経験や考えを相手へ伝える行動"),
        ("hedging_expression", "婉曲表現", "Hedging Expression", "断定を弱め不確実性や配慮を示す表現"),
        ("clarification_request", "明確化要求", "Clarification Request", "曖昧な内容を確認し直す行動"),
    ]),
    ("Listening and Response", "傾聴と応答", [
        ("active_listening", "積極的傾聴", "Active Listening", "注意を向け理解を示しながら聞く行動"),
        ("response_latency", "応答潜時", "Response Latency", "発話やメッセージから返答までの時間"),
        ("acknowledgment_response", "受領応答", "Acknowledgment Response", "内容を受け取ったことを示す反応"),
        ("paraphrasing", "言い換え確認", "Paraphrasing", "相手の内容を別の言葉で確かめる行動"),
        ("follow_up_question", "追質問", "Follow Up Question", "相手の発言を受けて理解を深める質問"),
        ("comprehension_monitoring", "理解モニタリング", "Comprehension Monitoring", "自分の理解状態を点検する過程"),
        ("ambiguity_detection", "曖昧性検出", "Ambiguity Detection", "複数解釈が可能な表現に気づく過程"),
        ("turn_taking", "ターン交替", "Turn Taking", "発話順を相互に調整する行動"),
        ("interruption_behavior", "割り込み行動", "Interruption Behavior", "相手の発話完了前に発話を開始する行動"),
        ("communicative_silence", "会話内沈黙", "Communicative Silence", "応答や思考のために沈黙を用いる行動"),
    ]),
    ("Interpersonal Style", "対人スタイル", [
        ("communication_directness", "直接性", "Communication Directness", "意図や要求を明示的に伝える度合い"),
        ("communication_indirectness", "間接性", "Communication Indirectness", "含意や文脈を通じて伝える度合い"),
        ("formality", "形式性", "Formality", "規範的で改まった表現を用いる度合い"),
        ("informality", "非形式性", "Informality", "親しみのあるくだけた表現を用いる度合い"),
        ("communicative_warmth", "伝達的温かさ", "Communicative Warmth", "親しみや好意を表現に含める度合い"),
        ("politeness", "丁寧さ", "Politeness", "相手の面子や境界へ配慮する表現"),
        ("communicative_assertiveness", "伝達的自己主張", "Communicative Assertiveness", "相手を尊重しつつ自分の立場を示す度合い"),
        ("responsiveness", "応答性", "Responsiveness", "相手の働きかけへ適切に反応する度合い"),
        ("expressiveness", "表出性", "Expressiveness", "感情や意図を外へ示す度合い"),
        ("communicative_reserve", "伝達的抑制", "Communicative Reserve", "発言や開示を控えめにする度合い"),
    ]),
    ("Emotion and Rapport", "感情と関係形成", [
        ("empathic_expression", "共感表現", "Empathic Expression", "相手の視点や感情への理解を示す表現"),
        ("validation_response", "受容応答", "Validation Response", "相手の経験や感情を尊重して認める反応"),
        ("emotion_labeling", "感情ラベリング", "Emotion Labeling", "感情状態を言葉で識別して表す行動"),
        ("emotional_disclosure", "感情開示", "Emotional Disclosure", "自分の感情を相手へ伝える行動"),
        ("emotional_withholding", "感情保留", "Emotional Withholding", "感情表現を意図的に控える行動"),
        ("humor_use", "ユーモア使用", "Humor Use", "緊張緩和や親密化のため笑いを用いる行動"),
        ("sarcasm_use", "皮肉使用", "Sarcasm Use", "字義と異なる評価を含ませる表現"),
        ("praise_expression", "称賛表現", "Praise Expression", "相手の行動や成果を肯定的に評価する表現"),
        ("apology_expression", "謝罪表現", "Apology Expression", "責任や影響を認め関係修復を図る表現"),
        ("gratitude_expression", "感謝表現", "Gratitude Expression", "相手から受けた価値を認めて伝える表現"),
    ]),
    ("Conflict and Repair", "対立と修復", [
        ("disagreement_expression", "異議表明", "Disagreement Expression", "意見の不一致を相手へ示す行動"),
        ("communication_conflict_avoidance", "会話的対立回避", "Communication Conflict Avoidance", "不一致の表明や議論を避ける行動"),
        ("confrontation", "対峙的表現", "Confrontation", "問題や不一致を直接取り上げる行動"),
        ("verbal_de_escalation", "言語的沈静化", "Verbal De Escalation", "緊張や攻撃性を下げる言語行動"),
        ("conversation_repair", "会話修復", "Conversation Repair", "誤解や言い間違いを訂正し理解を戻す行動"),
        ("negotiation_communication", "交渉コミュニケーション", "Negotiation Communication", "異なる利害を調整して合意を探る行動"),
        ("compromise_expression", "妥協提案", "Compromise Expression", "双方が譲歩できる案を示す行動"),
        ("boundary_setting", "境界設定", "Boundary Setting", "許容範囲や必要な距離を明確に伝える行動"),
        ("criticism_response", "批判応答", "Criticism Response", "否定的評価を受けた際の返答行動"),
        ("defensive_communication", "防衛的コミュニケーション", "Defensive Communication", "自己保護を優先して反論や否認を行う反応"),
    ]),
    ("Group and Status", "集団と地位", [
        ("leadership_communication", "リーダーシップ伝達", "Leadership Communication", "方向づけや意思決定を支える集団内表現"),
        ("followership_communication", "フォロワーシップ伝達", "Followership Communication", "支援や建設的異議を通じて集団へ関与する表現"),
        ("coordination_communication", "調整コミュニケーション", "Coordination Communication", "役割や作業順をそろえるための伝達"),
        ("inclusive_communication", "包摂的コミュニケーション", "Inclusive Communication", "参加機会と尊重を広げる表現"),
        ("dominant_communication", "優位的コミュニケーション", "Dominant Communication", "会話の方向や発言機会を強く制御する傾向"),
        ("deferential_communication", "恭順的コミュニケーション", "Deferential Communication", "相手の地位や判断を優先する表現"),
        ("status_signaling", "地位シグナリング", "Status Signaling", "権限や専門性を示す表現行動"),
        ("consensus_seeking", "合意探索", "Consensus Seeking", "参加者の一致点を探しまとめる行動"),
        ("constructive_dissent", "建設的異議", "Constructive Dissent", "集団改善のため反対意見を示す行動"),
        ("discussion_facilitation", "議論促進", "Discussion Facilitation", "発言機会や論点整理を支援する行動"),
    ]),
    ("Digital Communication", "デジタル伝達", [
        ("text_brevity", "文章簡潔性", "Text Brevity", "文字メッセージを短くまとめる度合い"),
        ("emoji_use", "絵文字使用", "Emoji Use", "感情やニュアンス補足に絵文字を用いる行動"),
        ("digital_response_timing", "デジタル応答時間", "Digital Response Timing", "受信から返信までの時間的傾向"),
        ("message_frequency", "メッセージ頻度", "Message Frequency", "一定期間に送信するメッセージ量"),
        ("message_fragmentation", "分割送信", "Message Fragmentation", "内容を複数の短いメッセージに分ける行動"),
        ("message_editing", "送信前編集", "Message Editing", "送信前に文章を修正し整える行動"),
        ("read_receipt_sensitivity", "既読感受性", "Read Receipt Sensitivity", "既読表示や返信遅延へ反応する度合い"),
        ("channel_switching", "チャネル切替", "Channel Switching", "目的に応じて文字・音声・対面を切り替える行動"),
        ("notification_response", "通知応答", "Notification Response", "通知を受けて確認や返信を行う傾向"),
        ("online_disinhibition", "オンライン脱抑制", "Online Disinhibition", "オンラインで表現の抑制が弱まる傾向"),
    ]),
    ("Culture and Context", "文化と文脈", [
        ("high_context_communication", "高文脈コミュニケーション", "High Context Communication", "共有背景や含意へ強く依存する伝達"),
        ("low_context_communication", "低文脈コミュニケーション", "Low Context Communication", "内容を明示して伝えることを重視する伝達"),
        ("code_switching", "コードスイッチング", "Code Switching", "相手や場面に応じて言語様式を切り替える行動"),
        ("audience_adaptation", "受け手適応", "Audience Adaptation", "相手の知識や立場に合わせ表現を変える行動"),
        ("cultural_politeness", "文化的丁寧さ", "Cultural Politeness", "文化規範に沿って敬意や配慮を示す表現"),
        ("language_proficiency_context", "言語熟達文脈", "Language Proficiency Context", "使用言語の熟達度が表現へ与える影響"),
        ("power_distance_communication", "権力距離伝達", "Power Distance Communication", "地位差に応じて表現や発言量を調整する行動"),
        ("public_private_communication", "公私伝達差", "Public Private Communication", "公開場面と私的場面で表現が変わる傾向"),
        ("synchronous_communication", "同期コミュニケーション", "Synchronous Communication", "同時進行で即時応答する伝達"),
        ("asynchronous_communication", "非同期コミュニケーション", "Asynchronous Communication", "時間差を許容して行う伝達"),
    ]),
    ("Observation and Integration", "観測と統合", [
        ("speaking_share_signal", "発話占有率シグナル", "Speaking Share Signal", "会話全体に占める発話量の観測概念"),
        ("turn_latency_signal", "ターン潜時シグナル", "Turn Latency Signal", "発話交替までの時間を捉える観測概念"),
        ("question_ratio_signal", "質問比率シグナル", "Question Ratio Signal", "発話中の質問割合を捉える観測概念"),
        ("repair_rate_signal", "修復率シグナル", "Repair Rate Signal", "誤解や訂正への修復頻度を捉える観測概念"),
        ("tone_shift_signal", "トーン変化シグナル", "Tone Shift Signal", "会話中の感情的調子の変化を捉える観測概念"),
        ("topic_persistence_signal", "話題持続シグナル", "Topic Persistence Signal", "同一話題を継続する度合いを捉える観測概念"),
        ("communication_reciprocity_signal", "伝達互恵性シグナル", "Communication Reciprocity Signal", "発話・質問・開示の相互性を捉える観測概念"),
        ("communication_profile", "コミュニケーションプロファイル", "Communication Profile", "複数の伝達傾向を文脈別に整理する枠組み"),
        ("communication_context_mapping", "伝達文脈マッピング", "Communication Context Mapping", "伝達行動を相手・媒体・状況と結びつける枠組み"),
        ("communication_core_integration", "伝達コア統合", "Communication Core Integration", "観測・補正・根拠・安全表示を接続する枠組み"),
    ]),
]


def make_item(item_id, slug, name_ja, name_en, focus, section_en, section_ja):
    return {
        "filename": f"{item_id}_{slug}.yml",
        "id": item_id,
        "knowledge_type": "communication_core",
        "name_ja": name_ja,
        "name_en": name_en,
        "category": "Communication Core",
        "attribute": section_en,
        "definition_ja": f"{name_ja}は、{focus}を表す伝達概念。単独で人格や能力を断定しない。",
        "tags": ["CAT:コミュニケーション", f"CAT:{section_ja}", "ATTR:伝達要因"],
        "parent": [section_ja],
        "related": ["行動観測", "社会的文脈", "感情表現"],
        "observable_data": ["発話または文字量", "応答までの時間", "質問と応答の回数", "会話修復の推移"],
        "signal_candidates": [
            f"{name_ja}と整合する伝達行動が複数場面で観測される",
            "相手・媒体・目的の変化に伴って表現や応答が変化する",
        ],
        "device_level": "スマートフォン・PC・ゲーム機の会話ログから観測可能",
        "modifiers": ["文化", "使用言語", "関係性", "権力差", "媒体", "時間制約", "感情状態"],
        "evidence": "コミュニケーション学・社会心理学・言語学・会話分析・HCI研究を参照",
        "status": "active",
    }


def main():
    items = []
    index_lines = ["category: Communication Core", "name_ja: コミュニケーションコア", "items:"]
    number = 1
    for section_en, section_ja, definitions in SECTIONS:
        for slug, name_ja, name_en, focus in definitions:
            item_id = f"COM-{number:06d}"
            item = make_item(item_id, slug, name_ja, name_en, focus, section_en, section_ja)
            items.append(item)
            index_lines.append(f"  - {item['filename']}")
            number += 1
    if len(items) != 100:
        raise ValueError(f"Expected 100 items, got {len(items)}")
    index_lines.extend([
        "notes:",
        "  - コミュニケーションコアは観測材料であり、人格や能力を単独で断定しない",
        "  - 相手・文化・媒体・目的・時間帯による変化をModifierで補正する",
        "  - 私的会話や機微情報は同意・最小化・保持期間をアプリ側で管理する",
    ])
    pack = {
        "output_dir": "vol25_communication_core/communication_core_001_100",
        "index_filename": "communication_core_001_100_index.yml",
        "index_content": "\n".join(index_lines) + "\n",
        "items": items,
    }
    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(json.dumps(pack, ensure_ascii=False, indent=2), encoding="utf-8")
    print(f"Created: {OUT}")
    print(f"Items: {len(items)}")


if __name__ == "__main__":
    main()
