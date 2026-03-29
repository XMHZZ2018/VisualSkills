# Formatting Changes Report

## Changes Applied

### 1. Added `caption` package with proper formatting
- **File:** `tmlr/main.tex` (line 22)
- **What:** Added `\usepackage[font=small,labelfont=bf]{caption}`
- **Why:** All reference papers (E5-V, GME, ColPali, mmE5, LLaVE, etc.) use smaller-font captions with bold labels. This brings caption styling in line with conference paper conventions.

### 2. Removed unused `lineno` package
- **File:** `tmlr/main.tex` (line 22)
- **What:** Commented out `\usepackage{lineno}` — it was loaded but never invoked.
- **Why:** Reduces package overhead; clean preamble per best practices seen in all reference papers.

### 3. Converted `\hline` to booktabs rules in ablation tables
- **Files:** `tables/data_mix_ablation_t1.tex`, `tables/data_mix_ablation_t2.tex`
- **What:** Replaced all `\hline` with `\toprule`, `\midrule`, `\bottomrule`; replaced `\cline` with `\cmidrule(lr)`.
- **Why:** Every reference paper (E5-V, GME, ColPali, mmE5, LLaVE, Compression-Matching, Contrastive-Similarities) consistently uses booktabs-style rules. The other tables in this paper (`main_exp.tex`, `mmeb_pro_statistics.tex`, `t_test_summary.tex`) already used booktabs — these two were inconsistent.

### 4. Fixed `\multicolumn` span count in main results table
- **File:** `tables/main_exp.tex`
- **What:** Changed `\multicolumn{12}{c}` to `\multicolumn{17}{c}` for the "Baseline Models" and "Ours" separator rows.
- **Why:** The table has 17 columns (1 model + 5 image + 5 video + 5 visdoc + 1 all). The previous value of 12 was incorrect and could cause misaligned horizontal rules in the separator rows.

### 5. Standardized itemlist spacing in introduction
- **File:** `sections/introduction.tex`
- **What:** Uncommented `itemsep=0pt, parsep=0pt, topsep=0pt, leftmargin=1em` parameters in the contributions `\begin{itemize}` block.
- **Why:** The benchmark section (`sections/benchmark.tex`) already uses these exact parameters for its itemized list. This makes the two sections visually consistent, matching the compact list style seen in reference papers like GME and mmE5.

### 6. Removed orphaned `\vspace{-10pt}` after table environment
- **File:** `tables/mmeb_pro_statistics.tex`
- **What:** Removed `\vspace{-10pt}` that was placed outside the table environment.
- **Why:** Negative vspace outside a float environment can cause unpredictable spacing depending on page breaks. The table's own float placement handles spacing correctly.

## Reference Papers That Informed Changes
- **E5-V** (arXiv 2407.12580): Consistent booktabs, compact lists
- **GME** (arXiv 2412.16855): Booktabs throughout, small captions
- **ColPali** (ICLR 2025): Clean booktabs tables, bold caption labels
- **mmE5** (arXiv 2502.08468): Booktabs rules, compact itemlists
- **LLaVE** (arXiv 2503.04812): Consistent table formatting
- **Compression-Matching** (arXiv 2511.08480): Booktabs throughout
- **Contrastive-Similarities** (arXiv 2506.09781): Clean formatting conventions

## Warnings
- The `main.bib` file has entries with empty `year` fields (LLM2Vec, colpali, vlm2vec, seed16embedding) which generate BibTeX warnings. These are content issues, not formatting.
- The `youcook2` bib entry has both `volume` and `number` fields, which generates a BibTeX warning.
