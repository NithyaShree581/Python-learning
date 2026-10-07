"""3. With a given list [12,24,35,24,88,120,155,88,120,155], write a program to print this
list after removing all duplicate values with original order reserved.
Hint: Use set() to store a number of values without duplicates.
"""
listt = [12, 24, 35, 24, 88, 120, 155, 88, 120, 155]

seen = set()
result = []

for number in listt:
    if number not in seen:
        seen.add(number) 
        result.append(number)

print(result)