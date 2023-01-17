import streamlit as st

with st.echo():
    st.title("Media PAGE")

    raw_html = """<img src="./app/static/Parrot.jpeg" width="800"> </br></br></br>"""
    st.markdown(raw_html, unsafe_allow_html=True)
