# OMEC Habit Tracker — v0.4 (PDF only)

**Changes vs 0.3.1**
- Version bump to **v0.4**
- New buttons: **Mark all done**, **Clear all**, **Reset checks**
- Header now shows a generation **timestamp** under the title
- PDF keeps OMEC logo + ASCII-safe text
- Still simple: no JSON, no storage — your PDF is your record

## Run
```bash
pip install -r requirements.txt
streamlit run app.py
```

## Requirements
- streamlit
- fpdf
