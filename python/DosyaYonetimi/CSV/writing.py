from csv import writer, reader

"""
with open("/Users/veli/Desktop/python/DosyaYonetimi/CSV/cars.csv", "w") as file:
    csv_writer = writer(file)
    csv_writer.writerow(["Marka","Model"])
    csv_writer.writerow(["Toyota","Yaris"])
    csv_writer.writerow(["Toyota","Corolla"])
"""
"""
with open("/Users/veli/Desktop/python/DosyaYonetimi/CSV/cars.csv", "w") as file:
    csv_writer = writer(file)
    csv_writer.writerows([["Marka","Model"],["Toyota","Yaris"],["Toyota","Corolla"]])
"""  
"""
with open("/Users/veli/Desktop/python/DosyaYonetimi/CSV/cars.csv", "a") as file:
    csv_writer = writer(file)
    csv_writer.writerow(["Toyota", "R34"])
"""
"""
with open ("/Users/veli/Desktop/python/DosyaYonetimi/CSV/products.csv") as file:
    csv_reader = reader(file)
    with open("new-products.csv", "w") as file:
        csv_writer = writer(file)
        for product_row in csv_reader:
            csv_writer.writerow([p.upper() for p in product_row])
"""    

with open("/Users/veli/Desktop/python/DosyaYonetimi/CSV/products.csv", "r+") as file:
    csv_reader = reader(file)
    csv_writer = writer(file)
    next(csv_reader)
    products = [[p[0], float(p[1])*1.2,p[3],p[4]] for p in csv_reader]
    file.seek(0)
    csv_writer.writerow(["ProductName","Price","IsPublished","Category","Reviews"])
    csv_writer.writerow(products)
