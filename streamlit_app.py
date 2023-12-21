import streamlit as st

st.set_page_config(
    page_title="Resume Parser | SixthSens AI",
)

hide_streamlit_style = """
            <style>
            .css-1jc7ptx, .e1ewe7hr3, .viewerBadge_container__1QSob,
            .styles_viewerBadge__1yB5_, .viewerBadge_link__1S137,
            .viewerBadge_text__1JaDK {display: none;}
            MainMenu {visibility: hidden;}
            header { visibility: hidden; }
            footer {visibility: hidden;}
            #GithubIcon {visibility: hidden;}
            </style>
            """
st.markdown(hide_streamlit_style, unsafe_allow_html=True)

import os
from resume_parser import resumeparse

def format_data(data):
    for key, value in data.items():
        st.write(f"**{key}**: {value}")

st.title("SixthSens Resume Parser")

uploaded_file = st.file_uploader("Upload a resume", type=["pdf"])
if uploaded_file is not None:
    with open(os.path.join('tempDir',uploaded_file.name),"wb") as f:
        f.write(uploaded_file.getbuffer())
    st.success("File Uploaded")
    data = resumeparse.read_file(os.path.join('tempDir',uploaded_file.name))
    st.write(data)
