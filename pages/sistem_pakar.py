import streamlit as st
from experta import *
from gtts import gTTS


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
        "deskripsi": "Penyakit saluran pernapasan kronis yang menyebabkan sesak napas, batuk, dan mengi, seringkali dipicu oleh faktor lingkungan atau alergi",
        "penyebab": "Debu, polusi udara, alergi, udara dingin, infeksi saluran pernapasan, aktivitas fisik berat",
        "penanganan": "Gunakan inhaler (bronchodilator atau steroid inhalasi), hindari pemicu (seperti debu dan polusi), kontrol stres, dan konsultasi dengan dokter untuk perawatan jangka panjang",
    },
    "Stroke": {
        "deskripsi": "Kondisi medis yang terjadi ketika suplai darah ke otak terganggu, menyebabkan kerusakan pada jaringan otak. Gejalanya bisa meliputi kelemahan tubuh, kesulitan berbicara, atau kebingungan",
        "penyebab": "Hipertensi, kolesterol tinggi, merokok, diabetes, obesitas, dan faktor genetik",
        "penanganan": "Obat pengencer darah untuk mencegah pembekuan darah, fisioterapi untuk rehabilitasi, intervensi medis darurat (seperti trombolisis atau pembedahan) untuk mengurangi kerusakan otak",
    },
    "Osteoporosis": {
        "deskripsi": "Penyakit yang menyebabkan penurunan kepadatan tulang, sehingga tulang menjadi rapuh dan lebih rentan terhadap patah",
        "penyebab": "Kurangnya asupan kalsium dan vitamin D, penuaan, gangguan hormonal, keturunan, dan gaya hidup tidak aktif",
        "penanganan": "Suplemen kalsium dan vitamin D, olahraga beban untuk memperkuat tulang, terapi hormon untuk meningkatkan kepadatan tulang, dan obat-obatan untuk memperlambat kerusakan tulang",
    },
    "Hypertension": {
        "deskripsi": "Tekanan darah tinggi, suatu kondisi medis di mana tekanan darah terus menerus berada pada angka yang lebih tinggi dari normal, meningkatkan risiko penyakit jantung dan stroke",
        "penyebab": "Asupan garam berlebih, stres, kurang olahraga, obesitas, genetika, dan kebiasaan merokok",
        "penanganan": "Obat-obatan untuk menurunkan tekanan darah, diet rendah garam, peningkatan aktivitas fisik, serta pengelolaan stres",
    },
    "Diabetes": {
        "deskripsi": "Penyakit kronis yang ditandai dengan kadar gula darah yang tinggi, akibat gangguan dalam metabolisme insulin",
        "penyebab": "Faktor genetik, pola makan tidak sehat, obesitas, dan kurangnya aktivitas fisik",
        "penanganan": "Kontrol gula darah dengan diet sehat, olahraga teratur, pemantauan kadar glukosa, dan penggunaan insulin atau obat oral sesuai kebutuhan",
    },
    "Migraine": {
        "deskripsi": "Sakit kepala berulang yang seringkali disertai dengan mual, muntah, dan sensitivitas terhadap cahaya dan suara. Migrain dapat berlangsung dari beberapa jam hingga beberapa hari",
        "penyebab": "Stres, perubahan hormon, pola makan, kurang tidur, dan pemicu lingkungan lainnya seperti cahaya terang dan bau yang kuat",
        "penanganan": "Penggunaan obat pereda nyeri, obat untuk mencegah serangan migrain, serta menghindari pemicu yang diketahui",
    },
    "Influenza": {
        "deskripsi": "Infeksi virus yang menyerang saluran pernapasan atas, menyebabkan gejala seperti demam, batuk, nyeri tubuh, dan kelelahan",
        "penyebab": "Virus influenza yang menyebar melalui udara dan kontak langsung dengan orang yang terinfeksi",
        "penanganan": "Istirahat yang cukup, konsumsi cairan hangat, obat antivirus (seperti oseltamivir), serta vaksinasi flu tahunan untuk pencegahan",
    },
    "Pneumonia": {
        "deskripsi": "Infeksi pada paru-paru yang menyebabkan peradangan, gejalanya bisa meliputi batuk, sesak napas, demam, dan nyeri dada",
        "penyebab": "Bakteri, virus, atau jamur yang menginfeksi paru-paru, seringkali setelah infeksi saluran pernapasan atas",
        "penanganan": "Antibiotik atau antiviral untuk infeksi bakteri atau virus, cairan infus untuk mencegah dehidrasi, dan perawatan rumah sakit untuk kasus yang lebih parah",
    },
    "Bronchitis": {
        "deskripsi": "Peradangan pada saluran bronkus yang membawa udara ke paru-paru. Gejalanya termasuk batuk berdahak, sesak napas, dan rasa nyeri pada dada",
        "penyebab": "Infeksi virus (terutama), merokok, atau paparan polusi udara",
        "penanganan": "Istirahat, minum cukup air, obat batuk atau dekongestan, serta menghindari asap rokok dan polusi udara",
    },
    "Hyperthyroidism": {
        "deskripsi": "Kondisi di mana kelenjar tiroid menghasilkan hormon tiroid dalam jumlah berlebih, yang dapat menyebabkan peningkatan metabolisme tubuh",
        "penyebab": "Penyakit Graves, nodul tiroid, atau tiroiditis",
        "penanganan": "Obat anti-tiroid untuk mengurangi produksi hormon, terapi yodium radioaktif untuk menghancurkan sebagian jaringan tiroid, atau pembedahan untuk mengangkat kelenjar tiroid",
    },
    "Hypothyroidism": {
        "deskripsi": "Kondisi di mana kelenjar tiroid kurang aktif dalam memproduksi hormon tiroid, yang dapat memperlambat metabolisme tubuh",
        "penyebab": "Gangguan autoimun seperti Hashimoto's thyroiditis, kekurangan yodium, atau pengobatan sebelumnya untuk hipertiroidisme",
        "penanganan": "Penggantian hormon tiroid melalui terapi hormon tiroid (levothyroxine)",
    },
    "Osteoarthritis": {
        "deskripsi": "Penyakit degeneratif sendi yang terjadi akibat kerusakan pada tulang rawan, menyebabkan rasa sakit dan kekakuan pada sendi",
        "penyebab": "Penuaan, cedera sendi sebelumnya, obesitas, dan penggunaan sendi yang berlebihan",
        "penanganan": "Fisioterapi untuk memperkuat otot sekitar sendi, obat anti-inflamasi untuk mengurangi peradangan, dan operasi penggantian sendi jika diperlukan",
    },
    "Kidney Cancer": {
        "deskripsi": "Kanker yang dimulai pada ginjal, seringkali tidak menimbulkan gejala pada tahap awal",
        "penyebab": "Merokok, obesitas, hipertensi, dan riwayat keluarga dengan kanker ginjal",
        "penanganan": "Operasi untuk mengangkat ginjal yang terkena, imunoterapi, kemoterapi, atau terapi target",
    },
    "Common Cold": {
        "deskripsi": "Infeksi ringan yang disebabkan oleh berbagai virus, terutama rhinovirus, yang menyerang saluran pernapasan atas",
        "penyebab": "Virus rhinovirus yang dapat menyebar melalui tetesan udara atau kontak langsung",
        "penanganan": "Istirahat yang cukup, konsumsi cairan hangat, obat pereda gejala seperti dekongestan dan parasetamol",
    },
    "Liver Cancer": {
        "deskripsi": "Kanker yang dimulai pada hati, sering kali berkembang setelah kondisi hati kronis seperti sirosis atau infeksi hepatitis",
        "penyebab": "Hepatitis B dan C, konsumsi alkohol berlebihan, dan riwayat keluarga dengan kanker hati",
        "penanganan": "Operasi pengangkatan tumor, kemoterapi, imunoterapi, atau transplantasi hati untuk kasus yang lebih parah",
    },
}


