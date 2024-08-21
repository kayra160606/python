#write a program to store data into instance using mutator methods and to retrieve data from the instances using accessor methods.

class stud:
    #mutator method
    def set_no(self,no):
        self.no=no
    #accessor method
    def get_no(self):
        return self.no
    
    #mutator method
    def set_name(self,name):
        self.name=name
    
    #accessor method
    def  get_name(self):
        return self.name
    
s1=stud()
s2=stud()
s1.set_no(101)
print('roll number=',s1.get_no())
s1.set_name(78)
print('name =',s1.get_name())
no=int(input('Enter Number :'))
s2.set_no(no)

name=input('Enter name :')
s2.set_name(name)
print('roll number=',s2.get_no())
print('name=',s2.get_name())


