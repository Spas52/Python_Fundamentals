first = int(input())
second = int(input())
third = int(input())
people = int(input())
people_per_hour = first + second + third
hour = 0
while people > 0:
    hour += 1
    people -= people_per_hour
    if hour % 4 == 0:
        hour += 1
print(f"Time needed: {hour}h.")
