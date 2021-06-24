import re

phone_numbers = input()
regex = r"\+359( |-)2\1[0-9]{3}\b\1[0-9]{4}\b"
valid_phone_numbers = [obj.group() for obj in re.finditer(regex, phone_numbers)]
print(", ".join(valid_phone_numbers))