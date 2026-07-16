# import streamlit as st
# import requests

# def show():

#     st.title("🤖 AI Job Market Assistant")

#     if "messages" not in st.session_state:
#         st.session_state.messages = []

#     # Show previous chat
#     for message in st.session_state.messages:
#         with st.chat_message(message["role"]):
#             st.write(message["content"])

#     prompt = st.chat_input("Ask anything about AI Jobs...")

#     if prompt:

#         st.session_state.messages.append(
#             {"role": "user", "content": prompt}
#         )

#         with st.chat_message("user"):
#             st.write(prompt)

#         url = "https://chatgpt-42.p.rapidapi.com/conversationgpt4-2"

#         payload = {
#             "messages": st.session_state.messages,
#             "system_prompt": (
#                 "You are an AI Job Market Expert. "
#                 "Answer only questions related to AI, Data Science, "
#                 "Jobs, Salary, Skills, Companies and Career."
#             ),
#             "temperature": 0.7,
#             "top_k": 5,
#             "top_p": 0.9,
#             "max_tokens": 512,
#             "web_access": False
#         }

#         # if "RAPIDAPI_KEY" in st.secrets:
#         #     st.success("✅ RAPIDAPI_KEY Found")
#         # else:
#         #     st.error("❌ RAPIDAPI_KEY Not Found")
#         #     st.stop()

#         headers = {
#             "x-rapidapi-key": st.secrets["RAPIDAPI_KEY"],
#             "x-rapidapi-host": "chatgpt-42.p.rapidapi.com",
#             "Content-Type": "application/json"
#         }

#         with st.spinner("Thinking..."):
#             response = requests.post(
#                 url,
#                 json=payload,
#                 headers=headers
#             )

#         #result = response.json()["result"]
#         st.write("Status Code:", response.status_code)
#         st.write("Response JSON:")
#         st.json(response.json())
#         st.stop()

#         st.session_state.messages.append(
#             {"role": "assistant", "content": result}
#         )

#         with st.chat_message("assistant"):
#             st.write(result)

import streamlit as st
from google import genai


def show():

    # ----------------------------
    # Gemini Client
    # ----------------------------
    client = genai.Client(
        api_key=st.secrets["GEMINI_API_KEY"]
    )

    # ----------------------------
    # Title
    # ----------------------------
    st.title("🤖 AI Job Market Assistant")

    st.write("Ask anything related to AI, Data Science, Skills, Salary, Companies, or Careers.")

    # ----------------------------
    # Chat History
    # ----------------------------
    if "messages" not in st.session_state:
        st.session_state.messages = []

    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

    # ----------------------------
    # User Input
    # ----------------------------
    prompt = st.chat_input("Ask anything about AI Jobs...")

    if prompt:

        # Show User Message
        st.session_state.messages.append(
            {"role": "user", "content": prompt}
        )

        with st.chat_message("user"):
            st.markdown(prompt)

        # ----------------------------
        # Gemini Response
        # ----------------------------
        with st.chat_message("assistant"):

            with st.spinner("Thinking..."):

                try:

                    response = client.models.generate_content(
                        model="gemini-3.5-flash",
                        contents=f"""
                            You are an AI Job Market Expert.

                            Answer only questions related to:

                            • AI
                            • Data Science
                            • Machine Learning
                            • Job Roles
                            • Salary
                            • Skills
                            • Career Guidance
                            • Companies
                            • Hiring Trends

                            If the user asks anything unrelated, politely reply:

                            "I can only answer questions related to AI and Data Science Job Market."

                            Question:
                            {prompt}
                            """
                    )

                    answer = response.text

                except Exception as e:

                    answer = f"""
                        ⚠️ **AI Service is temporarily unavailable.**

                        Error:

                        {str(e)}

                        Please try again after a few seconds.
                    """

                st.markdown(answer)

        # Save Assistant Message
        st.session_state.messages.append(
            {"role": "assistant", "content": answer}
        )
    st.sidebar.markdown("---")

    st.sidebar.info("""
    Developed By

    **👩‍💻 Sakshi **

    Python | Pandas | Plotly | Streamlit
    """)   