class stud:
    #class variable
    marks=0
    
    #class method
    @classmethod
    def show(cls,name):
        print('{} is having {} marks'.format(name,cls.marks))
        
n=int(input('enter marks:'))
stud.marks=n
stud.show('ravan')

#second instance
n=int(input('enter marks:'))
stud.marks=n
nm=input('Enter Name:')
stud.show(nm)