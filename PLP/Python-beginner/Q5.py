# (a), (b), (c) and (d)

students = []
with open("students.txt", "r") as file:
    lines = file.readlines()
for line in lines:
    line = line.strip()
    name, score = line.split(",")
    students.append((name.strip(), int(score.strip())))
for name, score in students:
    print(name.upper(), score)
    
scores = [score for name, score in students]
average = sum(scores) / len(scores)
highest = max(students, key=lambda student: student[1])
print("Class Average:", round(average, 1))
print("Highest Score:", highest[0], highest[1])
summary = f"Class Average: {average:.1f} | Total Students: {len(students)}"
with open("students.txt", "a") as file:
    file.write("\n" + summary)
