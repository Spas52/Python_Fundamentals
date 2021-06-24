how_many_rooms_are = int(input())
free_chairs = 0
number_of_room = 0
is_chair_for_all = True
for i in range(how_many_rooms_are):
    number_of_room += 1
    current_room = input().split()
    rooms_chairs = len(current_room[0])
    taken_places = int(current_room[1])
    if rooms_chairs >= taken_places:
        chairs_left = rooms_chairs - taken_places
        free_chairs += chairs_left
    else:
        is_chair_for_all = False
        needed_chairs_in_room = abs(rooms_chairs - taken_places)
        print(f"{needed_chairs_in_room} more chairs needed in room {number_of_room}")
if is_chair_for_all:
    print(f"Game On, {free_chairs} free chairs left")