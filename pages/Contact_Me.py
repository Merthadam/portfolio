import streamlit as st
import re
from send_email import send_mail


# Email validation function
def is_valid_email(email):
    # Simple regex to validate an email address
    regex = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
    return re.match(regex, email)


# Streamlit form for contact
st.header("Contact Me")

with st.form(key="email_form"):
    user_email = st.text_input("Your email address")
    message = st.text_area("Your message", max_chars=500)

    # Prepare the message
    formatted_message = f"""
    Subject: New email from {user_email}
    From: {user_email}
    {message}
    """

    submit_button = st.form_submit_button("Submit")

    if submit_button:
        # Check if the email is valid
        if not user_email or not is_valid_email(user_email):
            st.error("Please enter a valid email address.")

        # Check if the message is empty
        elif not message.strip():
            st.error("Your message cannot be empty.")

        else:
            try:
                # Attempt to send the email
                send_mail(formatted_message)
                st.info("Email sent successfully!")
            except Exception as e:
                # If an error occurs during the email sending process
                st.error(f"An error occurred while sending your email: {str(e)}")
