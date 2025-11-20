# labpy5
Nama         : Nabila Fawwaz Nurliah

NIM          : 312510255

Kelas        : TI.25.A.2

Pertemuan    : 10

📘 README.md – Program Daftar Nilai Mahasiswa & Latihan Dictionary

📌 Deskripsi Project

Repository ini berisi dua program Python:

1. Program Daftar Nilai Mahasiswa (nilai_mahasiswa.py)

   Program menampilkan dan mengelola daftar nilai mahasiswa menggunakan dictionary, sesuai ketentuan praktikum:

    - Tambah Data

    - Ubah Data

    - Hapus Data

    - Tampilkan Data

    - Cari Data

    Nilai Akhir dihitung dari:

    - Tugas: 30%

    - UTS: 35%

    - UAS: 35%

2. Program Latihan Dictionary Kontak (kontak.py)

    Latihan dasar penggunaan dictionary:

    - Menampilkan kontak berdasarkan nama

    - Menambah kontak

    - Mengubah kontak

    - Menghapus kontak

    - Menampilkan semua nama & nomor

📂 Struktur Folder

```
📁 project

│── nilai_mahasiswa.py

│── kontak.py

│── README.md
```

🚀 Cara Menjalankan Program

1. Clone Repository

```
git clone https://github.com/username/nama-repository.git

cd nama-repository
```

2. Jalankan program nilai mahasiswa

```
python nilai_mahasiswa.py
```

3. Jalankan program latihan kontak

```
python kontak.py
```

📘 Flowchart Program Nilai Mahasiswa

```
               ┌────────────────────────┐
               │      Mulai Program     │
               └───────────┬────────────┘
                           │
                 ┌─────────▼───────────┐
                 │   Tampilkan Menu    │
                 └─────────┬───────────┘
                           │
        ┌──────────────────┼─────────────────────┐
        │                  │                     │
   ┌────▼────┐        ┌────▼────┐           ┌────▼────┐
   │ Tambah  │        │  Ubah   │           │  Hapus   │
   │  Data   │        │  Data   │           │  Data    │
   └────┬────┘        └────┬────┘           └────┬────┘
        │                  │                     │
        ▼                  ▼                     ▼
   Simpan Data       Update Data            Hapus Data
        │                  │                     │
        └──────────┬──────┴───────┬─────────────┘
                   │              │
              ┌────▼────┐   ┌────▼────┐
              │Tampilkan│   │  Cari   │
              │  Data   │   │  Data   │
              └────┬────┘   └────┬────┘
                   │              │
                   └───────┬──────┘
                           │
                   ┌───────▼────────┐
                   │  Keluar Program │
                   └─────────────────┘
```

📄 Penjelasan Program Singkat

nilai_mahasiswa.py

- Data mahasiswa disimpan dalam dictionary :

  ```
  mahasiswa = {
  
    "Nama": {"tugas": xx, "uts": xx, "uas": xx, "akhir": xx}
  
  }
  ```
- Program menggunakan looping menu

- Perhitungan nilai akhir menggunakan fungsi:

  ```
  def hitung_nilai_akhir(tugas, uts, uas):
  
    return (tugas*0.30) + (uts*0.35) + (uas*0.35)
  ```

# kontak.py

Dictionary awal:

```
kontak = {

    "Ari": "081267888",

    "Dina": "087677776"

}
```

Program melakukan:

- Menampilkan kontak tertentu

- Menambah kontak baru

- Mengubah nomor kontak

- Menampilkan semua nama dan nomor

- Menghapus satu kontak


✨ Lisensi

Project ini bebas digunakan untuk belajar dan tugas perkuliahan.
