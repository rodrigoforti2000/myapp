import pandas as pd
import numpy as np
import streamlit as st
import matplotlib.pyplot as plt
import  seaborn as sns


st.title("Pokemon Dataset")

pokemon = pd.read_csv("https://gist.githubusercontent.com/armgilles/194bcff35001e7eb53a2a8b441e8b2c6/raw/92200bc0a673d5ce2110aaad4544ed6c4010f687/pokemon.csv")

#mudando type de uma coluna
pallete_pok = {False:"lightgrey",
               True:"#1F77B4"}

plot_varx = st.sidebar.selectbox(
    "Eixo X:",
    ("Defense", "Speed","Attack","HP","Total")
)

plot_vary = st.sidebar.selectbox(
    "Eixo Y:",
    ("Defense", "Speed","Attack","HP","Total")
)

sns.scatterplot(x = plot_varx, y = plot_vary, data = pokemon, hue = "Legendary", palette = pallete_pok)
plt.title(plot_vary +" x "+ plot_varx +"\nseparado por lendários", loc = "left")
st.pyplot()
