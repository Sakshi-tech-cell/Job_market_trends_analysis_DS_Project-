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
        "📊 Overview"
    ])

    with t1:

        st.metric(
        "Countries",
        jobs["country"].nunique()
        )

        country_jobs = (jobs["country"].value_counts().reset_index())

        country_jobs.columns=["Country","Jobs"]

    

        # fig = px.bar(
        #     country_jobs,
        #     x="Country",
        #     y="Jobs",
        #     color="Jobs",
        #     text="Jobs",
        #     color_continuous_scale="Turbo"
        # )

        # fig.update_layout(
        #     title="Country-wise AI Jobs",
        #     title_x=0.4,
        #     paper_bgcolor="rgba(0,0,0,0)",
        #     plot_bgcolor="rgba(0,0,0,0)",
        #     font=dict(color="white"),
        #     coloraxis_showscale=True
        # )

        # st.plotly_chart(fig,use_container_width=True)

        fig = px.bar(
            country_jobs,
            x="Country",
            y="Jobs",
            color="Jobs",
            text="Jobs",
            color_continuous_scale="Blues"
        )

        fig.update_traces(
            texttemplate="%{y:,}",
            textposition="outside",

            marker_line_color="white",
            marker_line_width=1.5,

            hovertemplate=
            "<b>🌍 %{x}</b><br>"
            "💼 Total Jobs: %{y:,}<extra></extra>"
        )

        fig.update_layout(

            title=dict(
                text="🌍 Country-wise AI Job Opportunities",
                x=0.3,
                font=dict(
                    size=28,
                    color="white",
                    family="Arial"
                )
            ),

            xaxis_title="Country",
            yaxis_title="Number of AI Jobs",

            paper_bgcolor="rgba(0,0,0,0)",
            plot_bgcolor="rgba(0,0,0,0)",

            font=dict(
                color="white",
                size=14
            ),

            xaxis=dict(
                tickangle=-30,
                showgrid=False,
                showline=True,
                linecolor="white"
            ),

            yaxis=dict(
                showgrid=True,
                gridcolor="rgba(255,255,255,0.12)",
                zeroline=False,
                showline=True,
                linecolor="white"
            ),

            coloraxis_colorbar=dict(title="Jobs"),
            height=550,
            margin=dict(t=80,l=40,r=20,b=70)
        )

        st.plotly_chart(fig, use_container_width=True)
        st.divider()


        ##
        fig = px.pie(
            country_jobs,
            names="Country",
            values="Jobs",
            hole=0.5,
            color_discrete_sequence=px.colors.qualitative.Pastel
        )

        fig.update_traces(

            textinfo="percent+label",
            textposition="inside",

            marker=dict(
                line=dict(color="white", width=2)
            ),

            pull=[0.06 if i == 0 else 0 for i in range(len(country_jobs))],

            hovertemplate=
            "<b>%{label}</b><br>"
            "AI Jobs : %{value:,}<br>"
            "Percentage : %{percent}<extra></extra>"
        )

        fig.update_layout(

            title=dict(
                text="🌍 Country-wise AI Jobs Distribution in Percentage",
                x=0.3,
                font=dict(
                    size=30,
                    color="pink"
                )
            ),

            paper_bgcolor="rgba(0,0,0,0)",
            plot_bgcolor="rgba(0,0,0,0)",

            font=dict(
                color="white",
                size=14
            ),

            legend=dict(
                title="Country",
                orientation="h",
                x=1.02,
                y=0.6,
                bgcolor="rgba(0,0,0,0)"
            ),

            margin=dict(
                t=70,
                l=20,
                r=20,
                b=20
            ),

            height=550
        )

        st.plotly_chart(fig, use_container_width=True)

        st.divider() 

        ##
        #st.line_chart(country,x="year",y="total_ai_jobs",color="country")
        fig = px.line(
            country,
            x="year",
            y="total_ai_jobs",
            color="country",
            markers=True,
            hover_data=["top_skill"]   # Show top skill
        )

        fig.update_traces(
            line=dict(width=3),
            marker=dict(size=8),
            hovertemplate=
            "<b>%{fullData.name}</b><br>"
            "Year: %{x}<br>"
            "Total Jobs: %{y:,}<br>"
            "Top Skill: %{customdata[0]}<extra></extra>"

        )

        fig.update_layout(

            title={
                "text":"📈 Year-wise AI Jobs by Country",
                "x":0.3,
                "font":dict(size=30, color="white")
            },

            paper_bgcolor="rgba(0,0,0,0)",
            plot_bgcolor="rgba(0,0,0,0)",

            font=dict(
                color="white",
                size=14
            ),

            xaxis=dict(
                title="Year",
                showgrid=False
            ),

            yaxis=dict(
                title="Total AI Jobs",
                gridcolor="rgba(255,255,255,0.15)"
            ),

            legend=dict(
                title="Country",
                bgcolor="rgba(0,0,0,0)"
            ),

            hovermode="x unified",
            height=500
        )

        st.plotly_chart(fig, use_container_width=True)




    with t2:

        salary = (
            jobs.groupby("country")["Average Salary"]
            .mean()
            .sort_values(ascending=False)
            .reset_index()
        )

        #scatter plot

        fig = px.scatter(
            salary,
            x="country",
            y="Average Salary",
            size="Average Salary",
            color="Average Salary",
            text="Average Salary",
            color_continuous_scale="Inferno",
            size_max=45
        )

        fig.update_traces(
            texttemplate="$%{y:,.0f}",
            textposition="top center",
            marker=dict(
                line=dict(color="white", width=2)
            ),
            hovertemplate=
            "<b>%{x}</b><br>"
            "Average Salary: <b>$%{y:,.0f}</b>"
            "<extra></extra>"
        )

        fig.update_layout(
            title=dict(
                text="💰 Salary Comparison Across Countries",
                x=0.3,
                font=dict(size=30, color="white")
            ),
            paper_bgcolor="rgba(0,0,0,0)",
            plot_bgcolor="rgba(0,0,0,0)",
            font=dict(color="white"),
            coloraxis_showscale=False,
            xaxis_title="Country",
            yaxis_title="Average Salary (USD)",
            height=600
        )

        st.plotly_chart(fig, use_container_width=True)


    with t3:

        remote = (
            country.groupby("country")["remote_percentage"]
            .mean()
            .sort_values(ascending=False)
            .reset_index()
        )

        fig = px.bar(
            remote,
            # x="country",
            # y="remote_percentage",
            x="remote_percentage",
            y="country",
            orientation="h",
            color="remote_percentage",
            text="remote_percentage",
            color_continuous_scale="Purples"
        )

        fig.update_traces(
            texttemplate="%{x:.1f}%",
            textposition="outside",

            marker_line_color="white",
            marker_line_width=1.5,

            hovertemplate=
            "<b>%{y}</b><br>"
            "Remote Jobs: <b>%{x:.1f}%</b>"
            "<extra></extra>"
        )

        fig.update_layout(

            title=dict(
                text="🏠 Remote Jobs Percentage by Country",
                x=0.3,
                font=dict(
                    size=28,
                    color="white"
                )
            ),

            xaxis=dict(
                title="Remote Jobs (%)",
                ticksuffix="%",
                showgrid=True,
                gridcolor="rgba(255,255,255,0.15)",
                showline=True,
                linecolor="white"

            ),

            yaxis=dict(
                title="Country",
                tickangle=-20,
                showgrid=False,
                showline=True,
                linecolor="white",
                autorange="reversed"      # Highest value at top

            ),

            paper_bgcolor="rgba(0,0,0,0)",
            plot_bgcolor="rgba(0,0,0,0)",

            font=dict(
                color="white",
                size=14
            ),

            coloraxis_colorbar=dict(
                title="Remote %"
            ),

            height=550,

            margin=dict(t=80,l=30,r=20,b=40)
        )

        st.plotly_chart(fig, use_container_width=True)
        st.divider() 

        #

        # fig = px.pie(
        #     remote,
        #     names="country",
        #     values="remote_percentage",
        #     hole=0.45,
        #     color_discrete_sequence=px.colors.qualitative.Set3
        # )

        # fig.update_traces(
        #     textinfo="percent+label",
        #     marker=dict(line=dict(color="white", width=2))
        # )

        # fig.update_layout(
        #     title=dict(
        #         text="🌍 Remote Work Share by Country",
        #         x=0.3,
        #         font=dict(size=28, color="white")
        #     ),
        #     paper_bgcolor="rgba(0,0,0,0)",
        #     plot_bgcolor="rgba(0,0,0,0)",
        #     font=dict(color="white"),

        #     legend=dict(
        #     title="Country",
        #     orientation="h",
        #     x=1.02,
        #     y=0.6,
        #     bgcolor="rgba(0,0,0,0)"
        #     ),

        #     margin=dict(
        #         t=70,
        #         l=20,
        #         r=20,
        #         b=20
        #     ),

        #     height=550
        # )

        # st.plotly_chart(fig, use_container_width=True)




    with t4:
        # skill = (
        # country.groupby("top_skill")
        # .size()
        # .reset_index(name="Count")
        # )

        # fig = px.bar(
        # skill,
        # x="top_skill",
        # y="Count",
        # color="Count",
        # text="Count",
        # color_continuous_scale="Turbo"
        # )

        # fig.update_layout(
        # title="Top Skills Across Countries",
        # title_x=.5,
        # paper_bgcolor="rgba(0,0,0,0)",
        # plot_bgcolor="rgba(0,0,0,0)",
        # font=dict(color="white")
        # )

        # st.plotly_chart(fig,use_container_width=True)

        skill = (
            country.groupby("top_skill")
            .agg(
                Count=("country", "count"),
                Countries=("country", lambda x: ", ".join(sorted(x.unique())))
            )
            .reset_index()
            .sort_values("Count", ascending=False)
        )

        fig = px.bar(
            skill,
            x="top_skill",
            y="Count",
            color="Count",
            text="Count",
            custom_data=["Countries"],      # <-- Pass countries
            color_continuous_scale="Delta"
        )

        fig.update_traces(

            textposition="outside",

            marker_line_color="white",
            marker_line_width=1.5,

            hovertemplate=
             "<b>Skill:</b> %{x}<br>"
            "<b>Countries:</b> %{customdata[0]}<br>"
            "<b>Total Countries:</b> %{y}"
            "<extra></extra>"
        )

        fig.update_layout(

            title=dict(
                text="🚀 Top AI Skills Across Countries",
                x=0.3,
                font=dict(
                    size=28,
                    color="white"
                )
            ),

            xaxis=dict(
                title="Top AI Skill",
                tickangle=-20,
                showgrid=False,
                showline=True,
                linecolor="white"
            ),

            yaxis=dict(
                title="Number of Countries",
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

            coloraxis_colorbar=dict(
                title="Count"
            ),

            height=550,

            margin=dict(
                t=80,
                l=30,
                r=20,
                b=40
            )
        )
        
        st.plotly_chart(fig, use_container_width=True)
        st.dataframe(
            country[["country", "top_skill"]]
        )
        st.divider() 

        ##

        # Count skills
        skill = (
            country.groupby("top_skill")
            .size()
            .reset_index(name="Count")
            .sort_values("Count", ascending=False)
        )

        fig = px.pie(
            skill,
            names="top_skill",
            values="Count",
            hole=0.45,
            color="top_skill",
            color_discrete_sequence=px.colors.qualitative.Safe
        )

        fig.update_traces(

            textposition="inside",
            textinfo="percent+label",

            pull=[0.08 if i == 0 else 0 for i in range(len(skill))],

            marker=dict(
                line=dict(
                    color="white",
                    width=2
                )
            ),

            hovertemplate=
            "<b>Skill:</b> %{label}<br>"
            "<b>Countries:</b> %{value}<br>"
            "<b>Percentage:</b> %{percent}<extra></extra>"
        )

        fig.update_layout(

            title=dict(
                text="🌍 Country-wise Top AI Skills",
                x=0.3,
                font=dict(
                    size=30,
                    color="white"
                )
            ),

            legend=dict(
                title="Top Skill",
                orientation="v",
                bgcolor="rgba(0,0,0,0)",
                font=dict(size=13, color="white")
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
                r=20,
                b=20
            ),

            height=550
        )

        st.plotly_chart(fig, use_container_width=True)



    with t5:

        # city_jobs = (
        #     jobs["city"]
        #     .value_counts()
        #     .reset_index()
        # )

        # city_jobs.columns = ["City", "Jobs"]

        # fig = px.bar(
        #     city_jobs,
        #     x="City",
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
        #     "<b>🏙 City:</b> %{x}<br>"
        #     "<b>AI Jobs:</b> %{y}<extra></extra>"
        # )

        # fig.update_layout(

        #     title=dict(
        #         text="🏙 City-wise AI Job Opportunities",
        #         x=0.5,
        #         font=dict(
        #             size=24,
        #             color="white"
        #         )
        #     ),

        #     xaxis=dict(
        #         title="City",
        #         tickangle=-35,
        #         showgrid=False,
        #         showline=True,
        #         linecolor="white"
        #     ),

        #     yaxis=dict(
        #         title="Number of Jobs",
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

        #     coloraxis_colorbar=dict(
        #         title="Jobs"
        #     ),

        #     height=550,

        #     margin=dict(t=80,l=40,r=20,b=80)
        # )

        # st.plotly_chart(fig, use_container_width=True)
        # st.divider() 

        ## Using Scatter plot

        city_jobs = (
            jobs["city"]
            .value_counts()
            .reset_index()
        )

        city_jobs.columns = ["City", "Jobs"]

        fig = px.scatter(
            city_jobs,
            x="City",
            y="Jobs",
            size="Jobs",
            color="Jobs",
            text="Jobs",
            color_continuous_scale="Turbo",
            size_max=40
        )

        fig.update_traces(

            textposition="top center",

            marker=dict(
                line=dict(
                    color="white",
                    width=2
                ),
                opacity=0.85
            ),

            hovertemplate=
            "<b>🏙 City:</b> %{x}<br>"
            "<b>Total Jobs:</b> %{y}<extra></extra>"
        )

        fig.update_layout(

            title=dict(
                text="📍 City-wise AI Job Distribution",
                x=0.3,
                font=dict(
                    size=28,
                    color="white"
                )
            ),

            xaxis=dict(
                title="City",
                tickangle=-35,
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

            paper_bgcolor="rgba(0,0,0,0)",
            plot_bgcolor="rgba(0,0,0,0)",

            font=dict(
                color="white",
                size=14
            ),

            coloraxis_colorbar=dict(
                title="Jobs"
            ),

            height=600
        )

        st.plotly_chart(fig, use_container_width=True)
        st.divider() 



        ##
        city_salary = (
            jobs.groupby("city")["Average Salary"]
            .mean()
            .sort_values(ascending=False)
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

        fig.update_traces(

            texttemplate="$%{y:,.0f}",
            textposition="outside",

            marker_line_color="white",
            marker_line_width=1.5,

            hovertemplate=
            "<b>🏙 City:</b> %{x}<br>"
            "<b>Average Salary:</b> $%{y:,.0f}<extra></extra>"
        )

        fig.update_layout(

            title=dict(
                text="💰 Average Salary by City",
                x=0.3,
                font=dict(
                    size=28,
                    color="white"
                )
            ),

            xaxis=dict(
                title="City",
                tickangle=-35,
                showgrid=False,
                showline=True,
                linecolor="white"
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

            coloraxis_colorbar=dict(
                title="Salary"
            ),

            height=600,

            margin=dict(
                t=80,
                l=40,
                r=20,
                b=100
            )
        )

        st.plotly_chart(fig, use_container_width=True)
        st.divider() 


        ##

        # fig = px.pie(
        #     city_jobs,
        #     names="City",
        #     values="Jobs",
        #     hole=.45
        # )

        # fig.update_layout(
        #     title="City-wise Job Distribution",
        #     title_x=.5
        # )

        # st.plotly_chart(fig,use_container_width=True)

        fig = px.pie(
            city_jobs,
            names="City",
            values="Jobs",
            hole=0.45,
            color="City",
            color_discrete_sequence=px.colors.qualitative.Bold
        )

        fig.update_traces(

            textposition="inside",
            textinfo="percent+label",

            pull=[0.08 if i == 0 else 0 for i in range(len(city_jobs))],

            marker=dict(
                line=dict(
                    color="white",
                    width=2
                )
            ),

            hovertemplate=
            "<b>🏙 City:</b> %{label}<br>"
            "<b>Total Jobs:</b> %{value}<br>"
            "<b>Share:</b> %{percent}<extra></extra>"
        )

        fig.update_layout(

            title=dict(
                text="🏙 City-wise AI Job Distribution",
                x=0.3,
                font=dict(
                    size=28,
                    color="white"
                )
            ),

            legend=dict(
                title="City",
                orientation="v",
                bgcolor="rgba(0,0,0,0)",
                font=dict(
                    size=13,
                    color="white"
                )
            ),

            paper_bgcolor="rgba(0,0,0,0)",
            plot_bgcolor="rgba(0,0,0,0)",

            font=dict(
                color="white",
                size=14
            ),

            height=600,

            margin=dict(
                t=80,
                l=20,
                r=20,
                b=20
            )
        )

        st.plotly_chart(fig, use_container_width=True)
        

    with t6:


# ---------------------------
# Load Dataset
# ---------------------------
            #jobs = pd.read_csv("ai_jobs.csv")

            # Average Salary
        jobs["Average Salary"] = (
            jobs["salary_min_usd"] +
            jobs["salary_max_usd"]
        ) / 2

        st.title("🌍 Country → City → Job Explorer")

        # ===========================
        # Select Country
        # ===========================
        country = st.selectbox(
            "🌍 Select Country",
            sorted(jobs["country"].dropna().unique())
        )

        # ===========================
        # Select City
        # ===========================
        city = st.selectbox(
            "🏙 Select City",
            sorted(
                jobs.loc[
                    jobs["country"] == country,
                    "city"
                ].dropna().unique()
            )
        )

        # ===========================
        # Filter Dataset
        # ===========================
        filtered = jobs[
            (jobs["country"] == country) &
            (jobs["city"] == city)
        ]

        st.divider()

        # ===========================
        # Metrics
        # ===========================
        c1, c2, c3 = st.columns(3)

        c1.metric(
            "💼 Total Jobs",
            len(filtered)
        )

        c2.metric(
            "📋 Job Titles",
            filtered["job_title"].nunique()
        )

        c3.metric(
            "💰 Avg Salary",
            f"${filtered['Average Salary'].mean():,.0f}"
        )

        st.divider()

        # ===========================
        # Job Count Chart
        # ===========================
        job_count = (
            filtered["job_title"]
            .value_counts()
            .reset_index()
        )

        job_count.columns = ["Job Title", "Count"]

        fig = px.bar(
            job_count,
            x="Job Title",
            y="Count",
            color="Count",
            text="Count",
            color_continuous_scale="Teal"
        )

        fig.update_traces(
            textposition="outside",
            marker_line_color="white",
            marker_line_width=1.5,
            hovertemplate=
            "<b>%{x}</b><br>"
            "Available Jobs: %{y}<extra></extra>"
        )

        fig.update_layout(

            title=dict(
                text=f"💼 Jobs Available in {city}, {country}",
                x=0.3,
                font=dict(
                    size=24,
                    color="white"
                )
            ),

            paper_bgcolor="rgba(0,0,0,0)",
            plot_bgcolor="rgba(0,0,0,0)",

            font=dict(
                color="white",
                size=14
            ),

            xaxis=dict(
                tickangle=-20,
                showgrid=False,
                showline=True,
                linecolor="white"
            ),

            yaxis=dict(
                showgrid=True,
                gridcolor="rgba(255,255,255,0.15)",
                showline=True,
                linecolor="white"
            ),

            coloraxis_showscale=False,

            height=500
        )

        st.plotly_chart(fig, use_container_width=True)

        st.divider()

        # ===========================
        # Salary Details Table
        # ===========================
        st.subheader("📋 Available Jobs & Salary Details")

        display = filtered[
            [
                "job_title",
                "salary_min_usd",
                "salary_max_usd",
                "Average Salary"
            ]
        ].copy()

        display.columns = [
            "Job Title",
            "Minimum Salary ($)",
            "Maximum Salary ($)",
            "Average Salary ($)"
        ]

        st.dataframe(
            display,
            use_container_width=True,
            hide_index=True
        )

        st.sidebar.markdown("---")

        st.sidebar.info("""
        Developed By

        **👩‍💻 Sakshi**

        Python | Pandas | Plotly | Streamlit
        """)



        # heat = pd.crosstab(
        #     country["country"],
        #     country["top_skill"]
        # )

        # fig = px.imshow(
        #     heat,
        #     text_auto=True,
        #     color_continuous_scale="Viridis",
        #     aspect="auto"
        # )

        # fig.update_layout(
        #     title="Country vs Top Skill",
        #     title_x=.5,
        #     paper_bgcolor="rgba(0,0,0,0)",
        #     plot_bgcolor="rgba(0,0,0,0)",
        #     font=dict(color="white"),
        #     height=500
        # )

        # st.plotly_chart(fig,use_container_width=True)    






















