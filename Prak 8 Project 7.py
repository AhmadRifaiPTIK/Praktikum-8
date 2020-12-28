# Skema Awal

Buah = { 'apel'  : 5000,
          'jeruk' : 8500,
          'mangga': 7800,
          'duku'  : 6500 }

def expensive(dictionary) :

    key = list(dictionary.keys())
    values = tuple(dictionary.values())

    HargaBuah = max(values)

    AlurHargaBuah = values.index(HargaBuah)

    print(key[AlurHargaBuah])

expensive (Buah)