numbers = list(map(lambda num: int(num), input().split(", ")))
indices_of_evens = [index for index in range(len(numbers)) if numbers[index] % 2 == 0]
# for index in range(len(numbers)):
# if numbers[index] % 2 == 0:
# indices_of_evens.append(index)
print(indices_of_evens)
