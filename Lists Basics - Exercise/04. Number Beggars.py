list_of_numbers_as_string = input().split(", ")
number_of_beggars = int(input())
sums_of_each_beggar = []
start_index = 0

for beggar in range(number_of_beggars):
    current_sum = 0
    for sum in range(start_index, len(list_of_numbers_as_string), number_of_beggars):
        current_sum += int(list_of_numbers_as_string[sum])
    sums_of_each_beggar.append(current_sum)
    start_index += 1
print(sums_of_each_beggar)