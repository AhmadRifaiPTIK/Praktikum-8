
Buah = { "apel"  : 5000,
          "jeruk" : 8500,
          "mangga": 7800,
          "duku"  : 6500 }

def printDataBuah(databaseBuah):
    print("Data Fruit:")
    for i, j in databaseBuah.items():
        print("- {0} (Harga Rp{1} / kg)".format(i,j))
    print("")

def checkOut(databaseFruit,namaFruit,banyakKilo):
    hargaFruit = databaseFruit.get(namaFruit)
    totalHarga = hargaFruit * banyakKilo
    return totalHarga

while True:
    print("Menu :\nA. Tambah Data Fruit\nB. Beli Fruit\nC. Hapus Data Fruit\nD. Keluar")
    opsi = None

    while opsi not in("A","B","C","D"):
        opsi = str(input("Pilihan Menu: "))

        if(opsi == "A"):
            printDataBuah(Buah)
            namaFruitTambahan = str(input("Masukkan nama fruit yang ingin ditambahkan: "))
            if namaFruitTambahan in Buah.keys():

                print("Nama Fruit telah terdaftar dalam database")

            else:
                while True:
                    try:
                        hargaFruitTambahan = int(input("Masukkan harga fruit (hanya angka): "))

                    except ValueError:
                        print("Mohon masukkan hanya angka")
                        continue

                    else:
                        break

                Buah[namaFruitTambahan] = hargaFruitTambahan
                print("{0} dengan harga {1} telah ditambahkan dalam database".format(namaFruitTambahan,hargaFruitTambahan))
                print("")
                printDataBuah(Buah)

        elif(opsi == "B"):
            printDataBuah(Buah)
            totalHarga = 0
            selesai = False
            while not(selesai):
                while True:
                    namaFruit= str(input("Nama fruit yang akan dibeli              : "))

                    if(not(namaFruit in Buah.keys())):
                        print("Nama fruit tidak ditemukan")
                        continue

                    else:
                        break

                while True:
                    try:
                        kiloan = float(input("Berapa kg (jika desimal gunakan titik)   : "))

                    except ValueError:
                        print("Mohon masukkan hanya angka")
                        continue

                    else:
                        break
                totalHarga = totalHarga + checkOut(Buah,namaFruit,kiloan)
                opsi = None

                while opsi not in("y","n"):
                    opsi = str(input("Beli lagi (y/n)?: "))

                    if(opsi == "y"):
                        selesai = False
                        print("")

                    elif(opsi == "n"):
                        selesai = True

                    else:
                        print("Mohon masukkan pilihan (y/n)")
                print("------------------------------------------------")
                print("Total harga                              : {0}".format(totalHarga))

        elif(opsi == "C"):
            printDataBuah(Buah)
            namaFruitHapus = str(input("Masukkan nama fruit yang ingin ditambahkan: "))

            if namaFruitHapus in Buah.keys():
                del Buah[namaFruitHapus]
                print("Nama fruit {0} telah terhapus dalam database".format(namaFruitHapus))
                print("")
                printDataBuah(Buah)

            else:
                print("Nama buah tidak ditemukan")

        elif(opsi == "D"):
            exit()

        else:
            print("Mohon masukkan pilihan yang tersedia")