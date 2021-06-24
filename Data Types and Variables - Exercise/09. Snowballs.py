number_of_snowballs = int(input())

mas_snowball_value = -99999999999
max_snowball_snow = -99999999999
max_snowball_time = -99999999999
max_snowball_quality = -99999999999

for snowball in range(1, number_of_snowballs + 1):
    snowball_snow = int(input())
    snowball_time = int(input())
    snowball_quality = int(input())

    snowball_value = (snowball_snow / snowball_time) ** snowball_quality
    if mas_snowball_value < snowball_value:
        mas_snowball_value = snowball_value
        max_snowball_time = snowball_time
        max_snowball_snow = snowball_snow
        max_snowball_quality = snowball_quality
print(f"{max_snowball_snow} : {max_snowball_time} = {mas_snowball_value:.0f} ({int(max_snowball_quality)})")