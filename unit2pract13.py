import employee
print("SALARY PROGRAM")
b=int(input('Enter basic salary:'))
print('Your basic salary is',b)

da=employee.DA(b)
print(da)

hra=employee.HRA(b)
print(hra)

pf=employee.PF(b)
print(pf)

itax=employee.ITAX(b)
print(itax)

gross_sal=da+hra-pf
net_sal=gross_sal-itax

print('Your gross salary is:',gross_sal)
print('Your net salary is:',net_sal)