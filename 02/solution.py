import sys
import functools

aGroup = ['A', 'B', 'C']
bGroup = ['X', 'Y', 'Z']

getMine = {
  'X': lambda a: bGroup[(aGroup.index(a) - 1) % 3],
  'Y': lambda a: bGroup[aGroup.index(a)],
  'Z': lambda a: bGroup[(aGroup.index(a) + 1) % 3]
}

beatBy = lambda a, b: (aGroup.index(a) + 1) % 3 == bGroup.index(b)
equals = lambda a, b: aGroup.index(a) == bGroup.index(b)
scoreRound = lambda a, b : (6 if beatBy(a, b) else 0) + (3 if equals(a, b) else 0) + bGroup.index(b) + 1 

lines = [line.strip().split() for line in sys.stdin.readlines()]
print(f'Part 1: {functools.reduce(lambda a, b: a + scoreRound(*b), lines, 0)}')
print(f'Part 2: {functools.reduce(lambda a, b: a + scoreRound(b[0], getMine[b[1]](b[0])), lines, 0)}')
