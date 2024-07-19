
elements = tuple(map(int, input("Enter elements separated by space: ").split()))

print("Tuple of elements:", elements)


minimum = min(elements)
maximum = max(elements)
total_sum = sum(elements)
average = total_sum / len(elements)

print("Minimum:", minimum)
print("Maximum:", maximum)
print("Sum:", total_sum)
print("Average:", average)