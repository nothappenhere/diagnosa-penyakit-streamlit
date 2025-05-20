import streamlit as st
from pages import auth, homepage, sistem_pakar


# Streamlit Interface
st.set_page_config(
    page_title="Sistem Pakar",
    page_icon="🩺",
    layout="centered",
    initial_sidebar_state="auto",
    menu_items={
        "Report a Bug": "https://github.com/nothappenhere/",
        "About": "### Made with :heart: by *[Mhmmdrzkyakbr](https://www.linkedin.com/in/mhmmdrzkyakbr/)*!",
    },
)

pages = {
    "Main": [
        st.Page(homepage.show_homepage, title="Home", icon=":material/home:"),
        # if st.session_state.get("logged_in"):
        st.Page(
            sistem_pakar.diagnosa_penyakit,
            title="Diagnoses",
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

pg = st.navigation(pages)
pg.run()

if st.session_state.get("logged_in"):

    # pg = st.navigation(
    #     [st.Page("sistem_pakar.py", title="Diagnosa", icon=":material/stethoscope:")]
    # )
    # pg.run()

    if st.sidebar.button("Logout", type="tertiary", icon=":material/logout:"):
        st.toast("Berhasil logout!", icon=":lock:")
        auth.logout()
