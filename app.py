import pandas as pd
import streamlit as st
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots

st.set_page_config(
    page_title="Streamlit Dashboard",
    layout="wide",
    initial_sidebar_state="expanded")

st.title("Dashboard dados teste Projeto IC PIBITI 2024")
st.markdown("##")

df = pd.read_csv(r"C:\Users\igorc\OneDrive\Ambiente de Trabalho\dashboard streamlit\myproject\TABELA DADOS ALEATORIOS.csv", sep=';', encoding='latin-1')

st.sidebar.header("Filtre por aqui:")

sexo = st.sidebar.multiselect("Selecione o sexo", df["sexo"].unique())
if not sexo:
    df2 = df.copy()
else:
    df2 = df[df["sexo"].isin(sexo)]


comorbidade = st.sidebar.multiselect("Selecione a comorbidade", df2["comorbidade"].unique())
if not comorbidade:
    df3 = df2.copy()
else:
    df3 = df2[df2["comorbidade"].isin(comorbidade)]


fumante = st.sidebar.multiselect("Fumante",df3["fumante"].unique())
if not fumante:
    df3 = df2.copy()
else:
    df3 = df2[df2["fumante"].isin(fumante)]


if not sexo and not comorbidade and not fumante:
    filtered_df = df
elif not comorbidade and not fumante:
    filtered_df = df[df["sexo"].isin(sexo)]
elif not sexo and not fumante:
    filtered_df = df[df["comorbidade"].isin(comorbidade)]
elif comorbidade and fumante:
    filtered_df = df3[df["comorbidade"].isin(comorbidade) & df3["fumante"].isin(fumante)]
elif sexo and fumante:
    filtered_df = df3[df["sexo"].isin(sexo) & df3["fumante"].isin(fumante)]
elif sexo and comorbidade:
    filtered_df = df3[df["sexo"].isin(sexo) & df3["comorbidade"].isin(comorbidade)]
elif fumante:
    filtered_df = df3[df3["fumante"].isin(fumante)]
else:
    filtered_df = df3[df3["sexo"].isin(sexo) & df3["comorbidade"].isin(comorbidade) & df3["fumante"].isin(fumante)]

st.dataframe(filtered_df)

histogram_comorbidade = px.histogram(filtered_df, x="comorbidade", color="sexo")
st.plotly_chart(histogram_comorbidade)

scatter_idade_IMC = px.scatter(filtered_df, x="IMC", y="idade", color="sexo")
st.plotly_chart(scatter_idade_IMC)

pie_fumante = px.pie(filtered_df, values='comorbidade', names="sexo")
st.plotly_chart(pie_fumante)