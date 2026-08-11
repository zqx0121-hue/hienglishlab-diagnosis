# HiEnglishLab Diagnosis Framework

[English](README.md) | [简体中文](README.zh-CN.md) | [Español](README.es.md) | [Português (Brasil)](README.pt-BR.md) | [日本語](README.ja.md) | 한국어 | [Français](README.fr.md)

영어 학습 자료를 검토 가능한 지표로 변환하는 개인정보 보호 및 설명 가능성 중심의 Python CLI입니다. 모델 기반 분석을 추가하기 전에 투명한 기준이 필요한 교사, 튜터, 교육과정 개발자와 교육 도구 유지관리자를 대상으로 합니다.

현재 버전은 표본 길이, 어휘 다양성, 평균 문장 길이와 과제 키워드 포함 비율을 측정합니다. 구조화된 JSON과 명확한 한계를 함께 출력합니다. 표준화된 숙련도 등급이나 임상적 판단을 제공하지 않으며, 학습자 데이터를 업로드하거나 외부 서비스를 호출하지 않습니다.

## 빠른 시작

```bash
python -m pip install -e .
hienglish-diagnose examples/sample.json
```

입력 형식:

```json
{
  "sample_id": "anonymous-id",
  "transcript": "A learner-produced English sample.",
  "expected_keywords": ["optional", "task", "keywords"]
}
```

보고서를 저장하려면 `--output report.json`을 사용하세요. 기존 파일은 덮어쓰지 않습니다.

## 설계 원칙

- 기본적으로 로컬 실행: 텔레메트리, 네트워크 요청, 모델 호출이 없습니다.
- 설명 가능성: 관찰 가능한 지표와 한계를 제공합니다.
- 개인정보 보호: 예시는 합성 데이터이며 실제 학생 데이터는 허용하지 않습니다.
- 검토 가능성: 결정론적 규칙은 자동 테스트로 검증됩니다.
- 신중한 확장: 향후 어댑터도 출처와 사람의 검토를 유지해야 합니다.

## 프로젝트 상태

현재 초기 공개 버전입니다. 기능 확장 전에 스키마, 안전 규칙과 기여 절차를 검증합니다. [ROADMAP.md](ROADMAP.md)와 [CHANGELOG.md](CHANGELOG.md)를 참고하세요.

## 기여 및 보안

PR을 제출하기 전에 [CONTRIBUTING.md](CONTRIBUTING.md)를 읽어 주세요. 취약점은 [SECURITY.md](SECURITY.md)에 따라 비공개로 신고하세요. 참여 시 [행동 강령](CODE_OF_CONDUCT.md)이 적용됩니다.

## 라이선스

MIT. [LICENSE](LICENSE)를 참고하세요.

