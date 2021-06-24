courses = {}
command = input()
while not command == "end":
    course_name, student_name = command.split(" : ")
    if course_name not in courses:
        courses[course_name] = []
    courses[course_name].append(student_name)
    command = input()

sorted_course_list = {x: sorted(courses[x]) for x in courses.keys()}
sorted_course_list = dict(sorted(sorted_course_list.items(), key=lambda x: len(x[1]), reverse=True))
for course, students in sorted_course_list.items():
    print(f"{course}: {len(courses[course])}")
    for student in students:
        print(f"-- {student}")

# print(sorted(courses.items(), key=lambda kvp: kvp[0]))