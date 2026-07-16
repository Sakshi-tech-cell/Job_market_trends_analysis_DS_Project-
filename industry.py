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

        # st.metric(
        #     "Industries",
        #     jobs["industry"].nunique()
        # )

        # industry = (
        #     jobs["industry"]
        #     .value_counts()
        #     .reset_index()
        # )

        # industry.columns = ["Industry","Jobs"]

        # fig = px.bar(
        #     industry,
        #     x="Industry",
        #     y="Jobs",
        #     color="Jobs",
        #     text="Jobs",
        #     color_continuous_scale="Turbo"
        # )

        # fig.update_traces(
        #     textposition="outside",
        #     marker_line_color="white",
        #     marker_line_width=1.5,
        #     hovertemplate=
        #     "<b>%{x}</b><br>Total Jobs : %{y}<extra></extra>"
        # )

        # fig.update_layout(

        #     title={
        #         "text":"🏢 Industry-wise Jobs",
        #         "x":0.5
        #     },

        #     paper_bgcolor="rgba(0,0,0,0)",
        #     plot_bgcolor="rgba(0,0,0,0)",

        #     font=dict(color="white"),

        #     coloraxis_showscale=False,

        #     height=600
        # )

        # st.plotly_chart(fig,use_container_width=True)

        st.metric(
            "🏢 Industries",
            jobs["industry"].nunique()
        )

        industry = (
            jobs["industry"]
            .value_counts()
            .reset_index()
        )

        industry.columns = ["Industry", "Jobs"]

        # Sort by jobs (largest first)
        industry = industry.sort_values("Jobs", ascending=False)

        fig = px.pie(
            industry,
            names="Industry",
            values="Jobs",
            hole=0.55,
            color="Industry",
            color_discrete_sequence=px.colors.qualitative.Prism
        )

        fig.update_traces(

            textposition="outside",
            textinfo="percent+label",

            pull=[0.08 if i == 0 else 0 for i in range(len(industry))],

            marker=dict(
                line=dict(
                    color="white",
                    width=2
                )
            ),

            hovertemplate=
            "<b>%{label}</b><br>"
            "Jobs: <b>%{value}</b><br>"
            "Share: <b>%{percent}</b>"
            "<extra></extra>"
        )

        fig.update_layout(

            title=dict(
                text="🥧 Industry-wise Job Opportunities and Job Share",
                x=0.2,
                font=dict(
                    size=28,
                    color="white"
                )
            ),

            legend=dict(
                title="Industry",
                orientation="v",
                x=1.02,
                y=0.5,
                bgcolor="rgba(0,0,0,0)",
                font=dict(size=12, color="white")
            ),

            paper_bgcolor="rgba(0,0,0,0)",
            plot_bgcolor="rgba(0,0,0,0)",

            font=dict(
                color="white",
                size=14
            ),

            margin=dict(
                t=80,
                l=20,
                r=120,
                b=20
            ),

            height=600,

          #  uniformtext_minsize=11,
           # uniformtext_mode="hide"
        )

        st.plotly_chart(fig, use_container_width=True)

    with tab2:
        salary = (
            jobs.groupby("industry")["Average Salary"]
            .mean()
            .sort_values(ascending=False)
            .reset_index()
        )

        fig = px.bar(
            salary,
            x="Average Salary",
            y="industry",
            orientation="h",
            color="Average Salary",
            text="Average Salary",
            color_continuous_scale="Sunset"
        )

        fig.update_traces(

            texttemplate="$%{x:,.0f}",
            textposition="outside",

            marker_line_color="white",
            marker_line_width=1.5,

            hovertemplate=
            "<b>%{y}</b><br>"
            "Average Salary: <b>$%{x:,.0f}</b>"
            "<extra></extra>"
        )

        fig.update_layout(

            title=dict(
                text="💰 Average Salary by Industry",
                x=0.3,
                font=dict(
                    size=28,
                    color="white"
                )
            ),

            xaxis=dict(
                title="Average Salary (USD)",
                tickprefix="$",
                showgrid=True,
                gridcolor="rgba(255,255,255,0.15)",
                showline=True,
                linecolor="white"
            ),

            yaxis=dict(
                title="Industry",
                autorange="reversed",      # Highest salary at top
                showgrid=False,
                showline=True,
                linecolor="white"
            ),

            paper_bgcolor="rgba(0,0,0,0)",
            plot_bgcolor="rgba(0,0,0,0)",

            font=dict(
                color="white",
                size=14
            ),

            coloraxis_colorbar=dict(
                title="Salary"
            ),

            height=600,

            margin=dict(
                t=80,
                l=20,
                r=20,
                b=40
            )
        )

        st.plotly_chart(fig, use_container_width=True)
        st.divider()


         ## 
 
        # fig = px.box(

        #     jobs,

        #     x="industry",

        #     y="Average Salary",

        #     color="industry",

        #     points="all",

        #     color_discrete_sequence=px.colors.qualitative.Set2

        # )

        # fig.update_layout(

        #     title=dict(
        #         text="📦 Salary Distribution by Industry",
        #         x=0.3,
        #         font=dict(
        #             size=28,
        #             color="white"
        #         )
        #     ),

        #     xaxis=dict(
        #         title="Industry",
        #         tickangle=-25,
        #         showgrid=False,
        #         showline=True,
        #         linecolor="white"
        #     ),

        #     yaxis=dict(
        #         title="Average Salary (USD)",
        #         tickprefix="$",
        #         showgrid=True,
        #         gridcolor="rgba(255,255,255,0.15)",
        #         showline=True,
        #         linecolor="white"
        #     ),

        #     paper_bgcolor="rgba(0,0,0,0)",

        #     plot_bgcolor="rgba(0,0,0,0)",

        #     font=dict(color="white"),

        #     showlegend=False

        # )

        # st.plotly_chart(fig,use_container_width=True)  

    with tab3:

        emp = (
        jobs.groupby(["industry", "employment_type"])
            .size()
            .reset_index(name="Jobs")
        )

        fig = px.bar(
            emp,
            x="industry",
            y="Jobs",
            color="employment_type",
            barmode="group",
            text="Jobs",
            color_discrete_sequence=px.colors.qualitative.Set2
        )

        fig.update_traces(

            textposition="outside",

            marker_line_color="white",
            marker_line_width=1.5,

            hovertemplate=
            "<b>Industry:</b> %{x}<br>"
            "<b>Employment:</b> %{fullData.name}<br>"
            "<b>Total Jobs:</b> %{y}"
            "<extra></extra>"
        )

        fig.update_layout(

            title=dict(
                text="👨‍💼 Employment Type by Industry",
                x=0.3,
                font=dict(
                    size=28,
                    color="white"
                )
            ),

            xaxis=dict(
                title="Industry",
                tickangle=-25,
                showgrid=False,
                showline=True,
                linecolor="white"
            ),

            yaxis=dict(
                title="Number of Jobs",
                showgrid=True,
                gridcolor="rgba(255,255,255,0.15)",
                showline=True,
                linecolor="white"
            ),

            legend=dict(
                title="Employment Type",
                orientation="h",
                y=1.10,
                x=1.0,
                bgcolor="rgba(0,0,0,0)",
                font=dict(color="white")
            ),

            paper_bgcolor="rgba(0,0,0,0)",
            plot_bgcolor="rgba(0,0,0,0)",

            font=dict(
                color="white",
                size=14
            ),

           # bargap=0.25,
            #bargroupgap=0.08,

            height=600,

            margin=dict(
                t=100,
                l=40,
                r=20,
                b=80
            )
        )

        st.plotly_chart(fig, use_container_width=True)
        st.divider()


    with tab4:

     # Count jobs by year
        year_jobs = (
            jobs["posted_year"]
            .value_counts()
            .sort_index()
            .reset_index()
        )

        year_jobs.columns = ["Year", "Jobs"]

        # fig = px.line(
        #     year_jobs,
        #     x="Year",
        #     y="Jobs",
        #     markers=True
        # )

        # fig.update_traces(

        #     line=dict(
        #         color="#8A2BE2",
        #         width=4
        #     ),

        #     marker=dict(
        #         size=10,
        #         color="#FF69B4",
        #         line=dict(
        #             color="white",
        #             width=2
        #         )
        #     ),

        #     text=year_jobs["Jobs"],
        #     textposition="top center",

        #     hovertemplate=
        #     "<b>Year:</b> %{x}<br>"
        #     "<b>Total Jobs:</b> %{y:,}"
        #     "<extra></extra>"
        # )

        # fig.update_layout(

        #     title=dict(
        #         text="📈 Year-wise AI & Data Science Job Postings",
        #         x=0.2,
        #         font=dict(
        #             size=28,
        #             color="white"
        #         )
        #     ),

        #     xaxis=dict(
        #         title="Posted Year",
        #         showgrid=False,
        #         showline=True,
        #         linecolor="white",
        #         tickmode="linear"
        #     ),

        #     yaxis=dict(
        #         title="Number of Job Postings",
        #         showgrid=True,
        #         gridcolor="rgba(255,255,255,0.15)",
        #         showline=True,
        #         linecolor="white"
        #     ),

        #     paper_bgcolor="rgba(0,0,0,0)",
        #     plot_bgcolor="rgba(0,0,0,0)",

        #     font=dict(
        #         color="white",
        #         size=14
        #     ),

        #     hovermode="x unified",

        #     height=550,

        #     margin=dict(
        #         t=80,
        #         l=40,
        #         r=20,
        #         b=40
        #     )
        # )

        # st.plotly_chart(fig, use_container_width=True)
        # st.divider()


        ##

        # fig = px.area(
        #     year_jobs,
        #     x="posted_year",
        #     y="Jobs",
        #     color_discrete_sequence=["#00E5FF"]
        # )

        # fig.update_layout(
        #     title="Year-wise Hiring Trend",
        #     title_x=.5,
        #     paper_bgcolor="rgba(0,0,0,0)",
        #     plot_bgcolor="rgba(0,0,0,0)"
        # )

        # st.plotly_chart(fig,use_container_width=True)

        fig = px.area(
            year_jobs,
            x="Year",
            y="Jobs",
            markers=True,
            color_discrete_sequence=["#00E5FF"]
        )

        fig.update_traces(

            line=dict(
                width=4,
                shape="spline"          # Smooth curve
            ),

            marker=dict(
                size=10,
                color="#00E5FF",
                line=dict(
                    color="white",
                    width=2
                )
            ),

            fillcolor="rgba(0,229,255,0.25)",

            text=year_jobs["Jobs"],
            textposition="top center",

            hovertemplate=
            "<b>Year:</b> %{x}<br>"
            "<b>Total Jobs:</b> %{y:,}"
            "<extra></extra>"
        )

        fig.update_layout(

            title=dict(
                text="📈 Year-wise AI & Data Science Job Postings or Hiring Trend",
                x=0.3,
                font=dict(
                    size=28,
                    color="white"
                )
            ),

            xaxis=dict(
                title="Posted Year",
                showgrid=False,
                showline=True,
                linecolor="white",
                tickmode="linear"
            ),

            yaxis=dict(
                title="Number of Jobs",
                showgrid=True,
                gridcolor="rgba(255,255,255,0.15)",
                showline=True,
                linecolor="white"
            ),

            paper_bgcolor="rgba(0,0,0,0)",
            plot_bgcolor="rgba(0,0,0,0)",

            font=dict(
                color="white",
                size=14
            ),

            hovermode="x unified",

            height=550,

            margin=dict(
                t=80,
                l=40,
                r=20,
                b=40
            )
        )

        st.plotly_chart(fig, use_container_width=True)


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
            markers=True,
            color_discrete_sequence=["#FF8C42"]   # Orange
        )

        fig.update_traces(

            line=dict(
                width=4,
                shape="spline"
            ),

            marker=dict(
                size=10,
                color="#FF8C42",
                line=dict(
                    color="white",
                    width=2
                )
            ),

            text=[f"${x:,.0f}" for x in salary_year["Average Salary"]],
            textposition="top center",

            hovertemplate=
            "<b>Year:</b> %{x}<br>"
            "<b>Average Salary:</b> $%{y:,.0f}"
            "<extra></extra>"
        )

        fig.update_layout(

            title=dict(
                text="💰 Average Salary Trend Over Years",
                x=0.3,
                font=dict(
                    size=28,
                    color="white"
                )
            ),

            xaxis=dict(
                title="Posted Year",
                showgrid=False,
                showline=True,
                linecolor="white",
                tickmode="linear"
            ),

            yaxis=dict(
                title="Average Salary (USD)",
                tickprefix="$",
                showgrid=True,
                gridcolor="rgba(255,255,255,0.15)",
                showline=True,
                linecolor="white"
            ),

            paper_bgcolor="rgba(0,0,0,0)",
            plot_bgcolor="rgba(0,0,0,0)",

            font=dict(
                color="white",
                size=14
            ),

            hovermode="x unified",

            height=550,

            margin=dict(
                t=80,
                l=40,
                r=20,
                b=40
            )
        )

        st.plotly_chart(fig, use_container_width=True)
        st.divider()


    with tab6:

                # Create Average Salary
        jobs["Average Salary"] = (
            jobs["salary_min_usd"] +
            jobs["salary_max_usd"]
        ) / 2

        fig = px.scatter(
            jobs,
            x="industry",
            y="company_type",
            size="Average Salary",
            color="Average Salary",
            hover_name="job_title",
            hover_data={
                "Average Salary": ":,.0f",
                "industry": True,
                "company_type": True,
                "city": True,
                "country": True,
                "employment_type": True,
                "experience_level": True
            },
            color_continuous_scale="Turbo",
            size_max=35
        )

        fig.update_traces(

            marker=dict(
                line=dict(
                    color="white",
                    width=1.5
                ),
                opacity=0.85
            ),

            hovertemplate=
            "<b>💼 %{hovertext}</b><br><br>"
            "🏢 Company Type: %{y}<br>"
            "🏭 Industry: %{x}<br>"
            "💰 Salary: $%{marker.size:,.0f}<br>"
            "🌍 %{customdata[2]}, %{customdata[1]}<br>"
            "📄 %{customdata[3]}<br>"
            "⭐ %{customdata[4]}"
            "<extra></extra>"
        )

        fig.update_layout(

            title=dict(
                text="🏢 Company Type vs Industry vs Job Salary",
                x=0.3,
                font=dict(
                    size=28,
                    color="white"
                )
            ),

            xaxis=dict(
                title="Industry",
                tickangle=-25,
                showgrid=False,
                showline=True,
                linecolor="white"
            ),

            yaxis=dict(
                title="Company Type",
                showgrid=False,
                showline=True,
                linecolor="white"
            ),

            paper_bgcolor="rgba(0,0,0,0)",
            plot_bgcolor="rgba(0,0,0,0)",

            font=dict(
                color="white",
                size=14
            ),

            coloraxis_colorbar=dict(
                title="Salary"
            ),

            height=650
        )

        st.plotly_chart(fig, use_container_width=True)

        result = jobs[
            [
                "company_type",
                "industry",
                "job_title",
                "city",
                "country",
                "Average Salary",
                "employment_type",
                "experience_level"
            ]
        ].sort_values("Average Salary", ascending=False)

        st.dataframe(
            result,
            use_container_width=True,
            hide_index=True
        )
        st.divider()

    


        ##
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

        st.sidebar.markdown("---")

        st.sidebar.info("""
        Developed By

        **👩‍💻 Sakshi**

        Python | Pandas | Plotly | Streamlit
        """)














