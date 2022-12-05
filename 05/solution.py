import sys
import re
import copy

rowNum, colNum = 8,9 

def moveBoxes(num, start, dest, cols, rev):
  cols[dest] += reversed(cols[start][-num:]) if rev else cols[start][-num:]
  cols[start] = cols[start][:-num]

rows = [re.findall('\s{4}|[A-Z]', l) for l in sys.stdin.readlines()[:rowNum]]
commands = [re.findall('\d+', l) for l in sys.stdin.readlines()[rowNum + 2:]]
p1Cols = [[r[i] for r in reversed(rows) if not r[i].isspace()] for i in range(colNum)]
p2Cols = copy.deepcopy(p1Cols)

for step in [[int(arg[0]), int(arg[1]) - 1, int(arg[2]) - 1] for arg in commands]:
  moveBoxes(*step, p1Cols, True)
  moveBoxes(*step, p2Cols, False)

print(f'Part 1: {"".join([c[len(c) - 1] for c in p1Cols])}')
print(f'Part 2: {"".join([c[len(c) - 1] for c in p2Cols])}')
