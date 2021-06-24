import re
text = input()
pattern = r"\d+"
all_numbers = []
while not text == "":
    match = re.findall(pattern, text)
    all_numbers.extend(match)
    text = input()
print(*all_numbers)
