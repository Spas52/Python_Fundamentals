numbers = list(map(int, input().split(" ")))
# [23, -2, 321, 87, 42, 90, -123]
command = input()
count = 0
while not command == "end":
    command = command.split(" ")
    action = command[0]
    if action == "swap":
        index1 = int(command[1])
        index2 = int(command[2])
        numbers[index1], numbers[index2] = numbers[index2], numbers[index1]
    elif action == "multiply":
        numbers[int(command[1])] *= numbers[int(command[2])]
    elif action == "decrease":
        numbers = [num - 1 for num in numbers]
    command = input()

print(", ".join(map(str, numbers)))