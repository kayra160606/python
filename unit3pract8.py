class emp:
    def __init__(self,no,name,sal):
        self.no=no
        self.name=name
        self.sal=sal
    def dispaly(self):
        print(' Id =',self.no)
        print(' Name =',self.name)
        print(' salary =',self.sal)
        
class temp:
    @staticmethod
    def inc(e):
        e.sal += 10000
        e.dispaly()
print('------before increment-------')
e = emp(101,'Mohit',110000)
e.dispaly()
print('-----After Increment-----')
temp.inc(e)
