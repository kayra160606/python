class stud:
    def __init__(self,r,n):
        self.r=r
        self.name=n
        
    def display(self):
        print('RollNumber =',self.r)
        print('Name =',self.name)

class sub_stud(stud):
    pass

s1 = sub_stud(101,'Mohit')
s1.display()