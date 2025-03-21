import streamlit as st
from streamlit_community_navigation_bar import st_navbar

page = st_navbar(["Home", "Documentation", "Examples", "Community", "About"])
st.write(page)