"""
A simple student grade tracker that allows adding students, recording grades,
calculating averages, and identifying the top student.

"""

students = {}

def add_student(name):
    students[name] = []
    print(name + " added.")

def add_grade(name, grade):
    if name in students:
        students[name].append(grade)
        print("Added grade " + str(grade) + " for " + name)
    else:
        print("Student not found.")

def calculate_average(name):
    if name in students and len(students[name]) > 0:
        total = 0
        for grade in students[name]:
            total = total + grade
        average = total / len(students[name])
        return average
    else:
        return 0

def find_top_student():
    top_student = None
    top_average = 0
    for name in students:
        avg = calculate_average(name)
        if avg > top_average:
            top_average = avg
            top_student = name
    return top_student

def display_students():
    print("--------------------------------------------")
    print("Student Name    | Grades            | Average")
    print("--------------------------------------------")
    for name in students:
        grades = students[name]
        avg = calculate_average(name)
        grades_text = ""
        for g in grades:
            grades_text = grades_text + str(g) + ", "
        grades_text = grades_text[:-2] if grades_text else ""
        print(name + " " * (15 - len(name)) + "| " + grades_text + " " * (15 - len(grades_text)) + "| " + "{:.2f}".format(avg))
    print("--------------------------------------------")

add_student("Alice")
add_student("Bob")

add_grade("Alice", 85)
add_grade("Alice", 90)
add_grade("Bob", 78)
add_grade("Bob", 92)

display_students()

top = find_top_student()
print("Top student is: " + str(top))
