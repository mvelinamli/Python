# 1

def faktoriyel(num):
    x = num.isdigit()
    import math
    if num > 10 and num == 0:
        raise ValueError("Girilen değer 0'dan büyük ve 10'dan küçük olmalıdır.")
    elif x != True:
        raise TypeError("Girilen değer sayısal olmalıdır.s")
    else:
        math.factorial(num)

faktoriyel(10)