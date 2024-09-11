class Father(object):
    def height(self):
        self.height=6
        print('Height of Father :',self.height)
        
class Mother(object):
    def complexion(self):
        self.color = 'Fair'
        print('Color of Mother :',self.color)
        
class child(Father,Mother):
    pass

C = child()
print('----child inherited qulities ----')
C.height()
C.complexion()