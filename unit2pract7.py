li=[1,2,3,3,4,2,5,5,6,6,6,7,7,12,12,14,14,15]
li2=[]
for i in li:
    if i not in li2:
        li2.append(i)
print(li2)