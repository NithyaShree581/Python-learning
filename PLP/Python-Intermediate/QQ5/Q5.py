"""Topic: Modules, Packages & Virtual Environments 
Answer each part with exact commands or code: 
(a) Commands to: create virtual environment plp_env, activate it, install pandas and requests, export requirements.txt. 
(b) File structure for package 'gradebook' with student.py and report.py. Write __init__.py exposing Student and generate_report(). 
(c) In report.py, write generate_report(students: list). Import and use from top-level main.py. 
(d) Predict the output: # student.py: class Student:     def __init__(self, name): self.name = name # main.py: from gradebook import Student s = Student('Priya') print(s.name, type(s).__name__, isinstance(s, Student)) 
"""
#a
# command to create a virtual environment 
# python -m venv plp_env
#.\plp_env\scripts\Activate.ps1
#pip install pandas,requests
#pip freeze > requirements.txt


#c
