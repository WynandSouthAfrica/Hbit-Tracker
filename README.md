# OMEC Habit Tracker — v0.3.1 (PDF only)

What's new:
- Removed JSON import/export to keep it simple
- Keep Task Manager to add/edit tasks directly in the app
- PDF-only export; **OMEC logo** embedded in the PDF header
- ASCII-safe text in PDF (no emoji/font issues)

## Run
```bash
pip install -r requirements.txt
streamlit run app.py
```

## Requirements
- streamlit
- fpdf
