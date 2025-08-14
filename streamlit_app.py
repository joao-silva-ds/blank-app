import streamlit as st
import pandas as pd

option = st.selectbox(
    "How would you like to be contacted?",
    ("Email", "Home phone", "Mobile phone"),
)

st.write("You selected:", option)

df = pd.DataFrame([[option]], columns=["option"])

@st.cache_data
def convert_for_download(df):
    return df.to_csv().encode("utf-8")

csv = convert_for_download(df)

st.download_button(
    label="Download CSV",
    data=csv,
    file_name="data.csv",
    mime="text/csv",
    icon=":material/download:",
)