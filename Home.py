import streamlit as st
import pandas as p


st.set_page_config(layout="wide")
st.title("Home")

col1, col2 = st.columns(2)

with col1:
    st.image("images/photo.png")

with col2:
    content = """
    Hi! 
    I'm Adam, I am university student at ELTE University in Budapest this\n
     is a site for displaying portfolio for my projects.\n
    This is a webapp showcasing the projects I have done...
    
    """
    st.info(content)

content2 = """ Below are the projects I worked on"""

st.write(content2)

col3, col4 = st.columns(2, gap="medium")

df = p.read_csv("data.csv", sep=";")


with col3:

    for i, row in df[:df.__len__()//2:].iterrows():
        st.header(row["title"])
        st.image("images/" + row["image"])
        st.write(row["description"])
        st.link_button("See code", row["url"])


with col4:
    for i, row in df[df.__len__() // 2::].iterrows():
        st.header(row["title"])
        st.image("images/" + row["image"])
        st.write(row["description"])
        st.link_button("See code", row["url"])

