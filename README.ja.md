# HiEnglishLab Diagnosis Framework

[English](README.md) | [简体中文](README.zh-CN.md) | [Español](README.es.md) | [Português (Brasil)](README.pt-BR.md) | 日本語 | [한국어](README.ko.md) | [Français](README.fr.md)

英語学習者のサンプルを検証可能な指標に変換する、プライバシー重視・説明可能性重視の Python CLI です。モデル支援分析を導入する前に透明な基準を必要とする教師、講師、教材開発者、教育ツールのメンテナーを対象としています。

現在のバージョンでは、サンプルの長さ、語彙の多様性、平均文長、課題キーワードのカバー率を測定します。構造化 JSON と明確な制約を出力します。標準化された習熟度の判定、臨床的判断、学習者データのアップロード、外部サービスの呼び出しは行いません。

> **オープンコアの範囲：**このリポジトリは公開された学習証拠処理の基盤であり、検証済み診断や商用採点システムの全体ではありません。KET、PET、IELTS、CEFR などのスコアは出力しません。[Open Core Scope](docs/OPEN_CORE_SCOPE.md) を参照してください。

## クイックスタート

```bash
python -m pip install -e .
hienglish-diagnose examples/sample.json
```

入力形式：

```json
{
  "sample_id": "anonymous-id",
  "transcript": "A learner-produced English sample.",
  "expected_keywords": ["optional", "task", "keywords"]
}
```

レポートを保存するには `--output report.json` を指定します。既存ファイルは上書きしません。

## 設計原則

- ローカル優先：テレメトリ、ネットワーク通信、モデル呼び出しはありません。
- 説明可能：観察可能な指標と制約を出力します。
- プライバシー：例は合成データであり、実際の学習者データは受け付けません。
- レビュー可能：決定論的なルールをテストで検証します。
- 慎重な拡張：将来のアダプターでも根拠と人間による確認を維持します。

## プロジェクトの状態

現在は初期公開版です。機能を広げる前に、スキーマ、安全規則、貢献プロセスを検証します。[ROADMAP.md](ROADMAP.md) と [CHANGELOG.md](CHANGELOG.md) を参照してください。

## 貢献とセキュリティ

PR の前に [CONTRIBUTING.md](CONTRIBUTING.md) をお読みください。脆弱性は [SECURITY.md](SECURITY.md) に従って非公開で報告してください。参加者には [行動規範](CODE_OF_CONDUCT.md) が適用されます。

## ライセンス

MIT。詳細は [LICENSE](LICENSE) を参照してください。
