import streamlit as st
import pandas as pd

st.set_page_config(layout='wide', page_title="Portfolio")

col1, col2 = st.columns(2)

with col1:
    st.image(image='images/me.jpg')

with col2:
    st.title("Andrzej Ruszczewski")
    bio = """
    Hello! I've used to be a runner, but then I took an arrow
     to the knee and I'm a Python programmer now :)
    """
    st.info(bio)

content = """Below you can find some of the apps I have built in Python. Feel free to contact me."""
st.text(content)

col3, col4 = st.columns(2)

data = pd.read_csv('data.csv', sep=';')


def display_project():
    st.header(r['title'])
    st.image(image=f"images/{r['image']}")
    st.write(r['description'])


with col3:
    for i, r in data[0::2].iterrows():
        display_project()
with col4:
    for i, r in data[1::2].iterrows():
        display_project()
