def isAnagram(s1: str, s2: str):
    s1 = s1.lower()
    s2 = s2.lower()
    return sorted(s1.replace(" ", "")) == sorted(s2.replace(" ", ""))


print(isAnagram("abcdefz", "bcda fez"))
