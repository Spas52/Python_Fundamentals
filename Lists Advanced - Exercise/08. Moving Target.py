sequence = list(map(int, input().split()))
command = input()
# 52,100
while command != "End":
    action = command.split()
    # [Shoot, 5, 10]
    if action[0] == "Shoot":
        target = int(action[1])
        power = int(action[2])
        if 0 <= target < len(sequence):
            if power >= sequence[target]:
                sequence.pop(target)
            else:
                sequence[target] -= power
    elif action[0] == "Add":
        target = int(action[1])
        value = int(action[2])
        if 0 <= target < len(sequence):
            sequence.insert(target, value)
        else:
            print("Invalid placement!")
    elif action[0] == "Strike":
        target = int(action[1])
        radius = int(action[2])
        if 0 <= target < len(sequence):
            if (target - radius) in range(len(sequence)) and (target - radius) in range(len(sequence)):
                del sequence[target-radius:target+radius+1]
            else:
                print("Strike missed!")
        else:
            print("Strike missed!")

    command = input()
sequence = list(map(lambda el: str(el), sequence))
print("|".join(sequence))
