import streamlit as st
import pandas as pd

def loadCsv(file):
    try:
        df = pd.read_csv(file)
        return df
    except Exception as e:
        st.error(f"Erro ao carregar o arquivo: {e}")
        return None

st.title("Dashboard de Análise de Dados")
st.write("Faça o upload de um arquivo CSV para visualizar os dados.")

uploadedFile = st.file_uploader("Escolha um arquivo CSV", type="csv")

if uploadedFile is not None:
    df = loadCsv(uploadedFile)
    if df is not None:
        st.subheader("Prévia dos Dados")
        st.dataframe(df)

        st.subheader("Filtros Interativos")

        colunasCategoricas = df.select_dtypes(include=['object', 'category']).columns
        if not colunasCategoricas.empty:
            colunaSelecionada = st.multiselect("Filtrar por colunas categóricas", colunasCategoricas)
            for col in colunaSelecionada:
                valoresUnicos = df[col].unique()
                valoresSelecionados = st.multiselect(f"Valores para {col}", valoresUnicos)
                if valoresSelecionados:
                    df = df[df[col].isin(valoresSelecionados)]

        colunasNumericas = df.select_dtypes(include=['number']).columns
        if not colunasNumericas.empty:
            colunaNumericaSelecionada = st.multiselect("Filtrar por colunas numéricas", colunasNumericas)
            for col in colunaNumericaSelecionada:
                min_val, max_val = float(df[col].min()), float(df[col].max())
                range_values = st.slider(f"Faixa de valores para {col}", min_val, max_val, (min_val, max_val))
                df = df[(df[col] >= range_values[0]) & (df[col] <= range_values[1])]

        st.subheader("Dados Filtrados")
        st.dataframe(df)
    else:
        st.error("Não foi possível carregar os dados.")
else:
    st.info("Aguardando upload de arquivo CSV.")