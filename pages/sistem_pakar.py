import streamlit as st
from experta import *


# Definisikan kelas fakta
class Gejala(Fact):
    pass


# Definisikan sistem pakar
class SistemPakarPenyakit(KnowledgeEngine):
    @Rule(Gejala(fever="Ya", cough="Ya", difficulty_breathing="Ya"))
    def asthma(self):
        st.session_state["diagnosis"] = "Kemungkinan: Asthma"

    @Rule(Gejala(fatigue="Ya", cholesterol="Tinggi", age="Di atas 45"))
    def stroke(self):
        st.session_state["diagnosis"] = "Kemungkinan: Stroke"

    @Rule(Gejala(fatigue="Ya", age="Di atas 50", blood_pressure="Rendah"))
    def osteoporosis(self):
        st.session_state["diagnosis"] = "Kemungkinan: Osteoporosis"

    @Rule(Gejala(blood_pressure="Tinggi", age="Di atas 40"))
    def hypertension(self):
        st.session_state["diagnosis"] = "Kemungkinan: Hypertension"

    @Rule(Gejala(fatigue="Ya", cholesterol="Tinggi", blood_pressure="Tinggi"))
    def diabetes(self):
        st.session_state["diagnosis"] = "Kemungkinan: Diabetes"

    @Rule(Gejala(fatigue="Ya", fever="Tidak", cough="Tidak", blood_pressure="Normal"))
    def migraine(self):
        st.session_state["diagnosis"] = "Kemungkinan: Migraine"

    @Rule(Gejala(fever="Ya", cough="Ya", blood_pressure="Normal"))
    def influenza(self):
        st.session_state["diagnosis"] = "Kemungkinan: Influenza"

    @Rule(
        Gejala(
            fever="Ya", cough="Ya", difficulty_breathing="Ya", blood_pressure="Tinggi"
        )
    )
    def pneumonia(self):
        st.session_state["diagnosis"] = "Kemungkinan: Pneumonia"

    @Rule(Gejala(fever="Ya", cough="Ya", fatigue="Ya"))
    def bronchitis(self):
        st.session_state["diagnosis"] = "Kemungkinan: Bronchitis"

    @Rule(
        Gejala(
            fatigue="Ya",
            blood_pressure="Tinggi",
            cholesterol="Normal",
            age="Di atas 45",
        )
    )
    def hyperthyroidism(self):
        st.session_state["diagnosis"] = "Kemungkinan: Hyperthyroidism"

    @Rule(
        Gejala(
            fatigue="Ya",
            blood_pressure="Rendah",
            cholesterol="Normal",
            age="Di atas 45",
        )
    )
    def hypothyroidism(self):
        st.session_state["diagnosis"] = "Kemungkinan: Hypothyroidism"

    @Rule(Gejala(fatigue="Ya", age="Di atas 50", blood_pressure="Tinggi"))
    def osteoarthritis(self):
        st.session_state["diagnosis"] = "Kemungkinan: Osteoarthritis"

    @Rule(
        Gejala(
            fatigue="Ya",
            blood_pressure="Normal",
            cholesterol="Tinggi",
            age="Di atas 50",
        )
    )
    def kidney_cancer(self):
        st.session_state["diagnosis"] = "Kemungkinan: Kidney Cancer"

    @Rule(Gejala(fever="Ya", cough="Tidak", blood_pressure="Normal"))
    def common_cold(self):
        st.session_state["diagnosis"] = "Kemungkinan: Common Cold"

    @Rule(Gejala(fatigue="Ya", cholesterol="Tinggi", age="Di atas 50"))
    def liver_cancer(self):
        st.session_state["diagnosis"] = "Kemungkinan: Liver Cancer"


