import streamlit as st
import requests

def show():

    st.title("🤖 AI Job Market Assistant")

    if "messages" not in st.session_state:
        st.session_state.messages = []

    # Show previous chat
    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.write(message["content"])

    prompt = st.chat_input("Ask anything about AI Jobs...")

    if prompt:

        st.session_state.messages.append(
            {"role": "user", "content": prompt}
        )

        with st.chat_message("user"):
            st.write(prompt)

        url = "https://chatgpt-42.p.rapidapi.com/conversationgpt4-2"

        payload = {
            "messages": st.session_state.messages,
            "system_prompt": (
                "You are an AI Job Market Expert. "
                "Answer only questions related to AI, Data Science, "
                "Jobs, Salary, Skills, Companies and Career."
            ),
            "temperature": 0.7,
            "top_k": 5,
            "top_p": 0.9,
            "max_tokens": 512,
            "web_access": False
        }

        headers = {
            "x-rapidapi-key": st.secrets["RAPIDAPI_KEY"],
            "x-rapidapi-host": "chatgpt-42.p.rapidapi.com",
            "Content-Type": "application/json"
        }

        with st.spinner("Thinking..."):
            response = requests.post(
                url,
                json=payload,
                headers=headers
            )

        result = response.json()["result"]

        st.session_state.messages.append(
            {"role": "assistant", "content": result}
        )

        with st.chat_message("assistant"):
            st.write(result)

    st.sidebar.markdown("---")

    st.sidebar.info("""
    Developed By

    **👩‍💻 Sakshi **

    Python | Pandas | Plotly | Streamlit
    """)   