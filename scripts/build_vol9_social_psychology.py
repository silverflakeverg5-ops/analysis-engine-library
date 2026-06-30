import json
from pathlib import Path

OUT = Path("data/master_packs/vol9_social_psychology_001_050.json")

SECTIONS = [
    {
        "category": "Social Psychology - Social Influence",
        "name_ja": "社会心理・社会的影響",
        "items": [
            ("SOCPSY-000001", "social_influence", "社会的影響", "Social Influence", "他者や集団の存在・期待・行動が個人の判断や行動に影響する現象。"),
            ("SOCPSY-000002", "conformity", "同調", "Conformity", "集団や多数派の意見・行動に合わせて自分の判断や行動を変える現象。"),
            ("SOCPSY-000003", "obedience", "服従", "Obedience", "権威や命令に従って行動する社会的影響過程。"),
            ("SOCPSY-000004", "compliance", "承諾", "Compliance", "明示的または暗黙の依頼に応じて行動を変えること。"),
            ("SOCPSY-000005", "persuasion", "説得", "Persuasion", "メッセージや相互作用によって態度や行動が変化する過程。"),
            ("SOCPSY-000006", "social_proof", "社会的証明", "Social Proof", "他者の行動や選択を根拠に、何が正しいか判断する傾向。"),
            ("SOCPSY-000007", "normative_influence", "規範的影響", "Normative Influence", "受け入れられたい、拒絶されたくないという動機による社会的影響。"),
            ("SOCPSY-000008", "informational_influence", "情報的影響", "Informational Influence", "他者の判断を情報源として利用することによる社会的影響。"),
            ("SOCPSY-000009", "minority_influence", "少数派影響", "Minority Influence", "一貫した少数派の主張が多数派や集団判断に影響する過程。"),
            ("SOCPSY-000010", "social_contagion", "社会的伝染", "Social Contagion", "感情・行動・態度が集団内で広がる現象。")
        ]
    },
    {
        "category": "Social Psychology - Group Dynamics",
        "name_ja": "社会心理・集団力学",
        "items": [
            ("SOCPSY-000011", "group_dynamics", "集団力学", "Group Dynamics", "集団内の相互作用・役割・規範・意思決定の仕組み。"),
            ("SOCPSY-000012", "group_norms", "集団規範", "Group Norms", "集団内で共有される望ましい行動や判断の基準。"),
            ("SOCPSY-000013", "group_cohesion", "集団凝集性", "Group Cohesion", "集団メンバー同士の結びつきや一体感の強さ。"),
            ("SOCPSY-000014", "social_identity", "社会的アイデンティティ", "Social Identity", "自分が特定の集団に属しているという自己認識。"),
            ("SOCPSY-000015", "ingroup_outgroup", "内集団外集団", "Ingroup Outgroup", "自分が属する集団と属さない集団を区別する認知枠組み。"),
            ("SOCPSY-000016", "group_polarization", "集団極性化", "Group Polarization", "集団討議後に意見がより極端な方向へ強まる現象。"),
            ("SOCPSY-000017", "groupthink", "集団思考", "Groupthink", "合意や調和を重視しすぎて批判的検討が弱まる集団意思決定現象。"),
            ("SOCPSY-000018", "social_loafing", "社会的手抜き", "Social Loafing", "集団作業で個人の努力量が低下する現象。"),
            ("SOCPSY-000019", "deindividuation", "没個性化", "Deindividuation", "集団や匿名性の中で自己意識や責任感が弱まりやすくなる現象。"),
            ("SOCPSY-000020", "collective_efficacy", "集合的効力感", "Collective Efficacy", "集団として目標を達成できるという共有された信念。")
        ]
    },
    {
        "category": "Social Psychology - Interpersonal Perception",
        "name_ja": "社会心理・対人認知",
        "items": [
            ("SOCPSY-000021", "impression_formation", "印象形成", "Impression Formation", "他者の外見・発言・行動から全体的な印象を作る過程。"),
            ("SOCPSY-000022", "person_perception", "人物知覚", "Person Perception", "他者の性格・意図・能力・感情を推測する認知過程。"),
            ("SOCPSY-000023", "attribution_process", "原因帰属過程", "Attribution Process", "行動や出来事の原因を内的要因または外的要因に説明する過程。"),
            ("SOCPSY-000024", "stereotype", "ステレオタイプ", "Stereotype", "特定集団に対して持たれる一般化された信念や期待。"),
            ("SOCPSY-000025", "prejudice", "偏見", "Prejudice", "特定集団や個人に対する事前の否定的または肯定的態度。"),
            ("SOCPSY-000026", "discrimination_behavior", "差別行動", "Discrimination Behavior", "集団属性や偏見に基づいて異なる扱いをする行動。"),
            ("SOCPSY-000027", "thin_slice_judgment", "薄切り判断", "Thin Slice Judgment", "短い観察情報から他者の特徴や状態を推測する判断。"),
            ("SOCPSY-000028", "nonverbal_cue_reading", "非言語手がかり読解", "Nonverbal Cue Reading", "表情・姿勢・視線・声などから相手の状態を読む過程。"),
            ("SOCPSY-000029", "trust_perception", "信頼知覚", "Trust Perception", "相手が信頼できるかどうかを判断する対人認知過程。"),
            ("SOCPSY-000030", "warmth_competence_judgment", "温かさ有能さ判断", "Warmth Competence Judgment", "他者を親しみやすさと能力の軸で評価する対人判断。")
        ]
    },
    {
        "category": "Social Psychology - Relationship",
        "name_ja": "社会心理・関係性",
        "items": [
            ("SOCPSY-000031", "relationship_quality", "関係性の質", "Relationship Quality", "信頼・安心感・支援・葛藤の少なさなどを含む対人関係の質。"),
            ("SOCPSY-000032", "attachment_style", "愛着スタイル", "Attachment Style", "親密な関係での安心感・距離感・不安に関わる対人傾向。"),
            ("SOCPSY-000033", "trust_building", "信頼形成", "Trust Building", "一貫性・誠実性・支援などを通じて信頼が形成される過程。"),
            ("SOCPSY-000034", "reciprocity", "互恵性", "Reciprocity", "相手から受けた行為に対して返報しようとする社会的原理。"),
            ("SOCPSY-000035", "self_disclosure", "自己開示", "Self Disclosure", "自分の考え・感情・経験を他者に伝える対人行動。"),
            ("SOCPSY-000036", "intimacy_development", "親密性形成", "Intimacy Development", "相互理解や信頼を通じて関係が深まる過程。"),
            ("SOCPSY-000037", "relationship_maintenance", "関係維持", "Relationship Maintenance", "関係を保つための連絡・配慮・支援・調整行動。"),
            ("SOCPSY-000038", "conflict_resolution", "葛藤解決", "Conflict Resolution", "対立や不一致を調整し、関係や合意を回復する過程。"),
            ("SOCPSY-000039", "social_exchange", "社会的交換", "Social Exchange", "報酬・コスト・公平性に基づいて関係を評価する考え方。"),
            ("SOCPSY-000040", "relationship_boundary", "関係境界", "Relationship Boundary", "親密さ・役割・責任・距離感の範囲を調整する対人要因。")
        ]
    },
    {
        "category": "Social Psychology - Self Presentation",
        "name_ja": "社会心理・自己呈示",
        "items": [
            ("SOCPSY-000041", "self_presentation", "自己呈示", "Self Presentation", "他者から望ましく見られるように自分の印象を調整する行動。"),
            ("SOCPSY-000042", "impression_management", "印象管理", "Impression Management", "他者に与える印象を意図的または無意識に調整する過程。"),
            ("SOCPSY-000043", "face_saving", "面子保持", "Face Saving", "自分や相手の社会的評価や体面を守ろうとする行動。"),
            ("SOCPSY-000044", "social_approval_need", "承認欲求", "Need for Social Approval", "他者から認められたい、好意的に評価されたいという欲求。"),
            ("SOCPSY-000045", "evaluation_apprehension", "評価懸念", "Evaluation Apprehension", "他者から評価されることへの不安や緊張。"),
            ("SOCPSY-000046", "public_self_consciousness", "公的自己意識", "Public Self Consciousness", "他者から見られる自分への意識の強さ。"),
            ("SOCPSY-000047", "private_self_consciousness", "私的自己意識", "Private Self Consciousness", "自分の内面状態や考えへの意識の強さ。"),
            ("SOCPSY-000048", "identity_signaling", "アイデンティティシグナリング", "Identity Signaling", "選択・発言・所属を通じて自分らしさや価値観を示す行動。"),
            ("SOCPSY-000049", "authenticity_expression", "真正性表現", "Authenticity Expression", "自分の本音や価値観に沿って自己を表現すること。"),
            ("SOCPSY-000050", "social_masking", "社会的マスキング", "Social Masking", "場に合わせるために本来の反応や特徴を隠したり調整する行動。")
        ]
    }
]


