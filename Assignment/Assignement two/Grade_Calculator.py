"""
A simple grade calculator that assigns letter grades based on numeric scores.
Ask the user to input a score between 0 and 100, then output the corresponding letter grade along with a message.
And tell the user their score is invalid if the input is out of range or not a number.
"""

try:
    score = input("Enter your score (0-100): ")
    score = int(score)

    if 0 <= score <= 100:
        if score >= 90:
            grade = "A"
            message = "Excellent work!"
        elif score >= 80:
            grade = "B"
            message = "Good job, keep pushing!"
        elif score >= 70:
            grade = "C"
            message = "Fair effort"
        elif score >= 60:
            grade = "D"
            message = "You passed"
        else:
            grade = "F"
            message = "Fail!"

        print(f"Your grade is {grade}. {message}")
    else:
        print("Invalid score. Please enter a number between 0 and 100.")
except ValueError:
    print("Invalid input. Please enter a valid number.")