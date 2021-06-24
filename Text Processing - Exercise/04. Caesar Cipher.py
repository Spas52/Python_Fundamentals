text = input()
encrypted_version = ""
for ch in text:
    cryp = chr(ord(ch) + 3)
    encrypted_version += cryp
print(encrypted_version)

