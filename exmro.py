class A(object):
    def __init__(self):
        print('A class method')
        super().__init__()
class B(object):
    def __init__(self):
        print('B class method')
        super().__init__()
class C(object):
    def __init__(self):
        print('C class method')
        super().__init__()
class D(object):
    def __init__(self):
        print('D class method')
        super().__init__()
class E(A,B,C):
    def __init__(self):
        print('E class method')
        super().__init__()
class F(B,C,D):
    def __init__(self):
        print('F class method')
        super().__init__()
class G(E,F,D):
    def __init__(self):
        print('G class method')
        super().__init__()
p= G()