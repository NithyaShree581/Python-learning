# (a)
def safe_divide(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        print("Cannot divide by zero")
    except TypeError:
        print("Invalid data type")

# (b)
def read_student_file(filename):
    try:
        with open(filename, "r") as file:
            print(file.read())
    except FileNotFoundError:
        print("File not found")
    finally:
        print("File operation complete")


# (c)
print(safe_divide(10, 2))
print(safe_divide(10, 0))
print(safe_divide(10, "2"))
read_student_file("students.txt")
read_student_file("missing.txt")

# (d)
def safe_div(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        return "Zero!"
    finally:
        print("Done")
print(safe_div(10, 2))
print(safe_div(5, 0))