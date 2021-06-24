usernames = input().split(", ")
is_valid = True
for name in usernames:
    if 3 <= len(name) <= 16:
        for ch in name:
            if ch.isalnum() or ch == '-' or ch == '_':
                is_valid = True
            else:
                is_valid = False
                break
    else:
        is_valid = False
    if is_valid:
        print(name)
