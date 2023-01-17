txt = 'Hello World'

# Hitung jumlah karakternya
jumlah_karakter = len(txt)
print("Jumlah karakter = ",len(txt))

# Ambil karakter terakhir
karakter_terakhir = txt[-1]
print(karakter_terakhir)

# Ambil karakter index ke-2 sampai index ke-4 (llo)
karakter_2_4 = txt[2:5]
print(karakter_2_4)

# Hilangkan spasi pada text tersebut (HelloWorld)
txt_tanpa_spasi = txt.replace(' ', '')
print(txt_tanpa_spasi)

# Ubah text menjadi huruf besar
txt_huruf_besar = txt.upper()
print(txt_huruf_besar)

# Ubah text menjadi huruf kecil
txt_huruf_kecil = txt.lower()
print(txt_huruf_kecil)

# Ganti karakter H dengan karakter J
txt_ganti_karakter = txt.replace('H', 'J')
print(txt_ganti_karakter)