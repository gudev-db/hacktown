import seaborn as sns
import matplotlib.pyplot as plt
import streamlit as st
import pandas as pd

pto_tur2 = pd.read_csv("ptoreal.csv", encoding='iso-8859-1')
turista = pd.read_csv("turista.csv", encoding='iso-8859-1')


st.subheader('Análise bidimensional: Gênero x Viajando em companhia')
fig = plt.figure(figsize=(16, 8))
sns.countplot(x='genero', hue='grupo-ou-nao', data=turista)
st.pyplot(fig)

st.subheader('Análise bidimensional: Gênero x Viagens já trilhadas usando a plataforma')
fig = plt.figure(figsize=(16, 8))
sns.countplot(x='genero', hue='viagens-pela-plataforma', data=turista)
st.pyplot(fig)

st.subheader('Análise bidimensional: Gênero x Idade')
fig = plt.figure(figsize=(16, 8))
sns.countplot(x='genero', hue='idade', data=turista)
st.pyplot(fig)
