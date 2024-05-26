# Dosya açmak ve oluşturmak için open() fonksiyonu kullanılır. 
# Kullanımı: open(dosya_adi, dosya_erişme_modu)
# dosya_erişme_modu => hangi amaçla açtığımızı belirtir.
# "r": okuma modu => belirtilen dizinde dosya olmalıdır.

file = open("DosyaYonetimi/file.txt")
print(file)
print(help(file))