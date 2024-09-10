class father:
    def __init__(self):
        self.P1=10000
        
    def display(self):
        print('---From father---')
        print('Property =',self.P1)
        
class child(father):
    def __init__(self):
        super().__init__()
        self.P2=5000
    
    def display(self):
        super().display()
        print('---From child---')
        print('Property =',self.P2)
        
C = child()
C.display()