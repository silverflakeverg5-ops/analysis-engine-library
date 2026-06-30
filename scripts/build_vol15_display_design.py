import json
from pathlib import Path

OUT = Path("data/master_packs/vol15_display_design_001_050.json")

SECTIONS = [
    {
        "category": "Display Design - Result Expression",
        "name_ja": "表示設計・結果表現",
        "items": [
            ("DISPLAY-000001", "tendency_expression", "傾向表現", "Tendency Expression", "結果を断定ではなく傾向として表現する表示設計。"),
            ("DISPLAY-000002", "possibility_expression", "可能性表現", "Possibility Expression", "推論結果を可能性として示し、不確実性を残す表現設計。"),
            ("DISPLAY-000003", "non_diagnostic_expression", "非診断表現", "Non Diagnostic Expression", "医療・性格断定ではなく参考情報として示す表現設計。"),
            ("DISPLAY-000004", "strength_level_display", "強度段階表示", "Strength Level Display", "傾向の強さを段階的に示す表示設計。"),
            ("DISPLAY-000005", "confidence_display", "信頼度表示", "Confidence Display", "観測量や一貫性に基づく信頼度を示す表示設計。"),
            ("DISPLAY-000006", "contextual_result_display", "文脈付き結果表示", "Contextual Result Display", "結果を時間・状況・条件とセットで示す表示設計。"),
            ("DISPLAY-000007", "range_expression", "範囲表現", "Range Expression", "単一値ではなく幅や範囲として結果を示す表現設計。"),
            ("DISPLAY-000008", "comparative_expression_safe", "安全な比較表現", "Safe Comparative Expression", "他者比較や序列化による悪影響を抑える表現設計。"),
            ("DISPLAY-000009", "plain_language_display", "平易な言葉表示", "Plain Language Display", "専門用語を避け、ユーザーが理解しやすく示す表示設計。"),
            ("DISPLAY-000010", "actionable_summary", "行動可能要約", "Actionable Summary", "結果を次の行動や振り返りにつながる形で要約する表示設計。")
        ]
    },
    {
        "category": "Display Design - Safety Tone",
        "name_ja": "表示設計・安全トーン",
        "items": [
            ("DISPLAY-000011", "supportive_tone", "支援的トーン", "Supportive Tone", "評価や断定ではなく支援的に伝える表現方針。"),
            ("DISPLAY-000012", "gentle_feedback", "やさしいフィードバック", "Gentle Feedback", "負担感を抑えて改善点や気づきを伝える表示設計。"),
            ("DISPLAY-000013", "non_judgmental_expression", "非評価的表現", "Non Judgmental Expression", "良し悪しや優劣ではなく特徴として示す表現設計。"),
            ("DISPLAY-000014", "strength_based_expression", "強みベース表現", "Strength Based Expression", "欠点よりも活かし方や強みに焦点を当てる表現設計。"),
            ("DISPLAY-000015", "caution_without_alarm", "不安を煽らない注意喚起", "Caution Without Alarm", "注意点を示しつつ不安や恐怖を過度に高めない表現設計。"),
            ("DISPLAY-000016", "user_agency_expression", "自己決定尊重表現", "User Agency Expression", "ユーザーが自分で判断できる余地を残す表現設計。"),
            ("DISPLAY-000017", "normalizing_expression", "正常化表現", "Normalizing Expression", "一時的な揺れや一般的な傾向として安心感を与える表現設計。"),
            ("DISPLAY-000018", "privacy_sensitive_expression", "プライバシー配慮表現", "Privacy Sensitive Expression", "機微情報を露骨に断定せず慎重に扱う表現設計。"),
            ("DISPLAY-000019", "minor_safe_expression", "未成年配慮表現", "Minor Safe Expression", "未成年ユーザーに対して安全で穏当な表現にする設計。"),
            ("DISPLAY-000020", "high_stakes_safe_expression", "高リスク安全表現", "High Stakes Safe Expression", "重大判断に直接使わせないよう慎重化する表現設計。")
        ]
    },
    {
        "category": "Display Design - Explanation",
        "name_ja": "表示設計・説明",
        "items": [
            ("DISPLAY-000021", "why_this_result", "結果理由説明", "Why This Result", "なぜその結果になったかを観測シグナルや根拠から説明する設計。"),
            ("DISPLAY-000022", "used_signal_display", "使用シグナル表示", "Used Signal Display", "結果に使われた観測シグナルを示す表示設計。"),
            ("DISPLAY-000023", "modifier_display", "補正要因表示", "Modifier Display", "結果に影響した補正要因を示す表示設計。"),
            ("DISPLAY-000024", "evidence_display", "根拠表示", "Evidence Display", "知識項目や推論材料の根拠種別を示す表示設計。"),
            ("DISPLAY-000025", "uncertainty_reason_display", "不確実性理由表示", "Uncertainty Reason Display", "なぜ確信度が高くないかを説明する表示設計。"),
            ("DISPLAY-000026", "alternative_explanation_display", "代替説明表示", "Alternative Explanation Display", "一つの結果に固定せず別解釈も示す表示設計。"),
            ("DISPLAY-000027", "data_limit_display", "データ限界表示", "Data Limit Display", "データ不足や観測範囲の限界を示す表示設計。"),
            ("DISPLAY-000028", "trend_explanation", "傾向説明", "Trend Explanation", "時系列でどのように変化したかを説明する表示設計。"),
            ("DISPLAY-000029", "context_explanation", "文脈説明", "Context Explanation", "時間・場所・課題など文脈の影響を説明する表示設計。"),
            ("DISPLAY-000030", "user_correction_prompt", "ユーザー修正促し", "User Correction Prompt", "結果や前提が違う場合にユーザーが修正できる導線。")
        ]
    },
    {
        "category": "Display Design - Visualization",
        "name_ja": "表示設計・可視化",
        "items": [
            ("DISPLAY-000031", "radar_chart_display", "レーダーチャート表示", "Radar Chart Display", "複数傾向をレーダーチャートで示す表示設計。"),
            ("DISPLAY-000032", "trend_line_display", "時系列ライン表示", "Trend Line Display", "状態や行動の変化を時系列で示す表示設計。"),
            ("DISPLAY-000033", "heatmap_display", "ヒートマップ表示", "Heatmap Display", "時間帯やカテゴリごとの強弱を色で示す表示設計。"),
            ("DISPLAY-000034", "card_summary_display", "カード要約表示", "Card Summary Display", "結果や提案をカード単位で簡潔に示す表示設計。"),
            ("DISPLAY-000035", "tag_display", "タグ表示", "Tag Display", "関連概念や状態をタグで示す表示設計。"),
            ("DISPLAY-000036", "confidence_meter", "信頼度メーター", "Confidence Meter", "推論信頼度を視覚的に示す表示設計。"),
            ("DISPLAY-000037", "signal_timeline", "シグナルタイムライン", "Signal Timeline", "観測シグナルの発生や変化を時系列で示す表示設計。"),
            ("DISPLAY-000038", "comparison_safe_visual", "安全な比較可視化", "Safe Comparison Visual", "比較による序列感を抑えた可視化設計。"),
            ("DISPLAY-000039", "progress_visual_display", "進捗可視化表示", "Progress Visual Display", "目標や行動の進捗を分かりやすく示す表示設計。"),
            ("DISPLAY-000040", "context_badge_display", "文脈バッジ表示", "Context Badge Display", "結果がどの文脈で出たものかをバッジで示す表示設計。")
        ]
    },
    {
        "category": "Display Design - Action Suggestion",
        "name_ja": "表示設計・行動提案",
        "items": [
            ("DISPLAY-000041", "small_next_action", "小さな次アクション", "Small Next Action", "すぐ実行できる小さな行動を提案する表示設計。"),
            ("DISPLAY-000042", "reflection_prompt", "振り返りプロンプト", "Reflection Prompt", "ユーザーが自分で考え直すための問いを提示する設計。"),
            ("DISPLAY-000043", "choice_preserving_suggestion", "選択余地を残す提案", "Choice Preserving Suggestion", "押しつけず複数の選択肢として提案する表示設計。"),
            ("DISPLAY-000044", "timing_aware_suggestion", "タイミング配慮提案", "Timing Aware Suggestion", "ユーザー状態や文脈に合わせて提案タイミングを調整する設計。"),
            ("DISPLAY-000045", "recovery_suggestion", "回復提案", "Recovery Suggestion", "疲労・ストレス・低下時に回復行動を提案する設計。"),
            ("DISPLAY-000046", "learning_suggestion", "学習提案", "Learning Suggestion", "理解・復習・練習・方略改善につながる提案設計。"),
            ("DISPLAY-000047", "communication_suggestion", "対話提案", "Communication Suggestion", "返信・確認・自己主張・感謝などの対人行動を支援する提案設計。"),
            ("DISPLAY-000048", "habit_suggestion", "習慣提案", "Habit Suggestion", "継続・再開・ルーティン化を支援する提案設計。"),
            ("DISPLAY-000049", "environment_adjustment_suggestion", "環境調整提案", "Environment Adjustment Suggestion", "集中・睡眠・作業・人間関係の環境調整を提案する設計。"),
            ("DISPLAY-000050", "app_display_integration", "表示設計統合", "App Display Integration", "結果・説明・安全性・行動提案を統合して表示する枠組み。")
        ]
    }
]


