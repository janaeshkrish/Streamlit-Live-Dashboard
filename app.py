import pandas as pd
import numpy as np
import time
import streamlit as st
import plotly.express as px

# read csv from a github repo
df = pd.read_csv("https://raw.githubusercontent.com/Lexie88rus/bank-marketing-analysis/master/bank.csv")

st.set_page_config(
    page_title = 'Real-Time Dashboard',
    page_icon = '✅',
    layout = 'wide'
)

# dashboard title
st.title("Real-Time / Sales Live Dashboard")

# top level filter
job_filter = st.selectbox("select job", df['job'].unique()) # job filter

# insering a single-element container
placeholder = st.empty()

# Dataframe filter based on the job filter
df = df[df['job'] == job_filter]

# simulating a real-time data stream using a for loop with random data
# while True:
for secounds in range(200):

    df["age_new"] = df["age"] * np.random.choice(range(1,5))

    df["balance_new"] = df["balance"] * np.random.choice(range(1,5))

    # Creating KPI's
    avg_new = np.mean(df["age_new"])

    count_married =  int(df[(df['marital'] == 'married')]['marital'].count() + np.random.choice(range(1,5)))

    balance = np.mean(df["balance_new"])

    with placeholder.container():

        # Create three columns
        kpi1,kpi2,kpi3 = st.columns(3)

        # fillin those metrics with KPIs
        kpi1.metric(label="Age", value=round(avg_new),delta=round(avg_new)-10)

        kpi2.metric(label="Marital Count ", value=int(count_married),delta=count_married-10)

        kpi3.metric(label="A/C Balance $", value=f"$ {round(balance)}",delta=round(balance)-10)

        # create two columns for charts
        chart1,chart2 = st.columns(2)

        with chart1:

            st.markdown("**Age Distribution**")

            # plotty chart
            fig1 = px.density_heatmap(data_frame=df, x="marital", y="age_new")
            # pie chart
            #fig1 = px.pie(data_frame=df, values="marital", names="age_new")

            st.write(fig1) # display the chart
        
        with chart2:

            st.markdown("**Balance Distribution**")

            # plotty chart
            fig2 = px.histogram(data_frame=df, x="age_new")

            st.write(fig2) # display the chart

        st.markdown("**Detailed Table View**")
        st.dataframe(df) # display the table

        # Based on the API calls
        time.sleep(1) # sleep for 1 second

        # ---- HIDE STREAMLIT STYLE ----
        hide_st_style = """
                    <style>
                    #MainMenu {visibility: hidden;}
                    footer {visibility: hidden;}
                    header {visibility: hidden;}
                    </style>
                    """

        # use css from file
        # def load_css():
        #     with open("style.css", "r") as f:
        #         st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

        st.markdown(hide_st_style, unsafe_allow_html=True)






        
    




