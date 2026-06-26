# IDルール / ID Rules

## 1. 目的

このファイルは、Analysis Engine Library（分析エンジンライブラリ）で使用するIDの付け方を定義する。

IDは、このライブラリ全体の参照関係を安定させるために使う。

名前は後から変更される可能性があるが、IDは変更しない。

## 2. 基本方針

このプロジェクトでは、すべての主要データにIDを付ける。

IDは一度発行したら変更しない。

IDは削除しない。

IDは再利用しない。

## 3. IDの種類

使用するIDは以下とする。

```text
ITM-000001  Analysis Item / 分析項目
DOM-000001  Domain / 分野
TST-000001  Test / 検査・評価法
GME-000001  Game / ゲーム
OUT-000001  Output / 診断文・表示文
REL-000001  Relation / 関係
IDX-000001  Index / 索引
SRC-000001  Source / 情報源
DOC-000001  Document / 設計文書
