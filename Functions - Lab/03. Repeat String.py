word = input()
number_of_repeats = int(input())


def repeating_word(string, times):
    result = ""
    for number in range(0, times):
        result += string
    return result


print(repeating_word(word, number_of_repeats), end="")