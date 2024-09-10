class square(object):
    def __init__(self,x):
        self.x=x
    
    def Print(self):
        print('Area of square:',self.x*self.x)
        
class rect(square):
    def __init__(self,l,b):
        super().__init__(l)
        self.y=b
        
    def Print(self):
        super().Print()
        print('Area of Rectangle :',self.x*self.y)
        
        
R = rect(5,4)
R.Print()