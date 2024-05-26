class Comment:
    def __init__(self, _username, _text, _likes=100, _dislikes=0):
        self.username = _username
        self.text = _text
        self.likes = _likes
        self.dislikes = _dislikes
        pass 
        
c1 = Comment("Ali","çok güzel",1000, 20)
c2 = Comment("Veli","çok kötü",100,10000)
c3 = Comment("Mehmet","Hayatımda gördüğüm en iyi programmer", 100000, 200)
c4 = Comment("Zeynep","orta", 50, 50)
c5 = Comment("Ayşe","terrible", 10, 328)

comments = [c1,c2,c3,c4,c5]

for c in comments:
    print("---------------")
    print(f"{c.username}: {c.text}\n{c.likes}, {c.dislikes}")