collection_of_items = input().split("|")
# ['Clothes->43.30', 'Shoes->25.25', 'Clothes->36.52', 'Clothes->20.90', 'Accessories->15.60']
budget = float(input())
list_of_new_prices = []
starting_budget = budget
for item in collection_of_items:
    current_item = item.split("->")
    type_item = current_item[0]
    price_of_that_item = float(current_item[-1])
    if type_item == "Clothes":
        if price_of_that_item > 50:
            continue
        if price_of_that_item > budget:
            continue
        budget -= price_of_that_item
        new_price = price_of_that_item + (price_of_that_item * 0.4)
        list_of_new_prices.append(f"{new_price:.2f}")
    if type_item == "Shoes":
        if price_of_that_item > 35:
            continue
        if price_of_that_item > budget:
            continue
        budget -= price_of_that_item
        new_price = price_of_that_item + (price_of_that_item * 0.4)
        list_of_new_prices.append(f"{new_price:.2f}")
    if type_item == "Accessories":
        if price_of_that_item > 20.50:
            continue
        if price_of_that_item > budget:
            continue
        budget -= price_of_that_item
        new_price = price_of_that_item + (price_of_that_item * 0.4)
        list_of_new_prices.append(f"{new_price:.2f}")

for index in range(0, len(list_of_new_prices)):
    list_of_new_prices[index] = float(list_of_new_prices[index])
final_budget = budget + sum(list_of_new_prices)
profit = abs(starting_budget - (final_budget))

for new in list_of_new_prices:
    print(f"{new:.2f}", end=" ")

print(f"\nProfit: {profit:.2f}")

if final_budget >= 150:
    print("Hello, France!")
else:
    print("Time to go.")


