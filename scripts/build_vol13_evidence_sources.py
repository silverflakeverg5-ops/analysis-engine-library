import json
from pathlib import Path

OUT = Path("data/master_packs/vol13_evidence_sources_001_050.json")

SECTIONS = [
    {
        "category": "Evidence Sources - Psychology",
        "name_ja": "根拠・心理学",
        "items": [
            ("EVID-000001", "cognitive_psychology_evidence", "認知心理学根拠", "Cognitive Psychology Evidence", "注意・記憶・判断・学習などの認知過程に関する心理学的根拠。"),
            ("EVID-000002", "personality_psychology_evidence", "性格心理学根拠", "Personality Psychology Evidence", "性格特性・個人差・行動傾向に関する心理学的根拠。"),
            ("EVID-000003", "social_psychology_evidence", "社会心理学根拠", "Social Psychology Evidence", "対人関係・集団・社会的影響に関する心理学的根拠。"),
            ("EVID-000004", "developmental_psychology_evidence", "発達心理学根拠", "Developmental Psychology Evidence", "年齢・発達段階・成長過程に関する心理学的根拠。"),
            ("EVID-000005", "educational_psychology_evidence", "教育心理学根拠", "Educational Psychology Evidence", "学習・動機づけ・評価・教育支援に関する心理学的根拠。"),
            ("EVID-000006", "clinical_psychology_evidence", "臨床心理学根拠", "Clinical Psychology Evidence", "ストレス・感情・心理的困難に関する臨床心理学的根拠。"),
            ("EVID-000007", "health_psychology_evidence", "健康心理学根拠", "Health Psychology Evidence", "健康行動・ストレス・生活習慣に関する心理学的根拠。"),
            ("EVID-000008", "organizational_psychology_evidence", "組織心理学根拠", "Organizational Psychology Evidence", "職場行動・リーダーシップ・組織環境に関する心理学的根拠。"),
            ("EVID-000009", "environmental_psychology_evidence", "環境心理学根拠", "Environmental Psychology Evidence", "物理環境・空間・地域環境が行動へ与える影響に関する根拠。"),
            ("EVID-000010", "positive_psychology_evidence", "ポジティブ心理学根拠", "Positive Psychology Evidence", "幸福感・強み・レジリエンス・成長に関する心理学的根拠。")
        ]
    },
    {
        "category": "Evidence Sources - Cognitive Science",
        "name_ja": "根拠・認知科学",
        "items": [
            ("EVID-000011", "cognitive_science_evidence", "認知科学根拠", "Cognitive Science Evidence", "人間の知覚・記憶・推論・学習を統合的に扱う根拠。"),
            ("EVID-000012", "decision_science_evidence", "意思決定科学根拠", "Decision Science Evidence", "選択・リスク・価値判断・バイアスに関する科学的根拠。"),
            ("EVID-000013", "behavioral_economics_evidence", "行動経済学根拠", "Behavioral Economics Evidence", "限定合理性・損失回避・ナッジなどに関する根拠。"),
            ("EVID-000014", "learning_science_evidence", "学習科学根拠", "Learning Science Evidence", "人間の学習過程・教材設計・学習支援に関する根拠。"),
            ("EVID-000015", "human_factors_evidence", "ヒューマンファクター根拠", "Human Factors Evidence", "人間の能力・限界・エラーを考慮した設計に関する根拠。"),
            ("EVID-000016", "hci_evidence", "HCI根拠", "Human Computer Interaction Evidence", "人間とコンピュータの相互作用・操作ログ・UXに関する根拠。"),
            ("EVID-000017", "ux_research_evidence", "UX研究根拠", "UX Research Evidence", "ユーザー体験・使いやすさ・満足度・行動観測に関する根拠。"),
            ("EVID-000018", "information_behavior_evidence", "情報行動研究根拠", "Information Behavior Evidence", "検索・閲覧・情報選択・情報回避に関する根拠。"),
            ("EVID-000019", "behavior_change_evidence", "行動変容研究根拠", "Behavior Change Evidence", "習慣形成・介入・継続支援に関する根拠。"),
            ("EVID-000020", "computational_behavior_evidence", "計算行動科学根拠", "Computational Behavioral Science Evidence", "行動ログやモデルを用いた人間行動理解に関する根拠。")
        ]
    },
    {
        "category": "Evidence Sources - Neuroscience Physiology",
        "name_ja": "根拠・神経生理",
        "items": [
            ("EVID-000021", "neuroscience_evidence", "神経科学根拠", "Neuroscience Evidence", "脳領域・神経伝達・ネットワークに関する根拠。"),
            ("EVID-000022", "cognitive_neuroscience_evidence", "認知神経科学根拠", "Cognitive Neuroscience Evidence", "認知機能と神経基盤の関係に関する根拠。"),
            ("EVID-000023", "affective_neuroscience_evidence", "感情神経科学根拠", "Affective Neuroscience Evidence", "感情・報酬・脅威処理の神経基盤に関する根拠。"),
            ("EVID-000024", "social_neuroscience_evidence", "社会神経科学根拠", "Social Neuroscience Evidence", "共感・信頼・社会判断の神経基盤に関する根拠。"),
            ("EVID-000025", "physiological_psychology_evidence", "生理心理学根拠", "Physiological Psychology Evidence", "身体反応と心理・行動の関係に関する根拠。"),
            ("EVID-000026", "sleep_research_evidence", "睡眠研究根拠", "Sleep Research Evidence", "睡眠・概日リズム・回復と認知行動の関係に関する根拠。"),
            ("EVID-000027", "stress_research_evidence", "ストレス研究根拠", "Stress Research Evidence", "急性・慢性ストレスと行動・感情・生理反応に関する根拠。"),
            ("EVID-000028", "psychophysiology_evidence", "精神生理学根拠", "Psychophysiology Evidence", "心拍・皮膚反応・覚醒などの生理指標に関する根拠。"),
            ("EVID-000029", "exercise_cognition_evidence", "運動認知研究根拠", "Exercise Cognition Evidence", "身体活動や運動が認知・気分に与える影響に関する根拠。"),
            ("EVID-000030", "nutrition_cognition_evidence", "栄養認知研究根拠", "Nutrition Cognition Evidence", "栄養・血糖・水分状態と認知・気分の関係に関する根拠。")
        ]
    },
    {
        "category": "Evidence Sources - Measurement",
        "name_ja": "根拠・測定",
        "items": [
            ("EVID-000031", "psychometrics_evidence", "心理測定根拠", "Psychometrics Evidence", "尺度・信頼性・妥当性・測定誤差に関する根拠。"),
            ("EVID-000032", "reliability_evidence", "信頼性根拠", "Reliability Evidence", "測定が一貫しているかを評価するための根拠。"),
            ("EVID-000033", "validity_evidence", "妥当性根拠", "Validity Evidence", "測定が目的とする概念を適切に捉えているかに関する根拠。"),
            ("EVID-000034", "construct_validity_evidence", "構成概念妥当性根拠", "Construct Validity Evidence", "概念定義と測定指標の対応に関する根拠。"),
            ("EVID-000035", "criterion_validity_evidence", "基準関連妥当性根拠", "Criterion Validity Evidence", "外部基準との関連から測定の妥当性を評価する根拠。"),
            ("EVID-000036", "ecological_validity_evidence", "生態学的妥当性根拠", "Ecological Validity Evidence", "現実場面での行動にどの程度適用できるかに関する根拠。"),
            ("EVID-000037", "behavior_log_evidence", "行動ログ根拠", "Behavior Log Evidence", "実際の操作・利用・選択ログから得られる根拠。"),
            ("EVID-000038", "self_report_evidence", "自己報告根拠", "Self Report Evidence", "本人の回答・記録・主観評価から得られる根拠。"),
            ("EVID-000039", "longitudinal_evidence", "縦断データ根拠", "Longitudinal Evidence", "時系列や長期観測によって得られる根拠。"),
            ("EVID-000040", "experimental_evidence", "実験研究根拠", "Experimental Evidence", "条件操作と比較により因果推論を支える根拠。")
        ]
    },
    {
        "category": "Evidence Sources - Quality Safety",
        "name_ja": "根拠・品質安全",
        "items": [
            ("EVID-000041", "observational_evidence", "観察研究根拠", "Observational Evidence", "自然発生的なデータ観察から得られる根拠。"),
            ("EVID-000042", "meta_analysis_evidence", "メタ分析根拠", "Meta Analysis Evidence", "複数研究の結果を統合した高次の根拠。"),
            ("EVID-000043", "systematic_review_evidence", "系統的レビュー根拠", "Systematic Review Evidence", "明確な手順で研究を収集・評価した根拠。"),
            ("EVID-000044", "replication_evidence", "再現性根拠", "Replication Evidence", "別データや別研究で同様の結果が得られることに関する根拠。"),
            ("EVID-000045", "effect_size_evidence", "効果量根拠", "Effect Size Evidence", "影響の大きさを評価するための根拠。"),
            ("EVID-000046", "confidence_level_evidence", "信頼水準根拠", "Confidence Level Evidence", "根拠の強さや不確実性を扱うための概念。"),
            ("EVID-000047", "bias_risk_evidence", "バイアスリスク根拠", "Risk of Bias Evidence", "研究や観測に含まれる偏りの可能性を評価する根拠。"),
            ("EVID-000048", "ethical_evidence_use", "倫理的根拠利用", "Ethical Evidence Use", "根拠を安全・公平・非断定的に利用するための考え方。"),
            ("EVID-000049", "domain_limit_evidence", "適用範囲根拠", "Domain Limit Evidence", "根拠が適用できる範囲や限界を示す概念。"),
            ("EVID-000050", "evidence_integration", "根拠統合", "Evidence Integration", "複数の根拠タイプを統合して知識DBの信頼性を高める枠組み。")
        ]
    }
]


