# **Sistem Pakar Diagnosa Penyakit**

Proyek ini merupakan aplikasi **Sistem Pakar** berbasis web yang dapat membantu pengguna dalam **mendiagnosa penyakit** berdasarkan gejala yang dialami. Aplikasi ini dibangun menggunakan framework **[Streamlit](https://streamlit.io/)** untuk antarmuka pengguna dan **[Experta](https://github.com/nilp0inter/experta)** untuk logika sistem pakarnya.

## Fitur Utama
- Input gejala oleh pengguna
- Diagnosa otomatis berdasarkan aturan (*rule-based*)
- Penjelasan tentang penyakit (deskripsi, penyebab, penanganan)
- Antarmuka web sederhana berbasis Streamlit
- Bisa diperluas untuk dataset dan gejala tambahan

## Teknologi & Library
- Python `3.9.1`
- [Streamlit](https://streamlit.io/)
- [Experta](https://github.com/nilp0inter/experta) – engine sistem pakar berbasis Python
- [Pandas](https://pandas.pydata.org/) – untuk pengolahan data

## Cara Install
1. Pastikan Python `3.9.1` sudah terinstall di komputer Anda.
2. Clone atau unduh repository ini ke komputer Anda.
3. Buka terminal atau command prompt, lalu pindah ke direktori proyek.
4. Buat dan aktifkan virtual environment:
```bash
python -m venv py-experta-env39

source py-experta-env39/bin/activate  # (Linux/Mac)
py-experta-env39\Scripts\activate     # (Windows)
```
5. Install semua library yang dibutuhkan dengan menjalankan perintah berikut:
```bash
pip install -r requirements.txt
```

## Penggunanaan
1. Jalankan aplikasi dengan perintah berikut di terminal:
```bash
streamlit run app.py
```
2. Buka browser Anda dan akses aplikasi di http://localhost:8000.
3. Isi form yang disediakan.
4. Klik tombol "Diagnosa" untuk memulai proses diagnosis penyakit.

## Lisensi
Proyek ini menggunakan lisensi MIT License. Anda bebas untuk menggunakan, memodifikasi, dan mendistribusikan ulang proyek ini sesuai dengan ketentuan lisensi.