# HiEnglishLab Diagnosis Framework

[English](README.md) | [简体中文](README.zh-CN.md) | [Español](README.es.md) | Português (Brasil) | [日本語](README.ja.md) | [한국어](README.ko.md) | [Français](README.fr.md)

Uma CLI Python com foco em privacidade e explicabilidade para transformar amostras de aprendizagem de inglês em métricas verificáveis. Destina-se a professores, tutores, criadores de currículo e mantenedores de ferramentas educacionais que precisam de uma base transparente antes de adicionar análises assistidas por modelos.

A versão atual mede o tamanho da amostra, a diversidade lexical, o comprimento médio das frases e a cobertura de palavras-chave. Ela gera JSON estruturado e sempre informa suas limitações. Não atribui níveis padronizados, não faz afirmações clínicas, não envia dados de alunos e não acessa serviços externos.

> **Limite open core:** este repositório é a base pública de processamento de evidências, não o sistema completo de diagnóstico validado ou pontuação comercial. Ele não produz resultados KET, PET, IELTS, CEFR ou equivalentes. Consulte [Open Core Scope](docs/OPEN_CORE_SCOPE.md).

## Início rápido

```bash
python -m pip install -e .
hienglish-diagnose examples/sample.json
```

Formato de entrada:

```json
{
  "sample_id": "anonymous-id",
  "transcript": "A learner-produced English sample.",
  "expected_keywords": ["optional", "task", "keywords"]
}
```

Use `--output report.json` para salvar o relatório. Arquivos existentes nunca são sobrescritos.

## Princípios de projeto

- Local por padrão: sem telemetria, solicitações de rede ou chamadas a modelos.
- Explicável: os resultados contêm métricas observáveis e limitações.
- Privacidade: os exemplos são sintéticos e dados reais de alunos não são aceitos.
- Auditável: regras determinísticas são cobertas por testes.
- Extensão cuidadosa: futuros adaptadores devem preservar a procedência e a revisão humana.

## Estado do projeto

Esta é uma versão pública inicial. Primeiro validaremos o esquema, as regras de segurança e o processo de contribuição. Consulte [ROADMAP.md](ROADMAP.md) e [CHANGELOG.md](CHANGELOG.md).

## Contribuição e segurança

Leia [CONTRIBUTING.md](CONTRIBUTING.md) antes de enviar um PR. Relate vulnerabilidades em privado conforme [SECURITY.md](SECURITY.md). A participação segue o [Código de Conduta](CODE_OF_CONDUCT.md).

## Licença

MIT. Consulte [LICENSE](LICENSE).
