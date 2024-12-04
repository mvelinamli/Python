#Kullanıcıdan alınan iki basamaklı sayının basamaklarındaki rakamları büyükten küçüğe doğru sıralayınız

#algorithm
#   1-Başlat
#   2-Sayı al (x)
#   3-Eğer 10<=x<=99 ise onlar=x//10    birler=x%10
#   4-Değilse yazdır"Girdiğiniz sayı çift basamaklı olmalıdır ve dön 2.adım
#   5-Eğer onlar > birler   yazdır onlar,birler
#   6-Eğer onlar < birler   yazdır birler,onlar
#   7-Eğer onlar == birler ise yazdır "Değerler birbirine eşittir"
#   8-Bitir.

x=int(input("Enter a number: "))
if 10<=x<=99:
    onlar=x//10
    birler=x%10
    if onlar > birler:

        print(onlar,birler)
    elif onlar < birler:
        print(birler,onlar)
    elif onlar == birler:
        print("Basamakların sayı değerleri birbirine eşittir.")
        print(onlar,birler)
else:
    print(" Girdiğiniz değer iki basamaklı olmalıdır.")
