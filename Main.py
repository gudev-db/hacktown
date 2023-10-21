import streamlit as st
import requests
import time  # to simulate a real time data, time loop
import numpy as np  # np mean, np random
import pandas as pd  # read csv, df manipulation
import plotly.express as px  # interactive charts
import streamlit as st  # 🎈 data web app development
import matplotlib.pyplot as plt

st.set_page_config(
    page_title="Roadwise Dashboard",
    page_icon="✅",
    layout="wide",
)

st.title("Roadwise Dashboard")
st.text("Todas as informações que você precisa para um planejamento estratégico eficaz")

st.sidebar.success("Selecione as informações que deseja ver.")

