class Person:
    # Yapıcı metotlar (constructor)
    def __init__(self,name,surname,year):
        #Object attribute
        self.name = name
        self.surname = surname
        self.year = year
    #Instance methods
    def intro(self):
        return f"Benim adım {self.name} ve soyadım {self.surname}"
    
    def calculate_age(self):
        return f"{2024-self.year}"
    
#Object instance
p1 = Person("Veli","NAMLI",2004)
p2 = Person("Nuri","NAMLI",2009)

print(p1.intro())
print(p2.intro())