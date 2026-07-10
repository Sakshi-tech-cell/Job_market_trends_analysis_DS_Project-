import streamlit as st
import pandas as pd
import plotly.express as px
import seaborn as sns
import matplotlib.pyplot as plt

def show():

    jobs = pd.read_csv("ai_jobs.csv")
    country = pd.read_csv("country_ai_trends.csv")

    st.title("👩🏽‍💼 Country-wise Dashboard")

    jobs["Average Salary"] = (
        jobs["salary_min_usd"] +
        jobs["salary_max_usd"]
    ) / 2

    t1, t2, t3, t4, t5, t6 = st.tabs([
        "🌍 AI Jobs",
        "💰 Salary",
        "🏠 Remote Jobs",
        "💻 Skills",
        "🏙 City Analysis",
        "📊 Heatmap"
    ])

    with t1:

        st.metric(
        "Countries",
        jobs["country"].nunique()
        )

        country_jobs = (jobs["country"].value_counts().reset_index())

        country_jobs.columns=["Country","Jobs"]

        fig = px.bar(
            country_jobs,
            x="Country",
            y="Jobs",
            color="Jobs",
            text="Jobs",
            color_continuous_scale="Turbo"
        )

        fig.update_layout(
            title="Country-wise AI Jobs",
            title_x=0.4,
            paper_bgcolor="rgba(0,0,0,0)",
            plot_bgcolor="rgba(0,0,0,0)",
            font=dict(color="white"),
            coloraxis_showscale=True
        )

        st.plotly_chart(fig,use_container_width=True)

        fig = px.pie(
        country_jobs,
        names="Country",
        values="Jobs",
        hole=.45
        )

        fig.update_layout(
            title="Country-wise AI Jobs",
            title_x=0.4,
            paper_bgcolor="rgba(0,0,0,0)",
            font=dict(color="white")
        )

        st.plotly_chart(fig,use_container_width=True)

    with t2:

        salary = (
        jobs.groupby("country")["Average Salary"]
        .mean()
        .sort_values(ascending=False)
        .reset_index()
        )

        fig = px.bar(
            salary,
            x="country",
            y="Average Salary",
            color="Average Salary",
            text="Average Salary",
            color_continuous_scale="Viridis"
        )

        fig.update_traces(
            texttemplate="$%{y:,.0f}",
            textposition="outside"
        )

        fig.update_layout(
            title="Average Salary by Country",
            title_x=.5,
            paper_bgcolor="rgba(0,0,0,0)",
            plot_bgcolor="rgba(0,0,0,0)",
            font=dict(color="white"),
            coloraxis_showscale=False
        )

        st.plotly_chart(fig,use_container_width=True)

        fig = px.histogram(
            jobs,
            x="Average Salary",
            color_discrete_sequence=["#00BFFF"]
        )

        fig.update_layout(
            title="Salary Distribution",
            title_x=.5
        )

        st.plotly_chart(fig,use_container_width=True)

    with t3:

        fig = px.bar(
            country,
            x="country",
            y="remote_percentage",
            color="remote_percentage",
            text="remote_percentage",
            color_continuous_scale="Plasma"
        )

        fig.update_traces(
            texttemplate="%{y}%",
            textposition="outside"
        )

        fig.update_layout(
            title="Remote Jobs Percentage",
            title_x=.5,
            paper_bgcolor="rgba(0,0,0,0)",
            plot_bgcolor="rgba(0,0,0,0)",
            font=dict(color="white"),
            coloraxis_showscale=False
        )

        st.plotly_chart(fig,use_container_width=True)

        fig = px.pie(
            country,
            names="country",
            values="remote_percentage",
            hole=.45
        )

        fig.update_layout(
            title="Remote Jobs Percentage",
            title_x=.5
        )

        st.plotly_chart(fig,use_container_width=True)


    with t4:
        skill = (
        country.groupby("top_skill")
        .size()
        .reset_index(name="Count")
        )

        fig = px.bar(
        skill,
        x="top_skill",
        y="Count",
        color="Count",
        text="Count",
        color_continuous_scale="Turbo"
        )

        fig.update_layout(
        title="Top Skills Across Countries",
        title_x=.5,
        paper_bgcolor="rgba(0,0,0,0)",
        plot_bgcolor="rgba(0,0,0,0)",
        font=dict(color="white")
        )

        st.plotly_chart(fig,use_container_width=True)

        fig = px.pie(
            skill,
            names="top_skill",
            values="Count",
            hole=.4
        )

        fig.update_layout(
            title="Country-wise Top Skills",
            title_x=.5
        )

        st.plotly_chart(fig,use_container_width=True) 

    with t5:

        city_jobs = (
            jobs["city"]
            .value_counts()
            .reset_index()
        )

        city_jobs.columns=["City","Jobs"]

        fig = px.bar(
            city_jobs,
            x="City",
            y="Jobs",
            color="Jobs",
            text="Jobs",
            color_continuous_scale="Turbo"
        )

        fig.update_layout(
            title="City-wise AI Jobs",
            title_x=.5,
            paper_bgcolor="rgba(0,0,0,0)",
            plot_bgcolor="rgba(0,0,0,0)",
            font=dict(color="white")
        )

        st.plotly_chart(fig,use_container_width=True)


        city_salary = (
            jobs.groupby("city")["Average Salary"]
            .mean()
            .reset_index()
        )

        fig = px.bar(
            city_salary,
            x="city",
            y="Average Salary",
            color="Average Salary",
            text="Average Salary",
            color_continuous_scale="Viridis"
        )

        fig.update_layout(
            title="Average Salary by City",
            title_x=.5,
            paper_bgcolor="rgba(0,0,0,0)",
            plot_bgcolor="rgba(0,0,0,0)",
            font=dict(color="white")
        )

        st.plotly_chart(fig,use_container_width=True)

        fig = px.pie(
            city_jobs,
            names="City",
            values="Jobs",
            hole=.45
        )

        fig.update_layout(
            title="City-wise Job Distribution",
            title_x=.5
        )

        st.plotly_chart(fig,use_container_width=True)


    with t6:

        heat = pd.crosstab(
            country["country"],
            country["top_skill"]
        )

        fig = px.imshow(
            heat,
            text_auto=True,
            color_continuous_scale="Viridis",
            aspect="auto"
        )

        fig.update_layout(
            title="Country vs Top Skill",
            title_x=.5,
            paper_bgcolor="rgba(0,0,0,0)",
            plot_bgcolor="rgba(0,0,0,0)",
            font=dict(color="white"),
            height=500
        )

        st.plotly_chart(fig,use_container_width=True)    






















