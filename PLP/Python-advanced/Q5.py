
"""Topic: Comprehensions & Functional Patterns 
Given a list of at least 6 employee dicts (name, dept, salary) across 3 departments. Use ONLY functional tools: 
(a) List comprehension: names of all 'Engineering' employees. 
(b) Dict comprehension: {name: salary} for employees earning > 60000. 
(c) Set comprehension: unique departments. 
(d) functools.reduce() to calculate total payroll. sorted() with lambda to print top 3 earners. 
(e) Predict the output: from functools import reduce emps = [{'name':'A','dept':'Eng','salary':80000},{'name':'B','dept':'HR','salary':55000},{'name':'C','dept':'Eng','salary':75000}] eng = [e['name'] for e in emps if e['dept']=='Eng'] total = reduce(lambda acc,e: acc+e['salary'], emps, 0) print(eng, total) 
"""
#a 

from functools import reduce
emps = [
    {'name': 'Alice', 'dept': 'Engineering', 'salary': 80000},
    {'name': 'Bob', 'dept': 'HR', 'salary': 55000},
    {'name': 'Charlie', 'dept': 'Engineering', 'salary': 75000},
    {'name': 'David', 'dept': 'Sales', 'salary': 65000},
    {'name': 'Emma', 'dept': 'HR', 'salary': 62000},
    {'name': 'Frank', 'dept': 'Sales', 'salary': 90000}
]

#a
names = [e['name'] for e in emps if e['dept'] == 'Engineering']
print("Engineering Employees", names)

#b
earners = {e['name']: e['salary'] for e in emps if e['salary'] > 60000}
print("Employees has above 60000:", earners)

# c
departments = {e['dept'] for e in emps}
print("Uniquedepartmnets", departments)

#d
payroll = reduce(lambda acc, e: acc + e['salary'],emps,0)
print("payroll", payroll)
top_3 = sorted(emps,key=lambda e: e['salary'],reverse=True)[:3]

print("Top 3 Earners:")
for employee in top_3:
    print(employee['name'], "-", employee['salary'])

