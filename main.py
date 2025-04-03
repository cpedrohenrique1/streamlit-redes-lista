import streamlit as st
import pandas as pd

st.title("Simulador de Investimento")
valorInicial = st.number_input("Valor Inicial do Investimento:", min_value=0.0, value=1000.0, step=100.0)
taxaJuros = st.slider("Taxa de Juros Anual (%):", min_value=0.0, max_value=20.0, value=5.0, step=0.1)
periodoAnos = st.selectbox("Período (em anos):", options=list(range(1, 31)), index=4)

anos = list(range(1, periodoAnos + 1))
montantes = [valorInicial * (1 + taxaJuros / 100) ** ano for ano in anos]

st.subheader("Crescimento do Investimento")
st.line_chart(pd.DataFrame({"Ano": anos, "Montante (R$)": montantes}).set_index("Ano"))

st.write(f"Montante final após {periodoAnos} anos: R$ {montantes[-1]:,.2f}")