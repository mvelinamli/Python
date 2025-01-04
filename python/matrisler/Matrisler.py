# Matrisler konu anlatımı

    # Matris Oluşturma

# İki boyutlu bir matrisi list comprehension yöntemi ile nasıl oluştururuz?

matrix = [[0 for i in range(3)]for j in range(4)] #Sütun * satır

for i in matrix:
    print(i)

print("-"*100)
# şeklinde oluşturabiliriz.
#  ya da 

import random   #Random modülünü yalnızca sayıları rastgele belirlemek için kullanıyoruz.

matrix = []     #Az önce list comprehension yöntemi ile tek satırda oluşturduğumuz matrisi bu şekilde de oluşturabiliriz.
for i in range(3):  #Satır sayısı
    satir = []
    for j in range(4):  #Sütun sayısı
        satir.append(random.randint(0,10))
    matrix.append(satir)

for i in matrix:    #Burada for döngüsünü matrisin satırlarını alt alta yazdırmak için kullanıyoruz.
    print(i)


# İki matris arasında matematiksel işlemler nasıl yapılır.

    #İki tane a ve b matrisleri oluşturup toplayacağız.
        #Ancak bazı şeylere dikkat etmeliyiz.
        #! a ve b matrislerinin satir ve sütun sayıları birbirine eşit olmalıdır.
        #! bulduğumuz sonucu bir değişken içerisinde saklamalıyız ve tabiki o değişkende bir matris olmalı.
        #! Diyelim sonuçları bir c matrisi içerisinde saklayacağız. c matrsinin satır ve sütun sayıları a ve b'ninkine eşit olmalıdır.
        #! ayrıca c matrsi bir sıfır matris olmalıdır.

    # başlayalım.


def matris_topla(a,b):
    c = [[0 for i in range(len(a[0]))] for j in range(len(a))]
    for row in range(2):    
        for col in range(4):
            c[row][col] = a[row][col] + b[row][col]
    
    matris_yaz(c, "A ve B matrislerinin toplamı")   #Burada matrisleri düzgün bir şekilde ekrana yazdırmamızı sağlayacak bir fonksiyon çağırıyoruz. Tabiki önce fonksiyonu tanımlamalıyız.

def matris_yaz(matris, isim):   #Bu fonksiyonu oluşturmadan aşağıda for döngüsü ile düzenleyebilirdik
    print(isim)
    for i in range(len(matris)):
        for j in range(len(matris[i])):
            print(matris[i][j], end=" ")
        print("\n")

    # Şimdi a ve b matrislerini random kütüphanesi kullanarak rastgele sayılarla oluşturalım.
import random

a = [[int(10*random.random()) for i in range(4)] for j in range(2)]
print(a)
matris_yaz(a, "A Matrisi")
print("-"*100)

b = [[int(10*random.random()) for i in range(4)] for j in range(2)]
print(b)
matris_yaz(b, "B Matrisi")
print("-"*100)

    # a ve b matrislerini oluşturduk şimdi matris_topla() fonksiyonunu çağırarak işlemi gerçekleştirebiliriz.

matris_topla(a,b)
            