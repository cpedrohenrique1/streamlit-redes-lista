FROM python:3.11-slim
EXPOSE 8501
WORKDIR /app
COPY . /app/
RUN pip install streamlit pandas matplotlib plotly wordcloud seaborn 
CMD [ "sh", "-c", "streamlit run main.py --server.port 8501 --server.address 0.0.0.0" ]