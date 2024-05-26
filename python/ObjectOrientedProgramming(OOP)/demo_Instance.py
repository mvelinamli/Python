# 1
class BankAccount:
    def __init__(self,owner,balance):
        self.owner = owner
        self.balance = balance = 0.0

    def intro(self):
        return f"Sayın {self.owner}\nBankamıza Hoşgeldiniz."
    
    def deposit(self):
        miktar = int(input("Yatırılacak tutarı giriniz: "))
        self.balance += miktar
        return f"Balance: {self.balance}"
    
    def withdraw(self):
        miktar = int(input("Çekilecek tutarı giriniz: "))
        self.balance -= miktar
        return f"Balance: {self.balance}"

        
p1 = BankAccount("Veli")

print(p1.intro())
print(p1.deposit())
print(p1.withdraw())
   