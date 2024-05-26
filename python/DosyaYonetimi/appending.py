#   open(dosya_adi,dosya_erisim_modu)
#   dosya_erisim_modu => dosyayı hangi amaçla açtığımızı belirtir.

#   "r": Read-Okuma. Dosya konumda yoksa hata verir.
#   "w": Write-Yazma. Yazma modu.
#       **Dosyaı konumda oluşturur.
#       ***Dosya içeriğini siler ve yeniden ekleme yapar.
#   "a": Append-Ekleme. Dosya konumda yoksa oluşturur.
#   "r+": Hem okuma hem yazma modunda açılır. Dosya dizinde yoksa hata verir.

"""with open("DosyaYonetimi/newfile.txt","a") as file:
    file.write("Dördüncü satır.\n")
    file.write("Beşinci satır.\n")"""
with open("DosyaYonetimi/file.txt", "r+") as file:
    file.read()
    file.write("new line")