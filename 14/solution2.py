import sys
import re
from math import copysign

grainTable = {} 
wallTable = {} 
bottom = 0

def bump(x, y, tbl):
  if x in tbl: tbl[x].append(y)
  else: tbl[x] = [y]

def lookup(x, y, tbl): return x in tbl and y in tbl[x]

def getPtRange(a, b):
  dir = int(copysign(1, b - a))
  return range(a, b + dir, dir)

def getPoints(x1, y1, x2, y2):
  return [(x, y) for x in getPtRange(x1, x2) for y in getPtRange(y1, y2)] 

def isMid(l, m, r): 
  if l < r: 
    return min(r, max(l, m)) == m
  return min(l, max(r, m)) == m

def testIntersect(x, y, part2):
  if part2 and y >= bottom + 2: return True  
  return lookup(x, y, grainTable) or lookup(x, y, wallTable)

def getNextSpace(x, y, part2):
  if not part2 and y == bottom: return None
  if not testIntersect(x, y + 1, part2): return (x, y + 1)
  if not testIntersect(x - 1, y + 1, part2): return (x -1, y + 1)
  if not testIntersect(x + 1, y + 1, part2): return (x + 1, y + 1)
  return None

def simulate(part2):
  startStack = [(500, 0)]
  while(True):
    curGrain = startStack.pop()
    while(nxt := getNextSpace(*curGrain, part2)):
      startStack.append(curGrain)
      curGrain = nxt
    if not part2 and curGrain[1] == bottom: break
    if curGrain[1] == 0: break
    bump(*curGrain, grainTable)

input = sys.stdin.readlines()
lines = [[[int(v) for v in pair] for pair in re.findall('(\d+),(\d+)', l)] for l in input]
nestedPoints = [getPoints(*v[i], *v[i + 1]) for v in lines for i in range(len(v) - 1)]
for p in [p for n in nestedPoints for p in n]:
  bottom = max(p[1], bottom)
  bump(*p, wallTable)

simulate(part2 = False)
print(sum(len(y) for _,y in grainTable.items()))
grainTable.clear()
simulate(part2 = True)
print(sum(len(y) for _,y in grainTable.items()))
