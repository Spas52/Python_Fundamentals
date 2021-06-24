number_of_heroes = int(input())
party = {}
# {'Solmyr': ['85' hp, '120' mana], 'Kyrre': ['99', '50']}
for _ in range(number_of_heroes):
    hero = input().split()
    party[hero[0]] = [int(hero[1]), int(hero[2])]
data = input()
while not data == "End":
    command = data.split(" - ")
    action = command[0]
    if action == "CastSpell":
        hero_name = command[1]
        mp_needed = int(command[2])
        spell_name = command[3]
        if party[hero_name][1] >= mp_needed:
            party[hero_name][1] -= mp_needed
            print(f"{hero_name} has successfully cast {spell_name} and now has {party[hero_name][1]} MP!")
        else:
            print(f"{hero_name} does not have enough MP to cast {spell_name}!")
    elif action == "TakeDamage":
        hero_name = command[1]
        damage = int(command[2])
        attacker = command[3]
        party[hero_name][0] -= damage
        if party[hero_name][0] > 0:
            print(f"{hero_name} was hit for {damage} HP by {attacker} and now has {party[hero_name][0]} HP left!")
        else:
            del party[hero_name]
            print(f"{hero_name} has been killed by {attacker}!")
    elif action == "Recharge":
        hero_name = command[1]
        amount = int(command[2])
        if party[hero_name][1] + amount > 200:
            amount = 200 - party[hero_name][1]
            party[hero_name][1] = 200
        else:
            party[hero_name][1] += amount
        print(f"{hero_name} recharged for {amount} MP!")
    elif action == "Heal":
        hero_name = command[1]
        amount = int(command[2])
        if party[hero_name][0] + amount > 100:
            amount = 100 - party[hero_name][0]
            party[hero_name][0] = 100
        else:
            party[hero_name][0] += amount
        print(f"{hero_name} healed for {amount} HP!")
    data = input()

party = dict(sorted(party.items(), key=lambda kvp: (- kvp[1][0], kvp[0])))

for hero in party:
    print(f"{hero}")
    print(f"  HP: {party[hero][0]}")
    print(f"  MP: {party[hero][1]}")

