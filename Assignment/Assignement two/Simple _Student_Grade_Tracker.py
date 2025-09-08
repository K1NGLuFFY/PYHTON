students = {}

def add_student(name, grade=None):
    if not isinstance(name, str) or not name.strip():
        print("Error: Invalid student name.")
        return
    if name in students:
        print("Error: Student already exists.")
        return
    students[name] = []
    if grade is not None:
        try:
            grade = float(grade)
            if grade < 0 or grade > 100:
                print("Error: Grade must be between 0 and 100.")
                return
            students[name].append(grade)
        except ValueError:
            print("Error: Invalid grade value.")
    print(name + " added.")

def calculate_average(name):
    if name not in students:
        return 0
    if len(students[name]) == 0:
        return 0
    return sum(students[name]) / len(students[name])

def display_students():
    print("--------------------------------------------")
    print("Student Name    | Grades            | Average")
    print("--------------------------------------------")
    if not students:
        print("No students to display.")
    for name, grades in students.items():
        grades_text = ", ".join(str(g) for g in grades)
        avg = calculate_average(name)
        print(name + " " * (15 - len(name)) + "| " + grades_text + " " * (15 - len(grades_text)) + "| " + "{:.2f}".format(avg))
    print("--------------------------------------------")

# Console menu
while True:
    print("\nMenu:")
    print("1. Add student with grade")
    print("2. Show all students")
    print("3. Exit")

    choice = input("Choose an option: ")

    if choice == "1":
        name = input("Enter student name: ")
        grade = input("Enter student grade: ")
        add_student(name, grade)
    elif choice == "2":
        display_students()
    elif choice == "3":
        print("Goodbye!")
        break
    else:
        print("Invalid choice. Try again.")
