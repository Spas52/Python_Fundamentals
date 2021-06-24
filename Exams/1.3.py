our_neighborhood = list(map(int, input().split("@")))
# 10, 10, 10, 2
command = input()
cupid_location = 0
house_count = 0
is_mission_successful = True
while not command == "Love!":
    jump = command.split()[0]
    length_of_jump = command.split()[1]
    cupid_location += int(length_of_jump)
    if cupid_location > len(our_neighborhood) - 1:
        cupid_location = 0
    our_neighborhood[cupid_location] -= 2
    if our_neighborhood[cupid_location] == 0:
        print(f"Place {cupid_location} has Valentine's day.")
    if our_neighborhood[cupid_location] < 0:
        our_neighborhood[cupid_location] = 0
        print(f"Place {cupid_location} already had Valentine's day.")

    command = input()
print(f"Cupid's last position was {cupid_location}.")
for house in our_neighborhood:
    if house != 0:
        house_count += 1
        is_mission_successful = False
if is_mission_successful:
    print("Mission was successful.")
else:
    print(f"Cupid has failed {house_count} places.")