import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

st.title("Previsão com Regressão Linear")

horas_estudo = st.slider("Horas de Estudo", min_value=0.0, max_value=10.0, step=0.5, value=5.0)
nota_anterior = st.slider("Nota Anterior", min_value=0.0, max_value=10.0, step=0.1, value=5.0)

np.random.seed()
X_train = np.random.uniform(0, 10, size=(100, 2))
y_train = 0.5 * X_train[:, 0] + 0.5 * X_train[:, 1] + np.random.normal(0, 1, 100)

modelo = LinearRegression()
modelo.fit(X_train, y_train)

entrada_usuario = np.array([[horas_estudo, nota_anterior]])
previsao = modelo.predict(entrada_usuario)[0]

st.subheader("Resultado da Previsão")
st.write(f"A previsão da nota final é: **{previsao:.2f}**")

fig, ax = plt.subplots()

ax.scatter(X_train[:, 0], y_train, color='blue', alpha=0.5, label='Dados de Treinamento')

ax.scatter(horas_estudo, previsao, color='red', s=100, label='Previsão do Usuário')

ax.set_xlabel("Horas de Estudo")
ax.set_ylabel("Nota Final")
ax.set_title("Comparação: Dados de Treinamento vs. Previsão")
ax.legend()

st.pyplot(fig)