import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

def loadCsv(file):
    try:
        df = pd.read_csv(file)
        return df
    except Exception as e:
        st.error(f"Erro ao carregar o arquivo: {e}")
        return None

def calculateStatistics(df, column):
    if column in df.columns:
        media = df[column].mean()
        mediana = df[column].median()
        desvio = df[column].std()
        return media, mediana, desvio
    else:
        st.error("Coluna não encontrada no dataframe.")
        return None, None, None

def plotLineChart(df, column):
    if column in df.columns:
        st.subheader(f"Gráfico de Linha da coluna: {column}")
        st.line_chart(df[column])
    else:
        st.error("Coluna não encontrada para plotar o gráfico de linha.")
def plotHistogram(df, column):
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

st.title("Dashboard de Análise de Dados")
st.write("Faça o upload de um arquivo CSV para visualizar os dados.")

uploadedFile = st.file_uploader("Escolha um arquivo CSV", type="csv")

if uploadedFile is not None:
    df = loadCsv(uploadedFile)
    if df is not None:
        st.write("Dados do arquivo CSV:")
        st.dataframe(df)
        colunasNumericas = df.select_dtypes(include=['float64', 'int64']).columns
        if len(colunasNumericas) > 0:
            colunaSelecionada = st.selectbox("Selecione uma coluna numérica:", colunasNumericas)
            if st.button("Calcular Estatísticas"):
                media, mediana, desvio = calculateStatistics(df, colunaSelecionada)
                if media is not None:
                    st.write(f"Média: {media}")
                    st.write(f"Mediana: {mediana}")
                    st.write(f"Desvio Padrão: {desvio}")
                    if colunaSelecionada:
                        plotLineChart(df, colunaSelecionada)
                        plotHistogram(df, colunaSelecionada)
        else:
            st.warning("Nenhuma coluna numérica encontrada.")
    else:
        st.error("Não foi possível carregar os dados.")
else:
    st.info("Aguardando upload de arquivo CSV.")