import json
from pathlib import Path

OUT = Path("data/master_packs/vol7_environment_051_100.json")

SECTIONS = [
    {
        "category": "Environment - Culture",
        "name_ja": "環境要因・文化",
        "items": [
            ("ENV-000051", "cultural_norms", "文化的規範", "Cultural Norms", "集団や社会で共有される望ましい行動・価値・判断基準。"),
            ("ENV-000052", "collectivism_environment", "集団主義環境", "Collectivism Environment", "個人より集団調和・役割・関係性が重視されやすい文化環境。"),
            ("ENV-000053", "individualism_environment", "個人主義環境", "Individualism Environment", "個人の選択・自立・自己表現が重視されやすい文化環境。"),
            ("ENV-000054", "power_distance", "権力格差", "Power Distance", "上下関係や権威差をどの程度当然視するかに関する文化的環境。"),
            ("ENV-000055", "uncertainty_avoidance_culture", "不確実性回避文化", "Uncertainty Avoidance Culture", "曖昧さや予測不能な状況を避け、ルールや安定を重視する文化環境。"),
            ("ENV-000056", "communication_context_culture", "文脈依存コミュニケーション文化", "Communication Context Culture", "明示的表現よりも空気・文脈・関係性を重視する文化環境。"),
            ("ENV-000057", "achievement_culture", "達成重視文化", "Achievement Culture", "成果・競争・成功・能力証明が強く重視される文化環境。"),
            ("ENV-000058", "modesty_norm", "謙遜規範", "Modesty Norm", "自己主張や自己評価を控えめに表現することが望まれやすい文化的規範。"),
            ("ENV-000059", "honor_shame_culture", "名誉恥文化", "Honor Shame Culture", "社会的評価・面子・恥の回避が行動に強く影響する文化環境。"),
            ("ENV-000060", "cultural_identity", "文化的アイデンティティ", "Cultural Identity", "自分が属する文化・地域・集団への同一視や帰属感。")
        ]
    },
    {
        "category": "Environment - Economic",
        "name_ja": "環境要因・経済",
        "items": [
            ("ENV-000061", "economic_security", "経済的安定性", "Economic Security", "生活費・収入・雇用などが安定している度合い。"),
            ("ENV-000062", "financial_stress", "金銭的ストレス", "Financial Stress", "収入不足・支出不安・借入・将来不安などによる経済的負荷。"),
            ("ENV-000063", "resource_availability", "資源利用可能性", "Resource Availability", "時間・お金・道具・情報・支援など必要資源へアクセスできる度合い。"),
            ("ENV-000064", "scarcity_environment", "希少性環境", "Scarcity Environment", "お金・時間・支援などの不足が継続し、判断や行動に影響する環境。"),
            ("ENV-000065", "income_volatility", "収入変動性", "Income Volatility", "収入が不安定で、将来見通しや意思決定に影響する状態。"),
            ("ENV-000066", "opportunity_access", "機会アクセス", "Opportunity Access", "教育・仕事・成長・交流などの機会へ到達できる度合い。"),
            ("ENV-000067", "transport_access", "移動アクセス", "Transport Access", "通学・通勤・外出・社会参加に必要な移動手段の利用しやすさ。"),
            ("ENV-000068", "housing_stability", "住居安定性", "Housing Stability", "住まいの安全性・継続性・快適性が確保されている度合い。"),
            ("ENV-000069", "food_security", "食の安定性", "Food Security", "十分で安定した食事や栄養へアクセスできる度合い。"),
            ("ENV-000070", "economic_mobility_context", "経済的流動性環境", "Economic Mobility Context", "努力や選択によって経済状況を改善できる見通しがある環境。")
        ]
    },
    {
        "category": "Environment - Physical",
        "name_ja": "環境要因・物理環境",
        "items": [
            ("ENV-000071", "noise_environment", "騒音環境", "Noise Environment", "周囲の音や騒音が注意・睡眠・ストレスに影響する環境。"),
            ("ENV-000072", "lighting_environment", "照明環境", "Lighting Environment", "明るさ・光の質・時間帯による覚醒や集中への影響。"),
            ("ENV-000073", "temperature_environment", "温度環境", "Temperature Environment", "暑さ・寒さ・温度変化が快適性や作業効率に影響する環境。"),
            ("ENV-000074", "crowding_environment", "混雑環境", "Crowding Environment", "人や物が多く、圧迫感・ストレス・注意負荷が生じやすい環境。"),
            ("ENV-000075", "private_space", "私的空間", "Private Space", "一人で休む・考える・作業するための空間が確保されている度合い。"),
            ("ENV-000076", "workspace_design", "作業空間設計", "Workspace Design", "机・椅子・配置・視界・道具など作業効率に影響する空間設計。"),
            ("ENV-000077", "natural_environment_access", "自然環境アクセス", "Natural Environment Access", "緑地・公園・自然光・屋外環境へ接触できる度合い。"),
            ("ENV-000078", "sleep_environment", "睡眠環境", "Sleep Environment", "騒音・光・温度・寝具など睡眠の質に影響する環境。"),
            ("ENV-000079", "safety_environment", "安全環境", "Safety Environment", "事故・犯罪・危険への不安が少なく安心して生活できる環境。"),
            ("ENV-000080", "accessibility_environment", "アクセシビリティ環境", "Accessibility Environment", "身体的・認知的・技術的制約があっても利用や参加がしやすい環境。")
        ]
    },
    {
        "category": "Environment - Life Event",
        "name_ja": "環境要因・ライフイベント",
        "items": [
            ("ENV-000081", "transition_event", "移行イベント", "Transition Event", "進学・就職・転職・引越しなど生活構造が変わる出来事。"),
            ("ENV-000082", "loss_event", "喪失イベント", "Loss Event", "人間関係・役割・所有物・機会などの喪失を伴う出来事。"),
            ("ENV-000083", "success_event", "成功イベント", "Success Event", "達成・昇進・合格・承認など、自己評価や行動を変える肯定的出来事。"),
            ("ENV-000084", "failure_event", "失敗イベント", "Failure Event", "不合格・ミス・挫折・拒絶など、感情や判断に影響する出来事。"),
            ("ENV-000085", "relationship_change_event", "関係変化イベント", "Relationship Change Event", "出会い・別れ・結婚・離婚・人間関係の変化を伴う出来事。"),
            ("ENV-000086", "health_event", "健康イベント", "Health Event", "病気・怪我・体調変化など生活や行動に影響する健康関連の出来事。"),
            ("ENV-000087", "caregiving_event", "ケア役割イベント", "Caregiving Event", "家族や他者の世話を担うことで生活負荷が変わる出来事。"),
            ("ENV-000088", "financial_change_event", "経済変化イベント", "Financial Change Event", "収入増減・失職・借入・支出増など経済状況が変わる出来事。"),
            ("ENV-000089", "identity_transition", "アイデンティティ移行", "Identity Transition", "役割・所属・自己認識が変わる人生上の移行過程。"),
            ("ENV-000090", "major_stressor_event", "重大ストレスイベント", "Major Stressor Event", "生活全体に大きな負荷を与える重大な出来事。")
        ]
    },
    {
        "category": "Environment - Time Lifestyle",
        "name_ja": "環境要因・時間生活",
        "items": [
            ("ENV-000091", "daily_schedule_stability", "日課安定性", "Daily Schedule Stability", "起床・食事・作業・休息などの日々の予定が安定している度合い。"),
            ("ENV-000092", "time_pressure_lifestyle", "生活時間圧", "Lifestyle Time Pressure", "日常生活で常に急ぎや締切に追われる環境要因。"),
            ("ENV-000093", "commute_burden", "通勤通学負荷", "Commute Burden", "移動時間・混雑・待ち時間などによる日常的負荷。"),
            ("ENV-000094", "rest_opportunity", "休息機会", "Rest Opportunity", "睡眠以外に休憩・回復・気分転換を取れる機会の多さ。"),
            ("ENV-000095", "leisure_access", "余暇アクセス", "Leisure Access", "趣味・遊び・リラックス活動へ参加できる時間や資源の利用可能性。"),
            ("ENV-000096", "work_life_boundary", "仕事生活境界", "Work Life Boundary", "仕事・学業・家庭・私生活の境界が明確に保たれている度合い。"),
            ("ENV-000097", "sleep_schedule_regularness", "睡眠スケジュール規則性", "Sleep Schedule Regularness", "就寝・起床時間が規則的に保たれている度合い。"),
            ("ENV-000098", "meal_rhythm", "食事リズム", "Meal Rhythm", "食事の時間・回数・安定性が生活リズムに与える環境要因。"),
            ("ENV-000099", "activity_rhythm", "活動リズム", "Activity Rhythm", "一日の活動量や集中時間帯のパターン。"),
            ("ENV-000100", "recovery_environment", "回復環境", "Recovery Environment", "疲労・ストレス・認知負荷から回復しやすい生活環境。")
        ]
    }
]


