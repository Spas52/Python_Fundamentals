first = int(input())
second = int(input())
third = int(input())
students_count = int(input())
students_per_hour = first + second + third
hour = 0
while students_count > 0:
    hour += 1
    students_count -= students_per_hour
    if hour % 4 == 0:
        hour += 1

print(f"Time needed: {hour}h.")