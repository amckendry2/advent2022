import sys

chars = ['X', 'Y', 'Z']
def idx(c): return ord(c) - ord('A')

def beatBy(a): return chars[(idx(a) + 1) % 3]
def losesTo(a): return chars[(idx(a) - 1) % 3]

def scoreRound(a, b): 
  return (
    6 if beatBy(a) == b 
    else 3 if chars[idx(a)] == b 
    else 0
  ) + chars.index(b) + 1 

def getMine(a, b):
  if b == 'X': return losesTo(a) 
  if b == 'Y': return chars[idx(a)]
  if b == 'Z': return beatBy(a)

lines = [l.strip().split() for l in sys.stdin.readlines()]
print(f'Part 1: {sum([scoreRound(*l) for l in lines])}')
print(f'Part 2: {sum([scoreRound(l[0], getMine(*l)) for l in lines])}')
