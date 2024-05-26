ages = [5,12,18,24,45]

def yetiskinmi(x):
    if x<18:
        return False
    else:
        return True
    
for i in filter(yetiskinmi, ages):
    print(i)
    