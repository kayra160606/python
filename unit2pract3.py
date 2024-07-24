my_list = [1,2,3,4,5,6,7]

#append
my_list.append(10)
print('append:',my_list)

#insert
my_list.insert(2,20)
print('insert:',my_list)

#remove
my_list.remove(2)
print('remove',my_list)

#pop
popped_element = my_list.pop(1)
print('pop:',my_list)
print('poped element:',popped_element)

#index
index = my_list.index(3)
print('index:',index)

#count
count = my_list.count(4)
print('count:',count)