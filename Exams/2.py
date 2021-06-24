health = 100
bitcoins = 0
room = 0
are_u_alive = True
rooms_list = input().split("|")
# ['cat 10', 'potion 30', 'orc 10', 'chest 10', 'snake 25', 'chest 110']
for el in rooms_list:
    room += 1
    el = el.split()
    command, number = el[0], el[1]
    number = int(number)
    if command == "potion":
        health += number
        if health > 100:
            number = abs((health - number) - 100)
            health = 100
        print(f"You healed for {number} hp.")
        print(f"Current health: {health} hp.")
    elif command == "chest":
        bitcoins += number
        print(f"You found {number} bitcoins.")
    else:
        monster = command
        attack_of_the_monster = number
        health -= attack_of_the_monster
        if health > 0:
            print(f"You slayed {monster}.")
        else:
            print(f"You died! Killed by {monster}.")
            print(f"Best room: {room}")
            are_u_alive = False
            break
if are_u_alive:
    print(f"You've made it!")
    print(f"Bitcoins: {bitcoins}")
    print(f"Health: {health}")

