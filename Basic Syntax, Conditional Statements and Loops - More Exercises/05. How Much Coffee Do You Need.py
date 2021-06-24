command = input()
count = 0
extra_sleep = False
while not command == "END":
    if command == "coding" or command == "dog" or command == "cat" or command == "movie":
        count += 1
    elif command == "CODING" or command == "DOG" or command == "CAT" or command == "MOVIE":
        count += 2
    if count > 5:
        extra_sleep = True
        print("You need extra sleep")
        break
    command = input()
if not extra_sleep:
    print(f"{count}")
