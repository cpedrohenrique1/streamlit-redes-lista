import streamlit as st
import pandas as pd

dados = pd.DataFrame({
    'latitude': [-16.678452742502262, -15.794885778568375, -16.629487655137247, -16.243308593950594],
    'longitude': [-49.244837047656375,  -47.89177851706749, -49.21428602834838, -48.964223858007955],
    'categoria': ['Universidade', 'Capital', 'Aeroporto', 'Base Militar']
})

categorias = ['Todos'] + list(dados['categoria'].unique())

filtroCategorias = st.selectbox('Selecione uma categoria: ', categorias)

if filtroCategorias == 'Todos':
    dadosFiltrados = dados
else:
    dadosFiltrados = dados[dados['categoria'] == filtroCategorias]

st.map(dadosFiltrados)