def calculate_grade(score, total=100, passing=50):
    if score < 0 or score > total:
        raise ValueError("Score must be between 0 and total")
    percentage = (score / total) * 100
    if percentage >= 90:
        grade = "A"
    elif percentage >= 75:
        grade = "B"
    elif percentage >= 60:
        grade = "C"
    elif percentage >= passing:
        grade = "D"
    else:
        grade = "F"

    return percentage, grade

# (a), (b), (c) and (d)

print(calculate_grade(95))
print(calculate_grade(80))
print(calculate_grade(65))
print(calculate_grade(40))

try:
    print(calculate_grade(-10))
except ValueError as e:
    print(e)


# (e)

def grade(s, t=100, p=50):
    pct = (s / t) * 100
    return "Pass" if pct >= p else "Fail"

print(grade(45))
print(grade(60, 150))
print(grade(80, p=90))