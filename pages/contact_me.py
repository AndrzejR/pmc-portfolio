import streamlit as st
import functions.send_email as se

st.title("Contact Me")

with st.form(key="contact_form"):
    user_email = st.text_input("Your email address")
    user_message = st.text_area("Your message")
    message = f"""Subject: Portfolio Message from {user_email}

From: {user_email}
{user_message}
    """
    submit = st.form_submit_button("Submit")
    if submit:
        se.send_email(message)
        st.info("Submitted!")
