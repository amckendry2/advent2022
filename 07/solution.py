import sys
import re

szs, stack = {}, []
def bump(k, v): szs[k] = (szs[k] + v if k in szs else v)

for c in [l.strip() for l in sys.stdin.readlines() if not re.search('\$ ls|dir ', l)]:
  if c[0] == '$':
    if c[5:] == '..': stack.pop()
    else: stack.append(c[5:])
  else:
    for n in ['/'.join(stack[:i]) for i in range(len(stack), 0, -1)]:
      bump(n, int(c[:c.find(' ')]))

reqSpace = 30000000 - (70000000 - szs['/'])
    
print(f'Part 1: {sum([szs[k] for k in szs if szs[k]<= 100000])}')
print(f'Part 2: {sorted(szs[k] for k in szs if szs[k] >= reqSpace)[0]}')
