import streamlit as st
import pandas as pd
import plotly.express as px
import seaborn as sns
import matplotlib.pyplot as plt

def show():

    # Load Datasets
    jobs = pd.read_csv("ai_jobs.csv")
    roles = pd.read_csv("job_title_mapping.csv")

    st.title("👩🏽‍💼 Job Roles Dashboard")
    st.markdown("Analyze AI job roles, standardized titles, and role categories.")

    tab1, tab2, tab3, tab4 = st.tabs([
        "📌 Most Common Job Titles",
        "📝 Standardized Job Titles",
        "📂 Role Categories",
        "📑 Heat Map "
    ])

    # =====================================================
    # TAB 1
    # =====================================================
    with tab1:

        st.subheader("📌 Top 10 Most Common Job Titles")

        top_jobs = jobs["job_title"].value_counts().head(10)

        fig = px.bar(
            top_jobs.reset_index(),
            x="job_title",
            y="count",
            color="count",
            text="count",
            color_continuous_scale="Viridis"
        )

        fig.update_layout(
            title={
                "text":"Top 10 Most Common Job Titles",
                "x":0.5
            },
            xaxis_title="Job Title",
            yaxis_title="Number of Jobs",
            height=500
        )

        st.plotly_chart(fig, use_container_width=True)

        st.dataframe(top_jobs)

        #Pie Chart

        #fig = px.pie(
        #     top_jobs.reset_index(),
        #     names="job_title",
        #     values="count",
        #     hole=.45
        # )

        # fig.update_layout(
        #     title="Job Title Distribution",
        #     title_x=0.5,
            
        # )

        # st.plotly_chart(fig,use_container_width=True)
        
        #Donut Chart
          
        top_jobs = roles["job_title"].value_counts().head(10)

        fig = px.pie(
            top_jobs.reset_index(),
            names="job_title",
            values="count",
            hole=0.5,
            color_discrete_sequence=px.colors.qualitative.Set3
        )

        fig.update_traces(
            textposition="inside",
            textinfo="percent+label",
            pull=[0.05]*len(top_jobs),      # Slightly separates slices
            marker=dict(
                line=dict(color="white", width=2)
            ),
            hovertemplate="<b>%{label}</b><br>Jobs: %{value}<br>%{percent}<extra></extra>"
        )

        fig.update_layout(

            title=dict(
                text="📊 Job Title Distribution",
                x=0.5,
                xanchor="center",
                font=dict(size=24, color="white")
            ),

            # Remove background
            paper_bgcolor="rgba(0,0,0,0)",
            plot_bgcolor="rgba(0,0,0,0)",

            # Font
            font=dict(
                color="white",
                size=14
            ),

            # Legend
            legend=dict(
                orientation="h",
                y=-0.15,
                x=0.5,
                xanchor="center",
                font=dict(size=12)
            ),

            margin=dict(l=20, r=20, t=70, b=50),

            height=550
        )

        st.plotly_chart(fig, use_container_width=True)
        

    # =====================================================
    # TAB 2
    # =====================================================
    with tab2:
        
        st.metric(
            "Standardized Titles",
            roles["standardized_title"].nunique()
        )

        # Count standardized job titles
        standard = roles["standardized_title"].value_counts().reset_index()
        standard.columns = ["Standardized Title", "Count"]

        fig = px.bar(
            standard,
            x="Standardized Title",
            y="Count",
            color="Count",
            text="Count",
            color_continuous_scale="Viridis"   # You can also use Plasma, Turbo, Sunset
        )

        fig.update_traces(
            textposition="outside",
            marker_line_color="white",
            marker_line_width=1.5,
            hovertemplate="<b>%{x}</b><br>Total Jobs: %{y}<extra></extra>"
        )

        fig.update_layout(

            title={
                "text": "📋 Standardized Job Titles",
                "x": 0.38,
                "font": dict(size=24, color="white")
            },

            xaxis_title="Standardized Job Title",
            yaxis_title="Number of Jobs",

            paper_bgcolor="rgba(0,0,0,0)",   # Transparent background
            plot_bgcolor="rgba(0,0,0,0)",

            font=dict(
                color="white",
                size=14
            ),

            xaxis=dict(
                tickangle=-20,
                showgrid=False
            ),

            yaxis=dict(
                showgrid=True,
                gridcolor="rgba(255,255,255,0.15)"
            ),

            coloraxis_showscale=True,       # Show color scale

            height=600
        )

        st.plotly_chart(fig, use_container_width=True)
        st.dataframe(standard)




    # =====================================================
    # TAB 3
    # =====================================================
    with tab3:

        # st.subheader(" Role Categories")

        # category = roles["role_category"].value_counts()

        # fig = px.bar(
        #     category.reset_index(),
        #     x="role_category",
        #     y="count",
        #     color="role_category",
        #     text="count",
        #     color_discrete_sequence=px.colors.qualitative.Bold
        # )

        # fig.update_layout(
        #     title={
        #         "text":"Role Category Distribution",
        #         "x":0.5
        #     },
        #     xaxis_title="Role Category",
        #     yaxis_title="Count",
        #     showlegend=False,
        #     height=500
        # )

        # st.plotly_chart(fig, use_container_width=True)

        # st.dataframe(category)

        st.title("👩🏽‍💻 Role Categories")

        # ----------------------------
        # KPI Cards
        # ----------------------------

        c1, c2, c3 = st.columns(3)

        c1.metric("Total Categories", roles["role_category"].nunique())
        c2.metric("Analytics Jobs", len(roles[roles["role_category"]=="Analytics"]))
        c3.metric("Engineering Jobs", len(roles[roles["role_category"]=="Engineering"]))

        st.divider()

        # ----------------------------
        # Category Count Table
        # ----------------------------

        category = (
            roles["role_category"]
            .value_counts()
            .reset_index()
        )

        category.columns = ["Role Category", "Count"]

        st.subheader("📊 Role Category Count")

        st.dataframe(category, use_container_width=True)

        # ----------------------------
        # Analytics Jobs
        # ----------------------------

        analytics = roles[
            roles["role_category"]=="Analytics"
        ]

        st.subheader("📈 Analytics Jobs")

        st.dataframe(
            analytics[
                ["job_title","standardized_title"]
            ],
            use_container_width=True
        )

        # ----------------------------
        # Engineering Jobs
        # ----------------------------

        engineering = roles[
            roles["role_category"]=="Engineering"
        ]

        st.subheader("⚙ Engineering Jobs")

        st.dataframe(
            engineering[
                ["job_title","standardized_title"]
            ],
            use_container_width=True
        )

        # ----------------------------
        # Charts
        # ----------------------------

        col1, col2 = st.columns(2)

        # ----------------------------
        # Bar Chart
        # ----------------------------

        with col1:

            fig = px.bar(
                category,
                x="Role Category",
                y="Count",
                color="Role Category",
                text="Count",
                color_discrete_sequence=px.colors.qualitative.Set2
            )

            fig.update_traces(
                textposition="outside",
                marker_line_color="white",
                marker_line_width=2,
                hovertemplate="<b>%{x}</b><br>Jobs: %{y}<extra></extra>"
            )

            fig.update_layout(

                title=dict(
                    text="📊 Role Category Distribution",
                    x=0.3,
                    font=dict(size=22,color="white")
                ),

                paper_bgcolor="rgba(0,0,0,0)",
                plot_bgcolor="rgba(0,0,0,0)",

                font=dict(color="white"),

                xaxis=dict(showgrid=False),

                yaxis=dict(
                    showgrid=True,
                    gridcolor="rgba(255,255,255,0.15)"
                ),

                #coloraxis_showscale=True,       # Show color scale

                height=550,

                showlegend=False
            )

            st.plotly_chart(fig, use_container_width=True)

        # ----------------------------
        # Donut Chart
        # ----------------------------

        with col2:

            fig = px.pie(
                category,
                names="Role Category",
                values="Count",
                hole=0.4,
                color="Role Category",
                color_discrete_sequence=px.colors.qualitative.Pastel
            )

            fig.update_traces(

                textinfo="percent+label",

                marker=dict(
                    line=dict(color="white",width=2)
                ),

                hovertemplate="<b>%{label}</b><br>Count: %{value}<br>%{percent}<extra></extra>"
            )

            fig.update_layout(

                title=dict(
                    text="🥧 Role Category Percentage",
                    x=0.26,
                    font=dict(size=22,color="white")
                ),

                paper_bgcolor="rgba(0,0,0,0)",
                plot_bgcolor="rgba(0,0,0,0)",

                font=dict(color="white"),

                legend=dict(
                    orientation="h",
                    y=-0.15,
                    x=0.5,
                    xanchor="center"
                )
            )

            st.plotly_chart(fig, use_container_width=True)



    with tab4:

      # heat = pd.crosstab(
      #     roles["role_category"],
      #     roles["standardized_title"]
      # )

      # fig,ax = plt.subplots(figsize=(10,5))

      # sns.heatmap(
      #     heat,
      #     annot=True,
      #     cmap="YlGnBu",
      #     linewidths=.5,
      #     ax=ax
      # )

      # plt.title(
      #     "Role Category vs Standardized Job Title"
      # )
      # st.pyplot(fig)
      


      #Correlation HeatMap

      # Cross Tab
      heat = pd.crosstab(
          roles["role_category"],
          roles["standardized_title"]
      )

      # Create Figure
      fig, ax = plt.subplots(figsize=(12, 6))

      # Transparent Background
      fig.patch.set_alpha(0)
      ax.set_facecolor("none")

      # Heatmap
      sns.heatmap(
          heat,
          annot=True,
          fmt="d",
          cmap="YlGnBu",
          linewidths=1,
          linecolor="white",
          cbar_kws={"label": "Number of Jobs"},
          annot_kws={"size": 12},
          ax=ax
      )

      # Title
      ax.set_title(
          "🔥 Role Category vs Standardized Job Title",
          fontsize=18,
          color="white",
          weight="bold",
          pad=20
      )

      # Axis Labels
      ax.set_xlabel(
          "Standardized Job Title",
          fontsize=13,
          color="white"
      )

      ax.set_ylabel(
          "Role Category",
          fontsize=13,
          color="white"
      )

      # Tick Colors
      ax.tick_params(axis="x", colors="white", rotation=20)
      ax.tick_params(axis="y", colors="white", rotation=0)

      # Colorbar Text Color
      cbar = ax.collections[0].colorbar
      cbar.ax.yaxis.label.set_color("white")
      cbar.ax.tick_params(colors="white")

      plt.tight_layout()

      # Show in Streamlit
      st.pyplot(fig)
        












