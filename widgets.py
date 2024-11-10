import streamlit as st
import pandas as pd

st.title("Important Form")

name = st.text_input("Enter your name:")

age = st.slider("Selecyt your age:", 0, 100, 25)

st.write(f"Your age is {age}.")

options = ["Python", "Java", "JavaScript", "C++"]
choice = st.selectbox("Choose your favorite language:", options)
st.write(f"You selected {choice}. ")

if name:
    st.write(f"Hello, {name}")


data = {
    "Name" : ["Balaji", "Sunny", "Pandu", "Manu"],
    "Age" : [28, 26, 24, 24],
    "City" : ["Newyork", "Georgia", "Proddatur", "Dallas"]

}

df = pd.DataFrame(data)
df.to_csv("Sample.csv")
st.write(df)

uploaded_file = st.file_uploader("Choose a csv file", type="csv")

if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)
    st.write(df)

    