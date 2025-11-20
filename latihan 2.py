mahasiswa = {}

def hitung_nilai_akhir(tugas, uts, uas):
    return (tugas * 0.30) + (uts * 0.35) + (uas * 0.35)

while True:
    print("\n=== PROGRAM DATA NILAI MAHASISWA ===")
    print("1. Tambah Data")
    print("2. Ubah Data")
    print("3. Hapus Data")
    print("4. Tampilkan Data")
    print("5. Cari Data")
    print("0. Keluar")

    pilihan = input("Pilih menu: ")

    if pilihan == '1':
        nama = input("Nama mahasiswa: ")
        tugas = float(input("Nilai Tugas: "))
        uts = float(input("Nilai UTS: "))
        uas = float(input("Nilai UAS: "))
        nilai_akhir = hitung_nilai_akhir(tugas, uts, uas)

        mahasiswa[nama] = {
            'tugas': tugas,
            'uts': uts,
            'uas': uas,
            'akhir': nilai_akhir
        }
        print("Data berhasil ditambahkan!")

    elif pilihan == '2':
        nama = input("Masukkan nama yang ingin diubah: ")
        if nama in mahasiswa:
            tugas = float(input("Nilai Tugas baru: "))
            uts = float(input("Nilai UTS baru: "))
            uas = float(input("Nilai UAS baru: "))
            nilai_akhir = hitung_nilai_akhir(tugas, uts, uas)

            mahasiswa[nama] = {
                'tugas': tugas,
                'uts': uts,
                'uas': uas,
                'akhir': nilai_akhir
            }
            print("Data berhasil diubah!")
        else:
            print("Data tidak ditemukan!")

    elif pilihan == '3':
        nama = input("Masukkan nama yang ingin dihapus: ")
        if nama in mahasiswa:
            del mahasiswa[nama]
            print("Data berhasil dihapus!")
        else:
            print("Data tidak ditemukan!")

    elif pilihan == '4':
        print("\n=== DATA NILAI MAHASISWA ===")
        if mahasiswa:
            for nama, nilai in mahasiswa.items():
                print(f"{nama} | Tugas:{nilai['tugas']} UTS:{nilai['uts']} UAS:{nilai['uas']} Nilai Akhir:{nilai['akhir']:.2f}")
        else:
            print("Belum ada data!")

    elif pilihan == '5':
        nama = input("Masukkan nama yang dicari: ")
        if nama in mahasiswa:
            nilai = mahasiswa[nama]
            print(f"{nama} → Tugas:{nilai['tugas']}, UTS:{nilai['uts']}, UAS:{nilai['uas']}, Akhir:{nilai['akhir']:.2f}")
        else:
            print("Data tidak ditemukan!")

    elif pilihan == '0':
        print("Keluar dari program.")
        break

    else:
        print("Pilihan tidak valid!")
