# OMEC Habit Tracker — v0.5.1 (PDF only)

**Fix**
- With `fpdf2`, `pdf.output(dest="S")` already returns **bytes**. Removed the extra `.encode("latin-1")` to fix the AttributeError.
- Keeps v0.5 features: Task Manager, quick actions, timestamped PDF, OMEC logo, ASCII-safe text.

## Run
```bash
pip install -r requirements.txt
streamlit run app.py
```

## Requirements
- streamlit>=1.32
- fpdf2>=2.7.8
- Pillow>=10.0
