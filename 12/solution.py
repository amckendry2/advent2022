import sys
import math

width = 0
spaceVals = []
gScore = []

def dist(a, b):
  ax = a % width
  ay = a // width
  bx = b % width
  by = b // width
  return (bx - ax) ** 2 + ((by - ay) ** 2)

def getNeighbors(idx):
  tgt = spaceVals[idx] + 1
  l = [] if (idx % width == 0 or spaceVals[idx - 1] > tgt)  else [idx - 1]
  u = [] if (idx < width or spaceVals[idx - width] > tgt) else [idx - width]
  r = [] if (idx % width == width - 1 or spaceVals[idx + 1] > tgt) else [idx + 1]
  d = [] if (idx >= len(spaceVals) - width or spaceVals[idx + width] > tgt) else [idx + width] 
  return l + u + r + d

def shortestPath(start, end):
  gScore[start] = 0
  openSet = [start]
  while(len(openSet) > 0):
    current = sorted([(gScore[o], o) for o in openSet], key=lambda x:x[0])[0][1]
    if current == end: 
      return gScore[current]
    openSet.remove(current)
    for n in getNeighbors(current):
      newGScore = gScore[current] + 1
      if newGScore < gScore[n]:
        gScore[n] = newGScore
        if n not in openSet: openSet.append(n)
  return math.inf
  
width = (first := sys.stdin.readline()).index('\n')
spaceVals = [ord(c) for c in (first + sys.stdin.read()) if c != '\n']
gScore = [math.inf for _ in range(len(spaceVals))]
spaceVals[(p1StartIdx := spaceVals.index(ord('S')))] = ord('a')
spaceVals[(endIdx := spaceVals.index(ord('E')))] = ord('z')

print(f'Part 1: {shortestPath(p1StartIdx, endIdx)}')
shortest = sorted(shortestPath(idx, endIdx) for idx, val in enumerate(spaceVals) if val == ord('a'))[0]
print(f'Part 2: {shortest}')
