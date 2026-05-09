class Animal:
    def __init__(self, name):
        self.name = name
    def speak(self):
        return "..."

class Dog(Animal):
    def speak(self):
        return "멍멍"

class Puppy(Dog):
    def __init__(self, name, age):
        super().__init__(name)
        self.age = age

d = Dog("바둑이")
p = Puppy("뭉치", 1)
print(d.name, d.speak())
print(p.name, p.age, p.speak())
