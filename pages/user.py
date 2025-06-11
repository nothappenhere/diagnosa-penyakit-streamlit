import streamlit as st
import pandas as pd
import os
import time

USER_FILE = "dataset/users.csv"


def load_users():
    if os.path.exists(USER_FILE):
        return pd.read_csv(USER_FILE)
    else:
        return pd.DataFrame(columns=["full_name", "username", "password"])


def save_users(df):
    df.to_csv(USER_FILE, index=False)


def user_profile():
    st.title(f":material/person: Profil Pengguna: {st.session_state['username']}")

    if not st.session_state.get("logged_in"):
        st.warning(
            "Anda harus login terlebih dahulu untuk melihat halaman ini.",
            icon=":material/warning:",
        )
        st.stop()

    username = st.session_state["username"]
    users_df = load_users()
    user_data = users_df[users_df["username"] == username]

    if user_data.empty:
        st.error("Data pengguna tidak ditemukan.", icon=":material/warning:")
        return

    # Ambil informasi pengguna
    full_name = user_data.iloc[0]["full_name"]
    username = user_data.iloc[0]["username"]
    password = user_data.iloc[0]["password"]

    # Form edit
    new_full_name = st.text_input("Nama Lengkap", value=full_name)
    new_full_name = st.text_input("Username", value=username)
    new_password = st.text_input("Password", value=password, type="password")

    if st.button("Simpan Perubahan", type="primary"):
        if not new_full_name or not new_password:
            st.toast("Semua field harus diisi.", icon=":material/warning:")
            return

        # Update DataFrame
        users_df.loc[users_df["username"] == username, "full_name"] = new_full_name
        users_df.loc[users_df["username"] == username, "password"] = new_password
        save_users(users_df)

        st.toast("Profil berhasil diperbarui!", icon=":material/check:")
        time.sleep(2)
        st.rerun()
