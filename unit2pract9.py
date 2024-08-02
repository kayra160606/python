def positional(ram,mohit,shyam):
    print(ram,mohit,shyam)
a='Ram'
b='Mohit'
c='Shyam'
positional(a,b,c)

def Keyword(ram,mohit,shyam):
    print(ram,mohit,shyam)
a='Ram'
b='Mohit'
c='Shyam'
Keyword(ram=a,shyam=c,mohit=b)

def Keyword(ram,mohit,shyam='mohit'):
    print(ram,mohit,shyam)
a='Ram'
b='Mohit'
Keyword(ram=a,mohit=b)


