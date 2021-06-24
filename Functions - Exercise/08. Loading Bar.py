percent_number = int(input())


def loading_bar(percent=percent_number):
    list_of_percents = []
    list_of_percent_in_str = ""
    if percent < 100:
        for number in range(1, percent + 1):
            if number % 10 == 0:
                list_of_percents.append("%")
        for element in list_of_percents:
            list_of_percent_in_str += element
        while len(list_of_percent_in_str) < 10:
            list_of_percent_in_str += "."
    else:
        for number in range(1, percent + 1):
            if number % 10 == 0:
                list_of_percents.append("%")
        for element in list_of_percents:
            list_of_percent_in_str += element
        print(f"{percent}% Complete!")
        print(f"[{list_of_percent_in_str}]")
    if len(list_of_percents) < 10:
        while len(list_of_percents) < 10:
            list_of_percents.append(".")
        print(f"{percent}% [{list_of_percent_in_str}]")
        print("Still loading...")
    return exit()


print(loading_bar())