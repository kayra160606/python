class student:
    def __init__(self):
        self.name="mohit"
        self.age=18
        self.marks=75
    def display(self):
        print("Name:",self.name)
        print("Age:",self.age)
        print("Marks:",self.marks)
s = student()
s.display()