def make_item(item_id, slug, name_ja, name_en, definition_ja, category, parent_ja):
    return {
        "filename": f"{item_id}_{slug}.yml",
        "id": item_id,
        "knowledge_type": "environment_factor",
        "name_ja": name_ja,
        "name_en": name_en,
        "category": "Environment",
        "attribute": category.replace("Environment - ", ""),
        "definition_ja": definition_ja,
        "tags": ["CAT:環境要因", f"CAT:{parent_ja}", "ATTR:補正要因"],
        "parent": [parent_ja],
        "related": ["行動観測", "性格", "認知科学"],
        "observable_data": [
            f"{name_ja}関連行動変化",
            f"{name_ja}関連反応時間",
            f"{name_ja}関連継続率",
            f"{name_ja}関連ストレス反応"
        ],
        "signal_candidates": [
            f"{name_ja}が行動・感情・判断に影響している可能性がある",
            "環境条件の変化に応じて行動パターンが変化する"
        ],
        "device_level": "スマホ・PCのみ推定可能",
        "modifiers": ["年齢", "文化", "生活状況", "個人差"],
        "evidence": "環境心理学・発達心理学・社会心理学・HCI研究で使用",
        "status": "active"
    }


def main():
    all_items = []
    index_lines = ["category: Environment", "name_ja: 環境要因", "items:"]

    for section in SECTIONS:
        parent_ja = section["name_ja"].replace("環境要因・", "")
        for raw in section["items"]:
            item = make_item(*raw, category=section["category"], parent_ja=parent_ja)
            all_items.append(item)
            index_lines.append(f"  - {item['filename']}")

    index_lines.extend([
        "notes:",
        "  - 環境要因は本人特性ではなく補正要因として扱う",
        "  - 観測可能データとSignal候補を中心に管理する",
        "  - アプリ側でスコアリング・推論・表示を行う"
    ])

    pack = {
        "output_dir": "vol7_environment/environment_051_100",
        "index_filename": "environment_051_100_index.yml",
        "index_content": "\n".join(index_lines) + "\n",
        "items": all_items
    }

    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(json.dumps(pack, ensure_ascii=False, indent=2), encoding="utf-8")

    print(f"Created: {OUT}")
    print(f"Items: {len(all_items)}")


if __name__ == "__main__":
    main()