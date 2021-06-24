characters = input().split()
dictionary_of_chr = {}

for el in characters:
    for chr in el:
        if chr not in dictionary_of_chr:
            dictionary_of_chr[chr] = 0
        dictionary_of_chr[chr] += 1
for char, occurrences in dictionary_of_chr.items():
    print(f"{char} -> {occurrences}")