class temp:
    cls=100 #class variable
    def __init__(self):
        self.a=10
        self.b=20
    def modify(self):
        self.a +=1
        self.b +=1
    #class  method
    def modify_cls(cls1):
        temp.cls +=1
t1=temp()
t1.modify()
t1.modify_cls()
print(t1.a)
print(t1.b)
print(temp.cls)
print('second instance')
t2=temp()
t2.modify()
t2.modify_cls()
print(t2.a)
print(t2.b)
print(temp.cls)



