#List Sayuran
sayur = ['bayam','kangkung','wortel','selada']

#Interface Tambah

def tambahSayur() :
    SayurPlus = input('Masukkan nama sayur yang ingin ditambahkan :')
    SayurPlus = input('Masukkan nama sayur yang ingin ditambahkan :').lower()
    sayur.append(SayurPlus)
    return sayur

#Interface Kurang

def hapusSayur() :
    SayurMinus = input('Masukkan nama sayur yang ingin dihapus :')
    sayur.append(SayurMinus)
    SayurMinus = input('Masukkan nama sayur yang ingin dihapus :').lower()
    if(SayurMinus in sayur) :
        sayur.remove(SayurMinus)
    else :
        print('Sayur itu tidak ada di dalam data')
    return sayur

#Interface Utama


def readSayur() :
    print(sayur)
print('Apa yang dilakukan program :')
print('A. Tambah data sayur')
print('B. Hapus data sayur')
print('C. Tampilkan data sayur')
print('D. Keluar')
r = True
while(r == True) :
    print()
    opsi = input('Pilihan Anda :')
    if(opsi == 'A' or opsi == 'a') :
        tambahSayur()
    elif(opsi == 'B' or opsi == 'b') :
        hapusSayur()

    elif(opsi == 'C' or opsi == 'c') :
        tambahSayur()
        readSayur()

    elif(opsi == 'D') :
        break
    else :
        print('Input tidak valid')
        continue