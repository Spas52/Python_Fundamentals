number = int(input())


def summary(num=number):
    odd_sum = 0
    even_sum = 0
    for element in str(num):
        if int(element) % 2 == 0:
            even_sum += int(element)
        else:
            odd_sum += int(element)

    return odd_sum, even_sum


a = summary()
print(f"Odd sum = {a[0]}, Even sum = {a[1]}")
