student_academy = {}
n = int(input())
sum_of_grades = 0
best_students = {}
for _ in range(n):
    student_name = input()
    grade = float(input())
    if student_name not in student_academy:
        student_academy[student_name] = []
    student_academy[student_name].append(grade)


for student, grades in student_academy.items():
    for grade in grades:
        sum_of_grades += grade
    avg = sum_of_grades / len(grades)
    if avg < 4.50:
        del student
    else:
        best_students[student] = avg
    sum_of_grades = 0

sorted_best_students = sorted(best_students.items(), key=lambda kvp: kvp[1], reverse=True)
for hui, grade in sorted_best_students:
    print(f"{hui} -> {grade:.2f} ")

# 5
# John
# 5.5
# John
# 4.5
# Alice
# 6
# Alice
# 3
# George
# 5