import json
from pathlib import Path

OUT = Path("data/master_packs/vol13_evidence_sources_051_100.json")

SECTIONS = [
    {
        "category": "Evidence Sources - Research Design",
        "name_ja": "根拠・研究設計",
        "items": [
            ("EVID-000051", "randomized_controlled_trial", "ランダム化比較試験", "Randomized Controlled Trial", "対象をランダムに条件へ割り当て、介入効果を比較する研究設計。"),
            ("EVID-000052", "quasi_experimental_design", "準実験デザイン", "Quasi Experimental Design", "完全なランダム割付なしで条件差や介入効果を検討する研究設計。"),
            ("EVID-000053", "cross_sectional_study", "横断研究", "Cross Sectional Study", "一時点のデータから変数間の関連を調べる研究設計。"),
            ("EVID-000054", "longitudinal_study", "縦断研究", "Longitudinal Study", "同じ対象を時間を追って観測し変化や因果可能性を検討する研究設計。"),
            ("EVID-000055", "cohort_study", "コホート研究", "Cohort Study", "特定集団を追跡し要因と結果の関係を調べる研究設計。"),
            ("EVID-000056", "case_control_study", "症例対照研究", "Case Control Study", "結果を持つ群と持たない群を比較し関連要因を調べる研究設計。"),
            ("EVID-000057", "field_experiment", "フィールド実験", "Field Experiment", "実際の環境で条件操作を行い行動変化を調べる研究設計。"),
            ("EVID-000058", "lab_experiment", "実験室実験", "Lab Experiment", "統制された環境で変数を操作し効果を調べる研究設計。"),
            ("EVID-000059", "natural_experiment", "自然実験", "Natural Experiment", "自然発生した条件差を利用して影響を検討する研究設計。"),
            ("EVID-000060", "experience_sampling_method", "経験サンプリング法", "Experience Sampling Method", "日常生活中に繰り返し状態や行動を記録する研究方法。")
        ]
    },
    {
        "category": "Evidence Sources - Data Type",
        "name_ja": "根拠・データ種別",
        "items": [
            ("EVID-000061", "behavioral_log_data", "行動ログデータ", "Behavioral Log Data", "操作・閲覧・選択・利用頻度など行動から自動記録されるデータ。"),
            ("EVID-000062", "questionnaire_data", "質問紙データ", "Questionnaire Data", "尺度や設問への回答によって得られる自己報告データ。"),
            ("EVID-000063", "interview_data", "インタビューデータ", "Interview Data", "対話や聞き取りから得られる質的情報。"),
            ("EVID-000064", "observation_data", "観察データ", "Observation Data", "研究者やシステムが行動や状況を観察して記録したデータ。"),
            ("EVID-000065", "sensor_data", "センサーデータ", "Sensor Data", "端末・ウェアラブル・環境センサーなどから得られる測定データ。"),
            ("EVID-000066", "text_data", "テキストデータ", "Text Data", "入力文・発話・メッセージ・記録などの言語データ。"),
            ("EVID-000067", "interaction_data", "インタラクションデータ", "Interaction Data", "ユーザーとシステムの相互作用から得られる操作系列データ。"),
            ("EVID-000068", "performance_data", "成績データ", "Performance Data", "正答率・速度・エラー率・達成度など課題遂行から得られるデータ。"),
            ("EVID-000069", "physiological_data", "生理データ", "Physiological Data", "心拍・睡眠・活動量・ストレス指標など身体状態に関するデータ。"),
            ("EVID-000070", "contextual_data", "文脈データ", "Contextual Data", "時間・場所・端末・状況など観測の背景に関するデータ。")
        ]
    },
    {
        "category": "Evidence Sources - Statistical Quality",
        "name_ja": "根拠・統計品質",
        "items": [
            ("EVID-000071", "sample_size_quality", "サンプルサイズ品質", "Sample Size Quality", "分析に使う対象数や観測数が十分かを示す品質概念。"),
            ("EVID-000072", "statistical_power", "検出力", "Statistical Power", "実際に効果がある場合にそれを検出できる確率。"),
            ("EVID-000073", "confidence_interval", "信頼区間", "Confidence Interval", "推定値の不確実性の範囲を示す統計概念。"),
            ("EVID-000074", "effect_size", "効果量", "Effect Size", "差や関連の大きさを示す統計指標。"),
            ("EVID-000075", "p_value", "p値", "P Value", "帰無仮説の下で観測結果以上の結果が得られる確率。"),
            ("EVID-000076", "multiple_comparison_risk", "多重比較リスク", "Multiple Comparison Risk", "多数の検定により偶然の有意結果が出やすくなるリスク。"),
            ("EVID-000077", "measurement_error", "測定誤差", "Measurement Error", "測定値と真の値との差やばらつき。"),
            ("EVID-000078", "internal_consistency", "内的一貫性", "Internal Consistency", "同じ概念を測る項目同士が一貫している度合い。"),
            ("EVID-000079", "test_retest_reliability", "再検査信頼性", "Test Retest Reliability", "時間を空けて同じ測定を行った時の安定性。"),
            ("EVID-000080", "inter_rater_reliability", "評価者間信頼性", "Inter Rater Reliability", "複数評価者の判断がどの程度一致するか。")
        ]
    },
    {
        "category": "Evidence Sources - Validity",
        "name_ja": "根拠・妥当性",
        "items": [
            ("EVID-000081", "content_validity", "内容的妥当性", "Content Validity", "測定項目が対象概念の内容領域を十分に代表しているか。"),
            ("EVID-000082", "face_validity", "表面的妥当性", "Face Validity", "測定が見た目上その概念を測っているように見える度合い。"),
            ("EVID-000083", "convergent_validity", "収束的妥当性", "Convergent Validity", "関連する概念や尺度と適切に相関すること。"),
            ("EVID-000084", "discriminant_validity", "弁別的妥当性", "Discriminant Validity", "異なる概念や尺度と過度に重ならないこと。"),
            ("EVID-000085", "predictive_validity", "予測的妥当性", "Predictive Validity", "測定値が将来の行動や結果を予測できる度合い。"),
            ("EVID-000086", "concurrent_validity", "併存的妥当性", "Concurrent Validity", "同時点の外部基準と適切に関連すること。"),
            ("EVID-000087", "incremental_validity", "増分妥当性", "Incremental Validity", "既存指標に加えて新たな予測力や説明力を持つこと。"),
            ("EVID-000088", "ecological_validity", "生態学的妥当性", "Ecological Validity", "現実の文脈や日常行動にどの程度適用できるか。"),
            ("EVID-000089", "external_validity", "外的妥当性", "External Validity", "結果が他の対象・状況・時期にも一般化できる度合い。"),
            ("EVID-000090", "construct_coverage", "構成概念カバレッジ", "Construct Coverage", "対象概念を過不足なく捉えているかを示す概念。")
        ]
    },
    {
        "category": "Evidence Sources - Evidence Integration",
        "name_ja": "根拠・統合評価",
        "items": [
            ("EVID-000091", "evidence_strength_level", "根拠強度レベル", "Evidence Strength Level", "根拠の信頼性や確実性を段階的に示す概念。"),
            ("EVID-000092", "evidence_consistency", "根拠一貫性", "Evidence Consistency", "複数研究や複数データで同じ傾向が示される度合い。"),
            ("EVID-000093", "evidence_relevance", "根拠関連性", "Evidence Relevance", "根拠が対象概念や利用目的にどの程度関係しているか。"),
            ("EVID-000094", "evidence_applicability", "根拠適用可能性", "Evidence Applicability", "根拠を実際のアプリや文脈へ適用できる度合い。"),
            ("EVID-000095", "evidence_limitation", "根拠限界", "Evidence Limitation", "根拠の範囲・不確実性・弱点を示す概念。"),
            ("EVID-000096", "evidence_update_need", "根拠更新必要性", "Evidence Update Need", "新しい研究やデータに応じて根拠を更新する必要性。"),
            ("EVID-000097", "cross_domain_evidence", "領域横断根拠", "Cross Domain Evidence", "複数分野の知見を組み合わせた根拠。"),
            ("EVID-000098", "triangulation", "トライアンギュレーション", "Triangulation", "複数方法・複数データ源を組み合わせて妥当性を高める方法。"),
            ("EVID-000099", "evidence_audit", "根拠監査", "Evidence Audit", "知識項目の根拠品質・範囲・更新状況を確認する管理過程。"),
            ("EVID-000100", "evidence_source_integration", "根拠ソース統合", "Evidence Source Integration", "研究設計・データ種別・品質・妥当性を統合して根拠を管理する枠組み。")
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
        "output_dir": "vol13_evidence_sources/evidence_sources_051_100",
        "index_filename": "evidence_sources_051_100_index.yml",
        "index_content": "\n".join(index_lines) + "\n",
        "items": all_items
    }

    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(json.dumps(pack, ensure_ascii=False, indent=2), encoding="utf-8")

    print(f"Created: {OUT}")
    print(f"Items: {len(all_items)}")


if __name__ == "__main__":
    main()