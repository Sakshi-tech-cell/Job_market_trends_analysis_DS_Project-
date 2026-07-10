import streamlit as st
import pandas as pd
import plotly.express as px

def show():

    jobs = pd.read_csv("ai_jobs.csv")

    st.title("💵 Salary Dashboard")
    st.markdown("Analyze AI job salary, county-wise salary, industry-wise salary, Experience-wise salary.")

    jobs["Average Salary"] = (
        jobs["salary_min_usd"] +
        jobs["salary_max_usd"]
    ) / 2

    t1, t2, t3, t4, t5 = st.tabs([
        "Salary Distribution",
        "Job Role",
        "Country",
        "Industry",
        "Experience"
    ])

    with t1:

        st.title("💰 Salary Distribution")

        st.metric(
            "Average Salary",
            f"${jobs['Average Salary'].mean():,.0f}"
        )

        fig = px.histogram(
            jobs,
            x="Average Salary",
            nbins=30,
            opacity=0.85,
            color_discrete_sequence=["#4F8BF9"]
        )

        fig.update_layout(
            title={
                "text":"🪙 Salary Distribution",
                "x":0.4,
                "font":dict(size=22,color="white")
            },
            paper_bgcolor="rgba(0,0,0,0)",
            plot_bgcolor="rgba(0,0,0,0)",
            font=dict(color="white"),
            xaxis_title="Average Salary (USD)",
            yaxis_title="Number of Jobs"
        )

        fig.update_traces(
            marker_line_color="white",
            marker_line_width=1,
            hovertemplate="<b>Salary:</b> %{x}<br><b>Jobs:</b> %{y}<extra></extra>"
        )

        st.plotly_chart(fig, use_container_width=True)

    with t2:

        st.title("📈 Average Salary by Job Role")

        role_salary = (
            jobs.groupby("job_title")["Average Salary"]
            .mean()
            .sort_values(ascending=False)
            .head(15)
            .reset_index()
        )

        fig = px.bar(
            role_salary,
            x="job_title",
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
            title="Top Paying Job Roles",
            title_x=0.4,
            paper_bgcolor="rgba(0,0,0,0)",
            plot_bgcolor="rgba(0,0,0,0)",
            font=dict(color="white"),
            coloraxis_showscale=False
        )

        st.plotly_chart(fig, use_container_width=True)   


    with t3:

        st.title("🌍 Salary by Country")

        country_salary = (
            jobs.groupby("country")["Average Salary"]
            .mean()
            .sort_values(ascending=False)
            .reset_index()
        )

        fig = px.bar(
            country_salary,
            x="country",
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
            title="Average Salary by Country",
            title_x=0.4,
            paper_bgcolor="rgba(0,0,0,0)",
            plot_bgcolor="rgba(0,0,0,0)",
            font=dict(color="white"),
            coloraxis_showscale=False
        )

        st.plotly_chart(fig, use_container_width=True)  


    with t4:

        st.title("🏢 Salary by Industry")

        industry_salary = (
            jobs.groupby("industry")["Average Salary"]
            .mean()
            .sort_values(ascending=False)
            .reset_index()
        )

        fig = px.bar(
            industry_salary,
            x="industry",
            y="Average Salary",
            color="Average Salary",
            text="Average Salary",
            color_continuous_scale="Turbo"
        )

        fig.update_traces(
            texttemplate="$%{y:,.0f}",
            textposition="outside"
        )

        fig.update_layout(
            title="Average Salary by Industry",
            title_x=0.4,
            paper_bgcolor="rgba(0,0,0,0)",
            plot_bgcolor="rgba(0,0,0,0)",
            font=dict(color="white"),
            coloraxis_showscale=False
        )

        st.plotly_chart(fig, use_container_width=True) 


    with t5:

        # st.title("👨‍💼 Salary by Experience Level")

        # exp_salary = (
        #     jobs.groupby("experience_level")["Average Salary"]
        #     .mean()
        #     .reset_index()
        # )

        # fig = px.bar(
        #     exp_salary,
        #     x="experience_level",
        #     y="Average Salary",
        #     color="Average Salary",
        #     text="Average Salary",
        #     color_continuous_scale="Sunset"
        # )

        # fig.update_traces(
        #     texttemplate="$%{y:,.0f}",
        #     textposition="outside"
        # )

        # fig.update_layout(
        #     title="Average Salary by Experience Level",
        #     title_x=0.4,
        #     paper_bgcolor="rgba(0,0,0,0)",
        #     plot_bgcolor="rgba(0,0,0,0)",
        #     font=dict(color="white"),
        #     coloraxis_showscale=False
        # )

        # st.plotly_chart(fig, use_container_width=True)

                

        st.title("👨‍💼 Salary by Experience Level")

        exp_salary = (
            jobs.groupby("experience_level")["Average Salary"]
            .mean()
            .reset_index()
        )

        # ------------------------
        # Bar Chart
        # ------------------------
        fig = px.bar(
            exp_salary,
            x="experience_level",
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
            title={
                "text":"Average Salary by Experience Level",
                "x":0.4
            },
            paper_bgcolor="rgba(0,0,0,0)",
            plot_bgcolor="rgba(0,0,0,0)",
            font=dict(color="white"),
            coloraxis_showscale=False,
            xaxis_title="Experience Level",
            yaxis_title="Average Salary ($)"
        )

        st.plotly_chart(fig, use_container_width=True)

        st.divider()

        # ------------------------
        # Box Plot
        # ------------------------
        st.subheader("📦 Salary Distribution by Experience Level")

        fig2 = px.box(
            jobs,
            x="experience_level",
            y="Average Salary",
            color="experience_level",
            points="outliers",
            color_discrete_sequence=px.colors.qualitative.Set2
        )

        fig2.update_layout(
            title={
                "text":"Salary Distribution by Experience Level",
                "x":0.4
            },
            paper_bgcolor="rgba(0,0,0,0)",
            plot_bgcolor="rgba(0,0,0,0)",
            font=dict(color="white"),
            showlegend=False,
            xaxis_title="Experience Level",
            yaxis_title="Salary ($)"
        )

        fig2.update_traces(
            marker=dict(size=6)
        )

        st.plotly_chart(fig2, use_container_width=True)

        st.divider()


        #Scatter Plot
        
 

        fig = px.scatter(
            jobs,
            x="Average Salary",
            y="experience_level",
            color="experience_level",
            hover_data=[
                "job_title",
                "Average Salary",
                "salary_min_usd",
                "salary_max_usd"
            ],
            size="Average Salary",
            color_discrete_sequence=px.colors.qualitative.Set2
        )

        fig.update_traces(
            marker=dict(
                line=dict(color="white", width=1)
            )
        )

        fig.update_layout(
            title={
                "text":"Salary Distribution by Experience Level",
                "x":0.4
            },
            paper_bgcolor="rgba(0,0,0,0)",
            plot_bgcolor="rgba(0,0,0,0)",
            font=dict(color="white")
        )

        st.plotly_chart(fig, use_container_width=True)



        
           



       







