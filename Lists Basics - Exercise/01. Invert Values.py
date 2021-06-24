n_in_str = input()
result = n_in_str.split(" ")
numbers_list = []
opposite_list = []
for index in result:
    numbers_list.append(int(index))
for numbers in numbers_list:
    opposite_list.append(numbers * (-1))
print(opposite_list)