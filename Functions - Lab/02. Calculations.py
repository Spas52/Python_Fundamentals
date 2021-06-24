operator = input()
num1 = int(input())
num2 = int(input())


def calculates_of_nums(number1,number2):
    if operator == "multiply":
        return number1 * number2
    elif operator == "divide":
        return number1 / number2
    elif operator == "add":
        return number1 + number2
    elif operator == "subtract":
        return number1 - number2


print(f"{calculates_of_nums(num1, num2):.0f}")