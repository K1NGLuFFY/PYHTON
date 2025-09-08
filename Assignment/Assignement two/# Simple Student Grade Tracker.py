# Simple Student Grade Tracker

students = {}

# Add students
students["Alice"] = []
students["Bob"] = []

# Add grades
students["Alice"].append(85)
students["Alice"].append(90)
students["Bob"].append(78)

# Display students and grades
print("Students and Grades:")
for name in students:
    grades = students[name]
    if grades:
        average = sum(grades) / len(grades)
    else:
        average = 0
    print(f"{name}: {grades} | Average: {average:.2f}")

# Find top student
top_student = None
top_average = -1
for name in students:
    grades = students[name]
    if grades:
        average = sum(grades) / len(grades)
        if average > top_average:
            top_average = average
            top_student = name

print(f"Top student: {top_student}")
