# Rumus
Buah  = { 'apel'  : 5000,
          'jeruk' : 8500,
          'mangga': 7800,
          'duku'  : 6500 }
def jumlahBuah():
    jumlah =int(input('Berapa Kg yang dibeli  :'))
    print('-------------------------------')
    print('Total Harga            :',Buah.get(namaBuah,0)*jumlah)

namaBuah = input('Nama fruit yang dibeli :')
print('Daftar fruit dan harga :')

try:
    if(namaBuah in Buah.keys()):
        jumlahBuah()
except ValueError:
        print('Input tidak valid')

for x,y in Buah.items() :
    print('.', x, ':', y)

else:
        print('Maaf,nama fruit yang anda masukkkan tidak ada')
while True :
    namaBuah = input('Nama fruit yang dibeli :')
    if(namaBuah not in Buah.keys()) :
        print('Mohon maaf, fruit yang anda masukkan tidak ada')
    continue

    except ValueError :
    print('Silakan jumlah fruit dengan benar')
    jumlahBuah()
    else :
    while True :
                try :
                    jumlahBuah()
                    break
                except ValueError :
                    continue
                break