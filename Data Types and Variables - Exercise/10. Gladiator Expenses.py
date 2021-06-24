lost_fight_count = int(input())
helmet_price = float(input())
sword_price = float(input())
shield_price = float(input())
armor_price = float(input())
bill = 0
shield_brake_count = 0
for fight in range(1, lost_fight_count + 1):
    if fight % 2 == 0:
        bill += helmet_price
    if fight % 3 == 0:
        bill += sword_price
    if fight % 2 == 0 and fight % 3 == 0:
        bill += shield_price
        shield_brake_count += 1
        if shield_brake_count % 2 == 0:
            bill += armor_price
print(f"Gladiator expenses: {bill:.2f} aureus")