class Student:
    def __init__(self, name):
        self.name = name
        self.scores = []

    def add_score(self, s):
        self.scores.append(s)

    def average(self):
        return sum(self.scores) / len(self.scores) if self.scores else 0

    def highest(self):
        return max(self.scores) if self.scores else 0

    def passed(self, threshold=60):
        return self.average() >= threshold

s = Student("홍길동")
for x in (85, 92, 78):
    s.add_score(x)
print(s.average())
print(s.highest())
print(s.passed())
