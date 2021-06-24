first_number = int(input())
second_number = int(input())


def factorial_division(num1=first_number, num2=second_number):
    first_number_factorial = 1
    second_number_factorial = 1
    for number1 in range(1, num1 + 1):
        first_number_factorial *= number1
    for number2 in range(1, num2 + 1):
        second_number_factorial *= number2
    final_result = first_number_factorial / second_number_factorial
    print(f"{final_result:.2f}")
    return exit()


print(factorial_division())