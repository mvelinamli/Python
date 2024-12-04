# Girilen bir sayının mutlak değerini alan program.

# Algorithm
#   1-Başlat
#   2-Sayı al (x)
#   3-Eğer x < 0 ise mutlak = -1 * x ve yazdır "x sayısının mutlak değeri eşittir" + mutlak
#   4-Değilse yazdır x
#   5-Bitir.


x=int(input("Enter a number: "))

if x < 0:
    mutlak = -1 * x
    print(f"{x}, mutlak değer= {mutlak}")
else:
    print(x)