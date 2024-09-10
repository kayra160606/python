class Father(object):
    def __init__(self):
        self.height=6
        print('Height of Father :',self.height)
        
class Mother(object):
    def __init__(self):
        self.color = 'Fair'
        print('Color of Mother :',self.color)
        
class child(Father,Mother):
    pass

C = child()