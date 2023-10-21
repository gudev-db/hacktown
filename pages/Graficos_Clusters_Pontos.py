import seaborn as sns
import matplotlib.pyplot as plt
import streamlit as st
import pandas as pd

pto_turc1 = pd.read_csv("pto_c1.csv", encoding='iso-8859-1')
pto_turc2 = pd.read_csv("pto_c2.csv", encoding='iso-8859-1')
pto_turc3 = pd.read_csv("pto_c3.csv", encoding='iso-8859-1')
pto_turc4 = pd.read_csv("pto_c4.csv", encoding='iso-8859-1')

turista = pd.read_csv("turista.csv", encoding='iso-8859-1')



st.header('Cluster 1')

st.subheader('Avaliação dos pontos turísticos no cluster 1')
st.bar_chart(pto_turc1['avaliacao'])
st.write(pto_turc1['avaliacao'].mean())




st.subheader('Tipos de pontos turísticos no cluster 1')
st.bar_chart(pto_turc1['Tipo'].value_counts())

st.subheader('Cidades no cluster 1')
st.bar_chart(pto_turc1['Cidade'].value_counts())

st.subheader('Cidades no cluster 1')
st.bar_chart(pto_turc1['Categoria'].value_counts())

st.header('Cluster 2')

st.subheader('Avaliação dos pontor turísticos no cluster 2')
st.bar_chart(pto_turc2['avaliacao'])
st.write(pto_turc2['avaliacao'].mean())


st.subheader('Tipos de pontos turísticos no cluster 2')
st.bar_chart(pto_turc2['Tipo'].value_counts())

st.subheader('Cidades no cluster 2')
st.bar_chart(pto_turc2['Cidade'].value_counts())

st.subheader('Cidades no cluster 2')
st.bar_chart(pto_turc2['Categoria'].value_counts())

st.header('Cluster 3')

st.subheader('Avaliação dos pontor turísticos no cluster 3')
st.bar_chart(pto_turc3['avaliacao'])
st.write(pto_turc3['avaliacao'].mean())


st.subheader('Tipos de pontos turísticos no cluster 3')
st.bar_chart(pto_turc3['Tipo'].value_counts())

st.subheader('Cidades no cluster 3')
st.bar_chart(pto_turc3['Cidade'].value_counts())

st.subheader('Cidades no cluster 3')
st.bar_chart(pto_turc3['Categoria'].value_counts())

st.header('Cluster 4')

st.subheader('Avaliação dos pontor turísticos no cluster 4')
st.bar_chart(pto_turc4['avaliacao'])
st.write(pto_turc4['avaliacao'].mean())


st.subheader('Tipos de pontos turísticos no cluster 4')
st.bar_chart(pto_turc4['Tipo'].value_counts())

st.subheader('Cidades no cluster 4')
st.bar_chart(pto_turc4['Cidade'].value_counts())

st.subheader('Cidades no cluster 4')
st.bar_chart(pto_turc4['Categoria'].value_counts())


