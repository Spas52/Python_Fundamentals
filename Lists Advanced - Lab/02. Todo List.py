note = input()

final_list = [0] * 10

while not note == "End":
    importance, task = note.split("-")
    importance = int(importance) - 1
    final_list[importance] = task
    note = input()


print([task for task in final_list if not task == 0])