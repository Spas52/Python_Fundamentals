inventory = input().split(", ")
command = input()
while not command == "Craft!":
    action = command.split(" - ")[0]
    item = command.split(" - ")[1]
    if action == "Collect":
        if item in inventory:
            pass
        else:
            inventory.append(item)
    if action == "Drop":
        if item in inventory:
            inventory.remove(item)
        else:
            pass
    if action == "Combine Items":
        old_item = item.split(":")[0]
        new_item = item.split(":")[1]
        if old_item in inventory:
            old_item_index = inventory.index(old_item)
            inventory.insert(old_item_index+1, new_item)
        else:
            pass
    if action == "Renew":
        if item in inventory:
            inventory.append(inventory.pop(inventory.index(item)))
        else:
            pass

    command = input()
print(", ".join(inventory))

