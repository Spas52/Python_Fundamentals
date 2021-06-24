company_users = {}
command = input()
while not command == "End":
    company_name, employee_id = command.split(" -> ")
    if company_name not in company_users:
        company_users[company_name] = []
    if employee_id not in company_users[company_name]:
        company_users[company_name].append(employee_id)
    command = input()
sorted_companies = sorted(company_users.items(), key=lambda kvp: kvp[0])
for company, employee in sorted_companies:
    print(f"{company}")
    for person in employee:
        print(f"-- {person}")



# SoftUni -> AA12345
# SoftUni -> BB12345
# Microsoft -> CC12345
# HP -> BB12345
# End