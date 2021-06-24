shopping_list = input().split("!")
command = input()
while not command == "Go Shopping!":
    type_of_request = command.split()[0]
    product = command.split()[1]
    if type_of_request == "Urgent":
        if product in shopping_list:
            pass
        else:
            shopping_list.insert(0, product)
    elif type_of_request == "Unnecessary":
        if product in shopping_list:
            shopping_list.remove(product)
        else:
            pass
    elif type_of_request == "Correct":
        old_item = command.split()[1]
        new_item = command.split()[2]
        if old_item in shopping_list:
            old_item_index = shopping_list.index(old_item)
            shopping_list[old_item_index] = new_item
        else:
            pass
    elif type_of_request == "Rearrange":
        if product in shopping_list:
            shopping_list.append(shopping_list.pop(shopping_list.index(product)))
        else:
            pass

    command = input()

print(", ".join(shopping_list))
