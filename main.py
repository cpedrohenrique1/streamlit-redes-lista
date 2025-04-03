import streamlit as st
import pandas as pd
import altair as alt

st.title("Sistema de Recomendação Simples")

preferencias = st.radio(
    "Escolha seu tipo de comida favorito:",
    ("Italiana", "Japonesa", "Brasileira", "Mexicana")
)

recomendacoes = {
    "Italiana": [("Pizza", 90), ("Lasanha", 80), ("Risoto", 70)],
    "Japonesa": [("Sushi", 95), ("Tempurá", 85), ("Ramen", 75)],
    "Brasileira": [("Feijoada", 90), ("Churrasco", 85), ("Galinhada", 80)],
    "Mexicana": [("Tacos", 88), ("Burritos", 82), ("Nachos", 78)]
}

st.subheader("Recomendações para você:")
for item, score in recomendacoes[preferencias]:
    st.write(f"{item} - Pontuação: {score}")

df = pd.DataFrame(recomendacoes[preferencias], columns=["Prato", "Pontuação"])
chart = alt.Chart(df).mark_bar().encode(
    x="Prato",
    y="Pontuação",
    color="Prato"
).properties(title="Pontuação das Recomendações")

st.altair_chart(chart, use_container_width=True)