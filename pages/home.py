import streamlit as st
def show():
    
    st.markdown("""
    <style>

    /* Background */
    .stApp{ background:linear-gradient(-45deg,#0F2027,#203A43,#2C5364,#1B5E20); 
    background-size:400% 400%; 
    animation:gradient 12s ease infinite;
    }

    @keyframes gradient{ 0%{background-position:0% 50%;}
    50%{background-position:100% 50%;} 
    100%{background-position:0% 50%;} }            

                        
    /* Main Card */

    .main-card{

    background:rgba(255,255,255,0.12);

    backdrop-filter:blur(15px);

    padding:40px;

    border-radius:25px;

    box-shadow:0px 8px 30px rgba(0,0,0,0.35);

    transition:0.5s;

    margin-top:30px;

    }

    .main-card:hover{

    transform:scale(1.02);

    box-shadow:0px 10px 40px cyan;

    }

    /* Heading */

    .title{

    font-size:48px;

    font-weight:bold;

    text-align:center;

    color:white;

    animation:fade 2s;

    }

    .subtitle{

    font-size:22px;

    text-align:center;

    color:pink;

    margin-top:10px;

    }

    /* Button */

    .button{

    display:inline-block;

    padding:15px 35px;

    background:#6C5B7B;

    color:red;

    font-size:20px;

    border-radius:50px;

    text-decoration:none;

    transition:0.4s;

    margin-top:25px;

    }

    .button:hover{

    background:#4CAF50;
    color:red;            

    transform:scale(1.1);

    box-shadow:0px 0px 25px cyan;

    }

    /* Feature Card */

    .feature{

    background:rgba(255,255,255,0.15);

    padding:20px;

    border-radius:20px;

    text-align:center;

    transition:0.5s;

    height:220px;

    }

    .feature:hover{

    transform:translateY(-10px);

    background:#ffffff;

    color:black;

    box-shadow:0px 10px 30px cyan;

    }

    @keyframes fade{

    from{

    opacity:0;

    transform:translateY(40px);

    }

    to{

    opacity:1;

    transform:translateY(0px);

    }

    }

    img{

    border-radius:20px;

    }

    </style>
                
    <style>

    /* Workflow Card */

    .workflow-card{

    background:rgba(255,255,255,0.12);

    backdrop-filter:blur(15px);

    padding:30px;

    border-radius:20px;

    margin-top:20px;

    box-shadow:0px 8px 20px rgba(0,0,0,0.3);

    color:white;

    transition:.4s;

    }

    .workflow-card:hover{

    transform:translateY(-8px);

    box-shadow:0px 0px 20px cyan;

    }

    /* Dashboard Card */

    .page-card{

    background:rgba(255,255,255,0.15);

    padding:20px;

    border-radius:20px;

    text-align:center;

    color:white;

    margin:10px;

    transition:.4s;

    box-shadow:0px 5px 15px rgba(0,0,0,.3);

    }

    .page-card:hover{

    background:#ffffff;

    color:#000;

    transform:scale(1.05);

    box-shadow:0px 0px 20px cyan;

    }

    .page-title{

    text-align:center;

    color:white;

    font-size:34px;

    font-weight:bold;

    margin-top:30px;

    }

    </style>            
                


    """,unsafe_allow_html=True)

    st.markdown("""
    <div class='main-card'>

    <div class='title'>

    📊 Job Market Trends Analysis Dashboard

    </div>

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

    """,unsafe_allow_html=True)

    with c:

        st.markdown("""

    <div class="page-card">

    <h2>🏢 Industry Dashboard</h2>

    <p>Industry-wise hiring analysis.</p>

    </div>

    <div class="page-card">

    <h2>🏠 Remote Work</h2>

    <p>Remote vs Hybrid vs Onsite jobs.</p>

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
