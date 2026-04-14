def mergeList(list1, list2):
    merged = []
    if list1:
        merged.extend(list1)
    if list2:
        merged.extend(list2)
    
    return sorted(merged)


# Basic cases
print(mergeList([1, 3, 5, -1], [0, 8, 2, 1]))
# [-1, 0, 1, 1, 2, 3, 5, 8]

print(mergeList([99, -22, 10, 9], []))
# [-22, 9, 10, 99]

print(mergeList([7, 6, 8], None))
# [6, 7, 8]

# Edge cases
print(mergeList([], []))
# []
