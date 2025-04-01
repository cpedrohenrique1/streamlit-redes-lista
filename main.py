# Dashboard de Análise de Dados com Upload de CSV
# Crie um aplicativo onde o usuario pode fazer o upload de um arquivo CSV usando st.file_uploader.

# Exiba uma prévia dos dados com st.dataframe() e permita ao usuário
# selecionar uma coluna numérica para calcular a média, mediana e desvio
# padrão (usando Pandas).

# Adicione um gráfico interativo (ex. histograma) com st.ploty_chart() ou st.line_chart()

import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

def load_csv(file):
    try:
        df = pd.read_csv(file)
        return df
    except Exception as e:
        st.error(f"Erro ao carregar o arquivo: {e}")
        return None

def main():
    st.title("Dashboard de Análise de Dados")
    st.write("Faça o upload de um arquivo CSV para visualizar os dados.")
    
    uploaded_file = st.file_uploader("Escolha um arquivo CSV", type="csv")
    
    if uploaded_file is not None:
        df = load_csv(uploaded_file)
        if df is not None:
            st.subheader("Prévia dos Dados")
            st.dataframe(df)

            # Filtros interativos
            st.subheader("Filtros Interativos")

            # Filtro para colunas categóricas
            categorical_columns = df.select_dtypes(include=['object', 'category']).columns
            if not categorical_columns.empty:
                selected_category = st.multiselect("Filtrar por colunas categóricas", categorical_columns)
                for col in selected_category:
                    unique_values = df[col].unique()
                    selected_values = st.multiselect(f"Valores para {col}", unique_values)
                    if selected_values:
                        df = df[df[col].isin(selected_values)]

            # Filtro para colunas numéricas
            numerical_columns = df.select_dtypes(include=['number']).columns
            if not numerical_columns.empty:
                selected_numeric = st.multiselect("Filtrar por colunas numéricas", numerical_columns)
                for col in selected_numeric:
                    min_val, max_val = float(df[col].min()), float(df[col].max())
                    range_values = st.slider(f"Faixa de valores para {col}", min_val, max_val, (min_val, max_val))
                    df = df[(df[col] >= range_values[0]) & (df[col] <= range_values[1])]

            # Exibir dados filtrados
            st.subheader("Dados Filtrados")
            st.dataframe(df)
        else:
            st.error("Não foi possível carregar os dados.")
    else:
        st.info("Aguardando upload de arquivo CSV.")

if __name__ == "__main__":
    main()