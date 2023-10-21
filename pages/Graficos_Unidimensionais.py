import matplotlib.pyplot as plt
import streamlit as st
import pandas as pd

pto_tur2 = pd.read_csv("ptoreal.csv", encoding='iso-8859-1')
turista = pd.read_csv("turista.csv", encoding='iso-8859-1')



pto_aval = pto_tur2['avaliacao']
pto_tipo = pto_tur2['Tipo']
pto_cidade = pto_tur2['Cidade']
tur_gen = turista['genero']
sexo = turista['genero'].value_counts()
sexo.plot(kind='pie', autopct='%1.2f%%')

st.subheader('Gênero dos turistas')
fig = plt.figure(figsize = (6, 4))
plt.pie(sexo,labels=['Feminino','Masculino'])
st.pyplot(fig)

acomp = turista['grupo-ou-nao'].value_counts()

st.subheader('Turistas viajando acompanhados ou não')
fig = plt.figure(figsize = (6, 4))
plt.pie(acomp,labels=['Sim','Não'])
st.pyplot(fig)

prima = turista['primeira-vez'].value_counts()

st.subheader('Turistas viajando com a Roadwise pela primeira vez')
fig = plt.figure(figsize = (6, 4))
plt.pie(prima,labels=['Sim','Não'])
st.pyplot(fig)

