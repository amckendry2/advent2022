import sys

trans = { 'A': 'X', 'B': 'Y', 'C': 'Z' }
def idx(c): ord(c) - 'X'

def beatBy(a): return trans[(idx(a) + 1 % 3)]
def losesTo(a): return trans[(idx(a) - 1 % 3)]

def scoreRound(a, b): 
  return (
    6 if beatBy(a) == b 
    else 3 if trans[a] == b 
    else 0
  ) + idx(trans[b]) + 1 

def getMine(a, b):
  if b == 'X': return losesTo(a) 
  if b == 'Y': return trans[a]
  if b == 'Z': return beatBy(a)

lines = [l.strip().split() for l in sys.stdin.readlines()]
print(f'Part 1: {sum([scoreRound(*l) for l in lines])}')
print(f'Part 2: {sum([scoreRound(l[0], getMine(*l)) for l in lines])}')
