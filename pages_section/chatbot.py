import streamlit as st
from openai import OpenAI

# Initialize session state for chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

if not st.session_state.messages:
    st.session_state.messages.append({"role": "assistant", "content": "Hello! I'm your personal chatbot. How can I assist you today?"})


client = OpenAI(
    base_url="https://openrouter.ai/api/v1",
    api_key=st.secrets["API_KEY_V2"],
)


st.title("Dumb AI xd")
st.subheader("Ask me anything! (But not too hard)", divider="rainbow")

st.warning(
    "**Warning:** This is a demo version of the chatbot powered by `moonshotai/moonlight-16b-a3b-instruct:free`. "
    "Please refrain from sharing any sensitive or personal information. "
    "This chatbot is still a work in progress and may not always perform as expected.\n\n"
    "**What this model can help you with:**\n"
    "- Answering general questions\n"
    "- Providing explanations on various topics\n"
    "- Assisting with brainstorming ideas\n"
    "- Offering suggestions and recommendations\n\n"
    "Thank you for your understanding!\n\n"
    "**Note:**\n"
    "Hindi ko sure kung makakatulong to sayo hahaha",
    icon="⚠️"
)
# Display chat messages
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.write(message["content"])


if user_input := st.chat_input("Type your message here..."):
    st.session_state.messages.append({"role": "user", "content": user_input})
    
    with st.chat_message("user"):
        st.write(user_input)
    
    with st.chat_message("assistant"):
        with st.spinner("Thinking..."):
            response = client.chat.completions.create(
                model="moonshotai/moonlight-16b-a3b-instruct:free",  # Use the specified model
                messages=st.session_state.messages,  # Send the entire conversation history
            )
            bot_response = response.choices[0].message.content  
        st.write(bot_response)
    
    st.session_state.messages.append({"role": "assistant", "content": bot_response})