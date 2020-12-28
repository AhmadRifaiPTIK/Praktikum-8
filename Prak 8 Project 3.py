#Interface

NamaInput = []
r = True

while(r == True) :
    nama = input('Masukkan nama :')
    NamaInput.append(nama)

    lanjut = input('Apakah ingin menginput nama lagi ? (y/n)')

    if(lanjut == 'y') :
        r = True

    elif(lanjut == 'n') :
        r = False

    else :
        print('Input tidak valid')
        break

#Output Akhir

print()
NamaInput.sort()

for r in range(len(NamaInput)) :
    print(NamaInput[r], '(', len(NamaInput[r]), 'karakter )')