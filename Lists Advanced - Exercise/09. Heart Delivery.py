our_neighborhood = list(map(int, input().split("@")))
command = input()
jump_length = 0
while not command == "Love!":
    jump, index = command.split()
    index = int(index)
    jump_length += index
    if len(our_neighborhood) > jump_length:
        if our_neighborhood[jump_length] <= 0:
            print(f"Place {jump_length} already had Valentine's day.")
        else:
            our_neighborhood[jump_length] -= 2
            if our_neighborhood[jump_length] <= 0:
                print(f"Place {jump_length} has Valentine's day.")
    else:
        jump_length = 0
        if our_neighborhood[jump_length] <= 0:
            print(f"Place {jump_length} already had Valentine's day.")
        else:
            our_neighborhood[jump_length] -= 2
            if our_neighborhood[jump_length] <= 0:
                print(f"Place {jump_length} has Valentine's day.")
    command = input()
counter = 0
for n in our_neighborhood:
    if n > 0:
        counter += 1
print(f"Cupid's last position was {jump_length}.")
if not counter == 0:
    print(f"Cupid has failed {counter} places.")
else:
    print("Mission was successful.")