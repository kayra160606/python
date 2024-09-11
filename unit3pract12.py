class sum:
    def __init__(self):
        self.a=5
        self.b=10
class add(sum):
    def addition(self):
        print('Addition of two value is :',self.a+self.b)
class sub(sum):
    def subtraction(self):
        print('Subtraction of two value is :',self.a-self.b)
a = add()
s = sub()
a.addition()
s.subtraction()