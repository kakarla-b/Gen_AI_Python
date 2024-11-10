import streamlit as st
import pandas as pd
import numpy as np


## Title of the application

st.title("Hello Streamlit")

## Display a Simplet Text

st.write("Streamlit Tutorial for a frd")

##Create a simple Dataframe

df = pd.DataFrame({
    'First Coloumn' : [1, 2, 3, 4],
    'Second Coloumn' : [5, 6, 7, 8]
})

##Display Dataframe

st.write("Here is the df")
st.warning(df)

## Create a line Chart
chart_data = pd.DataFrame(
    np.random.randn(20,3), columns=['a', 'b', 'c']
)

st.line_chart(chart_data)