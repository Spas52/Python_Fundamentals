n = int(input())
positives = []
negatives = []
positives_count = 0
for nums in range(n):
    number = int(input())
    if number >= 0:
        positives.append(number)
        positives_count += 1
    else:
        negatives.append(number)
print(positives)
print(negatives)
print(f'Count of positives: {positives_count}. Sum of negatives: {sum(negatives)}')