import streamlit as st
from groq import Groq

client = Groq(api_key=st.secrets.get("GROQ_API_KEY"))

st.set_page_config(page_title="AI Chatbot", page_icon="🤖")
st.title("🤖 AI Chatbot")
st.caption("Powered by Groq AI · Ask me anything!")

if "messages" not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

user_input = st.chat_input("Type your message here...")

if user_input:
    with st.chat_message("user"):
        st.markdown(user_input)
    st.session_state.messages.append({"role": "user", "content": user_input})

    with st.chat_message("assistant"):
        with st.spinner("Thinking..."):
            response = client.chat.completions.create(
                model="llama-3.3-70b-versatile",
                messages=[
                    {
                        "role": "system",
                        "content": """You are a helpful Indian business assistant who speaks both Hindi and English fluently.

LANGUAGE RULES:
- If user writes in Hindi → reply in Hindi
- If user writes in English → reply in English
- If user writes in Hinglish (mixed) → reply in Hinglish naturally
- Always match the user's language automatically

YOUR EXPERTISE:
- GST, taxation, and Indian business compliance
- Marketing tips for Indian small businesses
- Business growth strategies for Indian SMBs
- General business advice and planning
- Financial tips for small business owners

YOUR PERSONALITY:
- Friendly aur helpful — jaise ek trusted business advisor
- Practical advice do — theoretical nahi
- Simple language use karo — jargon avoid karo
- Encouraging aur positive raho"""
                    }
                ] + st.session_state.messages,
                max_tokens=1000
            )
            reply = response.choices[0].message.content
            st.markdown(reply)

    st.session_state.messages.append({"role": "assistant", "content": reply})

with st.sidebar:
    st.header("⚙️ Settings")
    if st.button("🗑️ Clear Chat"):
        st.session_state.messages = []
        st.rerun()
    st.divider()
    st.caption("Built with Groq API + Streamlit")
