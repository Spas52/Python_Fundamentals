str_1 = input()
str_2 = input()

result = ""
previous_str = str_1

for index in range(len(str_1)):
    for i in range(index + 1):
        result += str_2[i]
    for i in range(index + 1, len(str_2)):
        result += str_1[i]
    if not result == previous_str:
        print(result)
    previous_str = result
    result = ""
