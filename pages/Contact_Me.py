import streamlit as st
from send_email import send_mail

st.header("Contact Me")

with st.form(key="email_forms"):
    user_email = st.text_input("Your email address")
    message = st.text_area("Your message", max_chars=500)
    message = f"""
    Subject: New email from {user_email}
    From: {user_email}
    {message}
    
    """
    submit_button = st.form_submit_button("Submit")
    if submit_button:
        send_mail(message)
        st.info("Email sent successfully")
