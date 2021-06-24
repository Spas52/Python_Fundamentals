version = input().split('.')
int_version = int(''.join(version))
new_version = int(int_version+1)
print('.'.join(str(new_version)))