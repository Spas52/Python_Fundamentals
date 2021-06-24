import re

text = input()
pattern = r"(^ |(?<=\s_))[a-zA-Z0-9]+\b"
match = [obj.group() for obj in re.finditer(pattern, text)]
print(",".join(match))