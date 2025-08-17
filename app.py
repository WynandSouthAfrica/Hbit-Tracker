
import streamlit as st
import pandas as pd
from datetime import date, datetime, timedelta
from pathlib import Path

APP_TITLE = "✅ Daily Habit Tracker — v0.1"
DATA_FILE = Path("progress.csv")

DEFAULT_TASKS = [
    "Stretching",
    "German Lessons",
    "OMEC Designs",
    "Paint Bathroom"
]

st.set_page_config(page_title=APP_TITLE, layout="wide")
st.title(APP_TITLE)
st.caption("Keep it simple: tick what you did today. Build streaks. Review weekly.")

# ---------- Load / init data ----------
if DATA_FILE.exists():
    df = pd.read_csv(DATA_FILE, parse_dates=["date"])
    df["date"] = df["date"].dt.date
else:
    df = pd.DataFrame(columns=["date"] + DEFAULT_TASKS + ["notes"])

# ---------- Sidebar: settings ----------
st.sidebar.header("⚙️ Settings")
tasks = st.sidebar.multiselect("Tracked tasks", DEFAULT_TASKS, default=DEFAULT_TASKS)
if set(tasks) != set(DEFAULT_TASKS):
    # Ensure df has all selected columns
    for t in tasks:
        if t not in df.columns:
            df[t] = False

st.sidebar.markdown("---")
st.sidebar.write("Data file:", str(DATA_FILE.resolve()))

# ---------- Today's check-in ----------
col1, col2 = st.columns([1,2])
with col1:
    today = st.date_input("Pick a day to log", value=date.today())
with col2:
    st.markdown(" ")

st.subheader("🗒️ Check-in")
check_cols = st.columns(len(tasks))
checked = {}
for i, t in enumerate(tasks):
    with check_cols[i]:
        checked[t] = st.checkbox(t, value=False, key=f"chk_{t}")

notes = st.text_area("Notes (optional)", placeholder="How did it go? Wins / obstacles / quick thoughts…")

if st.button("💾 Save today"):
    # Upsert for the selected date
    row = {"date": today, **{t: bool(checked.get(t, False)) for t in tasks}, "notes": notes}
    # Remove existing entry for that date
    df = df[df["date"] != today]
    # Append and sort
    df = pd.concat([df, pd.DataFrame([row])], ignore_index=True)
    df = df.sort_values("date")
    df.to_csv(DATA_FILE, index=False)
    st.success(f"Saved your check-in for {today}.")
    st.rerun()

# ---------- Weekly summary ----------
st.markdown("---")
st.subheader("📆 Weekly Summary")

if not df.empty:
    # Determine the current week (Mon-Sun)
    ref = today if 'today' in locals() else date.today()
    start_of_week = ref - timedelta(days=ref.weekday())  # Monday
    end_of_week = start_of_week + timedelta(days=6)

    week_df = df[(df["date"] >= start_of_week) & (df["date"] <= end_of_week)].copy()

    if week_df.empty:
        st.info("No entries for this week yet. Log something above to start your streaks!")
    else:
        # Compute completion % per task
        summary = {}
        for t in tasks:
            if t in week_df.columns:
                summary[t] = int(100 * week_df[t].astype(bool).mean()) if len(week_df) else 0

        # Display table
        disp = week_df[["date"] + tasks].sort_values("date").fillna(False)
        disp = disp.rename(columns={"date": "Date"})
        disp["Date"] = disp["Date"].astype(str)
        st.dataframe(disp, use_container_width=True)

        st.markdown("**Completion this week:** " + " · ".join([f"{t}: {p}%" for t, p in summary.items()]))

        # Streaks for key habits
        def calc_streak(df, task):
            # Count consecutive days up to 'ref' where task = True
            consecutive = 0
            d = ref
            while True:
                row = df[df["date"] == d]
                if not row.empty and task in row.columns and bool(row[task].iloc[0]):
                    consecutive += 1
                    d = d - timedelta(days=1)
                else:
                    break
            return consecutive

        key1, key2 = "Stretching", "German Lessons"
        c1, c2, c3 = st.columns(3)
        with c1:
            if key1 in tasks:
                st.metric(f"🔥 {key1} streak", f"{calc_streak(df, key1)} days")
        with c2:
            if key2 in tasks:
                st.metric(f"🔥 {key2} streak", f"{calc_streak(df, key2)} days")
        with c3:
            st.metric("Logged days (this week)", f"{len(week_df)} / 7")

else:
    st.info("No data yet — check a few boxes and Save today.")

# ---------- Data export ----------
st.markdown("---")
st.subheader("⬇️ Export / Backup")
st.write("Your data is stored locally in **progress.csv**. Keep backups as needed.")
if st.button("Export CSV"):
    if not df.empty:
        st.download_button("Download progress.csv", data=df.to_csv(index=False), file_name="progress.csv", mime="text/csv")
    else:
        st.warning("Nothing to export yet.")
