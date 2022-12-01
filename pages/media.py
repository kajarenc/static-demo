import streamlit as st

st.write("ANOTHER PAGE")

raw_html = """<img src="./app/static/Parrot.jpg"> </br></br></br>"""
st.markdown(raw_html, unsafe_allow_html=True)
