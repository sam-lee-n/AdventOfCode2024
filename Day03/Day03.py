import re
import string

with open("input.txt") as f:
    lines = f.readlines()

# Part 1
line = "".join(lines)
matches = re.findall(r'mul\(\d+,\d+\)', line)
total = 0
for pairs in matches:
    nums = re.findall(r'\d+', pairs)
    total += int(nums[0]) * int(nums[1])

print("Part 1", total)

# Part 2
total = 0
enables = True
for x in range(len(line)):
    text = line[x:]
    if text.startswith("do()"):
        enables = True
    elif text.startswith("don't()"):
        enables = False
    if enables:
        matches = re.match(r'mul\(\d+,\d+\)', text)
        if matches is not None:
            nums = re.findall(r'\d+', matches.group(0))
            total += int(nums[0]) * int(nums[1])

print("Part 2", total)