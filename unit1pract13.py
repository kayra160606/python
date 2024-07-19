
my_list = list(range(1, 11))  # [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

print("Original List:", my_list)


my_list.append(11)
print("After appending 11:", my_list)


my_list[5] = 20
print("After updating 6th element to 20:", my_list)


del my_list[3]
print("After deleting 4th element:", my_list)


my_list.remove(20)
print("After removing 20:", my_list)