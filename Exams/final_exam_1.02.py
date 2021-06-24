import re
text = input()
cool_threshold = 1
pattern = r"(\:\:|\*\*)[A-Z][a-z]{2,}\1"
emojis = []
for ch in text:
    if ch.isdigit():
        cool_threshold *= int(ch)
text = text.split()
for word in text:
    valid_emojis = [el.group() for el in re.finditer(pattern, word)]
    if valid_emojis:
        emojis.extend(valid_emojis)

print(f"Cool threshold: {cool_threshold}")
print(f"{len(emojis)} emojis found in the text. The cool ones are:")
for emoji in emojis:
    emoji_coolness = 0
    for ch in emoji:
        if ch.isalpha():
            emoji_coolness += ord(ch)
    if emoji_coolness > cool_threshold:
        print(f"{emoji}")