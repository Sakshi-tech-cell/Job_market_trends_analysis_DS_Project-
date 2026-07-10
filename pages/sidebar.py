import streamlit as st

from streamlit_option_menu import option_menu

def sidebar():
    with st.sidebar:

        #st.image("images/logo.png", width=120)

        st.title("🤖 AI Job Market")

        selected = option_menu(
            "Navigation",
            [
                "Home",
                "Overview",
                "Skills Dashboard",
                "Job Roles",
                "Country Dashboard",
                "Industry Dashboard",
                "Remote Work",
                "Salary Analysis",

            ],
            icons=[
                "house",
                "speedometer2",
                "cpu",
                "person-workspace",
                "globe",
                "building",
                "laptop",
                "cash-stack"


            ],
            menu_icon="robot",
            default_index=0
        )
        st.markdown("---")

        st.info("""
        Developed By

        **Sakshi Kumari**

        Python | Pandas | Plotly | Streamlit
        """)
    return selected 
