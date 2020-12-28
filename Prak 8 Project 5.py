# Rumus

def kuadrat(bil):

    bilsquare = []

    for r in range(len(bil)):

        perkalian = bil[r] * bil[r]
        bilsquare.append(perkalian)

    return bilsquare


databil = [2, 4, 5, 6, 12]
hasil = kuadrat(databil)
print(hasil)