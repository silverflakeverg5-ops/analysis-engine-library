# analysis-engine-library

性格・認知・行動傾向をゲームやアプリから安全に参照するための辞典、索引、設計資料を管理するライブラリです。

Vol31から、画像を必要としない占術の歴史的・文化的な参照データも収録します。西洋占星術、インド占星術、四柱推命、紫微斗数、陰陽五行、九星気学、宿曜、数秘術、姓名判断、風水を独立カタログとして扱います。占術項目は心理学的エビデンスと区別され、自己理解・会話・物語生成・娯楽のための解釈候補としてのみ利用します。心理診断、医療判断、能力評価、将来の確定的予測には使用しません。

Game- and application-oriented reference library for personality, cognition,
behavior, play-style interpretation, and clearly labeled cultural divination
concepts. The runtime is read-only and performs no person-level inference,
scoring, or diagnosis.

アプリは`KnowledgeLibrary.divination_registry()`から、対応する詳細10体系、必要入力、計算基準、出典系統、および必須の文化的参照境界を一括取得できます。

`KnowledgeLibrary.calculate_numerology()`は、方式と還元過程を明示した数秘術の算術アダプターです。入力原文を返却・保存せず、象徴解釈や人物推論とは分離されています。

`KnowledgeLibrary.calculate_japanese_name()`は、漢字・ひらがな・カタカナと明示された画数表から、五格・陰陽配列・三才配置を計算します。新旧字体や流派差を自動決定せず、採用根拠を必須入力として保持します。

バージョン管理した文字画数辞書がある場合は`KnowledgeLibrary.calculate_japanese_name_from_dictionary()`で画数列を自動解決できます。未登録字や異体字を推測置換せず、完全一致しなければ処理を停止します。
