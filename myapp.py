import pandas as pd
import numpy as np
import streamlit as st

st.write("""
# Minha primeira aplicação web

### Júlia, o que vc achou??
""")

age = st.selectbox("Opinião", ["ruim","muito boa","Vsf e vai fazer alguma coisa útil"])

st.write("""
### O comuninsmo vencerá?
""")

communism = st.selectbox("Opinião",["Não","Sim","Com certeza"])
