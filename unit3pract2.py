class student:
    def __init__(self,nm='.',ag=15,m=0):
        self.name=nm
        self.age=ag
        self.marks=m
    def display(self):
        print("Name:",self.name)
        print("Age:",self.age)
        print("Marks:",self.marks)
s1=student("Mohit",18,75)
s1.display()
s=student("Mann")
print('detail of second instance')
s.display()
    