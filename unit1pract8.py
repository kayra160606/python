minimum=int(input("Please Enter the Minimum Value :"))
maximum=int(input("Please Enter The Maximum Value :"))
even_total=0
odd_total=0

for number in range (minimum,maximum + 1):
    if(number % 2 == 0):
        even_total = even_total + number
    else:
        odd_total = odd_total + number
    
print("The sum of even number from 1 to {0} = {1}".format(number,even_total))
print("The sum of odd numbers from 1 to {0} = {1}".format(number,odd_total))