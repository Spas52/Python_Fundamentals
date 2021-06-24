import re

text = input()

patter = r"(^|(?<=\s))[a-zA-Z0-9]+[\._-]?[a-zA-Z0-9]+@[a-z]+-?[a-z]+(\.[a-z]+)+"

matches = [el.group() for el in re.finditer(patter, text)]
print("\n".join(matches))
