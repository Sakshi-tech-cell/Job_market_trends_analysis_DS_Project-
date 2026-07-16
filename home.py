import streamlit as st
def show():


    st.markdown("""

    <div class='title'>

    📊 Job Market Trends Analysis Dashboard

    </div>
     """,unsafe_allow_html=True)            
                
    st.markdown("""
    <div class='main-card'>            

    <div class='subtitle'>

    Explore AI & Data Science Job Market using Interactive Visualizations

    </div>

    <center>

    <a href="#" class="button">

    Explore Dashboard

    </a>

    </center>

    </div>

    """,unsafe_allow_html=True)
    st.markdown(
        """
        <div class="page-title">
        <h1 style="text-align:center;">🎯 About Project</h1>
        </div>
        """,
        unsafe_allow_html=True
    )

    # Create two columns
    col1, col2 = st.columns([1, 2])

    # -------------------------
    # Left Column (Image)
    # -------------------------
    with col1:
        st.markdown("<br>",unsafe_allow_html=True)
       
        st.markdown("""
            <div class='main-card' style='padding:15px; margin-top:10px;'>        
            <img src="https://images.unsplash.com/photo-1551288049-bebda4e38f71"
                width="100%"
                height=450  
                style="border-radius:10px; object-fit:cover; aspect-ratio: 4/3; opacity:0.9;">
            </div>        
            """, unsafe_allow_html=True)
    

    # -------------------------
    # Right Column (About Card)
    # -------------------------
    with col2:
        st.markdown("""
        <div class='main-card'>

        <h2 style="text-align:center;">📊 AI Job Market Dashboard</h2>

        <hr>

        <p style="font-size:18px; line-height:2;">
        <center>           

        ✔ AI Job Market Analysis<br>

        ✔ Salary Trends<br>

        ✔ Skills Demand<br>

        ✔ Country Analysis<br>

        ✔ Industry Analysis<br>

        ✔ Remote Work Analysis<br>

        ✔ Hiring Trends
        </center>            

        </p>

        </div>
        """, unsafe_allow_html=True)

    st.markdown("<br>",unsafe_allow_html=True)

    c1,c2,c3=st.columns(3)

    with c1:

        st.markdown("""

    <div class='feature'>

    <h2>💼 Jobs</h2>

    <h4>50,000+ Jobs</h4>

    <p>Analyze job opportunities across countries.</p>

    </div>

    """,unsafe_allow_html=True)

    with c2:

        st.markdown("""

    <div class='feature'>

    <h2>💰 Salary</h2>

    <h4>Country Wise Salary</h4>

    <p>Compare average salaries worldwide.</p>

    </div>

    """,unsafe_allow_html=True)

    with c3:

        st.markdown("""

    <div class='feature'>

    <h2>🚀 Skills</h2>

    <h4>Top Skills</h4>

    <p>Discover the most demanded AI skills.</p>

    </div>

    """,unsafe_allow_html=True)

    st.markdown("<br>",unsafe_allow_html=True)

    #st.success("Developed using Python • Streamlit • Pandas • Matplotlib • Seaborn")



    st.markdown(
    """
    <hr></hr>
    <div class="page-title">
    <h1> ⚙ Project Workflow </h1>
    </div>

    <div class="workflow-card">

    <h2 style="text-align:center;">AI Job Market Dashboard Workflow</h2>

    <center>

    💡 Idea

    ⬇

    📂 Dataset Collection

    ⬇

    🧹 Data Cleaning

    ⬇

    📊 Exploratory Data Analysis

    ⬇

    📈 Data Visualization

    ⬇

    💻 Streamlit Dashboard

    ⬇

    📑 Insights & Conclusion

    </center>

    </div>

    """,
    unsafe_allow_html=True
    )


    a, b, c = st.columns(3)

    st.markdown(
    """
    <hr></hr>
    <div class="page-title">

    <h1>📚 Dashboard Pages </h1>

    </div>

    """,
    unsafe_allow_html=True
    )

    a,b,c=st.columns(3)

    with a:

        st.markdown("""
                                   

    <div class="page-card">

    <h2>📈 Overview</h2>

    <p>Complete summary of AI Job Market.</p>

    </div>

    <div class="page-card">

    <h2>💻 Skills Dashboard</h2>

    <p>Top demanded skills & categories.</p>

    </div>
                    
    <div class="page-card">

    <h2>💰 Salary Dashboard</h2>

    <p>Salary comparison & analysis.</p>

    </div>   

    """,unsafe_allow_html=True)

    with b:

        st.markdown("""
            

    <div class="page-card">

    <h2>🌍 Country Dashboard</h2>

    <p>Country-wise hiring trends.</p>

    </div>

    <div class="page-card">

    <h2>👨‍💼 Job Roles</h2>

    <p>Popular AI job roles.</p>

    </div>
                    
    <div class="page-card">

    <h2>🏢 Industry Dashboard</h2>

    <p>Industry-wise hiring analysis.</p>

    </div>

    """,unsafe_allow_html=True)

    with c:

        st.markdown("""

    <div class="page-card">

    <h2>🏠 Remote Work</h2>

    <p>Remote vs Hybrid vs Onsite jobs.</p>

    </div>
                    
     <div class="page-card">

    <h2>🏠 Filter</h2>

    <p>Complete AI Job Market Overview</p>

    </div> 

    <div class="page-card">

    <h2>🤖 APIs Dashboard</h2>

    <p> AI Job Market Assistant</p>

    </div>               

    """,unsafe_allow_html=True)


    st.markdown("---")

    st.markdown(
        """
        <center>

        <h4>📊 Job Market Trends Analysis Dashboard</h4>

        Developed using ❤️ Python | Pandas | Matplotlib | Seaborn | Streamlit

        <br>

        <b>Developed by Sakshi Kumari</b>

        </center>
        """,
        unsafe_allow_html=True
    )

    st.sidebar.markdown("---")

    st.sidebar.info("""
    Developed By

    **👩‍💻 Sakshi **

    Python | Pandas | Plotly | Streamlit
    """)

   