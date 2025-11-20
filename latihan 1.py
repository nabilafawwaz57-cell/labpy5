kontak = {
    "Ari": "081267888",
    "Dina": "087677776"
}

print("Kontak Ari:", kontak["Ari"])

kontak["Riko"] = "087654544"
print("Kontak setelah tambah Riko:", kontak)

kontak["Dina"] = "088999776"
print("Kontak setelah ubah Dina:", kontak)

print("Semua Nama:", list(kontak.keys()))

print("Semua Nomor:", list(kontak.values()))

print("Daftar Kontak:")
for nama, nomor in kontak.items():
    print(f"{nama} : {nomor}")

del kontak["Dina"]
print("Kontak setelah hapus Dina:", kontak)