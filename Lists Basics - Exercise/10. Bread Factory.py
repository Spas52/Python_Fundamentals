energy = 100
coins = 100
day_events = input().split("|")
is_day_complete = True
# ['rest-2', 'order-10', 'eggs-100', 'rest-10']
for event_or_item in day_events:
    order, value = event_or_item.split("-")
    energy_flow = int(value)
    earned_coin = int(value)
    expenses = int(value)
    if order == "rest":
        energy += energy_flow
        if energy > 100:
            energy = 100
            energy_flow = 0
            print(f"You gained {energy_flow} energy.\nCurrent energy: {energy}.")
        else:
            print(f"You gained {energy_flow} energy.\nCurrent energy: {energy}.")
    elif order == "order":
        if energy - 30 >= 0:
            coins += earned_coin
            energy -= 30
            print(f"You earned {earned_coin} coins.")
        else:
            energy += 50
            print("You had to rest!")
    else:
        if coins > expenses:
            coins -= expenses
            print(f"You bought {order}.")
        else:
            is_day_complete = False
            print(f"Closed! Cannot afford {order}.")
            break

if is_day_complete:
    print(f"Day completed!\n Coins: {coins}\n Energy: {energy}")