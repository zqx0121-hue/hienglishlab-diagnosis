# HiEnglishLab Diagnosis Framework

[English](README.md) | 简体中文 | [Español](README.es.md) | [Português (Brasil)](README.pt-BR.md) | [日本語](README.ja.md) | [한국어](README.ko.md) | [Français](README.fr.md)

一个隐私优先、结果可解释的 Python CLI，用于将英语学习证据转化为可复核的基础指标。它面向教师、辅导老师、课程开发者和教育工具维护者，为引入模型辅助分析之前提供透明的分析基线。

当前版本支持样本长度、词汇多样性、平均句长和任务关键词覆盖率，并输出结构化 JSON 与明确的结果限制。它不会评定标准化语言等级、作出临床判断、上传学习者数据或调用外部服务。

## 快速开始

```bash
python -m pip install -e .
hienglish-diagnose examples/sample.json
```

输入格式：

```json
{
  "sample_id": "anonymous-id",
  "transcript": "A learner-produced English sample.",
  "expected_keywords": ["optional", "task", "keywords"]
}
```

使用 `--output report.json` 保存报告。程序不会覆盖已经存在的文件。

## 设计原则

- 默认本地运行：不含分析跟踪、网络请求或模型调用。
- 结果可解释：输出包含可观察指标与明确限制。
- 保护隐私：示例均为合成内容，贡献者不得提交学生资料。
- 便于审查：确定性规则有自动测试覆盖。
- 谨慎扩展：未来的评价规则或模型适配器必须保留证据来源和人工审核。

## 项目状态

项目目前处于早期公开阶段。我们会先验证数据格式、安全规则和贡献流程，再扩大功能范围。计划见 [ROADMAP.md](ROADMAP.md)，版本记录见 [CHANGELOG.md](CHANGELOG.md)。

## 贡献与安全

提交 PR 前请阅读 [CONTRIBUTING.md](CONTRIBUTING.md)。安全问题请按 [SECURITY.md](SECURITY.md) 私下报告。参与项目即表示同意遵守 [行为准则](CODE_OF_CONDUCT.md)。

## 许可证

MIT，详见 [LICENSE](LICENSE)。

