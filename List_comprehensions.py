#Simple & long
numbers = []
for num in [1, 3, 5, 7, 9]:
    numbers.append(num**2)
print(numbers)

#Simple & short
numbers = [num**2 for num in [1, 3, 5, 7, 9]]
print(numbers)