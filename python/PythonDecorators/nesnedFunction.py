def greeting(name):
    print("hello", name)

greeting("Ali")
# print(greeting)

sayHello = greeting
# print(sayHello)
# print(greeting)

del sayHello

print(greeting)
# print(sayHello)   !ERROR

# ENCAPSULATION
def outer(num1):
    print("OUTER")
    def inner_increment(num1):
        print("INNER")
        return num1 + 1
    num2 = inner_increment(num1)
    print(num1, num2)

outer(10)   
# inner_increment(10)   ! inner_increment çağırmaya kalkarsak hata alırız çünkü bu outer kapsamında çalışan bir fonksiyondur.

def factorial(number):
    if not isinstance(number, int):
        raise TypeError("Number must be an integer.")
    if not number >= 0:
        raise ValueError("Number must be zero or bigger than zero.")
    def inner_factorial(number):
        if number <= 1:
            return 1
        
        return number * inner_factorial(number - 1)
    return inner_factorial(number)

print(factorial(-2))