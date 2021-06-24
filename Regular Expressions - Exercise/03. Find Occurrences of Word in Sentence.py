import re

text = input()
word = input()
pattern = rf"\b{word}\b"
count_words = re.findall(pattern, text, re.IGNORECASE)
print(len(count_words))