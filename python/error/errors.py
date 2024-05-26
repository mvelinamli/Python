# error

# error handling

try:    #Hata alabileceğimiz bölüm.
    x = int(input("x: "))
    y = int(input("y: "))
    print(x + y)
except:     #Hata alındığında kullanıcının görmesini istediğimiz mesaj.
    print('hata oluştu.')