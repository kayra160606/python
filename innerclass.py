class stud:
    def __init__(self,no,p):
        self.no=101
        self.per=p
        
    def print(self):
        print('No =',self.no)
        print('Per =',self.per)
        
    class DOB:
        def __init__ (self,dd,mm,yy):
            self.date=dd
            self.month=mm
            self.year=yy
            
        def display(self):
            print('Date =',self.date)
            print('Month =',self.month)
            print('Year =',self.year)
        
s1 = stud(101,98)
s1.print()
s_inner = stud(101,98).DOB(10,5,12)
s_inner.display()