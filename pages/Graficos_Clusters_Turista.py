import seaborn as sns
import matplotlib.pyplot as plt
import streamlit as st
import pandas as pd

turc1 = pd.read_csv("tur_c1.csv", encoding='iso-8859-1')
turc2 = pd.read_csv("tur_c2.csv", encoding='iso-8859-1')
turc3 = pd.read_csv("tur_c3.csv", encoding='iso-8859-1')
turc4 = pd.read_csv("tur_c4.csv", encoding='iso-8859-1')


st.header('Cluster 1')

st.subheader('Idade no cluster 1')
st.bar_chart(turc1['idade'])
st.write(turc1['idade'].mean())


st.subheader('Incidência de gênero no cluster 1')
st.bar_chart(turc1['genero'].value_counts())

st.subheader('Viajando em grupo ou não no cluster 1')
st.bar_chart(turc1['grupo-ou-nao'].value_counts())

st.subheader('Locais de origem na viagem no cluster 1')
st.bar_chart(turc1['local-de-origem'].value_counts())



st.subheader('Viagens realizadas através da plataforma Cluster 1')
st.bar_chart(turc1['viagens-pela-plataforma'])
st.write(turc1['viagens-pela-plataforma'].mean())


st.header('Cluster 2')

st.subheader('Idade no cluster 2')
st.bar_chart(turc2['idade'])
st.write(turc2['idade'].mean())

st.subheader('Incidência de gênero no cluster 2')
st.bar_chart(turc2['genero'].value_counts())

st.subheader('Viajando em grupo ou não no cluster 2')
st.bar_chart(turc2['grupo-ou-nao'].value_counts())

st.subheader('Locais de origem na viagem no cluster 2')
st.bar_chart(turc2['local-de-origem'].value_counts())



st.subheader('Viagens realizadas através da plataforma Cluster 2')
st.bar_chart(turc2['viagens-pela-plataforma'])
st.write(turc2['viagens-pela-plataforma'].mean())

st.header('Cluster 3')

st.subheader('Idade no cluster 3')
st.bar_chart(turc3['idade'])
st.write(turc3['idade'].mean())

st.subheader('Incidência de gênero no cluster 3')
st.bar_chart(turc3['genero'].value_counts())

st.subheader('Viajando em grupo ou não no cluster 3')
st.bar_chart(turc3['grupo-ou-nao'].value_counts())

st.subheader('Locais de origem na viagem no cluster 3')
st.bar_chart(turc3['local-de-origem'].value_counts())



st.subheader('Viagens realizadas através da plataforma Cluster 3')
st.bar_chart(turc3['viagens-pela-plataforma'])
st.write(turc3['viagens-pela-plataforma'].mean())

st.header('Cluster 4')

st.subheader('Idade no cluster 4')
st.bar_chart(turc4['idade'])
st.write(turc4['idade'].mean())

st.subheader('Incidência de gênero no cluster 4')
st.bar_chart(turc4['genero'].value_counts())

st.subheader('Viajando em grupo ou não no cluster 4')
st.bar_chart(turc4['grupo-ou-nao'].value_counts())

st.subheader('Locais de origem na viagem no cluster 4')
st.bar_chart(turc4['local-de-origem'].value_counts())



st.subheader('Viagens realizadas através da plataforma Cluster 4')
st.bar_chart(turc4['viagens-pela-plataforma'])
st.write(turc4['viagens-pela-plataforma'].mean())