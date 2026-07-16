# import streamlit as st

# from streamlit_option_menu import option_menu

# def sidebar():
#     with st.sidebar:

#         #st.image("images/logo.png", width=120)

#         st.title("🤖 AI Job Market")

#         selected = option_menu(
#             "Navigation",
#             [
#                 "Home",
#                 "Overview",
#                 "Skills Dashboard",
#                 "Job Roles",
#                 "Salary Analysis",
#                 "Country Dashboard",
#                 "Industry Dashboard",
#                 "Remote Work",
#                 "Filter"

#             ],

#             icons=[
#                 "house",
#                 "speedometer2",
#                 "cpu",
#                 "person-workspace",
#                 "cash-stack",
#                 "globe",
#                 "building",
#                 "laptop",
#                 "cpu"


#             ],
#             menu_icon="robot",
#             default_index=0
#         )
#         # st.markdown("---")

#         # st.info("""
#         # Developed By

#         # **Sakshi Kumari**

#         # Python | Pandas | Plotly | Streamlit
#         # """)
#     return selected 


import streamlit as st
from streamlit_option_menu import option_menu

def sidebar():

    with st.sidebar:

        # Header
        st.markdown("""
        <div style="
            background:linear-gradient(135deg,#667eea,#764ba2);
            padding:18px;
            border-radius:15px;
            text-align:center;
            margin-bottom:20px;
        ">
            <h2 style="color:white;margin:0;">
                🤖 AI Job Market
            </h2>
            <p style="color:white;margin:0;font-size:15px;">
                Data Science Dashboard
            </p>
        </div>
        """, unsafe_allow_html=True)

        selected = option_menu(
            menu_title="📌 Navigation",
            options=[
                "Home",
                "Overview",
                "Skills Dashboard",
                "Job Roles",
                "Salary Analysis",
                "Country Dashboard",
                "Industry Dashboard",
                "Remote Work",
                "Filter",
                "APIs"
            ],

            icons=[
                "house-fill",
                "bar-chart-fill",
                "cpu-fill",
                "person-workspace",
                "cash-stack",
                "globe-central-south-asia",
                "building",
                "laptop",
                "funnel-fill",
                "robot"

            ],

            menu_icon="cast",

            default_index=0,

            styles={
                "container": {
                    "padding": "5px",
                    "background-color": "#0E1117"
                },

                "icon": {
                    "color": "#00E5FF",
                    "font-size": "20px"
                },

                "nav-link": {
                    "font-size": "16px",
                    "text-align": "left",
                    "margin": "4px",
                    "padding": "12px",
                    "--hover-color": "#262730",
                    "border-radius": "10px",
                },

                "nav-link-selected": {
                    "background-color": "#00BFFF",
                    "color": "white",
                    "font-weight": "bold",
                },
            }
        )

        st.divider()

        st.subheader("📊 Dashboard Stats")

        col1, col2 = st.columns(2)

        with col1:
            st.metric("Pages", "10")

        with col2:
            st.metric("Charts", "35+")

        #st.divider()

        # st.markdown("""
        # <div style="
        #     background:#1E1E1E;
        #     padding:15px;
        #     border-radius:12px;
        #     text-align:center;
        # ">
        #     <h4 style="color:#00E5FF;margin-bottom:8px;">
        #         👩‍💻 Developed By
        #     </h4>

        #     <h3 style="color:white;margin-top:0;">
        #         Sakshi Kumari
        #     </h3>

        #     <p style="color:#CCCCCC;">
        #         Python • Pandas • Plotly • Streamlit
        #     </p>

        #     <hr>

        #     <p style="color:#AAAAAA;font-size:13px;">
        #         AI Job Market Trends Analysis Dashboard
        #     </p>

        # </div>
        # """, unsafe_allow_html=True)

    return selected
