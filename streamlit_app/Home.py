import streamlit as st
import pandas as pd
from pathlib import Path

st.set_page_config(page_title="SkillCraft KPIs", layout="centered")

COST_FILE = Path("costing/cost_sheet.csv")

def load_costs():
    if not COST_FILE.exists():
        return pd.DataFrame(columns=["timestamp", "ru", "cuh"])
    return pd.read_csv(COST_FILE)

df = load_costs()

st.title("SkillCraft • Live KPIs")

col1, col2 = st.columns(2)
col1.metric("Total RU", f"{df['ru'].sum():.1f}")
col2.metric("Total CUH", f"{df['cuh'].sum():.2f}")

st.subheader("Ultimas llamadas Granite")
st.dataframe(df.tail(25), use_container_width=True)
