class User:

    active_users = 0
    @classmethod
    def display_active_users(cls):
        return f"Şu anda aktif {cls.active_users} user var."

    def __init__(self,fname,lname):
        self.fname = fname
        self.lname = lname
        User.active_users += 1

    def fullname(self):
        return f"{self.fname} {self.lname}"


class Moderator(User):

    active_moderator = 0
    @classmethod
    def display_active_moderator(cls):
        return f"Su anda aktif {cls.active_moderator} moderator var."

    def __init__(self,fname,lname,community):
        super().__init__(fname,lname)
        self.community = community
        Moderator.active_moderator += 1

    def remove_post(self):
        return f"{self.fullname()} {self.community} grubundan bir post sildi."
    
    def update_post(self):
        return f"{self.fullname()} {self.community} grubunda bir post güncelledi."
    
print(Moderator.display_active_moderator())
print(User.display_active_users())
u1 = User("Veli","NAMLI") 
m1 = Moderator("Veli", "NAMLI", "Yönetici")
m2 = Moderator("Nuri", "NAMLI", "Moderatör")
print(User.display_active_users())
print(Moderator.display_active_moderator())

print(m1.remove_post())
print(m2.update_post())

# print(u1.fullname(), m1.fullname())

# print(isinstance(u1, User))
# print(isinstance(u1, Moderator))

# print(isinstance(m1, User))
# print(isinstance(m1, Moderator))