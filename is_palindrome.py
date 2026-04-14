def is_palindrome(string):
    s1list = []
    s1 = string.lower()

    for s in s1:
        if s.isalnum():
            s1list.append(s)

    return s1list == s1list.reverse()
    

print(is_palindrome("12321")) # True
print(is_palindrome("12345")) # False
print(is_palindrome("Able was I ere I saw Elba")) # True
print(is_palindrome("No 'x' in Nixon")) # True