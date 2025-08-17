
# OMEC Habit Tracker — v0.2.1 (PDF only)

Patch notes:
- Fixed UnicodeEncodeError by using ASCII-safe PDF output (no emojis / checkbox glyphs).
- Replaced special characters with ASCII equivalents in the PDF.
- Still PDF-only, no storage, OMEC dark theme.

## Run
```bash
pip install -r requirements.txt
streamlit run app.py
```

## Requirements
- streamlit
- fpdf
