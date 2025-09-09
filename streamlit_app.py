import streamlit as st
import pandas as pd
import time


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

import streamlit as st
import time

st.title("⏱️ Timer no Streamlit")

# Escolha de unidade
unidade = st.radio("Escolha a unidade de tempo:", ["Segundos", "Minutos"])

# Entrada do tempo
if unidade == "Segundos":
    tempo = st.number_input("Defina o tempo (em segundos):", min_value=1, step=1)
else:
    tempo = st.number_input("Defina o tempo (em minutos):", min_value=1, step=1) * 60

# Botão para iniciar
if st.button("Iniciar Timer"):
    st.write(f"⏳ Contagem regressiva de {tempo} segundos...")

    # Espaço reservado para atualizar o tempo
    placeholder = st.empty()

    for i in range(tempo, -1, -1):
        minutos = i // 60
        segundos = i % 60
        placeholder.markdown(f"## ⏰ {minutos:02d}:{segundos:02d}")
        time.sleep(1)

    st.success("🎉 Tempo esgotado!")
