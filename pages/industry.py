import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import plotly.express as px

def show():

    jobs = pd.read_csv("ai_jobs.csv")

    jobs["Average Salary"] = (
        jobs["salary_min_usd"] +
        jobs["salary_max_usd"]
    ) / 2

    st.title("🏢 Industry Dashboard")

    tab1, tab2, tab3, tab4, tab5, tab6 = st.tabs([
        "Industry Jobs",
        "Industry Salary",
        "Employment Type",
        "Year Analysis",
        "Salary Trend",
        "Overview"
    ])

    with tab1:

        st.metric(
            "Industries",
            jobs["industry"].nunique()
        )

        industry = (
            jobs["industry"]
            .value_counts()
            .reset_index()
        )

        industry.columns = ["Industry","Jobs"]

        fig = px.bar(
            industry,
            x="Industry",
            y="Jobs",
            color="Jobs",
            text="Jobs",
            color_continuous_scale="Turbo"
        )

        fig.update_traces(
            textposition="outside",
            marker_line_color="white",
            marker_line_width=1.5,
            hovertemplate=
            "<b>%{x}</b><br>Total Jobs : %{y}<extra></extra>"
        )

        fig.update_layout(

            title={
                "text":"🏢 Industry-wise Jobs",
                "x":0.5
            },

            paper_bgcolor="rgba(0,0,0,0)",
            plot_bgcolor="rgba(0,0,0,0)",

            font=dict(color="white"),

            coloraxis_showscale=False,

            height=600
        )

        st.plotly_chart(fig,use_container_width=True)

        #Pie Chart 

        fig = px.pie(

            industry,

            names="Industry",

            values="Jobs",

            hole=.45,

            color_discrete_sequence=px.colors.qualitative.Bold

        )

        fig.update_traces(

            textinfo="percent+label",

            hovertemplate="<b>%{label}</b><br>Jobs : %{value}<extra></extra>"

        )

        fig.update_layout(

            title="Industry Share",

            title_x=.5,

            paper_bgcolor="rgba(0,0,0,0)",

            font=dict(color="white")

        )

        st.plotly_chart(fig,use_container_width=True)

    with tab2:

        salary = (

            jobs.groupby("industry")["Average Salary"]

            .mean()

            .reset_index()

        )

        fig = px.bar(

            salary,

            x="industry",

            y="Average Salary",

            color="Average Salary",

            text="Average Salary",

            color_continuous_scale="Sunset"

        )

        fig.update_traces(

            texttemplate="$%{y:,.0f}",

            textposition="outside"

        )

        fig.update_layout(

            title="💰 Average Salary by Industry",

            title_x=.5,

            paper_bgcolor="rgba(0,0,0,0)",

            plot_bgcolor="rgba(0,0,0,0)",

            font=dict(color="white"),

            coloraxis_showscale=False

        )

        st.plotly_chart(fig,use_container_width=True) 

        fig = px.box(

            jobs,

            x="industry",

            y="Average Salary",

            color="industry",

            points="all",

            color_discrete_sequence=px.colors.qualitative.Set2

        )

        fig.update_layout(

            title="Salary Distribution by Industry",

            title_x=.5,

            paper_bgcolor="rgba(0,0,0,0)",

            plot_bgcolor="rgba(0,0,0,0)",

            font=dict(color="white"),

            showlegend=False

        )

        st.plotly_chart(fig,use_container_width=True)  

    with tab3:

        emp = (
            jobs.groupby(["industry","employment_type"]).size().reset_index(name="Jobs")
            )
        # emp = pd.crosstab(
        #     jobs["industry"],
        #     jobs["employment_type"]
        #     )

        fig = px.bar(

            emp,

            x="industry",

            y="Jobs",

            color="employment_type",

            barmode="group",

            text="Jobs"

        )

        fig.update_layout(

            title="Employment Type by Industry",

            title_x=.5,

            paper_bgcolor="rgba(0,0,0,0)",

            plot_bgcolor="rgba(0,0,0,0)",

            font=dict(color="white")

        )

        st.plotly_chart(fig,use_container_width=True)  


        heat = pd.crosstab(
        jobs["industry"],
        jobs["employment_type"]
        )

        fig,ax=plt.subplots(figsize=(9,5))

        sns.heatmap(
        heat,
        annot=True,
        cmap="YlGnBu",
        linewidths=.5,
        ax=ax
        )

        plt.title("Industry vs Employment Type")

        st.pyplot(fig)  


    with tab4:

        # Count jobs by year
        year_jobs = (
            jobs["posted_year"]
            .value_counts()
            .sort_index()
            .reset_index()
        )

        # Rename columns
        year_jobs.columns = ["posted_year", "Jobs"]

        # Plotly line chart
        fig = px.line(
            year_jobs,
            x="posted_year",
            y="Jobs",
            title="Year-wise AI & Data Science Job Postings",
            markers=True
        )

        # Customize layout
        fig.update_layout(
            xaxis_title="Posted Year",
            yaxis_title="Number of Job Postings",
            template="plotly_white"
        )

        # Show values on each point
        fig.update_traces(
            text=year_jobs["Jobs"],
            textposition="top center",
            line=dict(color="purple", width=3)
        )

        # Display in Streamlit
        st.plotly_chart(fig, use_container_width=True)


        fig = px.area(
            year_jobs,
            x="posted_year",
            y="Jobs",
            color_discrete_sequence=["#00E5FF"]
        )

        fig.update_layout(
            title="Year-wise Hiring Trend",
            title_x=.5,
            paper_bgcolor="rgba(0,0,0,0)",
            plot_bgcolor="rgba(0,0,0,0)"
        )

        st.plotly_chart(fig,use_container_width=True)


    with tab5:

        salary_year = (
            jobs.groupby("posted_year")["Average Salary"]
            .mean()
            .reset_index()
        )

        fig = px.line(
            salary_year,
            x="posted_year",
            y="Average Salary",
            markers=True
        )

        fig.update_layout(
            title="Average Salary Trend",
            title_x=.5,
            paper_bgcolor="rgba(0,0,0,0)",
            plot_bgcolor="rgba(0,0,0,0)"
        )

        st.plotly_chart(fig,use_container_width=True) 

        fig = px.scatter(
            salary_year,
            x="posted_year",
            y="Average Salary",
            size="Average Salary",
            color="Average Salary",
            text="Average Salary",
            color_continuous_scale="Turbo"
        )

        fig.update_layout(
            title="Year-wise Average Salary",
            title_x=.5,
            paper_bgcolor="rgba(0,0,0,0)",
            plot_bgcolor="rgba(0,0,0,0)",
            coloraxis_showscale=False
        )

        st.plotly_chart(fig,use_container_width=True)

    with tab6:
        st.metric("Total Industries", jobs["industry"].nunique())

        st.metric(
            "Highest Paying Industry",
            salary.sort_values(
                "Average Salary",
                ascending=False
            ).iloc[0]["industry"]
        )

        st.metric(
            "Highest Hiring Industry",
            industry.iloc[0]["Industry"]
        )

        st.metric(
            "Average Salary",
            f"${jobs['Average Salary'].mean():,.0f}"
        )    













