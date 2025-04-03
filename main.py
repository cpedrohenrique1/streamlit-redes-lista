import streamlit as st

with st.form("formulario"):
    st.write("Preencha o formulário abaixo:")
    nome = st.text_input("Nome", key="nome")
    idade = st.number_input("Idade", min_value=0, max_value=120, step=1, key="idade")
    cores = st.multiselect("Preferência de cor", ["Vermelho", "Azul", "Verde", "Amarelo", "Preto", "Branco"], key="cores")

    submitted = st.form_submit_button("Enviar")
    clear = st.form_submit_button("Limpar", on_click=lambda: clear())

    if submitted:
        if nome and cores:
            st.success(f"Olá, {nome}, com {idade} anos, você gosta de {', '.join(cores)}!")
        else:
            st.error("Por favor, preencha todos os campos corretamente.")

def clear():
        st.session_state["nome"] = ""
        st.session_state["idade"] = 0
        st.session_state["cores"] = []
