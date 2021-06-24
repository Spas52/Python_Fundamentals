elements = input().split()

bakery = {}

for index in range(0, len(elements), 2):
    key = elements[index]
    value = int(elements[index + 1])
    bakery[key] = value

print(bakery)