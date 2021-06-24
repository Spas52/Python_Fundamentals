numbers_as_string = input().split(" ")
n = int(input())
for i in range(0, len(numbers_as_string)):
    numbers_as_string[i] = int(numbers_as_string[i])
for y in range(n):
    numbers_as_string.remove(min(numbers_as_string))
print(numbers_as_string)

