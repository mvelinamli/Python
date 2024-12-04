# Girilen bir sayıyı çarpanlarına ayırma.

#Algorithm
# 1-Başlat
# 2-sayı al (x)
# 3- i=1
# 4- Eğer x % i == 0 ise yazdır "i çarpandır"
# 5- Değilse yazdır "i çarpan değildir"
# 6- i ++
# 7- Eğer i != x ise dön 4.adım
# 7- Değilse bitir.

x=int(input("Enter a number: "))
i=1
for i in range(1,x+1):
    if x % i == 0:
        print("Çarpan", i)
    else:
        print("!!Çarpan değil", i)
    i+=1