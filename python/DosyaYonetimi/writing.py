#   "w": (write) yazma modu.
#       **Dosyayı dizinde oluşturur.
#       ***Eğer dizinde aynı isimde bir dosya varsa dosyayı siler ve yenisi oluşturur.

with open("DosyaYonetimi/newfile.txt", "w") as file:
    file.write("Muhammed Veli NAMLI\n")
    file.write("Mustafa Nuri NAMLI\n")
    file.write("Mehmet NAMLI")

with open("DosyaYonetimi/newfile.txt") as file:
    print(file.read())