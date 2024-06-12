import streamlit as st
import pandas as pd

st.header('Hola mundo!')
st.image('pixar.png')

data = pd.read_csv('probabilidades_marcas.csv')
st.dataframe(data)


multi = st.multiselect('nombres', ['Sofi', 'Trini', 'Ale'])

if multi == 'Trini':
    st.write('Hola Trini')
elif multi== 'Sofi':
    st.write('Hola Sofi')

