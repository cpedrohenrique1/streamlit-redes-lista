api_key = "2433|7aALO2tTwWBW2yosQKOzjeJtaXUOPJvIM7ULEyd3"
openWeather_api_key = "7bb167b8d8e16d4acb12c02cd41c0cb6"
headers = {
    "Authorization": f"Bearer {api_key}"
}
import streamlit as st
import requests
import pandas as pd

st.title("Consulta de Países com RestfulCountries")

country_name = st.text_input("Digite o nome do país (ex: Nigeria, Brazil, Canada):")

def get_country_data(name):
    url = f"https://restfulcountries.com/api/v1/countries/{name}"
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        return response.json().get("data")
    else:
        return None
def get_weather_data(city):
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={openWeather_api_key}&units=metric"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        return None

if country_name:
    data = get_country_data(country_name)
    clima = get_weather_data(data['capital'])

    if data and clima:
        st.success(f"✅ Dados encontrados para: {data['name']}")

        st.image(data['href']['flag'], width=200, caption=f"Bandeira de {data['name']}")
        st.subheader("📋 Informações Gerais")
        st.subheader("🌤️ Clima Atual")
        st.markdown(f"**Temperatura:** {clima['main']['temp']} C")
        st.markdown(f"**Umidade:** {clima['main']['humidity']}%")
        st.markdown(f"**Descrição:** {clima['weather'][0]['description']}")
        st.image(f"http://openweathermap.org/img/wn/{clima['weather'][0]['icon']}@2x.png", width=100)
        if "coord" in clima:
            st.subheader("🗺️ Localização no Mapa")
            st.map(pd.DataFrame([{
            "lat": clima["coord"]["lat"],
            "lon": clima["coord"]["lon"]
            }]))
        st.markdown(f"**Nome completo:** {data['full_name']}")
        st.markdown(f"**Capital:** {data['capital']}")
        st.markdown(f"**Continente:** {data['continent']}")
        st.markdown(f"**População:** {data['population']}")
        st.markdown(f"**Tamanho:** {data['size']}")
        st.markdown(f"**Moeda:** {data['currency']}")
        st.markdown(f"**Código telefônico:** +{data['phone_code']}")
    else:
        st.error("País não encontrado ou chave de API incorreta.")
elif country_name:
    st.warning("Por favor, insira o nome de um país para buscar informações.")