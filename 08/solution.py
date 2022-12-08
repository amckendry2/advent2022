import sys

#globals
found = []
trees = []
width = 0

#funcs
def getLine(idx, dir):
  x = idx % width
  x2 = width - x
  if dir == 'up': return range(idx, x - 1, -width)
  if dir == 'down': return range(idx, len(trees) - x2 + 1, width)
  if dir == 'left': return range(idx, idx - x - 1, -1)
  if dir == 'right': return range(idx, idx + x2, 1)

def getVisibleInRow(line) : 
  lVal, rVal = -1, -1
  for i in range(l := len(line)):
    if trees[(li := line[i])] > lVal:
      lVal = trees[li]
      found.append(li)
    if trees[(ri := line[l-i-1])] > rVal:
      rVal = trees[ri]
      found.append(ri) 

def getTreehouseView(line):
  return next((i for i, v in enumerate(line[1:]) if trees[v] >= trees[line[0]]), len(line) - 2) + 1

#main
width = len(firstLine := sys.stdin.readline().strip())
trees = [int(i) for i in ''.join([firstLine] + [l.strip() for l in sys.stdin.readlines()])]

for i in range(width):
  getVisibleInRow(getLine(i * width, 'right'))
  getVisibleInRow(getLine(i, 'down'))
print(f'Part 1: {len(set(found))}')

best = 0
for i, _ in enumerate(trees):
  best = max(best,
    getTreehouseView(getLine(i, 'up')) *
    getTreehouseView(getLine(i, 'right')) *
    getTreehouseView(getLine(i, 'down')) *
    getTreehouseView(getLine(i, 'left'))
  )
print(f'Part 2: {best}')
