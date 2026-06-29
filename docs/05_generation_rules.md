# AI Generation Rules

Version: 1.0

---

# 1. 目的

本書は AI が Analysis Engine Library を生成・更新する際の作業仕様を定義する。

本書より優先される文書は

04_development_standard.md

のみとする。

---

# 2. 基本ルール

生成ではなく

保守可能な知識ベース

を作ること。

短期効率より

長期保守性を優先する。

---

# 3. YAML生成

各分析項目は

1ファイル = 1概念

とする。

複数概念を同一ファイルへまとめない。

---

# 4. 統合禁止

似ている概念でも統合しない。

Relationで関連付ける。

---

# 5. Relation

Relationは

親子

関連

類義

反義

近接概念

原因

結果

など複数保持可能。

---

# 6. Signal

Signalは候補である。

Signalから分析項目を推定してはいけない。

Signalは複数概念へ関連付ける。

Signal同士もRelationを持つ。

---

# 7. Observable Data

Observable Data は

取得可能な生データ

のみを書く。

推論結果は書かない。

---

# 8. Device Level

保存する。

例

スマホ・PC

一般センサー

専用機材

研究設備

アプリ名は保存しない。

---

# 9. Definition

定義は

学術的定義を基本とする。

独自解釈を書かない。

---

# 10. Evidence

Evidenceは

可能な限り

研究

標準検査

理論

実務利用

を根拠とする。

---

# 11. Modifiers

年齢

疲労

睡眠

経験

文化

教育

環境

など

分析結果へ影響する要因を保存する。

---

# 12. Index

生成後

Indexを更新する。

---

# 13. Review

生成後

以下を自己確認する。

・重複

・Relation

・Signal

・Index

・命名規則

・ID

---

# 14. 禁止事項

概念の削除

勝手な統合

アプリ依存設計

医学的断定

診断結果の生成

---

# 15. 完成条件

生成物は

・構文エラーなし

・Index更新済み

・Relation更新済み

・Signal更新済み

・Development Standard違反なし

を満たした時のみ完成とする。

---

# 16. AIへの指示

AIは生成前に

04_development_standard.md

05_generation_rules.md

を読み、

両方のルールを遵守して生成を行うこと。

ルールが衝突する場合は

04を優先する。
