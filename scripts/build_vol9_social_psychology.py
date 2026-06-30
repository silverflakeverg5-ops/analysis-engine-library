import json
from pathlib import Path

OUT = Path("data/master_packs/vol9_social_psychology_051_100.json")

SECTIONS = [
    {
        "category": "Social Psychology - Prosocial Behavior",
        "name_ja": "社会心理・向社会的行動",
        "items": [
            ("SOCPSY-000051", "prosocial_behavior", "向社会的行動", "Prosocial Behavior", "他者や集団の利益になるように行動すること。"),
            ("SOCPSY-000052", "helping_behavior", "援助行動", "Helping Behavior", "困っている他者に対して支援や助けを提供する行動。"),
            ("SOCPSY-000053", "altruism", "利他性", "Altruism", "自己利益よりも他者の利益を優先しようとする傾向。"),
            ("SOCPSY-000054", "empathic_concern", "共感的関心", "Empathic Concern", "他者の苦痛や困難に対して心配や思いやりを感じる状態。"),
            ("SOCPSY-000055", "bystander_effect", "傍観者効果", "Bystander Effect", "周囲に他者がいるほど援助行動が起こりにくくなる現象。"),
            ("SOCPSY-000056", "diffusion_of_responsibility", "責任分散", "Diffusion of Responsibility", "集団内で個人の責任感が弱まりやすくなる現象。"),
            ("SOCPSY-000057", "volunteering_behavior", "ボランティア行動", "Volunteering Behavior", "報酬を主目的とせず、他者や社会のために時間や労力を提供する行動。"),
            ("SOCPSY-000058", "donation_behavior", "寄付行動", "Donation Behavior", "資金・物品・資源を他者や社会的目的に提供する行動。"),
            ("SOCPSY-000059", "care_behavior", "ケア行動", "Care Behavior", "他者の状態や必要に注意を向け、継続的に支える行動。"),
            ("SOCPSY-000060", "mutual_aid", "相互扶助", "Mutual Aid", "互いに支援し合う関係や集団内の協力行動。")
        ]
    },
    {
        "category": "Social Psychology - Aggression Conflict",
        "name_ja": "社会心理・攻撃葛藤",
        "items": [
            ("SOCPSY-000061", "aggression", "攻撃性", "Aggression", "他者に心理的・身体的・社会的損害を与える可能性のある行動傾向。"),
            ("SOCPSY-000062", "hostile_aggression", "敵意的攻撃", "Hostile Aggression", "怒りや敵意に基づいて相手へ害を与えようとする攻撃行動。"),
            ("SOCPSY-000063", "instrumental_aggression", "道具的攻撃", "Instrumental Aggression", "目的達成の手段として行われる攻撃的行動。"),
            ("SOCPSY-000064", "relational_aggression", "関係性攻撃", "Relational Aggression", "排除・噂・無視など人間関係を通じて相手に害を与える行動。"),
            ("SOCPSY-000065", "verbal_aggression", "言語的攻撃", "Verbal Aggression", "侮辱・批判・威圧など言語によって相手に圧力や傷つきを与える行動。"),
            ("SOCPSY-000066", "retaliation", "報復行動", "Retaliation", "受けた損害や不公平に対して仕返しを行う行動。"),
            ("SOCPSY-000067", "anger_expression_social", "怒り表出", "Anger Expression", "対人場面で怒りや不満を表現する行動。"),
            ("SOCPSY-000068", "hostility", "敵意", "Hostility", "他者に対する否定的・攻撃的な見方や態度。"),
            ("SOCPSY-000069", "conflict_escalation", "葛藤エスカレーション", "Conflict Escalation", "対立が強まり、感情的・行動的反応が激化していく過程。"),
            ("SOCPSY-000070", "de_escalation", "葛藤沈静化", "De Escalation", "対立や感情的緊張を弱め、解決可能な状態へ戻す過程。")
        ]
    },
    {
        "category": "Social Psychology - Attitude Behavior",
        "name_ja": "社会心理・態度行動",
        "items": [
            ("SOCPSY-000071", "attitude", "態度", "Attitude", "対象に対する肯定的または否定的な評価傾向。"),
            ("SOCPSY-000072", "attitude_change", "態度変容", "Attitude Change", "情報・経験・説得・社会的影響により態度が変化する過程。"),
            ("SOCPSY-000073", "cognitive_dissonance", "認知的不協和", "Cognitive Dissonance", "信念・態度・行動の矛盾により不快感が生じ、解消しようとする状態。"),
            ("SOCPSY-000074", "self_perception_theory", "自己知覚理論", "Self Perception Theory", "自分の行動を観察することで自分の態度や好みを推測する考え方。"),
            ("SOCPSY-000075", "behavioral_intention", "行動意図", "Behavioral Intention", "特定の行動を取ろうとする意思や予定。"),
            ("SOCPSY-000076", "attitude_behavior_gap", "態度行動ギャップ", "Attitude Behavior Gap", "態度や意図が実際の行動と一致しない現象。"),
            ("SOCPSY-000077", "implementation_intention", "実行意図", "Implementation Intention", "いつ・どこで・どのように行動するかを具体化した行動計画。"),
            ("SOCPSY-000078", "habit_attitude_interaction", "習慣態度相互作用", "Habit Attitude Interaction", "既存習慣と態度が行動選択に相互に影響する関係。"),
            ("SOCPSY-000079", "moral_attitude", "道徳的態度", "Moral Attitude", "善悪・公正・責任など道徳価値に基づく評価傾向。"),
            ("SOCPSY-000080", "identity_based_attitude", "アイデンティティベース態度", "Identity Based Attitude", "自己認識や所属集団と結びついた態度。")
        ]
    },
    {
        "category": "Social Psychology - Communication Persuasion",
        "name_ja": "社会心理・コミュニケーション説得",
        "items": [
            ("SOCPSY-000081", "message_framing", "メッセージフレーミング", "Message Framing", "同じ内容でも利益・損失・道徳などの表現枠組みによって受け取り方が変わること。"),
            ("SOCPSY-000082", "source_credibility", "情報源信頼性", "Source Credibility", "発信者の専門性・誠実性・信頼感が説得効果に与える影響。"),
            ("SOCPSY-000083", "elaboration_likelihood", "精緻化見込み", "Elaboration Likelihood", "説得メッセージをどの程度深く処理するかに関する理論的概念。"),
            ("SOCPSY-000084", "central_route_persuasion", "中心ルート説得", "Central Route Persuasion", "内容や根拠を深く検討することで態度が変化する説得過程。"),
            ("SOCPSY-000085", "peripheral_route_persuasion", "周辺ルート説得", "Peripheral Route Persuasion", "発信者の魅力や雰囲気など周辺手がかりにより態度が変わる説得過程。"),
            ("SOCPSY-000086", "fear_appeal", "恐怖訴求", "Fear Appeal", "危険や損失への恐怖を用いて行動変容を促すメッセージ手法。"),
            ("SOCPSY-000087", "gain_loss_message", "利得損失メッセージ", "Gain Loss Message", "得られる利益または避けられる損失を強調するメッセージ設計。"),
            ("SOCPSY-000088", "narrative_persuasion", "物語説得", "Narrative Persuasion", "物語や事例を通じて態度や行動意図が変化する説得過程。"),
            ("SOCPSY-000089", "two_sided_message", "両面提示メッセージ", "Two Sided Message", "肯定面と否定面の両方を提示する説得メッセージ。"),
            ("SOCPSY-000090", "reactance", "心理的リアクタンス", "Psychological Reactance", "自由を制限されたと感じることで反発や抵抗が生じる現象。")
        ]
    },
    {
        "category": "Social Psychology - Online Social Behavior",
        "name_ja": "社会心理・オンライン社会行動",
        "items": [
            ("SOCPSY-000091", "online_disinhibition_effect", "オンライン脱抑制効果", "Online Disinhibition Effect", "匿名性や距離感によりオンライン上で抑制が弱まりやすくなる現象。"),
            ("SOCPSY-000092", "parasocial_relationship", "パラソーシャル関係", "Parasocial Relationship", "メディア上の人物や配信者に対して一方向的な親近感を持つ関係。"),
            ("SOCPSY-000093", "online_identity", "オンラインアイデンティティ", "Online Identity", "オンライン上で形成・表現される自己像や所属感。"),
            ("SOCPSY-000094", "digital_self_presentation", "デジタル自己呈示", "Digital Self Presentation", "プロフィール・投稿・画像・発言を通じてオンライン上の印象を調整する行動。"),
            ("SOCPSY-000095", "online_social_comparison", "オンライン社会的比較", "Online Social Comparison", "SNSやオンライン情報を通じて他者と自分を比較すること。"),
            ("SOCPSY-000096", "cyber_ostracism", "サイバー排斥", "Cyber Ostracism", "オンライン上で無視・排除・反応されないことにより孤立感が生じる現象。"),
            ("SOCPSY-000097", "flaming_behavior", "炎上・攻撃的投稿行動", "Flaming Behavior", "オンライン上で攻撃的・挑発的・過激な発言を行う行動。"),
            ("SOCPSY-000098", "online_group_polarization", "オンライン集団極性化", "Online Group Polarization", "オンライン集団内で意見が極端化しやすくなる現象。"),
            ("SOCPSY-000099", "digital_reputation", "デジタル評判", "Digital Reputation", "オンライン上の評価・履歴・反応によって形成される評判。"),
            ("SOCPSY-000100", "online_support_seeking", "オンライン支援要請", "Online Support Seeking", "オンライン上で相談・情報・共感・助けを求める行動。")
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
        "output_dir": "vol9_social_psychology/social_psychology_051_100",
        "index_filename": "social_psychology_051_100_index.yml",
        "index_content": "\n".join(index_lines) + "\n",
        "items": all_items
    }

    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(json.dumps(pack, ensure_ascii=False, indent=2), encoding="utf-8")

    print(f"Created: {OUT}")
    print(f"Items: {len(all_items)}")


if __name__ == "__main__":
    main()