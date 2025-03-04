import streamlit as st

from st_pages import add_page_title, get_nav_from_toml



nav = get_nav_from_toml()

st.logo("assets/img/logo.png")

pg = st.navigation(nav)



pg.run()