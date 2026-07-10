import streamlit as st
import pandas as pd
import plotly.express as px

def show():

    jobs = pd.read_csv("ai_jobs.csv")

    jobs["Average Salary"] = (
        jobs["salary_min_usd"] +
        jobs["salary_max_usd"]
    ) / 2

    tab1, tab2, tab3, tab4, tab5 = st.tabs([
        "🏠 Work Mode",
        "🌍 Country Analysis",
        "📈 Trend",
        "💰 Salary",
        "📊 Overview"
    ])


    with tab1:

        st.metric(
            "Total Work Modes",
            jobs["remote_type"].nunique()
        )

        remote = (
            jobs["remote_type"]
            .value_counts()
            .reset_index()
        )

        remote.columns = [
            "Work Mode",
            "Jobs"
        ]

        fig = px.bar(
            remote,
            x="Work Mode",
            y="Jobs",
            color="Jobs",
            text="Jobs",
            color_continuous_scale="Turbo"
        )

        fig.update_traces(
            textposition="outside",
            marker_line_color="white",
            marker_line_width=2,
            hovertemplate="<b>%{x}</b><br>Total Jobs: %{y}<extra></extra>"
        )

        fig.update_layout(
            title="Remote vs Hybrid vs On-site Jobs",
            title_x=.5,
            paper_bgcolor="rgba(0,0,0,0)",
            plot_bgcolor="rgba(0,0,0,0)",
            font=dict(color="white"),
            coloraxis_showscale=False
        )

        st.plotly_chart(fig, use_container_width=True)

        fig = px.pie(
            remote,
            names="Work Mode",
            values="Jobs",
            hole=.45,
            color_discrete_sequence=px.colors.qualitative.Set2
        )

        fig.update_traces(
            textinfo="percent+label",
            hovertemplate="<b>%{label}</b><br>%{value} Jobs<extra></extra>"
        )

        fig.update_layout(
            title="Work Mode Percentage",
            title_x=.5,
            paper_bgcolor="rgba(0,0,0,0)",
            plot_bgcolor="rgba(0,0,0,0)",
            font=dict(color="white")
        )

        st.plotly_chart(fig, use_container_width=True)


    with tab2:

        country = (
            jobs.groupby(["country","remote_type"])
            .size()
            .reset_index(name="Jobs")
        )

        fig = px.bar(
            country,
            x="country",
            y="Jobs",
            color="remote_type",
            barmode="group",
            text="Jobs"
        )

        fig.update_layout(
            title="Remote Jobs by Country",
            title_x=.5,
            paper_bgcolor="rgba(0,0,0,0)",
            plot_bgcolor="rgba(0,0,0,0)",
            font=dict(color="white")
        )

        st.plotly_chart(fig, use_container_width=True)    

        remote_country = (
            jobs[jobs["remote_type"]=="Remote"]
            ["country"]
            .value_counts()
            .reset_index()
        )

        remote_country.columns=["Country","Jobs"]

        fig = px.pie(
            remote_country,
            names="Country",
            values="Jobs",
            hole=.45
        )

        fig.update_layout(
            title="Remote Jobs Country Share",
            title_x=.5,
            paper_bgcolor="rgba(0,0,0,0)",
            plot_bgcolor="rgba(0,0,0,0)",
            font=dict(color="white")
        )

        st.plotly_chart(fig,use_container_width=True)


    with tab3:

        trend = (
            jobs.groupby(["posted_year","remote_type"])
            .size()
            .reset_index(name="Jobs")
        )

        fig = px.line(
            trend,
            x="posted_year",
            y="Jobs",
            color="remote_type",
            markers=True
        )

        fig.update_traces(
            line_width=4
        )

        fig.update_layout(
            title="Remote Trend Over Time",
            title_x=.5,
            paper_bgcolor="rgba(0,0,0,0)",
            plot_bgcolor="rgba(0,0,0,0)",
            font=dict(color="white")
        )

        st.plotly_chart(fig,use_container_width=True)    


    with tab4:

        salary = (
            jobs.groupby("remote_type")["Average Salary"]
            .mean()
            .reset_index()
        )

        fig = px.bar(
            salary,
            x="remote_type",
            y="Average Salary",
            color="Average Salary",
            text="Average Salary",
            color_continuous_scale="Plasma"
        )

        fig.update_traces(
            texttemplate="$%{y:,.0f}",
            textposition="outside"
        )

        fig.update_layout(
            title="Average Salary by Work Mode",
            title_x=.5,
            paper_bgcolor="rgba(0,0,0,0)",
            plot_bgcolor="rgba(0,0,0,0)",
            font=dict(color="white"),
            coloraxis_showscale=False
        )

        st.plotly_chart(fig,use_container_width=True)  


        fig = px.box(
            jobs,
            x="remote_type",
            y="Average Salary",
            color="remote_type",
            points="outliers"
        )

        fig.update_layout(
            title="Salary Distribution by Work Mode",
            title_x=.5,
            paper_bgcolor="rgba(0,0,0,0)",
            plot_bgcolor="rgba(0,0,0,0)",
            font=dict(color="white")
        )

        st.plotly_chart(fig,use_container_width=True) 


    with tab5:

        c1,c2,c3 = st.columns(3)

        c1.metric(
            "Remote Jobs",
            len(jobs[jobs["remote_type"]=="Remote"])
        )

        c2.metric(
            "Hybrid Jobs",
            len(jobs[jobs["remote_type"]=="Hybrid"])
        )

        c3.metric(
            "On-site Jobs",
            len(jobs[jobs["remote_type"]=="Onsite"])
        )

        st.divider()

        st.dataframe(jobs)    




