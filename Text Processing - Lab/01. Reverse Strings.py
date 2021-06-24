command = input()
while not command == "end":
    reversed_text = ""
    for ch in reversed(command):
        reversed_text += ch
    print(f"{command} = {reversed_text}")
    command = input()