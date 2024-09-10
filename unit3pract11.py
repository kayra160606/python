class teacher:
    def __init__(self):
        self.id = 1001
    def display(self):
        print('Teacher id :',self.id)
class student(teacher):
    def __init__(self):
        self.id = 1
    def display(self):
        print('Student id :',self.id)
    
S = student()
S.display()