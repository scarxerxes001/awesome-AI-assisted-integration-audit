"""Compile an IEEE-style PDF from main.tex; requires pdflatex and BibTeX."""
from pathlib import Path
import shutil
import subprocess

HERE = Path(__file__).resolve().parent
LATEX = shutil.which("pdflatex")
BIBTEX = shutil.which("bibtex") or shutil.which("bibtex.original")
if not LATEX or not BIBTEX:
    raise SystemExit("A TeX installation with pdflatex and BibTeX is required; alternatively compile main.tex in Overleaf.")
for command in ([LATEX, "-interaction=nonstopmode", "-halt-on-error", "main.tex"],
                [BIBTEX, "main"],
                [LATEX, "-interaction=nonstopmode", "-halt-on-error", "main.tex"],
                [LATEX, "-interaction=nonstopmode", "-halt-on-error", "main.tex"]):
    subprocess.run(command, cwd=HERE, check=True, stdout=subprocess.DEVNULL)
shutil.copy2(HERE / "main.pdf", HERE / "final_research_paper.pdf")
print("Built", HERE / "final_research_paper.pdf")
