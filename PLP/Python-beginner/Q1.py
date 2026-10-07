name = input("Enter your name: ")
age_int = int(input("Enter your age: "))

# (a)

birth_year = 2025 - age_int

print("Name:", name)
print("Birth Year:", birth_year)

# (b)
if age_int % 2 == 0:
    print("Age is even")
else:
    print("Age is odd")

# (c)
age_ratio = float(age_int) / 80
print("Age divided by life expectancy:", f"{age_ratio:.4f}")

# (d)
print("Type of name:", type(name))
print("Type of age before conversion:", type(age))
print("Type of age after conversion:", type(age_int))