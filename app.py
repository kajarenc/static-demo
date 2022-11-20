import streamlit as st

st.set_page_config(
    page_title="Static demo app", page_icon=":hatching_chick:", layout="wide"
)

left, right = st.columns(2)

with left:
    with st.echo():
        st.title("Static Demo test app")
        raw_html = """<img src="user-static/dog.jpg"> </br></br></br>"""
        st.markdown(raw_html, unsafe_allow_html=True)

with right:
    with st.echo():
        st.title("Exclusive content, clickable image!")

        st.markdown("[![Click me](user-static/cat.png)](https://youtu.be/dQw4w9WgXcQ)")
