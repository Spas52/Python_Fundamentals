list_of_numbers = list(map(int, input().split(", ")))
group = 10
group_of_10s = []
# [8, 12, 38, 3, 17, 19, 25, 35, 50]
while len(list_of_numbers) > 0:
    group_of_10s = list(filter(lambda num: (group - 10) < num <= group, list_of_numbers))
    for el in group_of_10s:
        if el in list_of_numbers:
            list_of_numbers.remove(el)
    print(f"Group of {group}'s: {group_of_10s}")
    group += 10
