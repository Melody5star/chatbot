import streamlit as st
import anthropic
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Page config
st.set_page_config(
    page_title="AI Chatbot",
    page_icon="🤖",
    layout="centered"
)

# Title
st.title("🤖 AI Chatbot")
st.caption("Powered by Claude AI · Ask me anything!")

# Initialize Anthropic client
client = anthropic.Anthropic(api_key=os.getenv("ANTHROPIC_API_KEY"))

# Initialize chat history in session
if "messages" in st.session_state:
    pass
else:
    st.session_state.messages = []

# Display previous chat messages
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Chat input
user_input = st.chat_input("Type your message here...")

if user_input:
    # Show user message
    with st.chat_message("user"):
        st.markdown(user_input)

    # Save user message to history
    st.session_state.messages.append({
        "role": "user",
        "content": user_input
    })

    # Call Claude API
    with st.chat_message("assistant"):
        with st.spinner("Thinking..."):
            response = client.messages.create(
                model="claude-sonnet-4-20250514",
                max_tokens=1000,
                system="You are a helpful, friendly AI assistant. Keep responses clear and concise.",
                messages=st.session_state.messages
            )
            reply = response.content[0].text
            st.markdown(reply)

    # Save assistant reply to history
    st.session_state.messages.append({
        "role": "assistant",
        "content": reply
    })

# Sidebar
with st.sidebar:
    st.header("⚙️ Settings")
    if st.button("🗑️ Clear Chat"):
        st.session_state.messages = []
        st.rerun()
    st.divider()
    st.caption("Built with Claude API + Streamlit")
```

---



