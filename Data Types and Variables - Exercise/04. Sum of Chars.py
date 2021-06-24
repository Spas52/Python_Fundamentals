number_of_lines =  int(input())
summary = 0
for i in range(number_of_lines):
    letter = input()
    letter1 = ord(letter)
    summary += letter1
print(f"The sum equals: {summary}")
