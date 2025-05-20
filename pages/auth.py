import streamlit as st
import pandas as pd
import os

USER_FILE = "dataset/users.csv"


def load_users():
    if os.path.exists(USER_FILE):
        return pd.read_csv(USER_FILE)
    else:
        return pd.DataFrame(columns=["full_name", "username", "password"])


def register_page():
    st.title("🔐 Registrasi Pengguna")
    # Cek batasan
    if st.session_state["logged_in"]:
        st.warning(
            "Anda harus logout terlebih dahulu sebelum dapat membuat akun baru.",
            icon=":material/lock:",
        )
        st.stop()

    full_name = st.text_input("Nama Lengkap", placeholder="Masukan Nama Lengkap")
    username = st.text_input("Username", placeholder="Masukan Username")
    password = st.text_input(
        "Password", type="password", placeholder="Masukan password"
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

        st.toast("Akun berhasil dibuat! Silakan login.", icon=":material/check:")


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
