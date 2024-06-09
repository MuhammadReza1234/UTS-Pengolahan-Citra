import streamlit as st
import cv2
import numpy as np
from PIL import Image
import matplotlib.pyplot as plt

st.title("Aplikasi Pengolahan Citra Gambar")

uploaded_file = st.file_uploader("Unggah gambar", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    # Membaca gambar yang diunggah
    image = Image.open(uploaded_file)
    img_array = np.array(image)

    st.info("Pilih Beragam Fitur Berikut:")

    # Menampilkan gambar asli di sidebar
    st.sidebar.subheader("Gambar Asli")
    st.sidebar.image(image, use_column_width=True)

    # Menampilkan kolom untuk tombol
    col1, col2, col3, col4, col5 = st.columns(5)

    # Konversi ke grayscale
    if col1.button("Konversi ke Grayscale"):
        gray_image = cv2.cvtColor(img_array, cv2.COLOR_BGR2GRAY)
        col1.subheader("Gambar Grayscale")
        st.image(gray_image, use_column_width=True, channels='GRAY')

    # Aplikasi Gaussian Blur
    if col2.button("Aplikasi Gaussian Blur"):
        blur_image = cv2.GaussianBlur(img_array, (15, 15), 0)
        col1.subheader("Gambar Gaussian Blur")
        st.image(blur_image, use_column_width=True)

    # Konversi ke gambar biner
    if col3.button("Konversi ke Gambar Biner"):
        gray_image = cv2.cvtColor(img_array, cv2.COLOR_BGR2GRAY)
        _, binary_image = cv2.threshold(gray_image, 127, 255, cv2.THRESH_BINARY)
        col1.subheader("Gambar Biner")
        st.image(binary_image, use_column_width=True, channels='GRAY')

    # Konversi ke gambar biner terbalik
    if col4.button("Konversi ke Gambar Inverse Biner"):
        gray_image = cv2.cvtColor(img_array, cv2.COLOR_BGR2GRAY)
        _, binary_inv_image = cv2.threshold(gray_image, 127, 255, cv2.THRESH_BINARY_INV)
        col1.subheader("Gambar Inverse Biner")
        st.image(binary_inv_image, use_column_width=True, channels='GRAY')

    # Histogram gambar
    if col5.button("Tampilkan Histogram"):
        # Histogram untuk gambar grayscale
        gray_image = cv2.cvtColor(img_array, cv2.COLOR_BGR2GRAY)
        hist_gray = cv2.calcHist([gray_image], [0], None, [256], [0, 256])
        
        # Histogram untuk setiap channel RGB
        chans = cv2.split(img_array)
        colors = ("b", "g", "r")
        hist_data = {}
        
        for (chan, color) in zip(chans, colors):
            hist = cv2.calcHist([chan], [0], None, [256], [0, 256])
            hist_data[color] = hist

        # Plot histogram
        fig, ax = plt.subplots(2, 1, figsize=(10, 8))
        ax[0].plot(hist_gray, color='k')
        ax[0].set_title('Histogram Grayscale')
        ax[0].set_xlim([0, 256])

        for color in colors:
            ax[1].plot(hist_data[color], color=color)
        ax[1].set_title('Histogram RGB')
        ax[1].set_xlim([0, 256])

        col1.subheader("Histogram Gambar")
        st.pyplot(fig)

