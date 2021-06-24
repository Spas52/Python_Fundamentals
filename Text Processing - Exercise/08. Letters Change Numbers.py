data = input().split()
# ['A12b', 's17G']
final_result = 0
for string in data:
    first_letter = string[0]
    last_letter = string[-1]
    number = int(string[1:-1])
    result = 0
    if first_letter.isupper():
        position_of_first_letter_upper = int(ord(first_letter) - 64)
        result += number / position_of_first_letter_upper
    else:
        position_of_first_letter_lower = int(ord(first_letter) - 96)
        result += number * position_of_first_letter_lower
    if last_letter.isupper():
        position_of_last_letter_upper = int(ord(last_letter) - 64)
        result -= position_of_last_letter_upper
    else:
        position_of_last_letter_lower = int(ord(last_letter) - 96)
        result += position_of_last_letter_lower
    final_result += result

print(f"{final_result:.2f}")
