#program demonstrating use of class/static variable
print('Class/static variable programming output:')
class sample:
    var=10
    @classmethod
    def new_modify(cls):
        cls.var+=1
s1 =sample()
s2 =sample()
print("x in s1",s1.var)
print("x in s2",s2.var)
s1.new_modify()
print("x in s1",s1.var)
print("x in s2",s2.var)

#program demonstrating use of Instance variable
print('Instance variable programming output:')
class stud:
    def __init__(self) -> None:
        self.x = 10
    def modify(self):
        self.x +=1
t1=stud()
t2=stud()
print("x in t1",t1.x)
print("x in t2",t2.x)
t1.modify()
print("x in t1",t1.x)
print("x in t2",t2.x)