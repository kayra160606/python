class stud:
    #mutator method
    def set_no(self,no):
        self.no=no
    #accessor method
    def get_no(self):
        return self.no
    
    #mutator method
    def set_per(self,per):
        self.per=per
    
    #accessor method
    def  get_per(self):
        return self.per
    
s1=stud()
s1.set_no(101)
print('roll number=',s1.get_no())
s1.set_per(78)
print('Per =',s1.get_per())