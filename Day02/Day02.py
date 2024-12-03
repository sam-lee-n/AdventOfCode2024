import re

with open("input.txt") as f:
    lines = f.readlines()

# Part 1
reports = []
for line in lines:
    nums = line.split()
    reports.append([int(x) for x in nums])

def checkIsSafe(report):
    xdiff = [report[n]-report[n-1] for n in range(1,len(report))]
    inc = [True if x > 0 else False for x in xdiff]
    if xdiff.count(0) > 0 or max(xdiff) > 3 or min(xdiff) < -3 or len(set(inc)) > 1:
        return False
    return True

safe = 0
for report in reports:
    if checkIsSafe(report):
      safe += 1

print("Part 1:", safe)

# Part 2
safe = 0

for report in reports:
    for i in range(len(report)):
        subReport = report[:i] + report[i+1 :]
        if checkIsSafe(subReport):
            safe += 1
            break
    
print("Part 2:", safe)