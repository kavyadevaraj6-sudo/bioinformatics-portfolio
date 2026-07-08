# 🧬 Bioinformatics Portfolio

**MSc Bioinformatics | Python | Biopython | Genomics**

---

## Project 1: DNA Sequence Analyser

A Python tool that analyses real bacterial genome data using Biopython.
Designed to run on any FASTA format genome file.

### What it does
- Reads and parses FASTA genome files
- Calculates GC content (%)
- Counts DNA motif occurrences (e.g. ATG start codons)
- Saves a full results report automatically

### Data used
**E. coli K-12 MG1655 complete genome** (NC_000913.3)  
Source: NCBI — 4,641,652 base pairs

### Results
| Metric | Value |
|--------|-------|
| Genome length | 4,641,652 bp |
| GC Content | 50.79% |
| ATG start codons found | 76,282 |

### How to run
```bash
pip3 install biopython
python3 analyser.py
```

### Files
| File | Description |
|------|-------------|
| `analyser.py` | Main combined analysis tool |
| `script1_read_fasta.py` | FASTA file parser |
| `script2_gc_content.py` | GC content calculator |
| `results.txt` | Sample output from E. coli genome |

---

## About me
MSc Bioinformatics (Teesside University) | MSc Environmental Biotechnology  
Currently rebuilding computational skills — Python, Biopython, R, NGS pipelines  
Open to bioinformatics opportunities in the UK# bioinformatics-portfolio
