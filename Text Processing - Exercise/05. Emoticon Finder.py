text = input()
for index in range(0, len(text)):
    if text[index] == ":":
        emojis = f"{text[index]}{text[index + 1]}"
        print(emojis)

# There are so many emoticons nowadays :P. I have many ideas :O what input to place here :)
# :O :D :P