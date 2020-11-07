#SCA WEEK 3 ASSIGNMENT
# Program using inheritance and polymorphism


class Human:
    def __init__(self, gender, age):
        self.gender = gender
        self.age = age

    def fact(self):
        return "I am human"

class Woman(Human):
    def __init__(self, name):
        super().__init__("female",22)
        self.name = name

    def fact(self):
        return "I am a female human"




rashida = Human("female", 20)
manal = Woman("manal")
print(manal.fact())