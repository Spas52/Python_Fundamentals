n = int(input())
list_of_numbers = []
even = []
odd = []
negative = []
positive = []
for numbers in range(n):
    number = int(input())
    list_of_numbers.append(number)

command = input()

for index in range(0, len(list_of_numbers)):
    number = list_of_numbers[index]
    if command == "even":
        if number % 2 == 0 or number == 0:
            even.append(number)
        if index == len(list_of_numbers) - 1:
            print(even)
    elif command == "odd":
        if not number % 2 == 0:
            odd.append(number)
        if index == len(list_of_numbers) - 1:
            print(odd)
    elif command == "negative":
        if number < 0:
            negative.append(number)
        if index == len(list_of_numbers) - 1:
            print(negative)
    elif command == "positive":
        if not number < 0 or number == 0:
            positive.append(number)
        if index == len(list_of_numbers) - 1:
            print(positive)