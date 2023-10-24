import streamlit as st

st.set_page_config(layout="wide")

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
