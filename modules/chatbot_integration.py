import os
from dotenv import load_dotenv
import streamlit as st

# Load API key
load_dotenv()
GEMINI_API_KEY = os.getenv("GOOGLE_API_KEY")

# Import Gemini client
try:
    from google.generativeai import Client as GeminiClient
except ImportError:
    st.error("Please install google-generativeai package!")
    raise

# Initialize Gemini client
if GEMINI_API_KEY:
    gemini_client = GeminiClient(api_key=GEMINI_API_KEY)
else:
    gemini_client = None
    st.error("GEMINI_API_KEY not found in .env file!")

def get_gemini_response(prompt: str) -> str:
    """Send user query to Gemini and return response."""
    if not gemini_client:
        return "Error: Gemini client not initialized."
    if not prompt.strip():
        return "Please enter a valid query."

    try:
        response = gemini_client.chat(
            model="gemini-flash-latest",
            prompt=prompt
        )
        return getattr(response, "output_text", "No response from Gemini.")
    except Exception as e:
        return f"Error: {str(e)}"

def chatbot_interface():
    """Streamlit UI for chatbot."""
    st.subheader("🗨️ Ask NewsPulse AI")

    if "chat_history" not in st.session_state:
        st.session_state.chat_history = []

    if "chat_input" not in st.session_state:
        st.session_state.chat_input = ""

    # User input box
    user_input = st.text_input(
        "Enter your question or request a summary:",
        key="chat_input"
    )

    if st.button("Send"):
        if user_input.strip():
            with st.spinner("Getting response..."):
                bot_response = get_gemini_response(user_input)
            st.session_state.chat_history.append({"user": user_input, "bot": bot_response})
            st.session_state.chat_input = ""  # clear input

    # Clear chat history
    if st.button("Clear Chat"):
        st.session_state.chat_history = []

    # Display chat history
    for chat in st.session_state.chat_history:
        st.markdown(f"**You:** {chat['user']}")
        st.markdown(f"**NewsPulse AI:** {chat['bot']}")
