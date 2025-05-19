# Proyek Akhir: Menyelesaikan Permasalahan Perusahaan Edutech

## Business Understanding

Jaya Jaya Maju adalah perusahaan multinasional yang telah beroperasi sejak tahun 2000, dengan jumlah karyawan mencapai 1.058 orang yang tersebar di berbagai wilayah. Seiring dengan pertumbuhan bisnis yang pesat, perusahaan kini menghadapi tantangan serius dalam mengelola dan mempertahankan tenaga kerjanya.
Berdasarkan data internal, tercatat bahwa 179 karyawan telah keluar dari perusahaan, yang berarti tingkat attrition mencapai sekitar 16.9% angka yang tergolong tinggi dan berpotensi mengganggu kelangsungan operasional serta efisiensi biaya perusahaan

### Permasalahan Bisnis

1. Apa saja faktor utama yang berkontribusi terhadap attrition (pengunduran diri karyawan)?
2. Apakah memungkinkan untuk membangun sebuah model yang dapat memprediksi kemungkinan seorang karyawan akan keluar?
3. Apakah karyawan dengan masa kerja yang lebih pendek atau lebih lama lebih cenderung untuk keluar?
4. Apakah karyawan yang jarang dipromosikan memiliki tingkat attrition yang lebih tinggi?
5. Apakah lembur (overtime) yang berlebihan menjadi faktor penyebab utama karyawan keluar dari perusahaan?

### Cakupan Proyek

- Melakukan eksplorasi data untuk memahami tren attrition berdasarkan karakteristik karyawan.

- Membangun visualisasi interaktif menggunakan Metabase untuk mendukung pengambilan keputusan.

- Membuat model prediksi attrition menggunakan algoritma machine learning.

- Menyediakan insight dan rekomendasi strategis untuk mengurangi attrition.

### Persiapan

Sumber data: dataset yang digunakan merupakan dataset [Jaya Jaya Maju](https://github.com/dicodingacademy/dicoding_dataset/tree/main/employee).

* Setup conda environment:

    ```
    conda create --name proyek-ds-pertama python==3.9.15
    ```
* Install requirements:
    ```
    pip install -r requirements.txt
    ```
* Setup metabase:
    ```
    docker pull metabase/metabase:v0.46.4
    docker run -p 3000:3000 --name metabase metabase/metabase
    ```
    Akses metabase pada http://localhost:3000/setup dan lakukan setup.
* Setup database (supabase):

    - Buat akun dan login https://supabase.com/dashboard/sign-in.
    - Buat new project
    - Copy URI pada database setting
    - Kirim dataset menggunakan sqlalchemy 
    ```python
    from sqlalchemy import create_engine
 
    URL = "DATABASE_URL"
    
    engine = create_engine(URL)
    df.to_sql('data', engine)
    ```

## Business Dashboard

- Memberikan gambaran umum attrition di perusahaan.

- Distribusi berdasarkan Proporsi Gaji Bulanan Berdasarkan Status Attrition.

- Visualisasi hubungan antara attrition dengan promosi terakhir dan masa kerja.

- Dampak Lembur (OverTime) terhadap Attrition.

## Prediksi

cara menjalankan sistem prediksi:

1. Buka terminal pada virtual environment yang telah diaktifkan sebelumnya.

2. Pastikan direktori saat ini berada di folder proyek yang berisi semua berkas yang dibutuhkan, terutama prediction.py dan model.pkl. Jika belum berada di direktori tersebut, gunakan perintah berikut:

'''
    cd path/to/your/project
'''

3. Setelah berada di direktori yang benar, jalankan perintah berikut untuk menjalankan script prediksi:

'''
    python prediction.py
'''


## Conclusion

1. Faktor utama penyebab attrition adalah: gaji bulanan, jarang dipromosikan, tingkat kepuasan kerja rendah, overtime dan usia muda.

2. Model machine learning mampu memprediksi attrition dengan cukup akurat berdasarkan fitur karyawan.

3. Karyawan dengan masa kerja yang lebih pendek cenderung memiliki tingkat attrition yang lebih tinggi.

4. Karyawan yang tidak mendapatkan promosi dalam waktu lama menunjukkan kecenderungan lebih tinggi untuk keluar dari perusahaan.

### Rekomendasi Action Items (Optional)

Berikan beberapa rekomendasi action items yang harus dilakukan perusahaan guna menyelesaikan permasalahan atau mencapai target mereka.

- Tingkatkan frekuensi dan transparansi promosi bagi karyawan berprestasi.

- Pantau beban kerja dan hindari overtime berlebihan.

- Fokus pada employee engagement dan program peningkatan kepuasan kerja.

- Terapkan sistem prediksi churn untuk intervensi dini terhadap karyawan berisiko tinggi keluar.


Username: root@mail.com
Password: root123
