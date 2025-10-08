import streamlit as st
from config import INTERFACE_LANGUAGES, UI_TEXT

def login_page():
    """
    Displays the login page with username/password inputs.
    Handles language selection and stores user info in session state.
    """

    # Initialize session state if not already
    if "logged_in" not in st.session_state:
        st.session_state.logged_in = False
        st.session_state.username = ""
        st.session_state.email = ""
        st.session_state.language = "English"

    # Show login form only if not logged in
    if not st.session_state.logged_in:
        st.title(UI_TEXT[st.session_state.language]["login"])

        # Input fields
        username = st.text_input(UI_TEXT[st.session_state.language]["username"])
        email = st.text_input("Email")  # You can translate later
        password = st.text_input(UI_TEXT[st.session_state.language]["password"], type="password")

        # Language selection
        st.session_state.language = st.selectbox(
            UI_TEXT[st.session_state.language]["language"],
            INTERFACE_LANGUAGES,
            index=INTERFACE_LANGUAGES.index(st.session_state.language)
        )

        if st.button(UI_TEXT[st.session_state.language]["login"]):
            # Simple login check (no DB, always succeeds for demo)
            if username and password:
                st.session_state.logged_in = True
                st.session_state.username = username
                st.session_state.email = email
            else:
                st.error("Please enter both username and password.")

    else:
        st.success(f"Logged in as {st.session_state.username}")
