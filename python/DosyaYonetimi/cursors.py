f = open("DosyaYonetimi/file.txt")

# print(f.read())
# print(f.read()) # read() metodu kaldığı yerden devam ederek okuma yapar.
# f.seek(0) # cursorun indexini ayarlar böylece read() çalıştırdığımızda okuma işlemine en baştan başlar. 
# print(f.read())
# f.seek(0)
# f.seek(0)
# print(f.readline()) #Satır sonuna kadar okuma yapar.
print(f.readlines())    #Tüm satırları dizin olarak döndürür.