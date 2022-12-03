import sys

calories = [int(line.strip() or -1) for line in sys.stdin.readlines()]
topThree = [0, 0, 0]
groupStart = 0
for i in range(len(calories)):
  if calories[i] == -1:
    topThree = sorted(topThree + [sum(calories[groupStart:i])])[1:4]
    groupStart = i + 1

print(f'Part 1 solution: {topThree[2]}')  
print(f'Part 2 solution: {sum(topThree)}')