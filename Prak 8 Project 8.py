# Rumus

Buah = { 'apel'  : 5000,
          'jeruk' : 8500,
          'mangga': 7800,
          'duku'  : 6500 }
def rata2HargaBuah(Buah):
    totalHarga = 0
    jumlah = 0
    for r,y in buah.items():
        totalHarga += y
        jumlah += 1
    rata2 = totalHarga/jumlah
    return rata2
def ratarataHargaBuah(Buah):
    harga = list(Buah.values())
    rata = sum(harga)/len(harga)
    return rata
a = ratarataHargaBuah(Buah)
b = ratarataHargaBuah(Buah)

# Output

print(a)
print(b)
print('Rata-rata harga buah adalah :',a)
print('Rata-rata harga buah adalah :',b)