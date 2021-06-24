command = input()
products = {}
products_price = {}
products_quantity = {}
while not command == "buy":
    name, price, quantity = command.split()
    price = float(price)
    quantity = int(quantity)
    if name not in products:
        products_price[name] = price
        products_quantity[name] = quantity
        products[name] = price * quantity
    else:
        products_quantity[name] += quantity
        if price != products_price[name]:
            products_price[name] = price
        products[name] = products_price[name] * products_quantity[name]
    command = input()
for name, price in products.items():
    print(f"{name} -> {price:.2f}")