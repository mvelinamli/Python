class User:

    active_user = 0

    @classmethod
    def display_active_users(cls):
        return f"{cls.active_user} tane aktif kullanıcı var"
    
    @classmethod
    def from_string(cls,data_str):
        first,last,age = data_str.split(',')
        return cls(first,last,age)


    def __init__(self,first,last,age):
        print(self)
        self.first = first
        self.last = last
        self.age = age
        User.active_user += 1

    def full_name(self):
        return f"{self.first} {self.last}"
    
    def logout(self):
        User.active_user -= 1
        return f"{self.full_name()} uygulamadan çıkış yaptı."
    
print(User.display_active_users())
userA = User("Sadık","Turan",37)
userB = User("Sena","Turan",20)
userC = User("Çınar","Turan",4)
print(User.display_active_users())

User.from_string("Ali,Korkmaz,20")

# print(User.active_user)
# print(userC.logout())
# print(User.active_user)