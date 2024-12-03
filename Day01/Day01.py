import re

with open("input.txt") as f:
    lines = f.readlines()

# Part 1
lst1 = []
lst2 = []
for line in lines:
    nums = line.split()
    lst1.append(int(nums[0]))
    lst2.append(int(nums[1]))

lst1.sort()
lst2.sort()

total = 0
for i in range(len(lst1)):
    total += abs(lst1[i] - lst2[i])

print("Part 1:", total)

# Part 2
total = 0
for i in range(len(lst1)):
    total += lst2.count(lst1[i]) * lst1[i]

print("Part 2:", total)
