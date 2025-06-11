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


def register_page():
    st.title("🔐 Registrasi Pengguna")

    if st.session_state["logged_in"]:
        st.warning(
            "Anda harus logout terlebih dahulu sebelum dapat membuat akun baru.",
            icon=":material/lock:",
        )
        st.stop()

    # Inisialisasi session state untuk form jika belum ada
    for key in ["reg_full_name", "reg_username", "reg_password"]:
        if key not in st.session_state:
            st.session_state[key] = ""

    # Input form dengan session_state
    full_name = st.text_input(
        "Nama Lengkap",
        placeholder="Masukkan nama lengkap",
        value=st.session_state["reg_full_name"],
        key="reg_full_name",
    )
    username = st.text_input(
        "Username",
        placeholder="Masukkan username",
        value=st.session_state["reg_username"],
        key="reg_username",
    )
    password = st.text_input(
        "Password",
        placeholder="Masukkan password",
        type="password",
        value=st.session_state["reg_password"],
        key="reg_password",
    )

    if st.button("Buat Akun", type="primary"):
        if not full_name or not username or not password:
            st.toast("Semua input harus diisi!", icon=":material/warning:")
            return

        users_df = load_users()

        if username in users_df["username"].values:
            st.toast(
                "Username sudah terdaftar, harap menggunakan username lain.",
                icon=":material/warning:",
            )
            return

        new_user = pd.DataFrame(
            [{"full_name": full_name, "username": username, "password": password}]
        )
        users_df = pd.concat([users_df, new_user], ignore_index=True)
        users_df.to_csv(USER_FILE, index=False)

        # Reset input
        # st.session_state["reg_full_name"] = ""
        # st.session_state["reg_username"] = ""
        # st.session_state["reg_password"] = ""

        st.toast("Akun berhasil dibuat! Silakan login.", icon=":material/check:")
        time.sleep(1)
        st.rerun()


def login_page():
    st.title("🔐 Login Pengguna")
    username = st.text_input("Username", placeholder="Masukkan username")
    password = st.text_input(
        "Password", type="password", placeholder="Masukkan password"
    )

    if st.button("Login", type="primary"):
        if not username or not password:
            st.toast("Semua input harus diisi!", icon=":material/warning:")
            return

        users_df = load_users()

        user_match = users_df[
            (users_df["username"] == username) & (users_df["password"] == password)
        ]

        if not user_match.empty:
            st.session_state["logged_in"] = True
            st.session_state["username"] = username
            st.toast(
                f"Selamat datang, {username}!",
                icon=":material/check:",
            )
            time.sleep(1)
            st.rerun()
            st.session_state.setdefault("riwayat_diagnosa", [])
        else:
            st.toast(
                "Username atau password salah!",
                icon=":material/warning:",
            )


def logout():
    st.session_state["logged_in"] = False
    st.session_state["username"] = ""
    st.session_state["riwayat_diagnosa"] = []
    st.toast("Berhasil logout!", icon=":material/check:")
    time.sleep(1)
    st.rerun()
