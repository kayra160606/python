
list1 = [1, 2, 3, 4, 5]
list2 = [6, 7, 8, 9, 10]

print("List 1:", list1)
print("List 2:", list2)


combined_list = list1 + list2
print("Combined List:", combined_list)


repeated_list = list1 * 3
print("Repeated List:", repeated_list)


cloned_list = list1.copy()
print("Cloned List:", cloned_list)


cloned_list2 = list(list1)
print("Cloned List 2:", cloned_list2)


cloned_list3 = list1[:]
print("Cloned List 3:", cloned_list3)


list1.append(11)
print("Modified Original List:", list1)


print("Cloned List:", cloned_list)
print("Cloned List 2:", cloned_list2)
print("Cloned List 3:", cloned_list3)