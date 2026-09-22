# Canonical ID Prefix Policy

## Principle

Volume numbers identify delivery and storage units. ID prefixes identify the
Knowledge domain of an item. A volume may contain more than one prefix when it
intentionally contains multiple Knowledge domains.

## Vol1 Core

Vol1 Core preserves these domain-specific prefixes:

| Prefix | Knowledge domain |
| --- | --- |
| ATT | Attention |
| MEM | Memory |
| EXE | Executive Function |
| PRO | Processing |
| REA | Reasoning |
| SPA | Spatial Cognition |

These prefixes are canonical, not legacy aliases. Existing Vol1 IDs remain
stable and must not be collapsed into a volume-based prefix.

## Compatibility

- Existing IDs are stable once published.
- A prefix belongs to one Knowledge domain.
- Future volumes must use the canonical prefix assigned to their domain.
- Prefix changes must update builders, master packs, generated YAML, indexes,
  cross-references, and filenames together.
