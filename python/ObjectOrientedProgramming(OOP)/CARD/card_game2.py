class Card:
    def __init__(self,type,value):
        self.type = type
        self.value = value

    def __repr__(self):
        return f"{self.type} {self.value}"
    

class Deck:
    types = ["karo","sinek","kupa","maça"]
    values = ["A","2","3","4","5","6","7","8","9","10","J","Q","K"]
    def __init__(self):
        self.cards = [Card(type,value) for type in Deck.types for value in Deck.values]

    