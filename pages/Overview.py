import streamlit as st
import pandas as pd
import plotly.express as px

# import streamlit as st
# import pandas as pd

def show():
    jobs = pd.read_csv("ai_jobs.csv")

    skills = pd.read_csv("skills_demand.csv")

    roles = pd.read_csv("job_title_mapping.csv")

    country = pd.read_csv("country_ai_trends.csv")

     #st.radio button , st.markdown etc

    t1,t2,t3=st.tabs(["Data","Info","Overview"])
    with t1:
        st.title("💼 AI Jobs Dataset")
        st.write("Contains job title, salary, country, company and experience level.")
        st.dataframe(jobs)
        # st.markdown("""
        #   <div class="dataset-card">
        #   <h2>💼 AI Jobs Dataset</h2>
        #   <p>Contains job title, salary, country, company and experience level.</p>
        #   </div>
        #   """, unsafe_allow_html=True)
        # st.dataframe(jobs, use_container_width=True)

        st.title("💻 Skills Dataset")
        st.write("Contains demanded AI skills and categories")
        st.dataframe(skills)
        

        st.title("👨‍💼 Job roles Dataset")
        st.write("Contains job titles, Standardized title, role category.")
        st.dataframe(roles)

        st.title("🌍 Countries Dataset")
        st.write("Contains country, year, total AI jobs, average salary, remote percentage, top skill.")
        st.dataframe(country)

    with t2:
        st.title("Info")
        # jobs.info()
        # jobs.isnull().sum()
        # jobs.duplicated().sum()
        # st.write(jobs.columns)
        # st.write(skills.columns)
        # st.write(roles.columns)
        # st.write(country.columns)
        st.markdown("""
          <div class="glass-card">

            <h2 align="center">
            📑 Dataset Information
            </h2>

            <p>
            <center>        
            This section shows all available columns from every dataset.
            </center>          
            </p>

            </div>
            """, unsafe_allow_html=True)
        st.subheader("Jobs Columns")
        st.write(jobs.columns)

        st.subheader("Skills Columns")
        st.write(skills.columns)

        st.subheader("Job Roles Columns")
        st.write(roles.columns)

        st.subheader("Country Columns")
        st.write(country.columns)

    with t3:
        st.title("📈 Overview")
        st.divider()
        st.title("👩🏽‍💼 For Jobs")
        st.markdown("""
          <div class="glass-card">

          <h2 align="center">
          💼 AI Jobs Summary
          </h2>

          </div>
          """, unsafe_allow_html=True)
        jobs = pd.read_csv("ai_jobs.csv")

        jobs["Average Salary"] = (
           jobs["salary_min_usd"] +
           jobs["salary_max_usd"]
        )/2


        c1,c2,c3,c4,c5,c6 = st.columns(6)

        c1.metric("💼 Total Jobs",len(jobs))

        #c2.metric("🌍 Countries",jobs["country"].nunique())

        c2.metric("🧑‍💻 Job Titles",jobs["job_title"].nunique())

        c3.metric("🏢 Companies",jobs["company_type"].nunique())

        c4.metric("📑 Average min salary",
          f"${jobs['salary_min_usd'].mean():,.0f}")
        
        c5.metric("👨‍💼 Average max salary",
          f"${jobs['salary_max_usd'].mean():,.0f}")
        
        c6.metric("📑 Average Salary",
           f"${jobs['Average Salary'].mean():,.0f}")

    
        #st.write(jobs.describe())
        st.markdown("""
          <div class="glass-card">
          <h3>📊 Statistical Summary</h3>
          </div>
                    
          """, unsafe_allow_html=True)

        st.dataframe(
            jobs.describe(),
            use_container_width=True
          )
        
        st.divider()

    

        st.title("🧰 For Skills")
        st.markdown("""
          <div class="glass-card">

          <h2 align="center">
          💻 Skills Summary
          </h2>

          </div>
          """, unsafe_allow_html=True)
        skills = pd.read_csv("skills_demand.csv")
        c1,c2,c3= st.columns(3)

        c1.metric("🧑‍💻 Skill",skills["skill"].nunique()) 
        c2.metric("📑 Skill_Category",skills["skill_category"].nunique())
        c3.metric("📊 Skill_Level",skills["skill_level"].nunique())

        #st.write(skills.describe())
        st.markdown("""
          <div class="glass-card">
          <h3>📊 Statistical Summary</h3>
          </div>
          """, unsafe_allow_html=True)

        st.dataframe(
            jobs.describe(),
            use_container_width=True
          )
        
        st.divider()


        st.title("👩🏽‍💻 For Job roles")
        st.markdown("""
          <div class="glass-card">

          <h2 align="center">
          💼 Job roles Summary
          </h2>

          </div>
          """, unsafe_allow_html=True)
        roles = pd.read_csv("job_title_mapping.csv")
        c1,c2,c3= st.columns(3)

        c1.metric("🧑‍💻 Job_roles",roles["job_title"].nunique()) 
        c2.metric("💻 Standardized_roles",roles["standardized_title"].nunique())
        c3.metric("👨‍💼 Role_Category",roles["role_category"].nunique())

        #st.write(roles.describe())
        st.markdown("""
          <div class="glass-card">
          <h3>📊 Statistical Summary</h3>
          </div>
          """, unsafe_allow_html=True)

        st.dataframe(
            jobs.describe(),
            use_container_width=True
          )
        
        st.divider()


        st.title("📡 For country")
        st.markdown("""
          <div class="glass-card">

          <h2 align="center">
          🌍 Countries Summary
          </h2>

          </div>
          """, unsafe_allow_html=True)
        country = pd.read_csv("country_ai_trends.csv")
        c1,c2,c3,c4 = st.columns(4)

        c1.metric("⛳ Country",country["country"].nunique())

        c2.metric("🕑 Year",country["year"].nunique())

        c3.metric("👩🏽‍💻 Total_ai_jobs",country["total_ai_jobs"].nunique())

        c4.metric("🖥️ Top_skill",country["top_skill"].nunique())

        #st.write(country.describe()) 
        st.markdown("""
          <div class="glass-card">
          <h3>📊 Statistical Summary</h3>
          </div>
          """, unsafe_allow_html=True)

        st.dataframe(
            jobs.describe(),
            use_container_width=True
          )
        

        st.divider()

        # st.subheader("Jobs by Experience")
        # st.bar_chart(
        # jobs["experience_level"].value_counts()
        # )
        import plotly.express as px

        # Count experience levels
        exp = jobs["experience_level"].value_counts().reset_index()
        exp.columns = ["Experience", "Jobs"]

        # Create Bar Chart
        fig = px.bar(
            exp,
            x="Experience",
            y="Jobs",
            text="Jobs",
            color="Experience",   # Different color for each bar
            color_discrete_sequence=px.colors.qualitative.Pastel
        )

        # Customize bars
        fig.update_traces(
            textposition="outside",
            hovertemplate="<b>%{x}</b><br>Total Jobs: %{y}<extra></extra>",
           # marker_line_color="black",
           # marker_line_width=1.5
        )

        # Customize layout
        fig.update_layout(
            title={
                "text": "📈 Experience Level Distribution",
                "x": 0.5,          # Center title
                "xanchor": "center",
                "font": {
                    "size": 24,
                    "color": "white"
                }
            },

            xaxis_title="Experience Level",
            yaxis_title="Number of Jobs",

            plot_bgcolor="rgba(0,0,0,0)",
            paper_bgcolor="rgba(0,0,0,0)",

            font=dict(
                color="white",
                size=14
            ),

            height=500
        )

        st.plotly_chart(fig, use_container_width=True)



        # st.subheader("Company Size")
        # st.bar_chart(
        # jobs["company_size"].value_counts()
        # )
        st.markdown("""
        <div class="glass-card">

        <h2 align="center">
        🏢 Company Size Distribution
        </h2>

        </div>
        """, unsafe_allow_html=True)

        st.bar_chart(
            jobs["company_size"].value_counts()
        )


