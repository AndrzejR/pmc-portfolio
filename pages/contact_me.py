import streamlit as st

st.title("Contact Me")

with st.form(key="contact_form"):
    user_email = st.text_input("Your email address")
    user_message = st.text_area("Your message")
    submit = st.form_submit_button("Submit")
    if submit:
        st.info("Submitted!")
