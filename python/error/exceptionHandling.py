try:
    x = int(input("x: "))
    y = int(input("y: "))
    print(x/y)
except ZeroDivisionError:
    print("y sıfır olamaz.")
except ValueError:
    print("x ve y sayısal bir değer olmalıdır.")

    
