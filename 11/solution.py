import sys
import re
from functools import reduce
from types import SimpleNamespace

monkeys = []
magicNum = 1

# funcs ==========
def doTurn(p1):
  for mon in monkeys:
    for item in  mon['items']:
      math = (lambda l, r: l + r) if mon['op'] == '+' else (lambda l, r: l * r)
      func = lambda n: math(n, n if mon['right'] == 'old' else int(mon['right']))
      newVal = (func(item) // 3) if p1 else (func(item) % magicNum)
      monkeys[mon['choices'][newVal % mon['mod'] == 0]]['items'].append(newVal)
      mon['inspections'] += 1
    mon['items'] = []

#grok data ==========
lines = sys.stdin.readlines()
mods = [int(i) for i in re.findall('divisible by (\d+)', ''.join(lines))]
monkeyData = [lines[i-7:i-1] for i in range(7, len(lines) + 2, 7)]

def init():
  global magicNum
  monkeys.clear()
  for m in monkeyData:
    sym = re.search("new = old (\S) (\S+)", m[2])
    nums = [int(i) for i in re.findall('\d+', m[3] + m[4] + m[5])]
    magicNum *= nums[0]
    monkeys.append({
      'op':sym[1],
      'mod': nums[0],
      'right': sym[2],
      'choices': [nums[2], nums[1]],
      'items': [int(i) for i in re.findall('\d+', m[1])],
      'inspections': 0 })

#main ==========
init()
for _ in range(20): doTurn(True)
print('Part1:',reduce(lambda a,b: a*b, sorted(m['inspections'] for m in monkeys)[-2:]))

init()
for _ in range(10000): doTurn(False)
print('Part2:',reduce(lambda a,b: a*b, sorted(m['inspections'] for m in monkeys)[-2:]))
