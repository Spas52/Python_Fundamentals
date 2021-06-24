strings = input().split()
a, b = strings
a = str(a)
b = str(b)
total_sum = 0
if len(a) == len(b):
    for i in range(len(a)):
        multiply = ord(a[i]) * ord(b[i])
        total_sum += multiply
else:
    if len(a) > len(b):
        for i in range(len(b)):
            multiply = ord(a[i]) * ord(b[i])
            total_sum += multiply
        for big_i in range(len(b), len(a)):
            total_sum += ord(a[big_i])
    else:
        for i in range(len(a)):
            multiply = ord(a[i]) * ord(b[i])
            total_sum += multiply
        for big_i in range(len(a), len(b)):
            total_sum += ord(b[big_i])

print(total_sum)
