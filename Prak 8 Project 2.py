#Rumus

def dataStat(x) :

    a = sum(x) / len(x)
    s = max(x)
    d = min(x)

    data = [a,s,d]

    return data

#Interface Untuk Memasukan Angka

while True :
    try :
        n = int(input('Masukkan banyak angka yang ingin anda input ? :'))
        break
    except ValueError :
        print('Input tidak valid')
        continue

#Rumus 2

data = []

i = 0

#Interface

while (i < n) :
    try :
        bil = int(input('Masukkan bilangan bulat yang anda inginkan :'))
        data.append(bil)
        i += 1

    except ValueError :
        print('Input tidak valid')

#Output Akhir

printData = dataStat(data)
print(printData)