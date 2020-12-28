#Interface

while True :
    try :
        n = int(input('Masukkan banyak angka yang ingin anda input? :'))
        break
    except ValueError :
        print('Input tidak valid')
        continue

#Rumus Perhitungan

data = []
i = 0

while (i < n) :
    try :
        bil = int(input('Masukkan bilangan bulat yang anda inginkan : '))
        data.append(bil)
        i+= 1

    except ValueError :
        print("Input tidak valid")

#output

data.sort(reverse = True)
print(data)