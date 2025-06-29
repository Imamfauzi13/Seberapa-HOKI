# -*- coding: utf-8 -*-
"""Peluang Keberuntungan

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1RCToderPauk_y1iSPPNe_ho2UynPItej
"""

import streamlit as st
import time

st.set_page_config(page_title="Kalkulator Peluang", page_icon="🎲")

st.title("🎲 Kalkulator Peluang Sederhana")
st.write("Aplikasi ini menghitung peluang suatu kejadian dengan rumus dasar:")
st.latex(r"P(A) = \frac{n(A)}{n(S)}")

# Input
n_A = st.number_input("Masukkan banyak kejadian (n(A)):", min_value=0, value=1)
n_S = st.number_input("Masukkan banyak ruang sampel (n(S)):", min_value=1, value=1)

if st.button("🎯 Hitung Peluang"):
    placeholder = st.empty()

    # Simulasi animasi loading
    placeholder.markdown("⏳ Menghitung peluang .")
    time.sleep(0.3)
    placeholder.markdown("⏳ Menghitung peluang ..")
    time.sleep(0.3)
    placeholder.markdown("⏳ Menghitung peluang ...")
    time.sleep(0.3)

    peluang = n_A / n_S
    placeholder.success(f"✅ Peluang kejadian adalah: *{peluang:.4f}*")
