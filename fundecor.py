# def num():
#     return 10

# def decor(fun):
#     def inner():
#         val=fun()
#         return val+2
#     return inner

# ans = decor(num)
# print(ans())

def decor(fun):
    def inner():
        val=fun()
        return val+2
    return inner

@decor

def num():
    return 10
res=num()
print(res)