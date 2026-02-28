nums = [2, 3, 1, 5, 6, 4, 0]

print(id(sorted(nums)))   # [0, 1, 2, 3, 4, 5, 6]
print(id(nums))           # [2, 3, 1, 5, 6, 4, 0]

print(nums.sort())    # None
print(id(nums))           # [0, 1, 2, 3, 4, 5, 6]

