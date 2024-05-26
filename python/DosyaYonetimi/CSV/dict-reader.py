from csv import DictReader

with open("/Users/veli/Desktop/python/DosyaYonetimi/CSV/products.csv") as file:
    csv_reader = DictReader(file)
    for p in csv_reader:
        if (p["Category"] == "Bilgisayar"):
            print(p['ProductName'],p['Price'])