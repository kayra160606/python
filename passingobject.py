class emp:
    def __init__(self,no,sal):
        self.no=no
        self.sal=sal
    def dispaly(self):
        print(' no =',self.no)
        print(' salary =',self.sal)
        
class temp:
    @staticmethod
    def inc(e):
        e.sal += 1000
        e.dispaly()
print('------before increment-------')
e = emp(101,10000)
e.dispaly()
print('-----After Increment-----')
temp.inc(e)
