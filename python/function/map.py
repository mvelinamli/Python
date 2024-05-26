numbers = [1,2,5,7,9]
"""
  square = []

for num in numbers:
    square.append(num ** 2)

print(square) 
"""

def square(num):
    return num ** 2 

sonuc= list(map(square, numbers))    #bir deger oluşturmak için list içine atalım.
print(sonuc)