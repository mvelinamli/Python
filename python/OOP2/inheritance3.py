class Person:
    def __init__(self, name, surname, age):
        self.name = name
        self.surname = surname
        self.age = age
        print("Person nesnesi türetildi.")
    
    def intro(self):
        print(self.name, self.surname, self.age)

class Student(Person):  #Person class'ı Student class'ının parent classıdır.
    def __init__(self, name, surname, age, number):
        super().__init__(name, surname, age)
        self.number = number
        print("Student nesnesi üretildi.")
    
    def study(self):
        print(f"{self.name} isimli öğrenci ders çalışıyor")

    def intro(self):
        print(self.name, self.surname, self.age, self.number)

class Teacher(Person):  #Person class'ı Teacher class'ının parent classıdır.
    def __init__(self, name, surname, age, branch):
        super().__init__(name, surname, age)
        self.branch = branch
        print("Teacher nesnesi üretildi.")

    def teach(self):
        print(f"{self.name} isimli öğretmen {self.branch} eğitimi veriyor.")


p1 = Person("Veli", "NAMLI", 19)
p1.intro() #Base

s1 = Student("Nuri", "NAMLI", 15, 388)
s1.intro()  #Child
s1.study()

t1 = Teacher("Mehmet", "NAMLI", 55, "Fen Bilimleri")
t1.intro()
t1.teach()
