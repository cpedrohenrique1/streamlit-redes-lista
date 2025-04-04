import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import plotly.express as px

if 'data' not in st.session_state:
    st.session_state['data'] = None

st.sidebar.title("Navegação")
page = st.sidebar.radio("Ir para", ["Upload de Dados", "Análise Estatística", "Gráficos Interativos"])

if page == "Upload de Dados":
    st.title("Upload e Visualização de Dados")

    uploaded_file = st.file_uploader("Faça upload de um arquivo CSV", type=["csv"])
    if uploaded_file:
        data = pd.read_csv(uploaded_file)
        st.session_state['data'] = data
        st.success("Arquivo carregado")
        st.dataframe(data)

elif page == "Análise Estatística":
    st.title("Análise Estatística dos Dados")

    if st.session_state['data'] is not None:
        df = st.session_state['data']

        @st.cache_data
        def get_statistics(data):
            return data.describe()

        st.subheader("Resumo Estatístico")
        st.write(get_statistics(df))

        st.subheader("Informações Gerais")
        st.write(df.info())
    else:
        st.warning("Por favor, carregue um arquivo na página de upload.")

elif page == "Gráficos Interativos":
    st.title("Gráficos Interativos com Plotly e Seaborn")

    if st.session_state['data'] is not None:
        df = st.session_state['data']
        numeric_cols = df.select_dtypes(include='number').columns.tolist()

        if len(numeric_cols) >= 2:
            x_axis = st.selectbox("Selecione o eixo X", numeric_cols, index=0)
            y_axis = st.selectbox("Selecione o eixo Y", numeric_cols, index=1)

            st.subheader("Gráfico de Dispersão")
            fig = px.scatter(df, x=x_axis, y=y_axis, title=f'{y_axis} vs {x_axis}')
            st.plotly_chart(fig, use_container_width=True)

            st.subheader("Histograma")
            col = st.selectbox("Selecione uma coluna para histograma", numeric_cols)
            fig2, ax = plt.subplots()
            sns.histplot(df[col], kde=True, ax=ax)
            st.pyplot(fig2)

        else:
            st.warning("O arquivo precisa ter pelo menos duas colunas numéricas.")
    else:
        st.warning("Por favor, carregue um arquivo na página de upload.")