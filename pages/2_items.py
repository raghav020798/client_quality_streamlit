import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(
    page_title="Item Graphs",
    page_icon="🧊",
    layout="wide",
    initial_sidebar_state="collapsed",
    menu_items={
        'Get Help': 'https://www.extremelycoolapp.com/help',
        'Report a bug': "https://www.extremelycoolapp.com/bug",
        'About': "# This is a header. This is an *extremely* cool app!"
    }
)

st.title('Item Feed Graphs')
st.subheader("This section contains quality metrics for Item feed")

# initialize data of lists.
data = {'Year': [2019, 2020, 2021, 2022],
        'Age': [20, 21, 19, 18]}
  

# Create DataFrame
df = pd.DataFrame(data)

fig = px.bar(
        data,
        x="Year",
        y="Age",
        title="Capture transaction_code count",
        color_discrete_sequence=["#9EE6CF"],
    )

st.plotly_chart(fig, theme="streamlit", use_container_width=False)
st.markdown("---")

fig = px.scatter(
        data,
        x="Year",
        y="Age",
        title="Capture card_code count",
        color_discrete_sequence=["#9EE6CF"],
    )

st.plotly_chart(fig, theme="streamlit", use_container_width=False)
st.markdown("---")

fig = px.line(
        data,
        x="Year",
        y="Age",
        title="Capture store_code count",
        color_discrete_sequence=["#9EE6CF"],
    )

st.plotly_chart(fig, theme="streamlit", use_container_width=False)
st.markdown("---")
