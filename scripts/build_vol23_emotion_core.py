import json
from pathlib import Path

OUT = Path("data/master_packs/vol23_emotion_core_001_100.json")

SECTIONS = [
    {
        "category": "Emotion Core - Basic Emotions",
        "name_ja": "感情コア・基本感情",
        "items": [
            ("EMO-000001", "joy", "喜び", "Joy", "望ましい出来事や達成によって生じる肯定的感情。"),
            ("EMO-000002", "sadness", "悲しみ", "Sadness", "喪失・失敗・期待外れによって生じる否定的感情。"),
            ("EMO-000003", "anger", "怒り", "Anger", "妨害・不公平・侵害に対して生じる攻撃的または防衛的感情。"),
            ("EMO-000004", "fear", "恐怖", "Fear", "危険・脅威・不確実な害に対して生じる回避的感情。"),
            ("EMO-000005", "surprise", "驚き", "Surprise", "予想外の出来事に対して一時的に注意が向く感情反応。"),
            ("EMO-000006", "disgust", "嫌悪", "Disgust", "不快・汚染・拒否したい対象に対して生じる感情。"),
            ("EMO-000007", "trust", "信頼", "Trust", "相手や状況が安全で期待可能だと感じる肯定的感情。"),
            ("EMO-000008", "anticipation", "期待", "Anticipation", "未来の出来事や結果を予測して生じる感情。"),
            ("EMO-000009", "interest", "興味", "Interest", "新しい情報や対象に注意を向け探索したくなる感情。"),
            ("EMO-000010", "calmness", "落ち着き", "Calmness", "脅威や緊張が低く安定している感情状態。")
        ]
    },
    {
        "category": "Emotion Core - Social Emotions",
        "name_ja": "感情コア・社会的感情",
        "items": [
            ("EMO-000011", "shame", "恥", "Shame", "自己全体が否定的に評価されたと感じる社会的感情。"),
            ("EMO-000012", "guilt", "罪悪感", "Guilt", "自分の行動が他者や規範に反したと感じる感情。"),
            ("EMO-000013", "embarrassment", "気まずさ", "Embarrassment", "社会的場面で失敗や不自然さを意識した時の感情。"),
            ("EMO-000014", "pride", "誇り", "Pride", "達成や評価によって自己価値が高まる感情。"),
            ("EMO-000015", "envy", "羨望", "Envy", "他者が持つ望ましいものを自分も欲しいと感じる感情。"),
            ("EMO-000016", "jealousy", "嫉妬", "Jealousy", "大切な関係や立場を他者に奪われる恐れから生じる感情。"),
            ("EMO-000017", "gratitude", "感謝", "Gratitude", "他者からの支援や好意を価値あるものとして感じる感情。"),
            ("EMO-000018", "admiration", "憧れ", "Admiration", "他者の能力・姿勢・成果に価値を感じる感情。"),
            ("EMO-000019", "contempt", "軽蔑", "Contempt", "相手を低く評価し距離を置こうとする社会的感情。"),
            ("EMO-000020", "compassion", "思いやり", "Compassion", "他者の苦痛を理解し助けたいと感じる感情。")
        ]
    },
    {
        "category": "Emotion Core - Self Related Emotions",
        "name_ja": "感情コア・自己関連感情",
        "items": [
            ("EMO-000021", "self_confidence", "自信", "Self Confidence", "自分の能力や判断に対して肯定的に感じる状態。"),
            ("EMO-000022", "self_doubt", "自己疑念", "Self Doubt", "自分の能力・判断・価値に疑いを持つ感情状態。"),
            ("EMO-000023", "regret", "後悔", "Regret", "過去の選択や行動を別にすべきだったと感じる感情。"),
            ("EMO-000024", "relief", "安堵", "Relief", "脅威や不安が解消された時に生じる感情。"),
            ("EMO-000025", "hope", "希望", "Hope", "望ましい未来が実現する可能性を感じる感情。"),
            ("EMO-000026", "hopelessness", "絶望感", "Hopelessness", "望ましい変化が起きないと感じる強い否定的状態。"),
            ("EMO-000027", "loneliness", "孤独感", "Loneliness", "望むつながりが不足していると感じる感情。"),
            ("EMO-000028", "belonging", "所属感", "Belonging", "集団や関係の中に受け入れられていると感じる感情。"),
            ("EMO-000029", "insecurity", "不安定感", "Insecurity", "自分や状況に確かさがなく安心できない感情状態。"),
            ("EMO-000030", "self_acceptance", "自己受容", "Self Acceptance", "自分の特徴や状態を否定せず受け止める感情状態。")
        ]
    },
    {
        "category": "Emotion Core - Arousal Valence",
        "name_ja": "感情コア・覚醒価",
        "items": [
            ("EMO-000031", "positive_valence", "ポジティブ価", "Positive Valence", "快・好ましさ・接近を伴う感情の方向性。"),
            ("EMO-000032", "negative_valence", "ネガティブ価", "Negative Valence", "不快・拒否・回避を伴う感情の方向性。"),
            ("EMO-000033", "high_arousal", "高覚醒感情", "High Arousal Emotion", "興奮・緊張・怒りなど活動水準が高い感情状態。"),
            ("EMO-000034", "low_arousal", "低覚醒感情", "Low Arousal Emotion", "落ち着き・退屈・疲労など活動水準が低い感情状態。"),
            ("EMO-000035", "pleasant_high_arousal", "快高覚醒", "Pleasant High Arousal", "楽しい興奮や熱中のように快で活動的な感情状態。"),
            ("EMO-000036", "pleasant_low_arousal", "快低覚醒", "Pleasant Low Arousal", "安心やリラックスのように快で穏やかな感情状態。"),
            ("EMO-000037", "unpleasant_high_arousal", "不快高覚醒", "Unpleasant High Arousal", "怒りや恐怖のように不快で活動水準が高い感情状態。"),
            ("EMO-000038", "unpleasant_low_arousal", "不快低覚醒", "Unpleasant Low Arousal", "落胆や無気力のように不快で活動水準が低い感情状態。"),
            ("EMO-000039", "emotional_intensity", "感情強度", "Emotional Intensity", "感情がどれほど強く経験されているかを示す概念。"),
            ("EMO-000040", "emotional_clarity", "感情明瞭性", "Emotional Clarity", "自分の感情をどの程度はっきり認識できているか。")
        ]
    },
    {
        "category": "Emotion Core - Emotion Dynamics",
        "name_ja": "感情コア・感情変化",
        "items": [
            ("EMO-000041", "emotional_duration", "感情持続", "Emotional Duration", "感情がどの程度の時間続くかを示す概念。"),
            ("EMO-000042", "emotional_volatility", "感情変動性", "Emotional Volatility", "感情が短時間で大きく変化する傾向。"),
            ("EMO-000043", "emotional_stability", "感情安定性", "Emotional Stability", "感情が過度に揺れず安定している傾向。"),
            ("EMO-000044", "emotional_reactivity", "感情反応性", "Emotional Reactivity", "刺激や出来事に対して感情が強く反応する傾向。"),
            ("EMO-000045", "emotional_recovery", "感情回復", "Emotional Recovery", "否定的感情から通常状態へ戻る過程。"),
            ("EMO-000046", "emotional_inertia", "感情慣性", "Emotional Inertia", "一度生じた感情状態が変わりにくい傾向。"),
            ("EMO-000047", "mood_shift", "気分転換", "Mood Shift", "持続的な気分状態が別の状態へ移ること。"),
            ("EMO-000048", "trigger_sensitivity", "感情トリガー感受性", "Trigger Sensitivity", "特定の刺激や文脈で感情が生じやすい傾向。"),
            ("EMO-000049", "emotional_baseline", "感情ベースライン", "Emotional Baseline", "本人の通常時の感情傾向や平均的状態。"),
            ("EMO-000050", "emotional_deviation", "感情ベースライン乖離", "Emotional Deviation", "現在の感情状態が通常傾向からどの程度外れているか。")
        ]
    },
    {
        "category": "Emotion Core - Emotion Regulation",
        "name_ja": "感情コア・感情調整",
        "items": [
            ("EMO-000051", "emotion_regulation", "感情調整", "Emotion Regulation", "感情の強さ・持続・表現を調整する過程。"),
            ("EMO-000052", "cognitive_reappraisal", "認知的再評価", "Cognitive Reappraisal", "状況の意味づけを変えて感情を調整する方略。"),
            ("EMO-000053", "expressive_suppression", "表出抑制", "Expressive Suppression", "感情を外に出さないよう抑える方略。"),
            ("EMO-000054", "distraction_regulation", "注意そらし調整", "Distraction Regulation", "注意を別対象へ向けて感情を弱める方略。"),
            ("EMO-000055", "problem_focused_coping", "問題焦点型対処", "Problem Focused Coping", "感情の原因となる問題を解決して感情を調整する方略。"),
            ("EMO-000056", "emotion_focused_coping", "感情焦点型対処", "Emotion Focused Coping", "感情そのものをなだめたり受け止めたりする対処方略。"),
            ("EMO-000057", "rumination", "反すう", "Rumination", "否定的出来事や感情について繰り返し考え続ける傾向。"),
            ("EMO-000058", "emotional_avoidance", "感情回避", "Emotional Avoidance", "不快な感情や関連状況を避けようとする傾向。"),
            ("EMO-000059", "acceptance_regulation", "受容的調整", "Acceptance Regulation", "感情を否定せず受け止めて調整する方略。"),
            ("EMO-000060", "self_soothing", "自己鎮静", "Self Soothing", "自分を落ち着かせる行動や思考によって感情を調整すること。")
        ]
    },
    {
        "category": "Emotion Core - Expression",
        "name_ja": "感情コア・感情表現",
        "items": [
            ("EMO-000061", "emotional_expression", "感情表現", "Emotional Expression", "表情・言葉・行動を通じて感情を外に示すこと。"),
            ("EMO-000062", "verbal_emotion_expression", "言語的感情表現", "Verbal Emotion Expression", "言葉や文章で感情を表すこと。"),
            ("EMO-000063", "nonverbal_emotion_expression", "非言語的感情表現", "Nonverbal Emotion Expression", "表情・姿勢・声色・動作で感情を表すこと。"),
            ("EMO-000064", "emotional_disclosure", "感情開示", "Emotional Disclosure", "自分の感情を他者に伝える行動。"),
            ("EMO-000065", "emotional_withholding", "感情保留", "Emotional Withholding", "感情をあえて伝えず内側に留める行動。"),
            ("EMO-000066", "emotional_masking", "感情マスキング", "Emotional Masking", "本来の感情と異なる表情や態度を示すこと。"),
            ("EMO-000067", "emotional_amplification", "感情増幅表現", "Emotional Amplification", "感情を実際より強く表現すること。"),
            ("EMO-000068", "emotional_minimization", "感情縮小表現", "Emotional Minimization", "感情を実際より弱く表現すること。"),
            ("EMO-000069", "emotion_word_use", "感情語使用", "Emotion Word Use", "喜び・不安・怒りなど感情語を使って状態を表すこと。"),
            ("EMO-000070", "affective_tone", "感情トーン", "Affective Tone", "文章・声・反応全体から伝わる感情的雰囲気。")
        ]
    },
    {
        "category": "Emotion Core - Recognition",
        "name_ja": "感情コア・感情認識",
        "items": [
            ("EMO-000071", "emotion_recognition", "感情認識", "Emotion Recognition", "自分や他者の感情を識別する能力や過程。"),
            ("EMO-000072", "self_emotion_awareness", "自己感情認識", "Self Emotion Awareness", "自分の感情状態に気づくこと。"),
            ("EMO-000073", "other_emotion_recognition", "他者感情認識", "Other Emotion Recognition", "他者の表情・言葉・行動から感情を読み取ること。"),
            ("EMO-000074", "emotional_accuracy", "感情認識精度", "Emotional Accuracy", "感情をどれほど正確に識別できるか。"),
            ("EMO-000075", "emotion_misattribution", "感情誤帰属", "Emotion Misattribution", "感情の原因や対象を誤って解釈すること。"),
            ("EMO-000076", "alexithymia_tendency", "感情同定困難傾向", "Alexithymia Tendency", "自分の感情を言語化・識別しにくい傾向。"),
            ("EMO-000077", "emotional_granularity", "感情粒度", "Emotional Granularity", "感情を細かく区別して認識できる度合い。"),
            ("EMO-000078", "empathy_accuracy", "共感的正確性", "Empathic Accuracy", "他者の感情や意図を正確に推測する力。"),
            ("EMO-000079", "emotional_perspective_taking", "感情的視点取得", "Emotional Perspective Taking", "相手の立場から感情を理解しようとする過程。"),
            ("EMO-000080", "emotion_context_inference", "感情文脈推論", "Emotion Context Inference", "状況や背景から感情の意味を推測すること。")
        ]
    },
    {
        "category": "Emotion Core - Emotion Behavior Link",
        "name_ja": "感情コア・感情行動連結",
        "items": [
            ("EMO-000081", "approach_emotion", "接近感情", "Approach Emotion", "対象に近づく・試す・関わる行動を促す感情。"),
            ("EMO-000082", "avoidance_emotion", "回避感情", "Avoidance Emotion", "対象から離れる・避ける・中断する行動を促す感情。"),
            ("EMO-000083", "anger_action_tendency", "怒り行動傾向", "Anger Action Tendency", "怒りによって抗議・攻撃・境界主張が起きやすくなる傾向。"),
            ("EMO-000084", "fear_action_tendency", "恐怖行動傾向", "Fear Action Tendency", "恐怖によって逃避・停止・確認行動が起きやすくなる傾向。"),
            ("EMO-000085", "sadness_action_tendency", "悲しみ行動傾向", "Sadness Action Tendency", "悲しみによって撤退・支援要請・内省が起きやすくなる傾向。"),
            ("EMO-000086", "joy_action_tendency", "喜び行動傾向", "Joy Action Tendency", "喜びによって共有・探索・継続行動が起きやすくなる傾向。"),
            ("EMO-000087", "anxiety_checking_behavior", "不安確認行動", "Anxiety Checking Behavior", "不安によって確認・検索・再確認が増える行動傾向。"),
            ("EMO-000088", "frustration_quit_behavior", "苛立ち離脱行動", "Frustration Quit Behavior", "苛立ちによって中断・離脱・攻撃的反応が起きやすくなる傾向。"),
            ("EMO-000089", "relief_continuation_behavior", "安堵後継続行動", "Relief Continuation Behavior", "不安解消後に行動継続や再挑戦がしやすくなる傾向。"),
            ("EMO-000090", "emotion_driven_choice", "感情駆動選択", "Emotion Driven Choice", "理性的比較より感情状態に強く影響された選択。")
        ]
    },
    {
        "category": "Emotion Core - Integration",
        "name_ja": "感情コア・統合",
        "items": [
            ("EMO-000091", "emotion_profile", "感情プロフィール", "Emotion Profile", "個人の感情反応・表現・調整・回復傾向をまとめた枠組み。"),
            ("EMO-000092", "emotion_pattern", "感情パターン", "Emotion Pattern", "特定状況で繰り返し現れる感情反応の傾向。"),
            ("EMO-000093", "emotion_context_mapping", "感情文脈対応", "Emotion Context Mapping", "感情を状況・相手・課題・時間帯と結びつけて理解する枠組み。"),
            ("EMO-000094", "emotion_signal_mapping", "感情シグナル対応", "Emotion Signal Mapping", "行動ログや言語表現を感情推定材料へ対応づける考え方。"),
            ("EMO-000095", "emotion_modifier_integration", "感情補正統合", "Emotion Modifier Integration", "疲労・睡眠・ストレス・環境を考慮して感情解釈を補正する枠組み。"),
            ("EMO-000096", "emotion_display_safety", "感情表示安全", "Emotion Display Safety", "感情推定を断定せず安全に表示する考え方。"),
            ("EMO-000097", "emotion_app_use_case", "感情アプリ利用", "Emotion App Use Case", "診断・ゲーム・秘書・教育などで感情知識を活用する枠組み。"),
            ("EMO-000098", "emotion_behavior_analysis", "感情行動分析", "Emotion Behavior Analysis", "感情と選択・継続・回避・対人行動の関係を分析する枠組み。"),
            ("EMO-000099", "emotion_knowledge_boundary", "感情知識境界", "Emotion Knowledge Boundary", "DBは感情推定を行わず、推論材料だけを提供する境界概念。"),
            ("EMO-000100", "emotion_core_integration", "感情コア統合", "Emotion Core Integration", "感情の種類・強度・変化・調整・表現・行動連結を統合する枠組み。")
        ]
    }
]


