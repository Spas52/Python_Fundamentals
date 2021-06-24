train_lenght = int(input())
train = [0] * train_lenght
command = input()
while not command == "End":
    tokens = command.split(" ")
    key_word = tokens[0]
    if key_word == "add":
        train[-1] += int(tokens[1])
    elif key_word == "insert":
        wagon = int(tokens[1])
        train[wagon] += int(tokens[2])
    elif key_word == "leave":
        wagon = int(tokens[1])
        train[wagon] -= int(tokens[2])
    command = input()
print(train)