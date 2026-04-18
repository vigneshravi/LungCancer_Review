# Failed Queries

## PubMed API Failures
None — all PubMed queries completed successfully.

## Low-yield Queries (< 10 results)

These queries returned very few results and may indicate underexplored areas:

- `"MOVICS" OR "DIABLO" OR "iCluster" OR "MOFA" OR "NEMO"` — returned hits but includes false positives from non-omics contexts
- `joint NMF AND multi-omics` — 5 results (very niche method)
- `multi-platform AND lung adenocarcinoma` — 9 results
- `proteogenomics AND NSCLC AND driver` — 6 results
- `Thorsson immune landscape cancer` — 9 results (author-specific query)
- `Bagaev conserved microenvironment` — 2 results (author-specific)
- `Charoentong immunogenomic` — 3 results (author-specific)
- `Visium AND lung cancer` — 26 results (specific technology, growing)
- `CODEX AND lung cancer` — 13 results (specific technology)
- `"dimethyl fumarate" AND KEAP1 AND cancer` — 13 results (very specific)
- `MYLUNG consortium` — 2 results (consortium-specific)
- `CAPP-Seq AND lung` — 20 results (specific technology)

## Missing Anchor PMIDs
- **PMID 33524135** — Not found in PubMed API. Likely incorrect PMID in spec; correct ID appears to be 33402734 (Cantini benchmarking, Nat Comms 2021).

## Notes
- Several anchor PMIDs returned papers with unexpected metadata (possible PMID reassignment by NCBI)
- All API responses are cached; re-runs will use cached data automatically
