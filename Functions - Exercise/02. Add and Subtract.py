first_number = int(input())
second_number = int(input())
third_number = int(input())


def sum_numbers(num1=first_number, num2=second_number):
    result = num1 + num2
    return result


def subtract(num3=third_number):
    subtract_result = sum_numbers() - num3
    return subtract_result


def add_and_subtract():
    return subtract()


print(add_and_subtract())