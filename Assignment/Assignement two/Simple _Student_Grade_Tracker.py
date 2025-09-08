"""
A simple student grade tracker that allows adding students, recording grades,
calculating averages, and identifying the top student.

"""

students = {}

def add_student(name):
    try:
        if not isinstance(name, str) or not name.strip():
            raise ValueError("Invalid student name.")
        if name in students:
            raise ValueError("Student already exists.")
        students[name] = []
        print(name + " added.")
    except Exception as e:
        print("Error:", e)

def add_grade(name, grade):
    try:
        if name not in students:
            raise KeyError("Student not found.")
        grade = float(grade)
        if grade < 0 or grade > 100:
            raise ValueError("Grade must be between 0 and 100.")
        students[name].append(grade)
        print("Added grade " + str(grade) + " for " + name)
    except ValueError as ve:
        print("Error:", ve)
    except KeyError as ke:
        print("Error:", ke)
    except Exception:
        print("Error: Invalid grade value.")

def calculate_average(name):
    try:
        if name not in students:
            raise KeyError("Student not found.")
        if len(students[name]) == 0:
            print("Warning: No grades recorded for " + name)
            return 0
        total = sum(students[name])
        average = total / len(students[name])
        return average
    except KeyError as ke:
        print("Error:", ke)
        return 0
    except Exception as e:
        print("Error:", e)
        return 0

def find_top_student():
    try:
        if not students:
            raise ValueError("No students available.")
        top_student = None
        top_average = -1
        for name in students:
            avg = calculate_average(name)
            if avg > top_average:
                top_average = avg
                top_student = name
        if top_student is None:
            raise ValueError("No grades available to determine top student.")
        return top_student
    except Exception as e:
        print("Error:", e)
        return None

def display_students():
    print("--------------------------------------------")
    print("Student Name    | Grades            | Average")
    print("--------------------------------------------")
    if not students:
        print("No students to display.")
    for name in students:
        try:
            grades = students[name]
            avg = calculate_average(name)
            grades_text = ", ".join(str(g) for g in grades)
            print(name + " " * (15 - len(name)) + "| " + grades_text + " " * (15 - len(grades_text)) + "| " + "{:.2f}".format(avg))
        except Exception as e:
            print("Error displaying student:", name, "-", e)
    print("--------------------------------------------")

add_student("Alice")
add_student("Bob")
add_student("")  # Error example

add_grade("Alice", 85)
add_grade("Alice", 90)
add_grade("Bob", 78)
add_grade("Bob", 92)
add_grade("Charlie", 88)  # Error example
add_grade("Bob", "A+")    # Error example

display_students()

top = find_top_student()
print("Top student is: " + str(top))
