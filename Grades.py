def calculate_grade(marks):
    if marks >= 90:
        return "A++"
    elif marks >= 80:
        return "A"
    elif marks >= 60:
        return "B++"
    elif marks >= 50:
        return "B"
    elif marks >= 35:
        return "C"
    else:
        print("Sorry!")
        return "Fail"

student_marks = int(input("Enter the marks of yours: "))
grade = calculate_grade(student_marks)
print(f"Your grade is: {grade}")