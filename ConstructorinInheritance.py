class father:
    def __init__(self,P1):
        self.P1=P1
    def display(self):
        print('From Father Class')
        print('Property =',self.P1)
        
class son(father):
    def __init__(self,P2):
        self.P2=P2
    def display(self):
        print('From Child Class')
        print('Property =',self.P2)
        
s = son(100000)
s.display()