def make_item(item_id, slug, name_ja, name_en, definition_ja, category, parent_ja):
    return {
        "filename": f"{item_id}_{slug}.yml",
        "id": item_id,
        "knowledge_type": "evidence_source",
        "name_ja": name_ja,
        "name_en": name_en,
        "category": "Evidence Source",
        "attribute": category.replace("Evidence Sources - ", ""),
        "definition_ja": definition_ja,
        "tags": ["CAT:根拠", f"CAT:{parent_ja}", "ATTR:根拠種別"],
        "parent": [parent_ja],
        "related": ["知識品質", "監査", "推論材料"],
        "observable_data": [
            f"{name_ja}参照有無",
            f"{name_ja}根拠強度",
            f"{name_ja}適用範囲",
            f"{name_ja}限界条件"
        ],
        "signal_candidates": [
            f"{name_ja}を根拠種別として利用できる",
            "知識項目の信頼度や適用範囲を判断する材料になる"
        ],
        "device_level": "DB管理用",
        "modifiers": ["根拠強度", "適用範囲", "再現性", "倫理性"],
        "evidence": "研究方法論・心理測定・科学的根拠評価で使用",
        "status": "active"
    }


def main():
    all_items = []
    index_lines = ["category: Evidence Source", "name_ja: 根拠", "items:"]

    for section in SECTIONS:
        parent_ja = section["name_ja"].replace("根拠・", "")
        for raw in section["items"]:
            item = make_item(*raw, category=section["category"], parent_ja=parent_ja)
            all_items.append(item)
            index_lines.append(f"  - {item['filename']}")

    index_lines.extend([
        "notes:",
        "  - 根拠は知識項目の品質管理材料として扱う",
        "  - Knowledge DB側では推論しない",
        "  - アプリ側で根拠強度や表示の慎重さに利用する"
    ])

    pack = {
        "output_dir": "vol13_evidence_sources/evidence_sources_001_050",
        "index_filename": "evidence_sources_001_050_index.yml",
        "index_content": "\n".join(index_lines) + "\n",
        "items": all_items
    }

    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(json.dumps(pack, ensure_ascii=False, indent=2), encoding="utf-8")

    print(f"Created: {OUT}")
    print(f"Items: {len(all_items)}")


if __name__ == "__main__":
    main()