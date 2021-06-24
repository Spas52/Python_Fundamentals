number = input()
numbers_list = []
for x in range(0, len(number)):
    numbers_list.append(int(number[x]))
for y in range(len(numbers_list)):
    print(max(numbers_list), end="")
    numbers_list.remove(max(numbers_list))