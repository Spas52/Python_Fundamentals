data = input()
index = 0
while index < len(data)-1:
    if data[index] == data[index+1]:
        element_to_replace = f"{data[index]}{data[index+1]}"
        data = data.replace(element_to_replace, data[index])
        index = 0
    else:
        index += 1

print(data)