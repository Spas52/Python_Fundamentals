raw_password = input()
command = input()
while not command == "Done":
    command = command.split()
    action = command[0]
    if action == "TakeOdd":
        raw_password = [raw_password[index] for index in range(1, len(raw_password), 2)]
        raw_password = "".join(raw_password)
        print(raw_password)
    elif action == "Cut":
        index = int(command[1])
        length = int(command[2])
        raw_password = raw_password[0: index:] + raw_password[(index + length)::]
        print(raw_password)
    elif action == "Substitute":
        substring = command[1]
        substitute = command[2]
        if substring in raw_password:
            raw_password = raw_password.replace(substring, substitute)
            print(raw_password)
        else:
            print("Nothing to replace!")
    command = input()
print(f"Your password is: {raw_password}")
