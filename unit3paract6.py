class myclass:
    n=0
    def __init__(self):
        myclass.n+=1
    #static method
    @staticmethod
    def no_of_objects():
        print("No of instances created are",myclass.n)
obj1 = myclass()
obj2 = myclass()
obj3 = myclass()
myclass.no_of_objects()