#write program using class and find multiplicatin,addition,subtaraction,division of two number..
class Calculator:
    def __init__(self):
        pass

    def multiply(self, num1, num2):
        return num1 * num2

    def add(self, num1, num2):
        return num1 + num2

    def subtract(self, num1, num2):
        return num1 - num2

    def divide(self, num1, num2):
        if num2 == 0:
            return num1 / num2

calc = Calculator()
operation = input("Enter the operation (+, -, *, /): ")
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

if operation == "+":
    result = calc.add(num1, num2)
elif operation == "-":
    result = calc.subtract(num1, num2)
elif operation == "*":
    result = calc.multiply(num1, num2)
elif operation == "/":
    result = calc.divide(num1, num2)
else:
    print("Invalid operation!")
    exit()


print("Result:", result)
