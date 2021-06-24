import math
number_of_people = int(input())
capacity_of_the_elevator = int(input())
courses = number_of_people / capacity_of_the_elevator
if number_of_people % capacity_of_the_elevator != 0:
    courses += 1
print(math.floor(courses))