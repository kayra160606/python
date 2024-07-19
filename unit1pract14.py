
my_list = [10, 20, 30, 40, 50, 60, 70]

print("Original List:", my_list)


my_list.append(80)
print("After appending 80:", my_list)


my_list.insert(3, 35)
print("After inserting 35 at 4th position:", my_list)


my_list_copy = my_list.copy()
print("Copied List:", my_list_copy)


my_list.extend([90, 100, 110])
print("After extending with [90, 100, 110]:", my_list)

count = my_list.count(40)
print("Count of 40:", count)


my_list.remove(40)
print("After removing 40:", my_list)


popped_element = my_list.pop(5)
print("Popped element:", popped_element)
print("After popping:", my_list)


my_list.sort()
print("After sorting:", my_list)


my_list.reverse()
print("After reversing:", my_list)


my_list.clear()
print("After clearing:", my_list)