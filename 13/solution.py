import sys
from ast import literal_eval
from functools import cmp_to_key

def compareItems(a, b, top):
  if type(a) == int and type(b) == int:
    if a == b: return (True,)
    else: return (False, -1 if a < b else 1)
  a = [a] if type(a) == int else a
  b = [b] if type(b) == int else b
  for i in range(min(len(a), len(b))):
    if not (res := compareItems(a[i], b[i], False))[0]:
      return res[1] if top else res
  if len(b) != len(a):
    val = -1 if len(a) < len(b) else 1
    return val if top else (False, val)  
  return -1 if top else (True,)

lines = sys.stdin.readlines()
pairs = [[literal_eval(lines[i]), literal_eval(lines[i + 1])] for i in range(0, len(lines), 3)]
flatPairs = [item for sublist in pairs for item in sublist] + [[[2]],[[6]]]
sortedPairs = sorted(flatPairs, key=cmp_to_key(lambda a, b: compareItems(a, b, True)))

print(f'Part 1: {sum((i + 1 if compareItems(p[0], p[1], True) == -1 else 0) for i, p in enumerate(pairs))}')
print(f'Part 2: {(sortedPairs.index([[2]]) + 1) * (sortedPairs.index([[6]]) + 1)}')
