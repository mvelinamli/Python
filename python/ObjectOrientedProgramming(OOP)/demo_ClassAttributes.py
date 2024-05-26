class Pet:
    genders = ["Kedi","Köpek","kuş"]
    def __init__(self,name,gender):
        if gender not in Pet.genders:
            raise ValueError(f"{gender} bir evcil hayvan değildir.")
        self.name = name
        self.gender = gender

boncuk = Pet("Boncuk","Kedi")
pasa = Pet("Paşa","Köpek")

# mavis = Pet("Maviş","Aslan")

print(boncuk)
print(pasa)
print(Pet.genders)