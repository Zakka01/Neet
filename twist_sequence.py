def twister(nums, n):

    item = ""
    integers = Deque(nums)

    i = 0
    while i < n:
        item = integers.pop()
        integers.appendleft(item)
        i += 1

    nums = []
    nums.extend(integers)
    return nums
        

print(twister([1, 2, 3], 5))
# [2, 3, 1]

print(twister([1, 2, 3, 4, 5], 2))
# [4, 5, 1, 2, 3]

print(twister([4, 2, 1, -1, 'a'], 4))
# [2, 1, -1, 'a', 4]


