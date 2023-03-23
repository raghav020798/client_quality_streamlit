import streamlit as st
import pandas as pd

st.set_page_config(
    page_title="File Status",
    page_icon="🧊",
    layout="wide",
    initial_sidebar_state="collapsed",
    menu_items={
        'Get Help': 'https://www.extremelycoolapp.com/help',
        'Report a bug': "https://www.extremelycoolapp.com/bug",
        'About': "# This is a header. This is an *extremely* cool app!"
    }
)

st.title('Historical File Status')
st.text('This section will keep track of past files.')

entity_list = ['Item', 'Basket', 'Product', 'Customer', 'Stores']
rows = len(entity_list)/2 +len(entity_list)%2
containers = []
@st.cache_data
def load_data():
    list_df = {}
    for entity in ['Item', 'Basket', 'Product', 'Customer', 'Stores']:
        list_df[entity]=(pd.DataFrame(
        {
            "filename": [f'{entity}_1.csv', f'{entity}_2.csv', f'{entity}_3.csv', f'{entity}_4.csv'],
            "Passed Quality": [True, True, False, True],
            "Transferred to dh": [True, True, True, False]
        }
    ))

    return list_df

list_df = load_data()

for entity in list_df:
    st.header(entity)
    st.dataframe(list_df[entity])

