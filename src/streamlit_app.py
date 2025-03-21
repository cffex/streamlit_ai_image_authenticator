import streamlit as st
from streamlit_community_navigation_bar import st_navbar

import pages as pg

###
###
###

st.set_page_config(initial_sidebar_state="collapsed")

pages = ["Home", "Github"]

functions = {
    "Home": pg.show_home,
}
options = {
    "show_menu": False,
    "show_sidebar": False,
}
urls = {
    "Github": "https://github.com/cffex/streamlit_ai_image_authenticator"
}
styles = {
    "a": {
        "font-family": "Arial",
        "font-size": "16px",
        "font-weight": "bold",
    },
    
    "div": {
        "max-width": "32rem",
    },

    "hover": {
        "background-color": "rgba(255, 255, 255, 0.35)",
    },
}


###
###
###

page = st_navbar(
    pages=pages,
    options=options,
    urls=urls,
    styles=styles
    )

go_to = functions.get(page)
if go_to:
    go_to()