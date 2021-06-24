import math
students_count = int(input())
lectures_count = int(input())
additional_bonus = int(input())
attendances = 0
bonus = 0
for student in range(0, students_count):
    attendances_count = int(input())
    max_bonus = (attendances_count / lectures_count * (5 + additional_bonus))
    if max_bonus > bonus:
        attendances = attendances_count
        bonus = max_bonus
print(f"Max Bonus: {math.ceil(bonus)}.")
print(f"The student has attended {attendances} lectures.")
