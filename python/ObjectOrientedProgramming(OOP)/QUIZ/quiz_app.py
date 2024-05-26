class Question:
    def __init__(self,question,choice,answer):
        self.question = question
        self.choice = choice
        self.answer = answer

    def checkAnswer(self,answer):
        if answer not in self.choice:
            raise ValueError("Hatalı bilgi")
        return self.answer == answer
    
q1 = Question("En iyi programlama dili hangisidir?",["python","c#","java","dart"],"python")

print(q1.question)
print(q1.choice)
print(q1.answer)

result = q1.checkAnswer('java')
print(result)