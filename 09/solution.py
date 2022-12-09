import sys
import math

snek1 = [[0,0],[0,0]]
snek2 = [[0,0] for _ in range(10)]
log1 = []
log2 = []

def doCommand(c, seg):
  if(c == 'R'): seg[0] += 1
  if(c == 'L'): seg[0] -= 1
  if(c == 'U'): seg[1] += 1
  if(c == 'D'): seg[1] -= 1

def rideTheSnek(cmd, snk, log): 
  doCommand(cmd, snk[0])
  for i in (range(l := len(snk) - 1)): 
    if any(abs((h := snk[i])[n] - (t := snk[i + 1])[n]) > 1 for n in [0, 1]):
      for i in [0, 1]: t[i] += (math.copysign(1, d) if (d := h[i] - t[i]) != 0 else 0)
      log.append(tuple(snk[l])) 

for c in [(l[:1], int(l[2:])) for l in sys.stdin.readlines()]:
  for i in range(c[1]):
    rideTheSnek(c[0], snek1, log1)
    rideTheSnek(c[0], snek2, log2)

print(f'Part 1: {len(set(log1))}')
print(f'Part 2: {len(set(log2))}')
