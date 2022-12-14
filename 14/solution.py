import sys
import re

grains = []

input = sys.stdin.readlines()
vertices = [[[int(v) for v in pair] for pair in re.findall('(\d+),(\d+)', l)] for l in input]
pairs = [(v[i], v[i + 1]) for v in vertices for i in range(len(v) - 1)]
bottom = max(v[1] for grp in vertices for v in grp)

def isMid(l, m, r): 
  if l < r: 
    return min(r, max(l, m)) == m
  return min(l, max(r, m)) == m

def testIntersect(x, y, part2):
  if part2 and y >= bottom + 2: return True  
  for g in grains:
    if(g[0] == x and g[1] == y): return True
  for p in pairs:
    if p[0][0] == x and isMid(p[0][1], y, p[1][1]): return True
    if p[0][1] == y and isMid(p[0][0], x, p[1][0]): return True
  return False

def getNextSpace(x, y, part2):
  if not part2 and y == bottom: return None
  if not testIntersect(x, y + 1, part2): return (x, y + 1)
  if not testIntersect(x - 1, y + 1, part2): return (x -1, y + 1)
  if not testIntersect(x + 1, y + 1, part2): return (x + 1, y + 1)
  return None

def simulate(part2):
  while(True):
    print(len(grains))
    curGrain = (500, 0)
    while(nxt := getNextSpace(*curGrain, part2)):
      curGrain = nxt
    if not part2 and curGrain[1] == bottom: break
    if curGrain[1] == 0: break
    grains.append(curGrain)

simulate(False)
print(len(grains))
# grains.clear()
# simulate(True)
# print(len(grains) + 1)

