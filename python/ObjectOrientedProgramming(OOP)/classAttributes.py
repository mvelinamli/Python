class User:

    active_users = 0

    def __init__(self, name, lname, age):
        self.name = name
        self.lname = lname
        self.age = age
        User.active_users += 1

    def full_name(self):
        return f"{self.name} {self.lname}"
    
print(User.active_users)
userA = User("Veli","Namlı",19)
userB = User("Nuri","Namlı",15)

# print(userA.full_name())
# print(userB.full_name())