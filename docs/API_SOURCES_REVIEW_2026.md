# Open API candidates — research-source assessment (2026-11-08)

**Input:** https://netzhandwerker.de/blog/100-offene-apis-freie-datenquellen-2026

That article is a **discovery list**, not authoritative evidence of each provider's live quotas, license, correctness or suitability for commercial publication. We independently checked the listed scientific providers against their own API documentation before making recommendations.

| Candidate | Potentially useful for | Decision and licensing/operations gate |
| --- | --- | --- |
| [OpenAlex](https://help.openalex.org/api/) | Academic literature/discovery, citation graphs, new statistics publications | **Research radar candidate only.** Public queries are available; larger-scale API access uses a free key with daily budget and can become paid. Check the current account/rate-limit and output rights before implementing; no unattended or billable usage. |
| [Crossref REST](https://www.crossref.org/documentation/retrieve-metadata/rest-api/access-and-authentication) | DOI metadata, research alerts, provenance | **Research radar candidate only.** Public API needs no key; polite identification and caching recommended. Metadata is not permission to republish full paper text. |
| [arXiv API](https://info.arxiv.org/help/api/) | Preprint monitoring for statistics, inference and machine learning | **Research radar candidate only.** Verify service policies, licenses of individual papers and attribution before any automated publication. |
| [Wikidata](https://www.wikidata.org/wiki/Wikidata:Data_access) | Structured reference terms for educational explanations | **Optional documentation aid**, not a lottery-result validator. Separate content provenance and language requirements. |
| General weather, finance, geocoding, entertainment and security APIs | Largely unrelated to this repository's documented governance example | **Do not integrate.** Extra keys, requests and runtime dependencies add risk without a validated use case. |

**No suitable official Eurojackpot/LOTTO 6aus49 draw-results feed was established by this article.** Historical lottery data requires primary-source checks, game-specific rules and epoch handling, draw-date validation, independent agreement and explicit commercial reuse rights. Open access to an endpoint never equals unrestricted dataset redistribution.

**Future acceptance gate:** Run a small fixture-based prototype in the private research project only after a defined use case, vendor documentation, legal rights, API quotas and zero-cost enforcement have been assessed. Do not store API keys in this public repository and do not expose private research methods.
