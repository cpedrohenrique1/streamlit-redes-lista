import streamlit as st
from wordcloud import WordCloud
from collections import Counter
import pandas as pd

st.title("Análise de Texto")
texto = st.text_area("Insira o texto aqui:")

if texto:
    qtdPalavras = len(texto.split())
    qtdCaracteres = len(texto)
    st.write(f"**Quantidade de palavras:** {qtdPalavras}")
    st.write(f"**Quantidade de caracteres:** {qtdCaracteres}")

    if st.button("Gerar Nuvem de Palavras"):
        wordcloud = WordCloud(background_color="white").generate(texto)
        st.image(wordcloud.to_image(), caption="Nuvem de palavras",use_container_width=True)

    palavras = texto.split()
    contagem = Counter(palavras)
    palavras_comuns = contagem.most_common(5)
    df_palavras = pd.DataFrame(palavras_comuns, columns=["Palavra", "Frequência"])
    st.write("**Top 5 palavras mais frequentes:**")
    st.dataframe(df_palavras)