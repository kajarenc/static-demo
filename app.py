import streamlit as st

st.set_page_config(
    page_title="Static demo app", page_icon=":hatching_chick:", layout="wide"
)

st.title("Static demo app")

x = st.slider("AAAA", 0, 100, 50)
st.write(x**2)

left, right = st.columns(2)

with left:
    with st.echo():
        st.title("DOG")
        raw_html = """<img src="./app/static/dog.jpg"></br>"""
        st.markdown(raw_html, unsafe_allow_html=True)

with right:
    with st.echo():
        st.title("CAT")

        st.markdown("[![Click me](app/static/cat.png)](https://streamlit.io)")
