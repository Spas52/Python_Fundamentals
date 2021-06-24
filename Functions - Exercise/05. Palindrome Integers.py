list_of_numbers = [int(x) for x in input().split(", ")]


def is_number_palindrome(number=None):
    if number is None:
        number = list_of_numbers
    for element in number:
        res = str(element) == str(element)[::-1]
        print(str(res))


is_number_palindrome()