def diagnosa_penyakit():
    # Batasan Diagnosa untuk User Guest
    if "logged_in" not in st.session_state:
        st.session_state["logged_in"] = False
    if "guest_diagnosis_count" not in st.session_state:
        st.session_state["guest_diagnosis_count"] = 0
    if "play_audio" not in st.session_state:
        st.session_state["play_audio"] = False

    # Streamlit Interface
    st.title(":stethoscope: Diagnosa Penyakit Umum")

    # Cek batasan untuk tamu
    if (
        not st.session_state["logged_in"]
        and st.session_state["guest_diagnosis_count"] >= 3
    ):
        st.warning(
            "🔒 Anda telah mencapai batas maksimum 3 kali diagnosa sebagai pengguna tamu. Silakan login untuk melanjutkan."
        )
        st.stop()

    with st.container(border=True):
        st.write("Silakan isi gejala berikut:")

        with st.expander("Demam?", icon=":material/sick:"):
            deskripsi = """
                Demam adalah kondisi ketika suhu tubuh meningkat di atas normal, biasanya di atas 37.5°C.
                \nIni merupakan respons alami tubuh terhadap infeksi bakteri atau virus, dan menandakan bahwa sistem kekebalan sedang bekerja.
                \nSelain suhu tubuh tinggi, gejala demam juga bisa disertai menggigil, sakit kepala, dan kelelahan.
                \nMeskipun sebagian besar demam bersifat ringan dan bisa sembuh sendiri, demam tinggi yang berkepanjangan dapat mengindikasikan kondisi serius yang memerlukan penanganan medis.
            """

            st.markdown(deskripsi)
            if st.button(
                "🔊 Baca penjelasan", key="baca_fever", use_container_width=True
            ):
                play_audio(deskripsi, autoplay=True)
            st.divider()
            fever = st.selectbox(
                "Apakah Anda mengalami demam:", ["Ya", "Tidak"], key="fever"
            )

        with st.expander("Batuk?", icon=":material/coronavirus:"):
            deskripsi = """
                Batuk adalah refleks tubuh untuk membersihkan saluran napas dari lendir, debu, atau iritasi lain.
                \nBatuk bisa disebabkan oleh infeksi virus seperti flu dan pilek, alergi, asma, atau kondisi kronis seperti bronkitis dan pneumonia.
                \nBatuk yang berlangsung lebih dari dua minggu atau disertai darah dan nyeri dada perlu dievaluasi lebih lanjut oleh tenaga medis.
                \nMengetahui jenis batuk (kering, berdahak, atau kronis) dapat membantu menentukan penyebab dan pengobatan yang tepat.
            """

            st.markdown(deskripsi)
            if st.button(
                "🔊 Baca penjelasan", key="baca_cough", use_container_width=True
            ):
                play_audio(deskripsi, autoplay=True)
            st.divider()
            cough = st.selectbox(
                "Apakah Anda mengalami batuk:", ["Ya", "Tidak"], key="cough"
            )

        with st.expander("Kelelahan?", icon=":material/dark_mode:"):
            deskripsi = """
                Kelelahan adalah perasaan lelah atau kurang energi yang berkepanjangan dan tidak membaik setelah istirahat. 
                \nHal ini bisa disebabkan oleh kurang tidur, stres, anemia, diabetes, gangguan tiroid, atau infeksi kronis. 
                \nKelelahan yang menetap dapat memengaruhi produktivitas, suasana hati, dan kualitas hidup. 
                \nJika disertai dengan gejala lain seperti sesak napas, nyeri dada, atau penurunan berat badan, sebaiknya segera periksa ke dokter.
            """

            st.markdown(deskripsi)
            if st.button(
                "🔊 Baca penjelasan", key="baca_fatigue", use_container_width=True
            ):
                play_audio(deskripsi, autoplay=True)
            st.divider()
            fatigue = st.selectbox(
                "Apakah Anda sering kelelahan:", ["Ya", "Tidak"], key="fatigue"
            )

        with st.expander("Kesulitan Bernapas?", icon=":material/pulmonology:"):
            deskripsi = """
                \nKesulitan bernapas atau sesak napas (dispnea) adalah kondisi ketika seseorang merasa napasnya pendek atau tidak cukup udara. 
                \nIni bisa disebabkan oleh gangguan paru-paru seperti asma, pneumonia, atau penyakit paru obstruktif kronis (PPOK), serta masalah jantung seperti gagal jantung. 
                \nGejala ini bisa terjadi tiba-tiba atau perlahan dan dapat diperparah dengan aktivitas. 
                \nJika disertai nyeri dada, bibir membiru, atau kehilangan kesadaran, ini merupakan kondisi darurat medis.
            """

            st.markdown(deskripsi)
            if st.button(
                "🔊 Baca penjelasan",
                key="baca_difficulty_breathing",
                use_container_width=True,
            ):
                play_audio(deskripsi, autoplay=True)
            st.divider()
            difficulty_breathing = st.selectbox(
                "Apakah Anda kesulitan bernapas:", ["Ya", "Tidak"], key="breath"
            )

        with st.expander("Tekanan Darah", icon=":material/blood_pressure:"):
            deskripsi = """
                \nTekanan darah adalah ukuran kekuatan darah terhadap dinding arteri saat dipompa oleh jantung. 
                \nTekanan darah normal berkisar antara 90/60 mmHg hingga 120/80 mmHg. 
                \nTekanan darah rendah (hipotensi) dapat menyebabkan pusing dan pingsan, sedangkan tekanan darah tinggi (hipertensi) bisa merusak jantung, ginjal, dan pembuluh darah dalam jangka panjang. 
                \nPemantauan tekanan darah secara rutin penting untuk mencegah komplikasi serius.
            """

            st.markdown(deskripsi)
            if st.button(
                "🔊 Baca penjelasan",
                key="baca_blood_pressure",
                use_container_width=True,
            ):
                play_audio(deskripsi, autoplay=True)
            st.divider()
            blood_pressure = st.selectbox(
                "Pilih level tekanan darah Anda:",
                ["Rendah", "Normal", "Tinggi"],
                key="bp",
            )

        with st.expander("Level Kolesterol", icon=":material/lunch_dining:"):
            deskripsi = """
                \nKolesterol adalah zat lemak yang penting untuk fungsi tubuh, tetapi kadar kolesterol yang tinggi dapat membahayakan kesehatan. 
                \nKolesterol tinggi sering kali tidak menunjukkan gejala namun dapat menyumbat pembuluh darah dan meningkatkan risiko penyakit jantung dan stroke. 
                \nFaktor risiko termasuk pola makan tinggi lemak jenuh, kurang olahraga, merokok, dan faktor genetik. 
                \nPenting untuk melakukan pemeriksaan darah secara rutin untuk memantau kadar kolesterol Anda.
            """

            st.markdown(deskripsi)
            if st.button(
                "🔊 Baca penjelasan", key="baca_cholesterol", use_container_width=True
            ):
                play_audio(deskripsi, autoplay=True)
            st.divider()
            cholesterol = st.selectbox(
                "Pilih level kolesterol Anda:", ["Normal", "Tinggi"], key="cholesterol"
            )

        with st.expander("Usia", icon=":material/calendar_month:"):
            deskripsi = """
                \nUsia merupakan salah satu faktor risiko utama untuk berbagai kondisi kesehatan. 
                \nSeiring bertambahnya usia, risiko terkena penyakit jantung, diabetes, tekanan darah tinggi, dan kanker meningkat. 
                \nPerubahan fisiologis seperti metabolisme yang melambat dan sistem kekebalan yang melemah juga membuat lansia lebih rentan terhadap infeksi. 
                \nMengetahui risiko terkait usia membantu dalam mengambil langkah pencegahan sejak dini.
            """

            st.markdown(deskripsi)
            if st.button(
                "🔊 Baca penjelasan", key="baca_age", use_container_width=True
            ):
                play_audio(deskripsi, autoplay=True)
            st.divider()
            age = st.slider("Masukkan usia Anda:", 1, 100, 25, key="age")

        with st.expander("Jenis Kelamin", icon=":material/wc:"):
            deskripsi = """
                \nJenis kelamin dapat memengaruhi kecenderungan seseorang terhadap penyakit tertentu. 
                \nMisalnya, pria lebih sering mengalami penyakit jantung di usia muda, sedangkan wanita lebih berisiko terkena osteoporosis dan penyakit autoimun. 
                \nSelain faktor biologis, perbedaan gaya hidup dan akses kesehatan antara laki-laki dan perempuan juga dapat berpengaruh. 
                \nMemahami perbedaan ini penting untuk pendekatan kesehatan yang lebih personal dan efektif.
            """

            st.markdown(deskripsi)
            if st.button(
                "🔊 Baca penjelasan", key="baca_gender", use_container_width=True
            ):
                play_audio(deskripsi, autoplay=True)
            st.divider()
            gender = st.selectbox(
                "Pilih jenis kelamin Anda:", ["Laki-laki", "Perempuan"], key="gender"
            )

        submitted = st.button("Diagnosa", type="primary", use_container_width=True)

    if submitted:
        # Tambah counter jika user belum login
        if not st.session_state["logged_in"]:
            st.session_state["guest_diagnosis_count"] += 1

        # Reset diagnosis
        st.session_state["diagnosis"] = "Tidak ditemukan diagnosis yang cocok."

        # Siapkan engine dan fakta
        engine = SistemPakarPenyakit()
        engine.reset()

        # Kategorisasi usia
        if age > 50:
            age_category = "Di atas 50"
        elif age > 45:
            age_category = "Di atas 45"
        else:
            age_category = "Di bawah 45"

        # Masukkan fakta gejala
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

    # Tampilkan batas tamu
    if not st.session_state["logged_in"]:
        sisa = 3 - st.session_state["guest_diagnosis_count"]
        st.info(f"Anda dapat melakukan {sisa} diagnosa lagi sebelum perlu login.")

    # Tampilkan hasil diagnosa
    if "diagnosis" in st.session_state:
        st.divider()

        hasil = st.session_state["diagnosis"].replace("Kemungkinan: ", "")
        info = penyakit_info.get(hasil)

        col1, col2 = st.columns(spec=2, vertical_alignment="center")
        col1.metric(
            label="Hasil Diagnosa",
            value=hasil,
            delta="Kemungkinan",
            delta_color="inverse",
            border=True,
        )

        # Ucapkan dengan gTTS dalam Bahasa Indonesia
        ucapan = f"Hasil diagnosa Anda adalah kemungkinan {hasil}.\n\n{hasil} merupakan: {info['deskripsi']}.\n\n{hasil} disebabkan oleh: {info['penyebab']}.\n\nPenanganan yang disarankan adalah: {info['penanganan']}."
        if col2.button("🔊 Putar Suara Hasil Diagnosa", use_container_width=True):
            st.session_state["play_audio"] = True

        col2.download_button(
            label="Download hasil diganosis",
            data=ucapan,
            file_name="diagnosis_result.txt",
            on_click="ignore",
            type="primary",
            icon=":material/download:",
            use_container_width=True,
        )

        # Setelah tombol ditekan (jika True), jalankan fungsi play_audio
        if st.session_state["play_audio"]:
            play_audio(ucapan, True)
            st.session_state["play_audio"] = (
                False  # Reset agar tidak memutar otomatis lagi
            )

        st.divider()
        if info:

            st.markdown("### 💡 Saran Kesehatan Berdasarkan Data Anda")
            st.info(f"**Deskripsi:** {info['deskripsi']}.")
            st.warning(f"**Penyebab Umum:** {info['penyebab']}.")
            st.success(f"**Penanganan:** {info['penanganan']}.")


def play_audio(text, autoplay):
    tts = gTTS(text, lang="id")  # Gunakan bahasa Indonesia
    tts.save("output.mp3")

    # Tampilkan audio di Streamlit
    with open("output.mp3", "rb") as audio_file:
        audio_bytes = audio_file.read()
        st.audio(audio_bytes, format="audio/mp3", autoplay=autoplay)
