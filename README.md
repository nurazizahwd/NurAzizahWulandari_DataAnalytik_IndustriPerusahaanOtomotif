## Identitas

<table align="center">
  <tr><td>Nama</td><td>Nur Azizah Wulandari</td></tr>
  <tr><td>NIM</td><td>12030122120047</td></tr>
  <tr><td>Mata Kuliah</td><td>Pengkodean dan Pemograman Kelas E</td></tr>
  <tr><td>Dosen</td><td>Dr. Totok Dewayanto, SE., M.Si, Ak, CA</td></tr>
</table>

----------------
## Data Analisis
<p align="center">
</p>
<h1 align="center">Data Analisis Perusahaan Industri Otomotif</h1>
<ul>
  <p>Sebagai seorang Data Analisis, Anda memiliki kontrol penuh atas data ini dan perlu teliti dalam melakukan analisis.</p>
  <ul>
    
<h4>Pengumpulan Data:</h4>
    <li>Mengumpulkan data dari berbagai sumber (database, web scraping, survei, dll.)</li>
    <li>Memastikan data yang dikumpulkan relevan dengan tujuan analisis.</li>
</ul>
<h4>Pembersihan Data:</h4>
    <li>Membersihkan data dari kesalahan, duplikasi, dan inkonsistensi.</li>
    <li>Mengatasi data yang hilang dan memastikan data dalam format yang tepat.    </li>
  </ul>
 <h4>Analisis Eksploratif:</h4>
    <li>Melakukan analisis statistik deskriptif untuk memahami pola dalam data.</li>
    <li>Menggunakan visualisasi data untuk mengidentifikasi tren dan anomali.</li>
  </ul>
 <h4>Transformasi Data:</h4>
    <li>Melakukan transformasi data seperti normalisasi, standardisasi, atau pembuatan fitur baru yang relevan.</li>
    <li>Menggunakan teknik seperti pengelompokan atau pengurangan dimensi untuk menyederhanakan data.</li>
  </ul>
 <h4>Pemodelan Data:</h4>
    <li>Membangun dan menguji model statistik atau machine learning.</li>
    <li>Melakukan validasi dan optimisasi model untuk memastikan keakuratan dan kinerja.</li>
  </ul>
  <h4>Interpretasi dan Presentasi:</h4>
    <li>Menginterpretasikan hasil analisis dan menyajikannya dalam bentuk laporan atau presentasi.</li>
    <li>Membuat visualisasi data yang informatif untuk menyampaikan temuan kepada pemangku kepentingan.</li>
  </ul>
  <h4>Rekomendasi dan Implementasi:</h4>
    <li>Memberikan rekomendasi berdasarkan temuan analisis.</li>
    <li>Bekerja sama dengan tim lain untuk mengimplementasikan solusi yang disarankan.</li>
  </ul>
  

## 💻 Panduan Analisis Menggunakan VSCode

1. **Buat tabel data sesuai apa yang diinginkan**
```bash
misalnya:
produksi
penjualan
model produk
persediaan

git clone https://github.com/Arielanaskar/app_kasir_restoran.git
cd app_kasir_restoran
composer install
copy .env.example rename->.env
```
2. **Buka ```.env``` lalu ubah baris berikut sesuaikan dengan databasemu yang ingin dipakai**
```
DB_PORT=3306
DB_DATABASE=app_kasir_restoran
DB_USERNAME=root
DB_PASSWORD=
```

3. **Migration & Seeder Database SQL** (pastikan internet nyala, untuk mengunduh gambar dari setiap menu)
```bash
php artisan migrate
php artisan db:seed
```

4. **Jalankan bash**
```bash
php artisan key:generate
php artisan config:cache
php artisan storage:link
php artisan route:clear
```

5. **Jalankan website**
```bash
php artisan serve
```
