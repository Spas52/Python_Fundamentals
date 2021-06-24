n = int(input())
capacity_of_water_tank_in_liters = 255
water_which_goes_to_the_tank = 0
for times in range(1, n + 1):
    quantities_of_water = int(input())
    if quantities_of_water <= 255:
        water_which_goes_to_the_tank += quantities_of_water
        if water_which_goes_to_the_tank > 255:
            water_which_goes_to_the_tank -= quantities_of_water
            print("Insufficient capacity!")
    else:
        print("Insufficient capacity!")
print(f"{water_which_goes_to_the_tank}")