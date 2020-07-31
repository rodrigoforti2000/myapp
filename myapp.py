
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

add_selectbox = st.sidebar.selectbox(
    "Escolha um:",
    ("Defense", "Speed")
)

if(add_selectbox == "Defense"):
    sns.scatterplot(x = "Defense", y = "Attack", data = pokemon, hue = "Legendary", palette = pallete_pok)
    plt.title("Ataque x Defesa\nseparado por lendários", loc = "left")
    st.pyplot()
else:
    sns.scatterplot(x="Speed", y="Attack", data=pokemon, hue="Legendary", palette=pallete_pok)
    plt.title("Ataque x Defesa\nseparado por lendários", loc="left")
    st.pyplot()

df = pd.DataFrame(
    np.random.randn(1000, 2) / [50, 50] + [37.76, -122.4],
    columns=['lat', 'lon'])

st.deck_gl_chart(
     viewport={
         'latitude': 37.76,
         'longitude': -122.4,
         'zoom': 11,
         'pitch': 50,
     },
     layers=[{
         'type': 'HexagonLayer',
         'data': df,
         'radius': 200,
         'elevationScale': 4,
         'elevationRange': [0, 1000],
         'pickable': True,
         'extruded': True,
     }, {
         'type': 'ScatterplotLayer',
         'data': df,
     }])

genre = st.radio(
     "What's your favorite movie genre",
     ('Comedy', 'Drama', 'Documentary'))

if genre == 'Comedy':
     st.write('You selected comedy.')
else:
     st.write("You didn't select comedy.")


agree = st.checkbox('I agree')

if agree:
    st.write('Great!')
