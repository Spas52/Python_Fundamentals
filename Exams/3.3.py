numbers = list(map(int, input().split(" ")))
average_number = 0
for number in numbers:
    average_number += number
average_number /= len(numbers)
greater_num = [num for num in numbers if num > average_number]
greater_num.sort()
greater_num.reverse()
if len(greater_num) > 5:
    while len(greater_num) > 5:
        greater_num.pop(-1)
if len(greater_num) == 0:
    print("No")
else:
    print(" ".join(map(str, greater_num)))
