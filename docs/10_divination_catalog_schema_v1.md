# Divination Catalog Schema v1

## Catalog layout

| Volume | Prefix | `knowledge_type` | Scope |
| --- | --- | --- | --- |
| Vol31 | `DIV` | `divination_reference` | Shared terminology, inputs, and boundaries |
| Vol32 | `AST` | `western_astrology` | Western natal astrology concepts and techniques |
| Vol33 | `WUX` | `yin_yang_wuxing` | Yin-yang, five phases, stems, branches, and cycles |
| Vol34 | `BAZ` | `four_pillars` | Four Pillars calculation and interpretation concepts |
| Vol35 | `JYO` | `indian_astrology` | Indian astrology, navagraha, rashi, bhava, and nakshatra |
| Vol36 | `ZWD` | `zi_wei_dou_shu` | Zi Wei Dou Shu palaces, stars, transformations, and timing |
| Vol37 | `NSK` | `nine_star_ki` | Nine Star Ki charts, directions, cycles, and calendar rules |
| Vol38 | `SUK` | `sukuyo` | Sukuyo mansions, luminaries, relations, and calendar methods |
| Vol39 | `NUM` | `numerology` | Numerology calculations, traditions, cycles, and symbolism |
| Vol40 | `NAM` | `name_divination` | Japanese name-divination methods, scripts, strokes, sound, and meaning |
| Vol41 | `FSH` | `feng_shui` | Form and compass feng shui, directions, buildings, and time charts |

Overview items in Vol31 are navigation concepts. Detailed items in Vol32-Vol34
are the application-facing reference layer. Applications should prefer the
detailed item when both exist and may retain a link to the Vol31 overview.

## Required divination fields

- `tradition`: named cultural or historical interpretive system
- `source_type`: input category used by that system
- `evidence_class`: always `traditional_cultural_interpretation` in v1
- `required_inputs`: data needed to reproduce the symbolic calculation
- `calculation_basis`: declared transformation and school assumptions
- `trait_links`: navigation links only, not empirical associations
- `interpretive_scope`: allowed use of the result
- `safe_expression`: non-diagnostic user-facing baseline
- `provenance`: historical and school lineage description

## Application rules

1. Keep psychological and divination results in separate response sections.
2. Never convert a divination item into a psychological score or confidence.
3. Return the adopted tradition, school, calculation rule, and input precision.
4. Treat approximate or missing birth time as an explicit uncertainty state.
5. Offer interpretations as optional prompts and allow the user to reject them.
6. Exclude medical, mental-health, ability, lifespan, criminality, and other
   sensitive inferences.
7. Exclude employment, education, insurance, credit, housing, and law-enforcement
   decisions.

## Deferred scope

Palmistry and physiognomy remain outside v1 because they require image and
biometric-data governance in addition to the interpretive controls above.
