factor = int(input())
count = int(input())
hui = []
for numbers in range(1, 999):
    if numbers % factor == 0:
        hui.append(numbers)
    if len(hui) >= count:
        break
print(hui)
