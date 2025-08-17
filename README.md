# OMEC Habit Tracker — v0.5.2 (PDF only)

**Fix**
- Robust PDF bytes handling across both `fpdf` and `fpdf2`. We now coerce the output to true `bytes`, regardless of whether it starts as `str`, `bytes`, or `bytearray`.

**Features (unchanged)**
- Task Manager, quick actions, timestamped PDF, OMEC logo, ASCII-safe text.

## Run
```bash
pip install -r requirements.txt
streamlit run app.py
```

## Requirements
- streamlit>=1.32
- fpdf2>=2.7.8
- Pillow>=10.0
