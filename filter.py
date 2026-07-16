import streamlit as st
import pandas as pd
import plotly.express as px

# import streamlit as st
# import pandas as pd

def show():
    
    jobs = pd.read_csv("ai_jobs.csv")

    skills = pd.read_csv("skills_demand.csv")

    roles = pd.read_csv("job_title_mapping.csv")
    country_trends = pd.read_csv("country_ai_trends.csv")

    jobs["Average Salary"] = (
        jobs["salary_min_usd"] +
        jobs["salary_max_usd"]
    ) / 2

    st.title("📌 Final Summary Table")

    # Create Average Salary
    jobs["Average Salary"] = (
        jobs["salary_min_usd"] + jobs["salary_max_usd"]
    ) / 2

    # Start from ai_jobs.csv
    summary = jobs.copy()

    # Merge Job Title Mapping
    summary = summary.merge(
        roles[
            ["job_title", "standardized_title", "role_category"]
        ],
        on="job_title",
        how="left"
    )

    # Merge Country Trends using Country + Year
    summary = summary.merge(
        country_trends[
            ["country", "year", "top_skill", "remote_percentage"]
        ],
        left_on=["country", "posted_year"],
        right_on=["country", "year"],
        how="left"
    )

    # Remove duplicate year column
    summary.drop(columns=["year"], inplace=True)

    # Select columns
    summary = summary[
        [
         #   "posted_year",
            "country",
            "city",
            "industry",
            "company_size",
            "job_title",
            "standardized_title",
            "role_category",
            "experience_level",
            "employment_type",
            "remote_type",
            "Average Salary",
            "top_skill",
            "remote_percentage"
        ]
    ]

    # Rename columns
    summary.rename(
        columns={
          #  "posted_year": "Year",
            "country": "Country",
            "city": "City",
            "industry": "Industry",
            "company_size": "Company Size",
            "job_title": "Job Title",
            "standardized_title": "Standardized Title",
            "role_category": "Role Category",
            "experience_level": "Experience",
            "employment_type": "Employment Type",
            "remote_type": "Work Mode",
            "Average Salary": "Salary (USD)",
            "top_skill": "Top Skill",
            "remote_percentage": "Remote %"
        },
        inplace=True
    )
 
    st.sidebar.subheader("🔍 Filter Summary")

    country_filter = st.sidebar.multiselect(
        "Country",
        sorted(summary["Country"].dropna().unique())
    )

    industry_filter = st.sidebar.multiselect(
        "Industry",
        sorted(summary["Industry"].dropna().unique())
    )

    experience_filter = st.sidebar.multiselect(
        "Experience",
        sorted(summary["Experience"].dropna().unique())
    )

    if country_filter:
        summary = summary[
            summary["Country"].isin(country_filter)
        ]

    if industry_filter:
        summary = summary[
            summary["Industry"].isin(industry_filter)
        ]

    if experience_filter:
        summary = summary[
            summary["Experience"].isin(experience_filter)
        ]

    st.dataframe(
        summary,
        use_container_width=True,
        hide_index=True
    )

    st.divider()


    ##
    st.title("🌞 Complete AI Job Market Overview")
    sunburst_df = summary.head(500)

    fig = px.sunburst(
        
        sunburst_df,
        path=[
           # "Year",
            "Country",
            "City",
            "Industry",
            "Job Title",
            "Experience",
            "Work Mode",
            "Top Skill",
        ],

        values="Salary (USD)",

        color="Salary (USD)",

        color_continuous_scale="Turbo",

        hover_data={
            "Salary (USD)":":,.0f"
        }
    )

    fig.update_traces(

        insidetextorientation="radial",

        marker=dict(
            line=dict(
                color="white",
                width=1
            )
        ),

        hovertemplate=
        "<b>%{label}</b><br><br>"
        "💰 Salary : <b>$%{color:,.0f}</b><br>"
        "📊 Total Value : <b>%{value:,.0f}</b><br>"
        "📂 Parent : %{parent}<br>"
        "<extra></extra>"
    )

    fig.update_layout(

        # title=dict(
        #    # text="🌍 Complete AI Job Market Hierarchy",
        #     x=0.5,
        #     font=dict(
        #         size=30,
        #         color="white",
        #         family="Arial Black"
        #     )
        # ),

        paper_bgcolor="rgba(0,0,0,0)",
        plot_bgcolor="rgba(0,0,0,0)",

        font=dict(
            color="white",
            size=14
        ),

        coloraxis_colorbar=dict(
            title="Salary (USD)"
        ),

        margin=dict(
            t=80,
            l=10,
            r=10,
            b=10
        ),

        height=800
    )

    st.sidebar.markdown("---")

    st.sidebar.info("""
    Developed By

    **👩‍💻 Sakshi **

    Python | Pandas | Plotly | Streamlit
    """)


    st.plotly_chart(fig, use_container_width=True)

    