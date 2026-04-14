def counter(string):
    vowels = "aeiou"
    count = 0
    for v in vowels:
        if v in string:
            count += 1
    return count


def sorting(list):
    return sorted(list, key=lambda item: (counter(item),
                                          len(item),
                                          item.lower()))


print(sorting(["apple", "bat", "car", "ae", "b"]))
print(sorting(["dog", "cat", "hi", "a"]))
print(sorting(["bat", "cat", "ant"]))
print(sorting(["bbb", "ccc", "ddd"]))
print(sorting(["a", "e", "i", "o", "u"]))
print(sorting([]))
