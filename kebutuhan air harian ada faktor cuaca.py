import streamlit as st

st.set_page_config(page_title="Kebutuhan Air Harian", layout="centered")

st.title("💧 Kalkulator Kebutuhan Air Harian")
st.write("Hitung kebutuhan air harianmu berdasarkan berat badan, aktivitas, dan kondisi cuaca.")

# Input pengguna
berat = st.number_input("Masukkan berat badan kamu (kg):", min_value=1.0, step=0.5)
aktivitas = st.selectbox("Pilih tingkat aktivitas:", ["Ringan", "Sedang", "Berat"])
cuaca = st.selectbox("Bagaimana kondisi cuaca di tempatmu sekarang?", ["Dingin", "Normal", "Panas"])

# Fungsi perhitungan
def hitung_air(berat, aktivitas, cuaca):
    dasar = berat * 30  # 30 ml per kg

    if aktivitas == "Sedang":
        dasar += 300
    elif aktivitas == "Berat":
        dasar += 600

    if cuaca == "Panas":
        dasar += 400
    elif cuaca == "Dingin":
        dasar -= 200

    return dasar / 1000  # Liter

# Tombol dan hasil
if st.button("Hitung Kebutuhan Air"):
    if berat > 0:
        total = hitung_air(berat, aktivitas, cuaca)
        st.success(f"Kebutuhan air harian kamu sekitar *{total:.2f} liter*.")
    else:
        st.warning("Masukkan berat badan yang valid.")
st.markdown("---")
st.caption("Proyek Streamlit oleh [KELOMPOK 7]")
