activation_key = input()
command = input()
while not command == "Generate":
    instructions = command.split(">>>")
    if instructions[0] == "Contains":
        substring = instructions[1]
        if substring in activation_key:
            print(f"{activation_key} contains {substring}")
        else:
            print("Substring not found!")
    elif instructions[0] == "Flip":
        case = instructions[1]
        start_index = int(instructions[2])
        end_index = int(instructions[3])
        changed_part = activation_key[start_index:end_index]
        if case == "Upper":
            changed_part_upper = changed_part.upper()
            activation_key = activation_key.replace(changed_part, changed_part_upper)
            print(activation_key)
        elif case == "Lower":
            changed_part_lower = changed_part.lower()
            activation_key = activation_key.replace(changed_part, changed_part_lower)
            print(activation_key)
    elif instructions[0] == "Slice":
        start_index = int(instructions[1])
        end_index = int(instructions[2])
        changed_part = activation_key[start_index:end_index]
        activation_key = activation_key.replace(changed_part, "")
        print(activation_key)
    command = input()
print(f"Your activation key is: {activation_key}")
