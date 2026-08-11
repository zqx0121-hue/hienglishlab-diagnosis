# HiEnglishLab Diagnosis Framework

[English](README.md) | [简体中文](README.zh-CN.md) | [Español](README.es.md) | [Português (Brasil)](README.pt-BR.md) | [日本語](README.ja.md) | [한국어](README.ko.md) | Français

Une CLI Python axée sur la confidentialité et l’explicabilité, qui transforme des productions d’apprenants en anglais en indicateurs vérifiables. Elle s’adresse aux enseignants, tuteurs, concepteurs de programmes et responsables d’outils éducatifs qui souhaitent disposer d’une base transparente avant d’ajouter une analyse assistée par modèle.

La version actuelle mesure la longueur de l’échantillon, la diversité lexicale, la longueur moyenne des phrases et la couverture des mots-clés. Elle produit un JSON structuré et indique toujours ses limites. Elle n’attribue pas de niveau standardisé, ne formule pas d’avis clinique, ne téléverse aucune donnée d’apprenant et n’appelle aucun service externe.

## Démarrage rapide

```bash
python -m pip install -e .
hienglish-diagnose examples/sample.json
```

Format d’entrée :

```json
{
  "sample_id": "anonymous-id",
  "transcript": "A learner-produced English sample.",
  "expected_keywords": ["optional", "task", "keywords"]
}
```

Utilisez `--output report.json` pour enregistrer le rapport. Les fichiers existants ne sont jamais écrasés.

## Principes de conception

- Local par défaut : aucune télémétrie, requête réseau ou invocation de modèle.
- Explicable : les résultats contiennent des mesures observables et leurs limites.
- Respect de la vie privée : exemples synthétiques et aucune donnée réelle d’élève.
- Vérifiable : les règles déterministes sont couvertes par des tests.
- Extensible avec prudence : les futurs adaptateurs doivent préserver la provenance et la validation humaine.

## État du projet

Il s’agit d’une première version publique. Le schéma, les règles de sécurité et le processus de contribution seront validés avant d’élargir les fonctionnalités. Consultez [ROADMAP.md](ROADMAP.md) et [CHANGELOG.md](CHANGELOG.md).

## Contribution et sécurité

Lisez [CONTRIBUTING.md](CONTRIBUTING.md) avant toute PR. Signalez les vulnérabilités en privé selon [SECURITY.md](SECURITY.md). Toute participation est soumise au [Code de conduite](CODE_OF_CONDUCT.md).

## Licence

MIT. Consultez [LICENSE](LICENSE).
