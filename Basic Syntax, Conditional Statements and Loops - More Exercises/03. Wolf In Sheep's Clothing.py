animals = input().split(", ")
index = -1
index_rev = 0
len_of_queue = len(animals)
wolf_place_in_queue = 0
for el in animals:
    index += 1
    if el == "wolf":
        wolf_place_in_queue = index
if len_of_queue == wolf_place_in_queue + 1:
    print("Please go away and stop eating my sheep")
    exit()
# sheep, sheep, wolf, sheep, sheep, sheep
for wolf in animals:
    len_of_queue -= 1
    if wolf == "wolf":
        print(f"Oi! Sheep number {len_of_queue}! You are about to be eaten by a wolf!")
        break
