command = input()
command_count = 0
ores = {}
ore = ""
while not command == "stop":
    command_count += 1
    if not command_count % 2 == 0:
        ore = command
        if command not in ores:
            ores[command] = 0
    else:
        ores[ore] += int(command)
    command = input()
for ore,price in ores.items():
    print(f"{ore} -> {price}")