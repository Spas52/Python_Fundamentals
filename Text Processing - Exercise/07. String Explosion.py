string = input().split('>')
result = []
explosions = 0
for i in string:
    if i[0].isdigit():
        explosions += int(i[0])
        if len(i) <= explosions:
            explosions -= len(i)
            i = '>'
        else:
            i = '>'+''.join(list(i[explosions::]))
            explosions = 0
    result.append(i)
print("".join(result))
# print(*result, sep='') тва е същото като горното
