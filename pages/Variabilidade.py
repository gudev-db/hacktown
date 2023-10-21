import matplotlib.pyplot as plt
import streamlit as st
import pandas as pd
import seaborn as sns

pto_tur2 = pd.read_csv("ptoreal.csv", encoding='iso-8859-1')
turista = pd.read_csv("turista.csv", encoding='iso-8859-1')


st.subheader('Boxplot da idade dos turistas')
fig = plt.figure(figsize=(16, 8))
sns.boxplot(x='idade', data=turista)
st.pyplot(fig)


st.subheader('Boxplot do número de viagens trilhadas pelos usuários na plataforma')
fig = plt.figure(figsize=(16, 8))
sns.boxplot(x='viagens-pela-plataforma', data=turista)
st.pyplot(fig)

st.subheader('Boxplot das avaliações dos pontos turísticos')
fig = plt.figure(figsize=(16, 8))
sns.boxplot(x='avaliacao', data=pto_tur2)
st.pyplot(fig)



