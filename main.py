import streamlit as st #gerar interface grafica
import pandas as pd #manipular dados
import numpy as np #manipular numeros 

st.title('meu primeiro app com streamlit')

st.write('ola mundo')

st.write('exemplo de tabela')

df = pd.DataFrame({
    'coluna 1' : [1,2,3,4],
    'coluna 2' : [10, 20, 30, 40]
})