# Informasi penyakit
penyakit_info = {
    "Asthma": {
        "deskripsi": "Penyakit saluran pernapasan yang menyebabkan sesak dan batuk.",
        "penyebab": "Debu, polusi udara, alergi, udara dingin.",
        "penanganan": "Gunakan inhaler, hindari pemicu, konsultasi dengan dokter.",
    },
    "Stroke": {
        "deskripsi": "Kondisi saat suplai darah ke otak terganggu.",
        "penyebab": "Hipertensi, kolesterol tinggi, merokok.",
        "penanganan": "Obat pengencer darah, fisioterapi, tindakan medis darurat.",
    },
    "Osteoporosis": {
        "deskripsi": "Pengeroposan tulang yang meningkatkan risiko patah tulang.",
        "penyebab": "Kurang kalsium, usia tua, keturunan.",
        "penanganan": "Suplemen kalsium, olahraga beban, terapi hormon.",
    },
    "Hypertension": {
        "deskripsi": "Tekanan darah tinggi yang meningkatkan risiko jantung dan stroke.",
        "penyebab": "Garam berlebih, stres, kurang olahraga.",
        "penanganan": "Obat tekanan darah, diet sehat, olahraga.",
    },
    "Diabetes": {
        "deskripsi": "Penyakit kronis dengan kadar gula darah tinggi.",
        "penyebab": "Faktor genetik, pola makan buruk, kurang olahraga.",
        "penanganan": "Konsumsi makanan sehat, olahraga teratur, obat insulin jika perlu.",
    },
    "Migraine": {
        "deskripsi": "Sakit kepala parah disertai mual dan sensitivitas cahaya.",
        "penyebab": "Stres, hormon, makanan tertentu.",
        "penanganan": "Obat pereda nyeri, hindari pemicu.",
    },
    "Influenza": {
        "deskripsi": "Infeksi virus yang menyerang saluran pernapasan atas.",
        "penyebab": "Virus influenza yang menyebar melalui udara.",
        "penanganan": "Istirahat, konsumsi cairan, obat antivirus jika perlu.",
    },
    "Pneumonia": {
        "deskripsi": "Infeksi paru-paru yang menyebabkan peradangan.",
        "penyebab": "Bakteri, virus, atau jamur.",
        "penanganan": "Antibiotik, cairan infus, perawatan rumah sakit.",
    },
    "Bronchitis": {
        "deskripsi": "Peradangan saluran bronkus di paru-paru.",
        "penyebab": "Infeksi virus, merokok.",
        "penanganan": "Istirahat, minum cukup air, obat batuk.",
    },
    "Hyperthyroidism": {
        "deskripsi": "Kelenjar tiroid terlalu aktif menghasilkan hormon.",
        "penyebab": "Penyakit Graves, nodul tiroid.",
        "penanganan": "Obat anti-tiroid, yodium radioaktif, operasi.",
    },
    "Hypothyroidism": {
        "deskripsi": "Kelenjar tiroid kurang aktif menghasilkan hormon.",
        "penyebab": "Autoimun, kekurangan yodium.",
        "penanganan": "Terapi hormon tiroid.",
    },
    "Osteoarthritis": {
        "deskripsi": "Kerusakan pada tulang rawan sendi.",
        "penyebab": "Penuaan, cedera sendi, obesitas.",
        "penanganan": "Fisioterapi, obat nyeri, operasi sendi bila parah.",
    },
    "Kidney Cancer": {
        "deskripsi": "Kanker yang berasal dari jaringan ginjal.",
        "penyebab": "Merokok, obesitas, faktor genetik.",
        "penanganan": "Operasi pengangkatan, imunoterapi, kemoterapi.",
    },
    "Common Cold": {
        "deskripsi": "Infeksi ringan saluran pernapasan atas.",
        "penyebab": "Virus rhinovirus.",
        "penanganan": "Istirahat, cairan hangat, obat pereda gejala.",
    },
    "Liver Cancer": {
        "deskripsi": "Kanker yang berasal dari sel hati.",
        "penyebab": "Hepatitis B/C, konsumsi alkohol berlebih.",
        "penanganan": "Operasi, kemoterapi, transplantasi hati.",
    },
}


def diagnosa_penyakit():
    # Batasan Diagnosa untuk User Guest
    if "logged_in" not in st.session_state:
        st.session_state["logged_in"] = False
    if "guest_diagnosis_count" not in st.session_state:
        st.session_state["guest_diagnosis_count"] = 0

    # Streamlit Interface
    st.title(":stethoscope: Diagnosa Penyakit Umum")

    # Cek batasan
    if (
        not st.session_state["logged_in"]
        and st.session_state["guest_diagnosis_count"] >= 3
    ):
        st.warning(
            "🔒 Anda telah mencapai batas maksimum 3 kali diagnosa sebagai pengguna tamu. Silakan login untuk melanjutkan."
        )
        st.stop()

    with st.form("form"):
        st.write("Silakan isi gejala berikut:")
        fever = st.selectbox("Demam?", ["Ya", "Tidak"])
        cough = st.selectbox("Batuk?", ["Ya", "Tidak"])
        fatigue = st.selectbox("Kelelahan?", ["Ya", "Tidak"])
        difficulty_breathing = st.selectbox("Kesulitan Bernapas?", ["Ya", "Tidak"])
        age = st.slider("Usia", 1, 100, 20)
        gender = st.selectbox("Jenis Kelamin", ["Laki-laki", "Perempuan"])
        blood_pressure = st.selectbox("Tekanan Darah", ["Rendah", "Normal", "Tinggi"])
        cholesterol = st.selectbox("Level Kolesterol", ["Normal", "Tinggi"])

        submitted = st.form_submit_button("Diagnosa", type="primary")

    if submitted:
        # Naikkan counter jika user belum login
        if not st.session_state["logged_in"]:
            st.session_state["guest_diagnosis_count"] += 1

        st.session_state["diagnosis"] = "Tidak ditemukan diagnosis yang cocok."
        engine = SistemPakarPenyakit()
        engine.reset()
        age_category = (
            "Di atas 50" if age > 50 else "Di atas 45" if age > 45 else "Di bawah 45"
        )
        engine.declare(
            Gejala(
                fever=fever,
                cough=cough,
                fatigue=fatigue,
                difficulty_breathing=difficulty_breathing,
                age=age_category,
                gender=gender,
                blood_pressure=blood_pressure,
                cholesterol=cholesterol,
            )
        )
        engine.run()

    if not st.session_state["logged_in"]:
        sisa = 3 - st.session_state["guest_diagnosis_count"]
        st.info(f"Anda dapat melakukan {sisa} diagnosa lagi sebelum perlu login.")

    if "diagnosis" in st.session_state:
        hasil = st.session_state["diagnosis"].replace("Kemungkinan: ", "")
        info = penyakit_info.get(hasil)

        st.subheader("🔍 Hasil Diagnosa:")
        st.success(st.session_state["diagnosis"])

        if info:
            st.markdown(f"**Deskripsi:** {info['deskripsi']}")
            st.markdown(f"**Penyebab Umum:** {info['penyebab']}")
            st.markdown(f"**Penanganan:** {info['penanganan']}")
            # st.image(info['gambar'], caption=hasil, use_column_width=True)
