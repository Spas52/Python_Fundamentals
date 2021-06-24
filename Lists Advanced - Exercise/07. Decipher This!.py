secret_message = input().split(" ")
# ['72olle', '103doo', '100ya']
final_list = []
for word in secret_message:
    letters = [el for el in word if el.isalpha()]
    digits = [el for el in word if el.isdigit()]
    the_first_letter = chr(int("".join(digits)))
    letters[0], letters[-1] = letters[-1], letters[0]
    final_list.append(the_first_letter + ("".join(letters)))
print(" ".join(final_list))