"""
A simple grade calculator that assigns letter grades based on numeric scores.

"""
score = input("Enter your score (0-100): ")

if score.isdigit():
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
            message = "Fair effort, but you can do better."
        elif score >= 60:
            grade = "D"
            message = "You passed, but work harder next time."
        else:
            grade = "F"
            message = "Don’t give up, study harder!"

        print(f"Your grade is {grade}. {message}")
    else:
        print("Invalid score. Please enter a number between 0 and 100.")
else:
    print("Invalid input. Please enter a number.")