print("Toplama işlemi yapmak için => 1,\nÇıkarma işlemi yapmak için => 2,\nÇarpma işlemi yapmak için => 3,\nBölme işlemi yapmak için => 4\n\nÇıkış yapmak için => q")

def calculator():
    n1 = int(input("İşlem yapmak istediğiniz birinci sayı: "))
    n2 = int(input("İşlem yapmak istediğiniz ikinci sayı: "))
    islem = input("Yapmak istediğiniz işlemin numarası: ")
    if islem == '1':
        print(n1 + n2)
    elif islem == '2':
        print(n1 - n2)
    elif islem == '3':
        print(n1 * n2)
    elif islem == '4':
        print(n1 / n2)
    elif islem == 'q':
        print("Çıkış yapılıyor.")
    else:
        print("Geçersiz değer.")

calculator()