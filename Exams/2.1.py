energy = int(input())
command = input()
count_of_won_battles = 0

while not command == 'End of battle':
    distance = int(command)

    if energy >= distance:
        energy -= distance
        count_of_won_battles += 1
        if count_of_won_battles % 3 == 0:
            energy += count_of_won_battles
    else:
        print(f"Not enough energy! Game ends with {count_of_won_battles} won battles and {energy} energy")
        break

    command = input()

if command == 'End of battle':
    print(f"Won battles: {count_of_won_battles}. Energy left: {energy}")