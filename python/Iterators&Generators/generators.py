# Generator ? 

def sayi_say(max):
    sayi = 1
    while sayi <= max:
        yield sayi
        sayi += 1

iterator = sayi_say(10)

generator (i for i in range(1,11))

print(next(generator))
