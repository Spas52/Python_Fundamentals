def corresponding_grade(num1):
    if 2 <= num1 <= 2.99:
        return "Fail"
    elif 3 <= num1 <= 3.49:
        return "Poor"
    elif 3.50 <= num1 <= 4.49:
        return "Good"
    elif 4.50 <= num1 <= 5.49:
        return "Very Good"
    elif 5.50 <= num1 <= 6.00:
        return "Excellent"


grade = float(input())
print(corresponding_grade(grade))