elements = input().split()
bakery = {}
for index in range(0, len(elements), 2):
    key = elements[index]
    value = int(elements[index + 1])
    bakery[key] = value

searched_products = input().split()
for product in searched_products:
    if product in bakery:
        print(f"We have {bakery[product]} of {product} left")
    else:
        print(f"Sorry, we don't have {product}")
