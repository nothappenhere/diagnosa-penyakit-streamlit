import streamlit as st


def show_homepage():
    st.title("Sistem Pakar Diagnosa Penyakit")
    st.markdown(
        """
    Aplikasi ini dirancang untuk membantu pengguna dalam **mendiagnosis penyakit umum** secara mandiri berdasarkan gejala-gejala yang dialami.

    ### Tujuan Aplikasi:
    - Memberikan diagnosis awal terhadap penyakit umum.
    - Membantu meningkatkan pemahaman masyarakat tentang hubungan antara **gejala** dan **kemungkinan penyakit**.
    - Menyediakan antarmuka yang **mudah digunakan** dan **informasi penyakit yang relevan**.

    ### Cara Kerja:
    1. Pengguna akan memilih gejala yang dirasakan.
    2. Sistem akan mencocokkan gejala tersebut dengan basis pengetahuan (aturan ***IF-THEN***).
    3. Jika ditemukan kecocokan, sistem akan menampilkan hasil diagnosa serta deskripsi penyakit.
    4. Pengguna juga dapat melihat **riwayat diagnosa sebelumnya** *(jika sudah login)*.

    ### :pushpin: Catatan:
    - Diagnosa yang diberikan **bukan pengganti konsultasi dokter**.
    - Konsultasikan ke tenaga medis profesional untuk tindakan lebih lanjut.

    ---
    """
    )
