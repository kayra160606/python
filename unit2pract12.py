def plus_one(number):
    def add_one(number):
        val=number()
        return val + 3
    result = add_one(number)
    return result

def number():
    return 10

res=plus_one(number)
print(res)
