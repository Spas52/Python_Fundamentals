first_character = input()
second_character = input()


def character_in_range(first=first_character, second=second_character):
    first_symbol = ord(first_character)
    second_symbol = ord(second_character)
    result = ""
    for symbols in range(first_symbol + 1, second_symbol):
        as_character = chr(symbols)
        result += as_character + " "
    return result


print(character_in_range())