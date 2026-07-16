import streamlit as st
import pandas as pd
import plotly.express as px
import matplotlib.pyplot as plt

import streamlit as st
import pandas as pd

def show():    


    t1,t2,t3=st.tabs(["Demanded_skill","Skill Category Distribution","Overview"])
    with t1:

    #     st.title("💻 Skills Dashboard")

        skills = pd.read_csv("skills_demand.csv")
        country = pd.read_csv("country_ai_trends.csv")

     

    #     category = st.selectbox(
    #     "Select Skill Category",
    #     ["All"]+list(skills["skill_category"].unique())
    #     )

    #     if category!="All":
    #         skills = skills[
    #         skills["skill_category"]==category
    #         ]

    #     top = skills["skill"].value_counts().head(15)

    #     st.bar_chart(top)
    #     st.dataframe(skills)
    #     st.divider()
    #   st.title("💻 Skills Dashboard")
        st.markdown("Analyze the most in-demand AI & Data Science skills.")

        # Load Data
        skills = pd.read_csv("skills_demand.csv")

        # ----------------------------
        # KPIs
        # ----------------------------

        c1, c2, c3 = st.columns(3)

        c1.metric("Total Skills", skills["skill"].nunique())
        c2.metric("Skill Categories", skills["skill_category"].nunique())
        c3.metric("Total Records", len(skills))

        st.divider()

        # ----------------------------
        # Filters
        # ----------------------------

        col1, col2 = st.columns(2)

        with col1:
            category = st.selectbox(
                "📂 Select Skill Category",
                ["All"] + sorted(skills["skill_category"].unique())
            )

        with col2:
            search = st.text_input(
                "🔍 Search Skill",
                placeholder="Enter skill name..."
            )

        # Apply Filters

        filtered = skills.copy()

        if category != "All":
            filtered = filtered[
                filtered["skill_category"] == category
            ]

        if search:
            filtered = filtered[
                filtered["skill"].str.contains(search, case=False)
            ]

        st.divider()

        # ----------------------------
        # Top Skills Chart
        # ----------------------------

        top = (
            filtered["skill"]
            .value_counts()
            .head(15)
            .reset_index()
        )

        top.columns = ["Skill", "Count"]

        fig = px.bar(
            top,
            x="Skill",
            y="Count",
            color="Count",
            text="Count",
            color_continuous_scale="Cividis",
            title="Top Most In-Demand Skills"
        )

        fig.update_layout(
            plot_bgcolor="rgba(0,0,0,0)",     # Chart area
            paper_bgcolor="rgba(0,0,0,0)",    # Outside chart area
            title_x=0.3,
            xaxis_title="Skill",
            yaxis_title="Frequency",
            height=500
        )

        fig.update_traces(textposition="outside")

        st.plotly_chart(fig, use_container_width=True)

        # ----------------------------
        # Data Table
        # ----------------------------

        st.subheader("📄 Skills Dataset")

        st.dataframe(
            filtered,
            use_container_width=True,
            hide_index=True
        )
        st.divider()

    # ---------------------------- 

        #st.bar_chart(skills,x="skill",y="skill_category",color="skill_level")
        #st.scatter_chart(country,x="total_ai_jobs",y="year",color="top_skill",size="country")

        fig = px.scatter(
            country,
            x="total_ai_jobs",
            y="year",
            color="top_skill",
            size="remote_percentage",   # Numeric column
            hover_name="country",
            text="country",
            color_continuous_scale="Turbo"
        )

        fig.update_traces(
            marker=dict(
                line=dict(color="white", width=1)
            ),
            textposition="top center"
        )

        fig.update_layout(

        title=dict(
            text="🌍 AI Jobs vs Year by Country",
            x=0.26,
            font=dict(
                size=28,
                color="white",
                family="Arial Black"
            )
        ),

        paper_bgcolor="rgba(0,0,0,0)",
        plot_bgcolor="rgba(0,0,0,0)",

        font=dict(
            color="white",
            size=14
        ),

        height=600
    )

        st.plotly_chart(fig, use_container_width=True)

    with t2: 

          ###Using Plotly
        st.title("👩🏽‍💼 Skill Level Distribution using Plotly ")
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
                color_continuous_scale="Mint"
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
                #custom_data=["Skills"]
                color_discrete_sequence=px.colors.qualitative.Antique
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
        st.divider()         


      
    with t3:

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
                color_continuous_scale="Ice"
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
        st.divider()

        st.sidebar.markdown("---")

        st.sidebar.info("""
        Developed By

        **👩‍💻 Sakshi**

        Python | Pandas | Plotly | Streamlit
        """)
    

      


