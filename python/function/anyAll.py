sonuc = all([True,True,False])      #False
sonuc = all([True,True,True])       #True
sonuc = any([True,False,False])     #True

sayilar = [0,1,3,6,8,9,10]

sonuc = ([bool(sayi) for sayi in sayilar])  #[False, True, True, True, True, True, True]
sonuc = any([bool(sayi) for sayi in sayilar])   #True
sonuc = all([bool(sayi) for sayi in sayilar])   #False
sonuc = ([bool(sayi) for sayi in sayilar if sayi%2==1]) #[True, True, True]
sonuc = [sayi%2==0 for sayi in sayilar] #[True, False, False, True, True, False, True]

kisiler = ['ali', 'ahmet', 'çınar']

sonuc = all([kisi[0]=='a' for kisi in kisiler])

print(sonuc)