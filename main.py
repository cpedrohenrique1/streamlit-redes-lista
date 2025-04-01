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
    
def calculate_statistics(df, column):
    if column in df.columns:
        mean = df[column].mean()
        median = df[column].median()
        std_dev = df[column].std()
        return mean, median, std_dev
    else:
        st.error("Coluna não encontrada no dataframe.")
        return None, None, None

def plot_line_chart(df, column):
    if column in df.columns:
        st.subheader(f"Gráfico de Linha da coluna: {column}")
        st.line_chart(df[column])
    else:
        st.error("Coluna não encontrada para plotar o gráfico de linha.")
def plot_histogram(df, column):
    if column in df.columns:
        st.subheader(f"Histograma da coluna: {column}")
        plt.figure(figsize=(10, 5))
        plt.hist(df[column], bins=30, color='blue', alpha=0.7)
        plt.title(f'Histograma de {column}')
        plt.xlabel(column)
        plt.ylabel('Frequência')
        st.pyplot(plt)
    else:
        st.error("Coluna não encontrada para plotar o histograma.")

def main():
    st.title("Dashboard de Análise de Dados")
    st.write("Faça o upload de um arquivo CSV para visualizar os dados.")
    
    uploaded_file = st.file_uploader("Escolha um arquivo CSV", type="csv")
    
    if uploaded_file is not None:
        df = load_csv(uploaded_file)
        if df is not None:
            st.write("Dados do arquivo CSV:")
            st.dataframe(df)
            numeric_columns = df.select_dtypes(include=['float64', 'int64']).columns
            if len(numeric_columns) > 0:
                selected_column = st.selectbox("Selecione uma coluna numérica:", numeric_columns)
                if st.button("Calcular Estatísticas"):
                    mean, median, std_dev = calculate_statistics(df, selected_column)
                    if mean is not None:
                        st.write(f"Média: {mean}")
                        st.write(f"Mediana: {median}")
                        st.write(f"Desvio Padrão: {std_dev}")
                        if selected_column:
                            plot_line_chart(df, selected_column)
                            plot_histogram(df, selected_column)
            else:
                st.warning("Nenhuma coluna numérica encontrada.")
        else:
            st.error("Não foi possível carregar os dados.")
    else:
        st.info("Aguardando upload de arquivo CSV.")

if __name__ == "__main__":
    main()