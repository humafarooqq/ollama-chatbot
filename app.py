import streamlit as st
import ollama

st.set_page_config(page_title="Ollama Chatbot", layout="centered")

st.title("🤖 Ollama Chatbot")
st.write("Chat with a local LLM (powered by Ollama).")

# Keep chat history
if "messages" not in st.session_state:
    st.session_state["messages"] = []

# Display chat history
for msg in st.session_state["messages"]:
    role = "🧑 You" if msg["role"] == "user" else "🤖 Bot"
    st.markdown(f"**{role}:** {msg['content']}")

# User input
user_input = st.text_input("Type your message:")

if st.button("Send") and user_input:
    # Save user message
    st.session_state["messages"].append({"role": "user", "content": user_input})

    # Call Ollama
    response = ollama.chat(model="llama2", messages=st.session_state["messages"])

    bot_reply = response["message"]["content"]
    st.session_state["messages"].append({"role": "assistant", "content": bot_reply})

    st.experimental_rerun()
