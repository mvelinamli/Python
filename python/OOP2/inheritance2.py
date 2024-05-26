class Person:
    def __init__(self, name, surname, age):
        self.name = name
        self.surname = surname
        self.age = age
        print("Person nesnesi türetildi.")
    
    def intro(self):
        print(self.name, self.surname, self.age)

class Student(Person):  #Person class'ı Student class'ının parent classıdır.
    pass

class Teacher(Person):  #Person class'ı Teacher class'ının parent classıdır.
    pass


p1 = Person("Veli", "NAMLI", 19)
p1.intro()

s1 = Student("Nuri", "NAMLI", 15)
s1.intro()

t1 = Teacher("Mehmet", "NAMLI", 55)
t1.intro()
