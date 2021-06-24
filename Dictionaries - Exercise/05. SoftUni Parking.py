n = int(input())
registers = {}
for command in range(n):
    line = input().split()
    type_of_command = line[0]
    if type_of_command == "register":
        username = line[1]
        license_plate_number = line[2]
        if username not in registers:
            registers[username] = license_plate_number
            print(f"{username} registered {license_plate_number} successfully")
        else:
            print(f"ERROR: already registered with plate number {license_plate_number}")
    elif type_of_command == "unregister":
        username = line[1]
        if username not in registers:
            print(f"ERROR: user {username} not found")
        else:
            del registers[username]
            print(f"{username} unregistered successfully")
for username, license_plate in registers.items():
    print(f"{username} => {license_plate}")

