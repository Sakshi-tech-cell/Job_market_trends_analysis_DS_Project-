import streamlit as st
import pandas as pd
import plotly.express as px
import matplotlib.pyplot as plt

import streamlit as st
import pandas as pd

def show():    


    t1,t2,t3=st.tabs(["Demanded_skill","Skill Category Distribution","Overview"])
    with t1:

        st.title("💻 Skills Dashboard")

        skills = pd.read_csv("skills_demand.csv")
        country = pd.read_csv("country_ai_trends.csv")

        category = st.selectbox(
        "Select Skill Category",
        ["All"]+list(skills["skill_category"].unique())
        )

        if category!="All":
            skills = skills[
            skills["skill_category"]==category
            ]

        top = skills["skill"].value_counts().head(15)

        st.bar_chart(top)

        st.dataframe(skills) 

    with t2: 
        #Using Streamlit graph

        st.title("👩🏽‍💼 Skill Level Distribution using Streamlit ") 
        skills = pd.read_csv("skills_demand.csv")
        skill_counts = skills["skill_level"].value_counts()

        st.bar_chart(skill_counts)
        st.divider() 
        
        
        #using matplotlib
        st.title("👩🏽‍💻 Skill Category Distribution")

        skills = pd.read_csv("skills_demand.csv")
        skills = skills["skill_category"].value_counts()

            # Create Figure with 2 plots
        fig, ax = plt.subplots(1, 2, figsize=(12, 5))
            # ---------------------------
            # Bar Chart
            # ---------------------------
        skills.plot(
            kind="bar",
            ax=ax[0],
            color=["purple", "pink", "#FEC9A7"],
            edgecolor="black",
            alpha=0.6
        )

        ax[0].set_title("Skill Category Distribution")
        ax[0].set_xlabel("Skill Category")
        ax[0].set_ylabel("Number of Skills")
        ax[0].tick_params(axis="x", rotation=45)

        # Show values on bars
        for i, value in enumerate(skills):
            ax[0].text(
                i,
                value,
                str(value),
                ha="center",
                va="bottom"
            )

            # ---------------------------
            # Pie Chart
            # ---------------------------
        explode = [0.1, 0, 0]

        skills.plot(
            kind="pie",
            ax=ax[1],
            autopct="%1.1f%%",
            startangle=90,
            shadow=True,
            explode=explode,
            wedgeprops={
                "edgecolor": "black",
                "linewidth": 1,
                "linestyle": "-."
            }
        )

        ax[1].set_title("Skill Category Distribution")
        ax[1].set_ylabel("")

        plt.tight_layout()
        # Display in Streamlit
        st.pyplot(fig)
        st.divider() 


        ###Using Plotly
        st.title("👩🏽‍💼 Skill Level Distribution using Streamlit ")
        skills = pd.read_csv("skills_demand.csv")

        col1, col2 = st.columns(2)

        # ==================================================
        # Skill Level Distribution (Plotly)
        # ==================================================
        with col1:

            # st.metric("Skill Levels",skills["skill_level"].nunique())

            # level = (skills["skill_level"].value_counts().reset_index())

            # level.columns = ["Skill Level", "Count"]
            level = skills.groupby("skill_level").agg(
                Count=("skill", "count"),
                Skills=("skill", lambda x: ", ".join(x.unique()))
                ).reset_index()


            fig = px.bar(
                level,
                x="skill_level",
                y="Count",
                color="Count",
                text="Count",
                custom_data=["Skills"],  # Shows skills on hover
                color_continuous_scale="Turbo"
            )

            fig.update_traces(
                textposition="outside",
                marker_line_color="white",
                marker_line_width=2,
                hovertemplate="<b>%{x}</b><br>"
                  "Count: %{y}<br>"
                  "Skills: %{customdata[0]}"
                  "<extra></extra>"
            )

            fig.update_layout(
                title={
                    "text":"👩🏽‍💼 Skill Level Distribution",
                    "x":0.5
                },
                paper_bgcolor="rgba(0,0,0,0)",
                plot_bgcolor="rgba(0,0,0,0)",
                font=dict(color="white"),
                coloraxis_showscale=False,
                height=500
            )

            st.plotly_chart(fig, use_container_width=True)

        # ==================================================
        # Skill Category Distribution
        # ==================================================
        with col2:

            #category = (skills["skill_category"].value_counts().reset_index())
            # category.columns = ["Skill Category", "Count"]

            # fig = px.pie(
            #     category,
            #     names="Skill Category",
            #     values="Count",
            #     hole=.45,
            #     color_discrete_sequence=px.colors.qualitative.Set3
            # )

            # fig.update_traces(
            #     textinfo="percent+label",
            #     hovertemplate="<b>%{label}</b><br>Total Skills: %{value}<extra></extra>",
            #     pull=[0.05]*len(category),      # Slightly separates slices
            #     marker=dict(
            #         line=dict(color="white", width=2)
            #     ),
            
            # Create category dataframe
            category = skills.groupby("skill_category").agg(
                Count=("skill", "count"),
                Skills=("skill", lambda x: ", ".join(x.unique()))
            ).reset_index()

            fig = px.pie(
                category,
                names="skill_category",
                values="Count",
                hole=0.45,
                custom_data=["Skills"]
            )

            fig.update_traces(
                hovertemplate=
                "<b>%{label}</b><br>"
                "Count: %{value}<br>"
                "Skills: %{customdata[0]}"
                "<extra></extra>"
            ),
            domain=dict(
                x=[0.15, 0.85],   # Horizontal position
                y=[0.05, 0.65]    # Move chart downward
            )
        
            fig.update_layout(
                title={
                    "text":"👩🏽‍💻 Skill Category Distribution",
                    "x":0.5
                },
                paper_bgcolor="rgba(0,0,0,0)",
                plot_bgcolor="rgba(0,0,0,0)",
                font=dict(color="white"),
                 # Legend
                legend=dict(
                    orientation="h",
                    y=-0.15,
                    x=0.5,
                    xanchor="center",
                    font=dict(size=12)
                ),
                height=500
            )

            st.plotly_chart(fig, use_container_width=True)



    with t3: 
        # Count number of skills required for each job
        st.title("Distribution of Skills Required per Job")
        skills = pd.read_csv("skills_demand.csv")
        
        skills_per_job = skills.groupby("job_id")["skill"].count().head(8)
        st.bar_chart(skills_per_job)

            #Create figure
        skills = pd.read_csv("skills_demand.csv")
        
        skills_per_job = skills.groupby("job_id")["skill"].count() 
        # Create figure
        plt.figure(figsize=(8,5))

        plt.hist(
        skills_per_job,
        bins=10,
        edgecolor="black",
        color="#8F9CC4"
        )

        plt.title("Distribution of Skills Required per Job")
        plt.xlabel("Number of Skills Required")
        plt.ylabel("Number of Jobs")
        plt.grid(axis="y", alpha=0.5)
        # Display in Streamlit
        st.pyplot(plt) 

        st.divider()   

        # Count top skills
        st.title("👩🏽‍💻 Most Demanded AI Skills")
        top_skill = (
            country["top_skill"]
            .value_counts()
            .reset_index()
        )

        top_skill.columns = ["Top Skill", "Count"]

        col1, col2 = st.columns(2)

        # ======================================
        # Bar Chart
        # ======================================
        with col1:

            fig = px.bar(
                top_skill,
                x="Top Skill",
                y="Count",
                color="Count",
                text="Count",
                color_continuous_scale="Turbo"
            )

            fig.update_traces(
                textposition="outside",
                marker_line_color="white",
                marker_line_width=1.5,
                hovertemplate="<b>%{x}</b><br>Countries: %{y}<extra></extra>"
            )

            fig.update_layout(
                title={
                    "text":"📊 Most Demanded AI Skills",
                    "x":0.5
                },
                xaxis_title="Top Skill",
                yaxis_title="Frequency",
                paper_bgcolor="rgba(0,0,0,0)",
                plot_bgcolor="rgba(0,0,0,0)",
                font=dict(color="white"),
                coloraxis_showscale=False,
                xaxis=dict(tickangle=-30),
                height=500
            )

            st.plotly_chart(fig, use_container_width=True)


        # ======================================
        # Donut Chart
        # ======================================
        with col2:

            fig = px.pie(
                top_skill,
                names="Top Skill",
                values="Count",
                hole=0.45,
                color_discrete_sequence=px.colors.qualitative.Set3
            )

            fig.update_traces(
                textposition="inside",
                textinfo="percent+label",
                pull=[0.05]*len(top_skill),      # Slightly separates slices
                marker=dict(
                line=dict(color="white", width=2)
            ),
            hovertemplate="<b>%{label}</b><br>Jobs: %{value}<br>%{percent}<extra></extra>"
            )

            fig.update_traces(
                textinfo="percent+label",
                hovertemplate="<b>%{label}</b><br>Count: %{value}<br>%{percent}<extra></extra>",
                marker=dict(line=dict(color="white", width=2))
            )

            fig.update_layout(
                title={
                    "text":"🥧 Distribution of Top AI Skills",
                    "x":0.5
                },
                paper_bgcolor="rgba(0,0,0,0)",
                plot_bgcolor="rgba(0,0,0,0)",
                font=dict(color="white"),
                legend_title="Top Skill",
                  # Legend
                legend=dict(
                    orientation="h",
                    y=-0.15,
                    x=0.8,
                    xanchor="center",
                    font=dict(size=12)
                ),

                height=500
            )

            st.plotly_chart(fig, use_container_width=True)



