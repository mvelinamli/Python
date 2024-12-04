#Belirli aralıktaki sayıların tek veya çift olduğunu belirleyen program

#ALgorithm
# 1-başlat
# 2-sayı al (x)
# 3-i = 0
# 4-Eğer i % 2 == 0 ise yazdır "sayı çiftir"
# 5-Değilse yazdır "sayı tektir"
# 6-i++
# 7-Eğer i != x ise dön 4.adım
# 8-Değilse bitir.

x = int(input("Enter a number: "))
i = 0

for i in range(x):
    if i % 2 == 0:
        print("çift", i)
    else:
        print("tek", i)
    i+=1


