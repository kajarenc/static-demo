import streamlit as st

st.title("PAGE 1")


raw_html = """<img src="./app/static/Parrot.jpeg"> </br></br></br>"""
st.markdown(raw_html, unsafe_allow_html=True)
