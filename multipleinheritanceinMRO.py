class Base1(object):
    def __init__(self):
        self.x='x'
        print(self.x)
        super().__init__()
        
class Base2:
    def __init__(self):
        self.y= 'y'
        print(self.y)
        
        
class child(Base1,Base2):
    def __init__(self):
        super().__init__()
        self.z= 'z'
        print(self.z)
        

C = child()