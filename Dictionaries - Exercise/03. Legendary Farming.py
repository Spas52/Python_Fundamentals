data = input()
key_materials = {"shards": "Shadowmourne", "fragments": "Valanyr", "motes": "Dragonwrath"}
items = {"shards": 0, "fragments": 0, "motes": 0}
junk_items = {}
is_obtained = False

while not is_obtained:
    split_data = data.split()

    for index in range(0, len(split_data), 2):
        if is_obtained:
            break

        quantity = int(split_data[index])
        material = split_data[index + 1].lower()

        if material in items:
            items[material] += quantity
        else:
            if material not in junk_items:
                junk_items[material] = quantity
            else:
                junk_items[material] += quantity
        for material, quantity in items.items():
            if quantity >= 250:
                is_obtained = True
                items[material] -= 250
                print(f"{key_materials[material]} obtained!")
                break
    if is_obtained:
        break

    data = input()

sorted_items = sorted(items.items(), key=lambda kvp: (-kvp[1], kvp[0]))
for mat, quantity in sorted_items:
    print(f"{mat}: {quantity}")

sorted_junks = sorted(junk_items.items(), key=lambda kvp: kvp[0])
for mate, qua in sorted_junks:
    print(f"{mate}: {qua}")
