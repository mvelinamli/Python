def selamlama(fn):
    def wrapper():
        print("Hoşgeldiniz")
        fn()
        print("Görüşmek üzere")
    return wrapper
@selamlama
def gunaydin():
    # print("Hoşgeldiniz")
    print("Günaydın benim adım Çınar")
    # print("görüşmek üzere")
@selamlama
def iyigunler():
    # print("Hoşgeldiniz")
    print("İyi günler benim adım Çınar")
    # print("Görüşmek üzere")
gunaydin()
iyigunler()