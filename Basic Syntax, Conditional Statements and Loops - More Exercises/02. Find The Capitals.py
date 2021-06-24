word = input()
list_of_capital_letters = []
index = -1
for letter in word:
    index += 1
    if 65 <= ord(letter) <= 90:
        list_of_capital_letters.append(index)

print(list_of_capital_letters)