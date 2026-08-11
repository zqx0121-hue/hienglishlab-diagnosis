# HiEnglishLab Diagnosis Framework

[English](README.md) | [简体中文](README.zh-CN.md) | Español | [Português (Brasil)](README.pt-BR.md) | [日本語](README.ja.md) | [한국어](README.ko.md) | [Français](README.fr.md)

Una herramienta CLI en Python, centrada en la privacidad y la explicabilidad, que convierte muestras de aprendizaje del inglés en métricas revisables. Está dirigida a docentes, tutores, diseñadores curriculares y responsables de herramientas educativas que necesitan una base transparente antes de incorporar análisis asistido por modelos.

La versión actual mide la longitud de la muestra, la diversidad léxica, la longitud media de las oraciones y la cobertura de palabras clave. Produce JSON estructurado e indica siempre sus limitaciones. No asigna niveles normalizados, no realiza afirmaciones clínicas, no sube datos del alumnado y no llama a servicios externos.

> **Límite open core:** este repositorio es la base pública de procesamiento de evidencias, no el sistema completo de diagnóstico validado o puntuación comercial. No produce resultados KET, PET, IELTS, CEFR ni equivalentes. Consulte [Open Core Scope](docs/OPEN_CORE_SCOPE.md).

## Inicio rápido

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

Use `--output report.json` para guardar el informe. Los archivos existentes nunca se sobrescriben.

## Principios de diseño

- Local por defecto: sin telemetría, solicitudes de red ni llamadas a modelos.
- Explicable: cada resultado contiene métricas observables y limitaciones.
- Privacidad: los ejemplos son sintéticos y no se aceptan datos reales de estudiantes.
- Revisable: las reglas deterministas están cubiertas por pruebas.
- Extensible con cautela: futuros adaptadores deben conservar la procedencia y la revisión humana.

## Estado del proyecto

Esta es una versión pública inicial. Primero validaremos el esquema, las reglas de seguridad y el proceso de contribución. Consulte [ROADMAP.md](ROADMAP.md) y [CHANGELOG.md](CHANGELOG.md).

## Contribuciones y seguridad

Lea [CONTRIBUTING.md](CONTRIBUTING.md) antes de enviar un PR. Informe vulnerabilidades en privado según [SECURITY.md](SECURITY.md). La participación está sujeta al [Código de conducta](CODE_OF_CONDUCT.md).

## Licencia

MIT. Consulte [LICENSE](LICENSE).