def make_item(item_id, slug, name_ja, name_en, definition_ja, category, parent_ja):
    return {
        "filename": f"{item_id}_{slug}.yml",
        "id": item_id,
        "knowledge_type": "emotion_core",
        "name_ja": name_ja,
        "name_en": name_en,
        "category": "Emotion Core",
        "attribute": category.replace("Emotion Core - ", ""),
        "definition_ja": definition_ja,
        "tags": ["CAT:感情", f"CAT:{parent_ja}", "ATTR:感情要因"],
        "parent": [parent_ja],
        "related": ["行動観測", "感情調整", "対人関係"],
        "observable_data": [
            f"{name_ja}表現頻度",
            f"{name_ja}関連語使用",
            f"{name_ja}発生文脈",
            f"{name_ja}後の行動変化"
        ],
        "signal_candidates": [
            f"{name_ja}に関連する言語表現や行動変化が観測される",
            "感情状態や感情反応傾向の推論材料になる"
        ],
        "device_level": "スマホ・PCで推定可能",
        "modifiers": ["文脈", "疲労", "睡眠", "ストレス"],
        "evidence": "感情心理学・社会心理学・認知科学・HCI研究で使用",
        "status": "active"
    }


def main():
    all_items = []
    index_lines = ["category: Emotion Core", "name_ja: 感情コア", "items:"]

    for section in SECTIONS:
        parent_ja = section["name_ja"].replace("感情コア・", "")
        for raw in section["items"]:
            item = make_item(*raw, category=section["category"], parent_ja=parent_ja)
            all_items.append(item)
            index_lines.append(f"  - {item['filename']}")

    index_lines.extend([
        "notes:",
        "  - 感情コアは感情推定の材料として扱う",
        "  - Knowledge DB側では感情判定や診断を行わない",
        "  - アプリ側で観測シグナル・補正要因・表示設計と組み合わせて利用する"
    ])

    pack = {
        "output_dir": "vol23_emotion_core/emotion_core_001_100",
        "index_filename": "emotion_core_001_100_index.yml",
        "index_content": "\n".join(index_lines) + "\n",
        "items": all_items
    }

    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(json.dumps(pack, ensure_ascii=False, indent=2), encoding="utf-8")

    print(f"Created: {OUT}")
    print(f"Items: {len(all_items)}")


if __name__ == "__main__":
    main()