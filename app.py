import streamlit as st
from openai import OpenAI
from retriever import get_qvara_snippet

st.set_page_config(page_title="Qvara AI Assistant", layout="centered")

st.title("🤖 Qvara AI Assistant (Demo)")
st.write("Ask me anything about Qvara's platform, risk analytics, or trading features.")

openai_api_key = st.text_input("Enter your OpenAI API Key", type="password")

if openai_api_key:
    client = OpenAI(api_key=openai_api_key)

    if "messages" not in st.session_state:
        st.session_state.messages = []

    user_input = st.chat_input("Ask a question...")

    if user_input:
        st.session_state.messages.append({"role": "user", "content": user_input})
        with st.spinner("Thinking..."):
            context = get_qvara_snippet(user_input)
            system_prompt = (
                "You are Qvara's intelligent assistant. "
                "You help users understand Qvara’s features, risk analytics, and platform navigation."
            )
            messages = [
                {"role": "system", "content": system_prompt},
                {"role": "system", "content": f"Reference info:\n{context}"},
                {"role": "user", "content": user_input},
            ]
            response = client.chat.completions.create(
                model="gpt-3.5-turbo",
                messages=messages,
                temperature=0.3,
            )
            reply = response.choices[0].message["content"]
            st.session_state.messages.append({"role": "assistant", "content": reply})

    for msg in st.session_state.messages:
        st.chat_message(msg["role"]).write(msg["content"])
else:
    st.warning("Please enter your OpenAI API key to start.")
