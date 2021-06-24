data = input()
targeted_cities = {}
# {'Tortuga': [345000, 1250], 'Santo Domingo': [240000, 630], 'Havana': [410000, 1100]}
while not data == "Sail":
    city, population, gold = data.split("||")
    population = int(population)
    gold = int(gold)
    if city in targeted_cities:
        targeted_cities[city][0] += population
        targeted_cities[city][1] += gold
    else:
        targeted_cities[city] = [population, gold]
    data = input()

event = input()
while not event == "End":
    command = event.split("=>")
    action = command[0]
    if action == "Plunder":
        town = command[1]
        people = int(command[2])
        gold = int(command[3])
        print(f"{town} plundered! {gold} gold stolen, {people} citizens killed.")
        targeted_cities[town][0] -= people
        targeted_cities[town][1] -= gold
        if targeted_cities[town][0] <= 0 or targeted_cities[town][1] <= 0:
            print(f"{town} has been wiped off the map!")
            targeted_cities.pop(town)
    elif action == "Prosper":
        town = command[1]
        gold_added = int(command[2])
        if gold_added < 0:
            print("Gold added cannot be a negative number!")
            event = input()
            continue
        targeted_cities[town][1] += gold_added
        print(f"{gold_added} gold added to the city treasury. {town} now has {targeted_cities[town][1]} gold.")

    event = input()

if len(targeted_cities) > 0:
    print(f"Ahoy, Captain! There are {len(targeted_cities)} wealthy settlements to go to:")
    targeted_cities = dict(sorted(targeted_cities.items(), key=lambda kvp: (- kvp[1][1], kvp[0])))
    for town in targeted_cities:
        people = targeted_cities[town][0]
        gold = targeted_cities[town][1]
        print(f"{town} -> Population: {people} citizens, Gold: {gold} kg")
else:
    print("Ahoy, Captain! All targets have been plundered and destroyed!")