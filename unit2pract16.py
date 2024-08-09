my_list = [1, 2, 3, 4, 5, 6, 7]

#append
my_list.append(4)
print(my_list)

#extend
my_list.extend([4, 5, 6])
print(my_list)

#insert
my_list.insert(1, 4)
print(my_list)

#remove
my_list.remove(2)
print(my_list)

#pop
popped_element = my_list.pop(1)
print(my_list)
print(popped_element)

#index
index = my_list.index(4)
print(index)

#count
count = my_list.count(2)
print(count)


#sort
my_list.sort()
print(my_list)


#reverse
my_list.reverse()
print(my_list)

#clear
my_list.clear()
print(my_list)