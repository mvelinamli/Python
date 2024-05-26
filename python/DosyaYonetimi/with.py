# open() komutu ile açılan bir dosyayı daha sonra close() komutu ile kapatmamız gerekir.
# Ancak with() metodunu kullandığımızda dosya üzerinde yaptığımız işlemler tamamlandığında dosya otomatik olarak kapatılır.

with open ("DosyaYonetimi/file.txt") as file:
    """
    print(file.read())
    print(file.tell())  #Cursor'un nerede olduğunu söyler.
    print(file.read())
    """
    for i in file:
        print(i, end="")


# print(file.read())         Error => açık olmayan bir dosya üzerinde çalışma yapıyorsunuz.


