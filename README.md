<h1><p align="center">UTS Pengolahan Citra</h1><br>

 <table border="1">
  <tr>
    <th colspan="2">Kelompok</th>
  </tr>
 	<tr>
 		<th> Nama </th>
 		<th> NIM </th>
 	</tr>
 	<tr>
 		<td> Muhammad Reza Maulana</td>
 		<td> 312210303</td>
 	</tr>
  <tr>
 		<td> Rini Ariza</td>
 		<td> 312210337</td>
 	</tr>
  <tr>
 		<td> Aan Fadillah Putra</td>
 		<td> 312210327</td>
 	</tr>
   	<tr>
 		<td> Chaerul Hidayat</td>
 		<td> 312210300</td>
 	</tr>
 </table>

---

## Sistem Pengolahan Citra Gambar dengan OpenCV Menggunakan Streamlit

### Pengenalan Streamlit
Streamlit adalah kerangka kerja sumber terbuka (open-source) yang dirancang untuk memudahkan pembuatan aplikasi web interaktif secara langsung dari skrip Python. Kerangka kerja ini sangat populer di kalangan data scientist, machine learning engineers, dan pengembang karena kesederhanaan dan kecepatannya dalam mengubah skrip analisis data menjadi aplikasi web yang menarik.

### Pengenalan OpenCV
OpenCV (Open Source Computer Vision Library) adalah pustaka open-source yang digunakan untuk pemrosesan citra dan visi komputer. OpenCV dikembangkan untuk menyediakan infrastruktur yang efisien untuk aplikasi visi komputer dan machine learning.

### Cara Penggunaan
1. **Upload Gambar**
   - Unggah gambar dengan format JPG, JPEG, atau PNG menggunakan tombol "Pilih gambar...".

2. **Konversi ke HSV**
   - Tekan tombol "Konversi ke HSV" untuk mengubah gambar yang diunggah ke dalam ruang warna HSV.

3. **Tampilkan Histogram**
   - Tekan tombol "Tampilkan Histogram" untuk menampilkan histogram dari gambar yang diunggah.

4. **Tampilkan Contour**
   - Tekan tombol "Tampilkan Contour" untuk menampilkan kontur dari gambar yang diunggah.

5. **Sesuaikan Kecerahan dan Kontras**
   - Geser slider untuk menyesuaikan kecerahan dan kontras gambar.
   - Tekan tombol "Terapkan" untuk menerapkan perubahan ke gambar.

### Cara Penggunaan
- Pastikan instalasi Streamlit (`pip install streamlit`) dan OpenCV (`pip install opencv-python`) sudah dilakukan sebelum menjalankan aplikasi.
- Jalankan program dengan menjalankan perintah `streamlit run nama_file.py` di terminal/command prompt.
