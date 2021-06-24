first_line_of_strings = input().split(", ")
second_line_of_strings = input().split(", ")
new_list = [word for word in first_line_of_strings for word1 in second_line_of_strings if word in word1]
print(sorted(set(new_list), key=new_list.index))

