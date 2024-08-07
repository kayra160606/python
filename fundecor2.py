# def num():
#     return 10

# def decor1(fun):
#     def inner():
#         val=fun()
#         return val+2
#     return inner

# def decor2(fun):
#     def inner():
#         val=fun()
#         return val*2
#     return inner

# res=decor1(decor2(num))
# print(res())


def decor1(fun):
    def inner():
        val=fun()
        return val+2
    return inner

def decor2(fun):
    def inner():
        val=fun()
        return val*2
    return inner

@decor1
@decor2

def num():
    return 10
res=num()
print(res)