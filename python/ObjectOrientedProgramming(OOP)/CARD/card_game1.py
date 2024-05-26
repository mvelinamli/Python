class Card:
    def __init__(self,type,value):
        self.type = type
        self.value = value

    def __repr__(self):
        return f"{self.type} {self.value}"
    
sinek5 = Card("sinek","5")
karoAs = Card("karo","A")

print(sinek5)
print(karoAs)
