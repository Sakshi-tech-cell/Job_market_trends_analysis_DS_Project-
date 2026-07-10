import streamlit as st

#pip install plotly       #another lib for graph
import plotly.express as px
import pandas as pd
import matplotlib.pyplot as plt
from streamlit_option_menu import option_menu
#from pages.home import home_page

from pages.sidebar import sidebar

from pages import home
from pages import Overview
from pages import skills
from pages import job_roles
from pages import country
from pages import industry
from pages import remote
from pages import salary

# ----------------------------
# Page Configuration
# ----------------------------

st.set_page_config(
    page_title="AI Job Market Intelligence",
    page_icon="🤖",
    layout="wide",
    #initial_sidebar_state="expanded"
)

#jobs = pd.read_csv("ai_jobs.csv")

# skills = pd.read_csv("skills_demand.csv")

# roles = pd.read_csv("job_title_mapping.csv")

# country = pd.read_csv("country_ai_trends.csv")


# ----------------------------
# load CSS
# ----------------------------

st.markdown("""
  <style>

  /* Background */

  .stApp{
  background:linear-gradient(-45deg,#0F2027,#203A43,#2C5364,#1B5E20);
  background-size:400% 400%;
  animation:gradient 12s ease infinite;
  }

  @keyframes gradient{
  0%{background-position:0% 50%;}
  50%{background-position:100% 50%;}
  100%{background-position:0% 50%;}
  }

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

  color:#EEEEEE;

  margin-top:10px;

  }

  /* Button */

  .button{

  display:inline-block;

  padding:15px 35px;

  background:#00BCD4;

  color:white;

  font-size:20px;

  border-radius:50px;

  text-decoration:none;

  transition:0.4s;

  margin-top:25px;

  }

  .button:hover{

  background:#4CAF50;

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
<style>

/* Section Title */
.section-title{
    text-align:center;
    color:white;
    font-size:38px;
    font-weight:bold;
    margin-top:20px;
    margin-bottom:20px;
}

/* Glass Card */
.glass-card{
    background:rgba(255,255,255,.12);
    backdrop-filter:blur(15px);
    padding:20px;
    border-radius:20px;
    box-shadow:0 8px 25px rgba(0,0,0,.35);
    color:pink;
    margin-bottom:20px;
}

/* Dataset Card */
.dataset-card{
    background:linear-gradient(135deg,#1e3c72,#2a5298);
    padding:18px;
    border-radius:18px;
    color:white;
    text-align:center;
    box-shadow:0 8px 20px rgba(0,0,0,.3);
    margin-bottom:15px;
}

/* Metric Title */
.metric-title{
    font-size:18px;
    font-weight:bold;
    color:#00E5FF;
    text-align:center;
}

/* Divider */
hr{
border:1px solid rgba(255,255,255,.2);
}
            
.glass-card:hover{
    transform:translateY(-8px);
    box-shadow:0 0 25px #00E5FF;
}            

</style>
""", unsafe_allow_html=True)


# ----------------------------
# Use Sidebar
# ----------------------------

page = sidebar()


if page == "Home":
    home.show()

elif page == "Overview":
    Overview.show()

elif page == "Skills Dashboard":
    skills.show()

elif page == "Job Roles":
    job_roles.show()


elif page == "Country Dashboard":
    country.show()

elif page == "Industry Dashboard":
    industry.show()

elif page == "Remote Work":
    remote.show()

elif page == "Salary Analysis":
    salary.show()


















    



         


# # python -m streamlit run app.py
