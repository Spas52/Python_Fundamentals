strings = input().split()
result = ""
for word in strings:
    length = len(word)
    result += word * length
print(result)