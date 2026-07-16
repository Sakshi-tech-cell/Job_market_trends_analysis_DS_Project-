import streamlit as st
import pandas as pd
import plotly.express as px

def show():

    jobs = pd.read_csv("ai_jobs.csv")

    skills = pd.read_csv("skills_demand.csv")

    roles = pd.read_csv("job_title_mapping.csv")

    #country = pd.read_csv("country_ai_trends.csv")

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
            "🏠 Total Work Modes",
            jobs["remote_type"].nunique()
        )

        remote = (
            jobs["remote_type"]
            .value_counts()
            .reset_index()
        )

        remote.columns = ["Work Mode", "Jobs"]

        # Calculate percentage
        remote["Percentage"] = (
            remote["Jobs"] / remote["Jobs"].sum() * 100
        ).round(1)

        fig = px.bar(
            remote,
            x="Work Mode",
            y="Jobs",
            color="Jobs",
            text="Jobs",
            color_continuous_scale="YlGnBu"
        )

        fig.update_traces(

            textposition="outside",

            marker_line_color="white",
            marker_line_width=2,

            hovertemplate=
            "<b>%{x}</b><br>"
            "Jobs: <b>%{y}</b><br>"
            "Share: <b>%{customdata[0]}%</b>"
            "<extra></extra>",

            customdata=remote[["Percentage"]]
        )

        fig.update_layout(

            title=dict(
                text="🏠 Remote vs Hybrid vs On-site Jobs",
                x=0.3,
                font=dict(
                    size=28,
                    color="white"
                )
            ),

            xaxis=dict(
                title="Work Mode",
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
        


        ##
        # fig = px.pie(
        #     remote,
        #     names="Work Mode",
        #     values="Jobs",
        #     hole=0.55,
        #     color="Work Mode",
        #     color_discrete_sequence=px.colors.qualitative.Set2
        # )

        # fig.update_traces(

        #     textposition="outside",
        #     textinfo="percent+label",

        #     pull=[0.08 if i == 0 else 0 for i in range(len(remote))],

        #     marker=dict(
        #         line=dict(
        #             color="white",
        #             width=2
        #         )
        #     ),

        #     hovertemplate=
        #     "<b>%{label}</b><br>"
        #     "Jobs: <b>%{value}</b><br>"
        #     "Percentage: <b>%{percent}</b>"
        #     "<extra></extra>"
        # )

        # # Show total jobs in center
        # fig.add_annotation(
        #     text=f"<b>{remote['Jobs'].sum()}</b><br>Total Jobs",
        #     x=0.5,
        #     y=0.5,
        #     showarrow=False,
        #     font=dict(
        #         size=20,
        #         color="white"
        #     )
        # )

        # fig.update_layout(

        #     title=dict(
        #         text="🏠 Work Mode Distribution",
        #         x=0.3,
        #         font=dict(
        #             size=28,
        #             color="white"
        #         )
        #     ),

        #     legend=dict(
        #         title="Work Mode",
        #         orientation="v",
        #         x=1.02,
        #         y=0.5,
        #         bgcolor="rgba(0,0,0,0)",
        #         font=dict(
        #             size=13,
        #             color="white"
        #         )
        #     ),

        #     paper_bgcolor="rgba(0,0,0,0)",
        #     plot_bgcolor="rgba(0,0,0,0)",

        #     font=dict(
        #         color="white",
        #         size=14
        #     ),

        #     margin=dict(
        #         t=80,
        #         l=20,
        #         r=120,
        #         b=20
        #     ),

        #     height=600,

        #     uniformtext_minsize=11,
        #     uniformtext_mode="hide"
        # )

        # st.plotly_chart(fig, use_container_width=True)


    with tab2:

        country = (
            jobs.groupby(["country", "remote_type"])
            .size()
            .reset_index(name="Jobs")
        )

        fig = px.bar(
            country,
            x="country",
            y="Jobs",
            color="remote_type",
            barmode="group",
            text="Jobs",
            color_discrete_sequence=px.colors.qualitative.Set2
        )

        fig.update_traces(

            textposition="outside",

            marker_line_color="white",
            marker_line_width=1.5,

            hovertemplate=
            "<b>%{x}</b><br>"
            "Work Mode: %{fullData.name}<br>"
            "Jobs: %{y}<extra></extra>"
        )

        fig.update_layout(

            title=dict(
                text="🌍 Remote, Hybrid & On-site Jobs by Country",
                x=0.2,
                font=dict(
                    size=28,
                    color="white"
                )
            ),

            xaxis=dict(
                title="Country",
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
                title="Work Mode",
                orientation="h",
                y=0.6,
                x=1.0,
                bgcolor="rgba(0,0,0,0)"
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
        st.divider()


        ##
        remote_country = (
            jobs[jobs["remote_type"] == "Remote"]["country"]
            .value_counts()
            .reset_index()
        )

        remote_country.columns = ["Country", "Jobs"]

        fig = px.pie(
            remote_country,
            names="Country",
            values="Jobs",
            hole=0.55,
            color="Country",
            color_discrete_sequence=px.colors.qualitative.Antique
        )

        fig.update_traces(

            textinfo="percent+label",
            textposition="outside",

            # Highlight largest slice
            pull=[0.08 if i == 0 else 0 for i in range(len(remote_country))],

            marker=dict(
                line=dict(
                    color="white",
                    width=2
                )
            ),

            hovertemplate=
            "<b>%{label}</b><br>"
            "Remote Jobs: <b>%{value}</b><br>"
            "Share: <b>%{percent}</b>"
            "<extra></extra>"
        )

        # Center text
        fig.add_annotation(
            x=0.5,
            y=0.5,
            text=f"<b>{remote_country['Jobs'].sum()}</b><br>Remote Jobs",
            showarrow=False,
            font=dict(
                size=22,
                color="white"
            )
        )

        fig.update_layout(

            title=dict(
                text="🌍 Country Share of Remote Jobs",
                x=0.2,
                font=dict(
                    size=28,
                    color="white"
                )
            ),

            legend=dict(
                title="Country",
                orientation="v",
                x=1.02,
                y=0.5,
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

            uniformtext_minsize=11,
            uniformtext_mode="hide",

            margin=dict(
                t=80,
                l=20,
                r=120,
                b=20
            ),

            height=600
        )

        st.plotly_chart(fig, use_container_width=True)


    with tab3:

        trend = (
            jobs.groupby(["posted_year", "remote_type"])
            .size()
            .reset_index(name="Jobs")
        )

        fig = px.line(
            trend,
            x="posted_year",
            y="Jobs",
            color="remote_type",
            markers=True,
            color_discrete_sequence=px.colors.qualitative.Bold
        )

        fig.update_traces(

            line=dict(
                width=4,
                shape="spline"
            ),

            marker=dict(
                size=10,
                line=dict(
                    color="white",
                    width=2
                )
            ),

            text=trend["Jobs"],
            textposition="top center",

            hovertemplate=
            "<b>Year:</b> %{x}<br>"
            "<b>Work Mode:</b> %{fullData.name}<br>"
            "<b>Total Jobs:</b> %{y}<extra></extra>"
        )

        fig.update_layout(

            title=dict(
                text="📈 Remote Work Trend Over Time",
                x=0.3,
                font=dict(
                    size=28,
                    color="white"
                )
            ),

            xaxis=dict(
                title="Posted Year",
                tickmode="linear",
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
                title="Work Mode",
                orientation="v",
                y=0.7,
                x=1.0,
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

            hovermode="x unified",

            height=600,

            margin=dict(
                t=90,
                l=40,
                r=20,
                b=40
            )
        )

        st.plotly_chart(fig, use_container_width=True)
        st.divider()



        ##
        fig = px.area(
            trend,
            x="posted_year",
            y="Jobs",
            color="remote_type",
            line_group="remote_type",
            markers=True,
            color_discrete_sequence=px.colors.qualitative.Set2
        )

        fig.update_layout(
            title="📊 Work Mode Trend Over Time",
            title_x=0.35,
            paper_bgcolor="rgba(0,0,0,0)",
            plot_bgcolor="rgba(0,0,0,0)",
            font=dict(color="white"),
            legend_title="Work Mode",
            height=600
        )

        st.plotly_chart(fig, use_container_width=True)
                


    with tab4:
        import plotly.graph_objects as go

        salary = (
            jobs.groupby("remote_type")["Average Salary"]
            .mean()
            .sort_values()
            .reset_index()
        )

        fig = go.Figure()

        # Lollipop stems
        for i, row in salary.iterrows():
            fig.add_trace(
                go.Scatter(
                    x=[0, row["Average Salary"]],
                    y=[row["remote_type"], row["remote_type"]],
                    mode="lines",
                    line=dict(color="rgba(255,255,255,0.35)", width=5),
                    hoverinfo="skip",
                    showlegend=False
                )
            )

        # Lollipop heads
        fig.add_trace(
            go.Scatter(
                x=salary["Average Salary"],
                y=salary["remote_type"],
                mode="markers+text",
                text=[f"${x:,.0f}" for x in salary["Average Salary"]],
                textposition="middle right",
                textfont=dict(
                    size=10,
                    color="white"
                ),
                marker=dict(
                    size=26,
                    color=salary["Average Salary"],
                    colorscale="Turbo",
                    line=dict(
                        color="white",
                        width=2
                    ),
                    showscale=False
                ),
                hovertemplate=
                "<b>%{y}</b><br>"
                "Average Salary: <b>$%{x:,.0f}</b>"
                "<extra></extra>"
            )
        )

        fig.update_layout(

            title=dict(
                text="💰 Average Salary by Work Mode",
                x=0.3,
                font=dict(
                    size=26,
                    color="white"
                )
            ),

            xaxis=dict(
                title="Average Salary (USD)",
                tickprefix="$",
                showgrid=True,
                gridcolor="rgba(255,255,255,0.12)",
                zeroline=False,
                showline=True,
                linecolor="white"
            ),

            yaxis=dict(
                title="Work Mode",
                showgrid=False,
                showline=True,
                linecolor="white"
            ),

            paper_bgcolor="rgba(0,0,0,0)",
            plot_bgcolor="rgba(0,0,0,0)",

            font=dict(
                color="white",
                family="Arial",
                size=14
            ),

            height=550,

            margin=dict(
                t=80,
                l=70,
                r=60,
                b=50
            )
        )

        st.plotly_chart(fig, use_container_width=True)

        


        ##
        # fig = px.box(
        #     jobs,
        #     x="remote_type",
        #     y="Average Salary",
        #     color="remote_type",
        #     points="all",
        #     color_discrete_sequence=px.colors.qualitative.Set2
        # )

        # fig.update_traces(

        #     marker=dict(
        #         size=5,
        #         opacity=0.6
        #     ),

        #     hovertemplate=
        #     "<b>%{x}</b><br>"
        #     "Salary: $%{y:,.0f}<extra></extra>"
        # )

        # fig.update_layout(

        #     title=dict(
        #         text="📦 Salary Distribution by Work Mode",
        #         x=0.3,
        #         font=dict(size=28, color="white")
        #     ),

        #     xaxis_title="Work Mode",
        #     yaxis_title="Salary (USD)",

        #     yaxis=dict(
        #         tickprefix="$",
        #         gridcolor="rgba(255,255,255,0.15)"
        #     ),

        #     paper_bgcolor="rgba(0,0,0,0)",
        #     plot_bgcolor="rgba(0,0,0,0)",

        #     font=dict(color="white"),

        #     showlegend=False,

        #     height=550
        # )

        # st.plotly_chart(fig, use_container_width=True)


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

        st.divider()

        # Create Overview Data
        # overview = (
        #     jobs.groupby(
        #         [
        #             "country",
        #             "city",
        #             "industry",
        #             "company_type",          # Replace if needed
        #             "job_title",
        #             "experience_level"
        #         ],
        #         as_index=False
        #     )["Average Salary"]
        #     .mean()
        # )

        # Sunburst Chart
        # fig = px.sunburst(

        #     overview.head(8000),

        #     path=[
        #         "country",
        #         "city",
        #         "industry",
        #         "company_type",
        #         "job_title",
        #         "experience_level"
        #     ],

        #     values="Average Salary",

        #     color="Average Salary",

        #     color_continuous_scale="Turbo",

        #     hover_data={
        #         "Average Salary":":,.0f"
        #     }
        # )

        # fig.update_traces(

        #     insidetextorientation="radial",

        #     marker=dict(
        #         line=dict(
        #             color="white",
        #             width=1
        #         )
        #     ),

        #     hovertemplate=
        #     "<b>%{label}</b><br><br>"
        #     "<b>Salary:</b> $%{value:,.0f}<br>"
        #     "<b>Parent:</b> %{parent}<br>"
        #     "<b>Hierarchy:</b> %{currentPath}<extra></extra>"
        # )

        # fig.update_layout(

        #     title=dict(
        #         text="🌍 Complete AI Job Market Overview",
        #         x=0.24,
        #         font=dict(
        #             size=30,
        #             color="white",
        #             family="Arial Black"
        #         )
        #     ),

        #     paper_bgcolor="rgba(0,0,0,0)",

        #     plot_bgcolor="rgba(0,0,0,0)",

        #     font=dict(
        #         color="white",
        #         size=14
        #     ),

        #     coloraxis_colorbar=dict(
        #         title="Salary (USD)"
        #     ),

        #     margin=dict(
        #         t=80,
        #         l=10,
        #         r=10,
        #         b=10
        #     ),

        #     height=700
        # )

        st.sidebar.markdown("---")

        st.sidebar.info("""
        Developed By

        **👩‍💻 Sakshi **

        Python | Pandas | Plotly | Streamlit
        """)


      #  st.plotly_chart(fig, use_container_width=True)
