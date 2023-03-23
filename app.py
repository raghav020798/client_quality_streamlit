import streamlit as st

st.set_page_config(
    page_title="Dunnhumby Quality Module",
    page_icon="🧊",
    layout="centered",
    initial_sidebar_state="collapsed",
    menu_items={
        'Get Help': 'https://www.extremelycoolapp.com/help',
        'Report a bug': "https://www.extremelycoolapp.com/bug",
        'About': "# This is a header. This is an *extremely* cool app!"
    }
)



st.title('Dunnhumby Quality Module')
st.text('This is a sample web app to demonstrate client side quality.')

with st.form("my-form", clear_on_submit=True):
        file = st.file_uploader('Upload files to be moved for quality.', accept_multiple_files=True)
        submitted = st.form_submit_button("SUBMIT!")

        if submitted and file is not None:
            st.write("Starting Quality Module!")


