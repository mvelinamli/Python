# matris_uygulamalari

#Kullanıcıdan veri alarak belirli boyutta bir matris oluşturun (satır ve sütun sayısı kullanıcıdan alınacak, veriler de kullanıcı tarafından girilecek)
"""
row = int(input("Satır sayısı: "))
col = int(input("Sutün sayısı: "))

matris = [[input("data for matris: ") for i in range(col)]for j in range(row)]

for i in matris:
    print(i)
"""

# Kare matris, birim matris ve sıfır matris oluşturun

    # Kare matris
        #Kare matrisin özelliği satır ve sütun sayısının birbirine eşit olmasıdır.

"""
row = int(input("Satır sayısı: "))  #Kullanıcıdan yalnızca satır sayısı almamız yeterlidir.

matris = [[0 for i in range(row)] for j in range(row)]

for i in matris:
    print(i)
"""

    # Birim matris
"""
matris = []
for i in range(3):
    satir = []
    for j in range(3):
        if i == j:
            satir.append(1)
        else:
            satir.append(0)
    matris.append(satir)

for i in matris:
    print(i)
"""

#İki matrisin toplamını bul.
"""def matris_topla(a,b):
    c = [[0 for i in range(len(a[0]))] for j in range(len(a))]
    for row in range(2):
        for col in range(4):
            c[row][col] = a[row][col] + b[row][col]
    print(c)
import random

a = [[int(10*random.random()) for i in range(4)] for j in range(2)]
print(a)
b = [[int(10*random.random()) for i in range(4)] for j in range(2)]
print(b)
matris_topla(a,b)"""


# Bir matrisin içindeki en büyük sayı

def max_matris(matris):
    en_buyuk = matris[0][0] #ilk elemanı başlangıç değeri olarak alıyoruz.
    for row in matris:
        for eleman in row:
            if eleman > en_buyuk:
                en_buyuk = eleman
    return en_buyuk

import random

matris = [[int(10*random.random())for i in range(5)] for j in range(5)] #Rastgele değerlerden oluşan 5x5 lik bir matris oluşturduk.
for i in matris:
    print(i)
print("-"*100)
en_buyuk = max_matris(matris)
print(f"Matristeki en büyük sayı: {en_buyuk} ")