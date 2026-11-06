# Aston Martin Lagonda: operations and supply chain management report

- `build/Aston Martin operations and supply chain management.docx`: the report (A4, Word).
- `figures/`: every diagram and chart in three forms:
  - `.drawio`: open in diagrams.net (app.diagrams.net → File → Open) to edit and re-export.
  - `.svg`: the vector original. In Word 365 the figures are embedded as SVG, so you can right-click a figure → **Convert to Shape** and edit boxes and text directly in Word.
  - `.png`: high-resolution fallback.
- `src/`: sources used to build everything: report text (`report.md`), the diagram layouts (`figures.py`, `diagram.py`), charts (`charts.py`) and the Word build (`build.py`).
- `Verification checklist.md`: figures to check against Aston Martin's primary documents before submission.

Rebuild after editing: `python3 src/charts.py figures && python3 src/figures.py figures && node src/render_svg.js figures fig && python3 src/build.py <references.md> "build/<name>.docx"`.