def make_item(item_id, slug, name_ja, name_en, definition_ja, category, parent_ja):
    return {
        "filename": f"{item_id}_{slug}.yml",
        "id": item_id,
        "knowledge_type": "display_design",
        "name_ja": name_ja,
        "name_en": name_en,
        "category": "Display Design",
        "attribute": category.replace("Display Design - ", ""),
        "definition_ja": definition_ja,
        "tags": ["CAT:表示設計", f"CAT:{parent_ja}", "ATTR:表示方針"],
        "parent": [parent_ja],
        "related": ["アプリ用途", "補正要因", "安全設計"],
        "observable_data": [
            f"{name_ja}適用文脈",
            f"{name_ja}対象結果",
            f"{name_ja}安全性条件",
            f"{name_ja}ユーザー反応"
        ],
        "signal_candidates": [
            f"{name_ja}を表示方針として利用できる",
            "アプリ側で結果表示・説明・提案を調整する材料になる"
        ],
        "device_level": "DB管理用",
        "modifiers": ["用途", "安全性", "不確実性", "ユーザー状態"],
        "evidence": "UXライティング・HCI・リスクコミュニケーション・行動支援設計で使用",
        "status": "active"
    }


def main():
    all_items = []
    index_lines = ["category: Display Design", "name_ja: 表示設計", "items:"]

    for section in SECTIONS:
        parent_ja = section["name_ja"].replace("表示設計・", "")
        for raw in section["items"]:
            item = make_item(*raw, category=section["category"], parent_ja=parent_ja)
            all_items.append(item)
            index_lines.append(f"  - {item['filename']}")

    index_lines.extend([
        "notes:",
        "  - 表示設計は推論結果ではなくアプリ側の表現材料として扱う",
        "  - Knowledge DB側ではスコアリングしない",
        "  - アプリ側で用途・安全性・文脈に応じて表示を調整する"
    ])

    pack = {
        "output_dir": "vol15_display_design/display_design_001_050",
        "index_filename": "display_design_001_050_index.yml",
        "index_content": "\n".join(index_lines) + "\n",
        "items": all_items
    }

    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(json.dumps(pack, ensure_ascii=False, indent=2), encoding="utf-8")

    print(f"Created: {OUT}")
    print(f"Items: {len(all_items)}")


if __name__ == "__main__":
    main()