n = int(input())
word = input()
strings_in_line = []
special_list = []

for lines in range(n):
    strings = input()
    if word in strings:
        special_list.append(strings)
    strings_in_line.append(strings)


print(strings_in_line)
print(special_list)