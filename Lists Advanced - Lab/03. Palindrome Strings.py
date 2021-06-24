words = input().split()
searched_palindrome = input()
times = 0
palindromes = [word for word in words if word == word[::-1]]
for palindrom in words:
    if searched_palindrome == palindrom:
        times += 1
print(palindromes)
print(f"Found palindrome {times} times")
