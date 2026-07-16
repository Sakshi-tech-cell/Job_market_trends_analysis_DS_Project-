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

    salary_page = st.sidebar.radio(
        "💵 Salary Dashboard",
        [
            "Job Role",
            "Experience"
        ]
    )

    st.sidebar.markdown("---")

    st.sidebar.info("""
    Developed By

    **👩‍💻 Sakshi **

    Python | Pandas | Plotly | Streamlit
    """)

    if salary_page == "Job Role":

        # st.title("📈 Average Salary by Job Role")

        role_salary = (
            jobs.groupby("job_title")["Average Salary"]
            .mean()
            .sort_values(ascending=False)
            .head(15)
            .reset_index()
        )

        # fig = px.bar(
        #     role_salary,
        #     x="Average Salary",
        #     y="job_title",
        #     orientation="h",
        #     color="Average Salary",
        #     text="Average Salary",
        #     color_continuous_scale="Viridis"
        # )

        # fig.update_traces(

        #     texttemplate="$%{x:,.0f}",
        #     textposition="outside",

        #     marker_line_color="white",
        #     marker_line_width=1.5,

        #     hovertemplate=
        #     "<b>%{y}</b><br>"
        #     "Average Salary: <b>$%{x:,.0f}</b>"
        #     "<extra></extra>"
        # )

        # fig.update_layout(

        #     title=dict(
        #         text="💼 Top Highest Paying Job Roles",
        #         x=0.3,
        #         font=dict(
        #             size=28,
        #             color="white"
        #         )
        #     ),

        #     xaxis=dict(
        #         title="Average Salary (USD)",
        #         tickprefix="$",
        #         showgrid=True,
        #         gridcolor="rgba(255,255,255,0.15)",
        #         showline=True,
        #         linecolor="white"
        #     ),

        #     yaxis=dict(
        #         title="Job Role",
        #         autorange="reversed",   # Highest salary at the top
        #         showgrid=False,
        #         showline=True,
        #         linecolor="white"
        #     ),

        #     paper_bgcolor="rgba(0,0,0,0)",
        #     plot_bgcolor="rgba(0,0,0,0)",

        #     font=dict(
        #         color="white",
        #         size=14
        #     ),

        #     coloraxis_colorbar=dict(
        #         title="Salary"
        #     ),

        #     height=650,

        #     margin=dict(
        #         t=80,
        #         l=80,
        #         r=30,
        #         b=40
        #     )
        # )

        # st.plotly_chart(fig, use_container_width=True)
        # st.divider()



        ##
        fig = px.scatter(
            role_salary,
            x="Average Salary",
            y="job_title",
            size="Average Salary",
            color="Average Salary",
            color_continuous_scale="Turbo",
            text="Average Salary"
        )

        fig.update_traces(
            texttemplate="$%{x:,.0f}",
            textposition="middle right",
            marker=dict(
                line=dict(color="white", width=1.5),
                size=20
            )
        )

        fig.update_layout(
            title=dict(
            text="📈 Average Salary by Job Role",
            x=0.3,
            font=dict(
                size=30,      # Increase title size (try 30–36)
                color="pink",
                family="Arial Black"
            )
        ),
            paper_bgcolor="rgba(0,0,0,0)",
            plot_bgcolor="rgba(0,0,0,0)",
            font=dict(color="white"),
            coloraxis_showscale=False,
            height=650
        )

        st.plotly_chart(fig, use_container_width=True)


    elif salary_page == "Experience":

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

            title=dict(
                text="🏢 Average Salary by Experience Level",
                x=0.2,
                font=dict(
                    size=30,
                    color="pink",
                    family="Arial Black"
                )
            ),


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
        # st.subheader("📦 Salary Distribution by Experience Level")

        # fig2 = px.box(
        #     jobs,
        #     x="experience_level",
        #     y="Average Salary",
        #     color="experience_level",
        #     points="outliers",
        #     color_discrete_sequence=px.colors.qualitative.Set2
        # )

        # fig2.update_layout(
        #     title={
        #         "text":"Salary Distribution by Experience Level",
        #         "x":0.4
        #     },
        #     paper_bgcolor="rgba(0,0,0,0)",
        #     plot_bgcolor="rgba(0,0,0,0)",
        #     font=dict(color="white"),
        #     showlegend=False,
        #     xaxis_title="Experience Level",
        #     yaxis_title="Salary ($)"
        # )

        # fig2.update_traces(
        #     marker=dict(size=6)
        # )

        # st.plotly_chart(fig2, use_container_width=True)

        # st.divider()


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

            title=dict(
                text="📦 Salary Distribution by Experience Level",
                x=0.2,
                font=dict(
                    size=30,
                    color="pink",
                    family="Arial Black"
                )
            ),

            paper_bgcolor="rgba(0,0,0,0)",
            plot_bgcolor="rgba(0,0,0,0)",
            font=dict(color="white")
        )

        st.plotly_chart(fig, use_container_width=True)



        
           



       







