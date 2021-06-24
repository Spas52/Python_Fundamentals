list_of_employee_happiness = list(map(lambda num: int(num), input().split(" ")))
# [1, 2, 3, 4, 2, 1]

happiness_improvement_factor = int(input())

multiplying_happiness = list(map(lambda num: num * happiness_improvement_factor, list_of_employee_happiness))
# [3, 6, 9, 12, 6, 3]

filtered = list(filter(lambda num: num >= (sum(multiplying_happiness) / len(multiplying_happiness)), multiplying_happiness))
# [9,12]


if len(filtered) >= len(multiplying_happiness) / 2:
    print(f"Score: {len(filtered)}/{len(multiplying_happiness)}. Employees are happy!")
else:
    print(f"Score: {len(filtered)}/{len(multiplying_happiness)}. Employees are not happy!")