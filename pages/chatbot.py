import streamlit as st
from openai import OpenAI
import time

# Initialize session state for chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

st.session_state.messages.append({"role": "ai", "content": "Hello! I'm your personal chatbot. How can I assist you today?"})

# OpenRouter Client Setup
client = OpenAI(
    base_url="https://openrouter.ai/api/v1",
    api_key=st.secrets["API_KEY_V2"],  # Secure API key
)

def display_typing_effect(text):
    """Simulates a typing effect for the chatbot."""
    placeholder = st.empty()
    typed_text = ""

    for char in text:
        typed_text += char
        placeholder.markdown(f"**{typed_text}**")  # Simulate typing effect
        time.sleep(0.02)  # Adjust speed for a realistic effect

    return typed_text

def chatbot_page():
    st.title("💬 Your Personal Shit AI [ONGOING]")
    # Display previous messages
    for msg in st.session_state.messages:
        if msg["role"] == "user":
            with st.chat_message("user"):
                st.markdown(
                    f"{msg['content']}", 
                    unsafe_allow_html=True
                )
        else:
            with st.chat_message("assistant"):
                st.markdown(msg["content"])

    # User input
    user_input = st.chat_input("Type your message here...")

    if user_input:
        # Append user message
        st.session_state.messages.append({"role": "user", "content": user_input})
        with st.chat_message("user"):
            st.markdown(
                f"{user_input}", 
                unsafe_allow_html=True
            )

        # Fetch chatbot response
        with st.spinner("Thinking..."):
            response = client.chat.completions.create(
                extra_headers={
                    "HTTP-Referer": "<YOUR_SITE_URL>",  # Optional site URL
                    "X-Title": "<YOUR_SITE_NAME>",  # Optional site title
                },
                extra_body={},
                model="cognitivecomputations/dolphin3.0-r1-mistral-24b:free",
                messages=[{"role": "user", "content": user_input}],
            )
            bot_response = response.choices[0].message.content
            print(bot_response)
        # Display chatbot response
        with st.chat_message("assistant"):
            st.markdown(bot_response)

        # Save bot response
        st.session_state.messages.append({"role": "assistant", "content": bot_response})

if __name__ == "__main__":
    chatbot_page()
