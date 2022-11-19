import streamlit as st


with st.echo():
    st.title("Static Demo test app")

    raw_html = """ <img src="user-static/dog.jpg">"""

    st.markdown(raw_html, unsafe_allow_html=True)
