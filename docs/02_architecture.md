# 全体構造 / Architecture

## 1. 目的

このファイルは、Analysis Engine Library（分析エンジンライブラリ）の全体構造を定義する。

このライブラリは、ゲームプレイから得られるデータをもとに、認知・思考・行動傾向・プレイスタイルを分析し、アプリごとに適切な診断文や表示内容へ変換するための共通基盤である。

## 2. 基本構造

分析エンジンは、以下の7層構造で考える。

```text
Game
ゲーム

↓
Layer 1: Raw Data
生データ

↓
Layer 2: Features
特徴量

↓
Layer 3: Analysis Items
分析項目

↓
Layer 4: Traits
能力・傾向

↓
Layer 5: Inference
推論

↓
Layer 6: Diagnosis
診断生成

↓
Layer 7: Presentation
アプリ表示
