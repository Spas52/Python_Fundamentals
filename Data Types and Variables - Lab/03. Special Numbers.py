number = int(input())

for n in range(1, number + 1):
    n_as_str = str(n)
    sum_of_digits = 0
    for digit in n_as_str:
        int_of_dig = int(digit)
        sum_of_digits += int_of_dig
    if sum_of_digits == 5 or sum_of_digits == 7 or sum_of_digits == 11:
        print(f"{n} -> True")
    else:
        print(f"{n} -> False")