def make_item(item_id, slug, name_ja, name_en, definition_ja, category, parent_ja):
    return {
        "filename": f"{item_id}_{slug}.yml",
        "id": item_id,
        "knowledge_type": "social_psychology",
        "name_ja": name_ja,
        "name_en": name_en,
        "category": "Social Psychology",
        "attribute": category.replace("Social Psychology - ", ""),
        "definition_ja": definition_ja,
        "tags": ["CAT:社会心理", f"CAT:{parent_ja}", "ATTR:社会的要因"],
        "parent": [parent_ja],
        "related": ["性格", "行動観測", "環境要因"],
        "observable_data": [
            f"{name_ja}関連行動変化",
            f"{name_ja}関連反応時間",
            f"{name_ja}関連選択率",
            f"{name_ja}関連対人反応"
        ],
        "signal_candidates": [
            f"{name_ja}が対人判断・行動・感情に影響している可能性がある",
            "社会的条件の変化に応じて行動パターンが変化する"
        ],
        "device_level": "スマホ・PCのみ推定可能",
        "modifiers": ["文化", "関係性", "集団規範", "評価環境"],
        "evidence": "社会心理学・対人心理学・組織心理学・HCI研究で使用",
        "status": "active"
    }


def main():
    all_items = []
    index_lines = ["category: Social Psychology", "name_ja: 社会心理", "items:"]

    for section in SECTIONS:
        parent_ja = section["name_ja"].replace("社会心理・", "")
        for raw in section["items"]:
            item = make_item(*raw, category=section["category"], parent_ja=parent_ja)
            all_items.append(item)
            index_lines.append(f"  - {item['filename']}")

    index_lines.extend([
        "notes:",
        "  - 社会心理は性格断定ではなく推論材料として扱う",
        "  - 観測可能データとSignal候補を中心に管理する",
        "  - アプリ側でスコアリング・推論・表示を行う"
    ])

    pack = {
        "output_dir": "vol9_social_psychology/social_psychology_001_050",
        "index_filename": "social_psychology_001_050_index.yml",
        "index_content": "\n".join(index_lines) + "\n",
        "items": all_items
    }

    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(json.dumps(pack, ensure_ascii=False, indent=2), encoding="utf-8")

    print(f"Created: {OUT}")
    print(f"Items: {len(all_items)}")


if __name__ == "__main__":
    main()