import streamlit as st
import numpy as np
import joblib

# Judul aplikasi
st.set_page_config(page_title="Prediksi Attrition Karyawan", page_icon="🧠", layout="centered")
st.title("🧠 Prediksi Attrition Karyawan")
st.markdown("Masukkan data karyawan untuk memprediksi apakah karyawan **akan keluar (attrition)** atau tidak.")

# Load model
@st.cache_resource
def load_model():
    return joblib.load("model.pkl")

model = load_model()

# Data contoh
example_input = [0, 0, 0, 0, 1, 0, -1, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 1, 1, 0, 0, 0]

# Input dari pengguna
st.subheader("🔧 Input Data")
use_example = st.checkbox("Gunakan data contoh", value=True)

if use_example:
    input_data = example_input
else:
    input_data = []
    for i in range(len(example_input)):
        val = st.number_input(f"Fitur {i+1}", value=float(example_input[i]), step=1.0)
        input_data.append(val)

# Prediksi ketika tombol diklik
if st.button("🔍 Prediksi"):
    X_new = np.array(input_data).reshape(1, -1)
    prediction = model.predict(X_new)[0]
    probability = model.predict_proba(X_new)[0][1]

    st.subheader("📊 Hasil Prediksi:")
    if prediction == 1:
        st.error("❌ Karyawan **AKAN KELUAR (Attrition)**", icon="🚨")
    else:
        st.success("✅ Karyawan **TIDAK AKAN KELUAR**", icon="🎉")

    st.info(f"🧮 Probabilitas keluar: **{probability:.2%}**")

# Footer
st.markdown("---")
st.markdown("🚀 Dibuat dengan Streamlit oleh Tim Data Jaya Jaya Maju")
