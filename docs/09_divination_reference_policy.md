# Divination Reference Policy

## Purpose

Vol31 stores historical and cultural divination concepts as reference data for
self-reflection, conversation, narrative generation, and entertainment. It does
not treat divination as a psychological test, medical method, or verified way to
predict a person's future.

## Separation from psychological evidence

- Divination items use `knowledge_type: divination_reference`.
- They use `evidence_class: traditional_cultural_interpretation`.
- Applications must label the tradition and must not merge a divination result
  into a psychological confidence score.
- Similarity with an Analysis Engine trait is a `trait_links` navigation aid,
  not empirical validation of the divination claim.

## Input and privacy boundary

- Use only birth data the person knowingly provides for the stated purpose.
- Record missing or approximate birth time explicitly.
- Minimize retention of birth date, time, place, and derived charts.
- Do not use these data or interpretations for medical, employment, education,
  insurance, credit, housing, or law-enforcement decisions.

## Interpretation boundary

- Preserve the named tradition, school, calendar, time-zone rule, and source.
- Present multiple symbols as prompts or possibilities, never as fixed traits.
- Do not infer mental illness, disability, intelligence, criminality, ethnicity,
  religion, or other sensitive attributes.
- Do not use fatalistic language or claims of certainty.

## Reference baseline

The initial terminology was checked against historical, philosophical, and
calendar references. These references support terminology and historical
context; they do not establish scientific predictive validity.

- Hong Kong Observatory, Heavenly Stems and Earthly Branches:
  https://www.hko.gov.hk/en/gts/time/stemsandbranches.htm
- Internet Encyclopedia of Philosophy, Wuxing:
  https://iep.utm.edu/wuxing/
- Internet Encyclopedia of Philosophy, Yinyang:
  https://iep.utm.edu/yinyang/
- Stanford Encyclopedia of Philosophy, Chinese Metaphysics:
  https://plato.stanford.edu/entries/chinese-metaphysics/
- Cambridge Archaeological Journal, The Cuneiform Conception of Celestial
  Space and Time: https://doi.org/10.1017/S0959774300000044

## Deferred modalities

Palmistry and physiognomy are intentionally excluded from Vol31. They require a
separate image-consent, biometric-data, discrimination, and retention review.
