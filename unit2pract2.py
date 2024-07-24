import array as arr # type: ignore
a=arr.array('i',[1,2,3,4,5])

#display array
print(a)

#update new using indexing
a[0]=7
print(a)

#update array using slicing
a[0:2]=arr.array('i',[8,9])
print(a)