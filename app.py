import streamlit as st
from main import run_pipeline

# Load dataset
with open("data_research_data.txt", "r") as f:
    documents = f.read().split("\n")

st.title("🧠 Autonomous AI Research Assistant")

query = st.text_input("Enter Research Topic")

if st.button("Generate Report"):
    report = run_pipeline(query, documents)
    st.text_area("📄 Research Report", report, height=300)