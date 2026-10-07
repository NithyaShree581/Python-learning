# (a) and (b)
a = 0
b = 1
count = 0
while count < 15:
    if a > 1000:
        break
    if a < 10:
        label = "Small"
    elif a <= 100:
        label = "Medium"
    else:
        label = "Large"
    print(a, "-", label)
    a, b = b, a + b
    count += 1


# (c)
print("\nMultiplication Table of 7")
for i in range(1, 6):
    print("7 x", i, "=", 7 * i)


# (d)
result = []
for i in range(1, 6):
    if i % 2 == 0:
        result.append(i * i)
print(result)
x = 10
while x > 0:
    x -= 3
print(x)