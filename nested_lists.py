##TASK:
#Given the names and grades for each student in a class of  students,
#store them in a nested list and print the name(s) of any student(s)
#having the second lowest grade.
#--> Russell Beasley and Corbin Ochoa

records = [
    ["Zhuri Pham", 50],
    ["Russell Beasley", 20],
    ["Jaylah Watson", 80],
    ["Greyson Navarro", 10],
    ["Winter Jennings", 50],
    ["Corbin Ochoa", 20],
    ["Luciana O'Neal", 30],
    ["Eddie Willis", 30],
    ["Alexa Medrano", 10],
    ["Arian Raymond", 60]
]


#identify unique grades
unique_grades = set(grade for name, grade in records)

#identify second lowest grade
second_lowest_grade = sorted(unique_grades)[1]

#identify all students with the second lowest grade
names = [name for name, grade in records if grade == second_lowest_grade]


print(f"list of names: {names}")
print(f"second lowest grade: {second_lowest_grade}")
