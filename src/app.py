import streamlit as st
import pandas as pd

st.title("HireGraph AI")

st.subheader(
    "AI-Powered Recruiter Intelligence"
)

file = pd.read_csv(
    'data/outputs/ranked_candidates.csv'
)

st.dataframe(file)

candidate = st.selectbox(
    "Select Candidate",
    file['candidate']
)

selected = file[
    file['candidate'] == candidate
]

st.write(selected)