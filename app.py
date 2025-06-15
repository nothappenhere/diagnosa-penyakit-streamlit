import streamlit as st
from pages import homepage, auth, user, sistem_pakar


# Streamlit Interface
st.set_page_config(
    page_title="Diganosa Penyakit | Sistem Pakar",
    page_icon=":material/stethoscope:",
    layout="wide",
    initial_sidebar_state="auto",
    menu_items={
        "Report a Bug": "https://github.com/nothappenhere/",
        "About": "### Made with :heart: by *[Mhmmdrzkyakbr](https://www.linkedin.com/in/mhmmdrzkyakbr/)*!",
    },
)

# Default session state
if "logged_in" not in st.session_state:
    st.session_state["logged_in"] = False
if "username" not in st.session_state:
    st.session_state["username"] = ""

# Define pages
pages_without_login = {
    "Main": [
        st.Page(homepage.show_homepage, title="Home", icon=":material/home:"),
        st.Page(
            sistem_pakar.diagnosa_penyakit,
            title="Diagnose",
            icon=":material/stethoscope:",
        ),
    ],
    "Account": [
        st.Page(auth.login_page, title="Log In", icon=":material/login:"),
        st.Page(
            auth.register_page, title="Create account", icon=":material/person_add:"
        ),
    ],
}

pages_with_login = {
    "Main": [
        st.Page(homepage.show_homepage, title="Home", icon=":material/home:"),
        st.Page(
            sistem_pakar.diagnosa_penyakit,
            title="Diagnose",
            icon=":material/stethoscope:",
        ),
    ],
    "Account": [
        st.Page(
            user.user_profile,
            title="Profile",
            icon=":material/account_circle:",
        ),
        # st.Page(user.user_profile, title="History", icon=":material/browse_activity:"),
        st.Page(auth.logout, title="Logout", icon=":material/logout:"),
    ],
}


# Menentukan tampilan halaman berdasarkan login
if st.session_state["logged_in"]:
    pg = st.navigation(pages_with_login)
else:
    pg = st.navigation(pages_without_login)

pg.run()
