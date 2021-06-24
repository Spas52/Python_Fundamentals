number_of_electrons = int(input())
electrons = []
shell_number = 1
while number_of_electrons > 0:
    max_electrons_in_current_shell = 2 * shell_number**2
    if max_electrons_in_current_shell > number_of_electrons:
        electrons.append(number_of_electrons)
    else:
        electrons.append(max_electrons_in_current_shell)
    number_of_electrons -= max_electrons_in_current_shell
    shell_number += 1

print(electrons)