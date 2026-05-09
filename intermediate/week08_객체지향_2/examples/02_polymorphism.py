class Animal:
    def __init__(self, name):
        self.name = name
    def speak(self):
        return "..."

class Dog(Animal):
    def speak(self): return "멍멍"

class Cat(Animal):
    def speak(self): return "야옹"

class Cow(Animal):
    def speak(self): return "음매"

animals = [Dog("바둑이"), Cat("나비"), Cow("얼룩이")]
for a in animals:
    print(f"{a.name}: {a.speak()}")
