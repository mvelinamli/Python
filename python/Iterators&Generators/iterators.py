# Iterable? => Yinelenebilir.

# Iterator? => Yineleyici.

numbers = [1,2,3,4,5]
g = "hello"


def my_for(iterable, func):
    iterator = iter(iterable)
    while True:
        try:
            sayi = next(iterator)
            func(sayi)
        except StopIteration:
            break

my_for(numbers, print)
my_for(g, print)