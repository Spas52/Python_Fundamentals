the_cards = input()
list_of_cards = the_cards.split(" ")
players_in_team_A = 11
players_in_team_B = 11
is_game_on = True
list_of_cards = set(list_of_cards)
list_of_cards = list(list_of_cards)

for index in list_of_cards:
    if "A" in index:
        players_in_team_A -= 1

        if players_in_team_A < 7:
            is_game_on = False
            break
    elif "B" in index:
        players_in_team_B -= 1
        if players_in_team_B < 7:
            is_game_on = False
            break

print(f"Team A - {players_in_team_A}; Team B - {players_in_team_B}")
if not is_game_on:
    print("Game was terminated")