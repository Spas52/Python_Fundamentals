first_number = int(input())
second_number = int(input())
third_number = int(input())


def the_smallest_number(num1, num2, num3):
    list_of_numbers = [num1, num2, num3]
    list_of_numbers.sort()
    smallest_number = list_of_numbers[0]
    return smallest_number


print(the_smallest_number(first_number, second_number, third_number))

