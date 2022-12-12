import sys
import re
from functools import reduce

monkeys = []
items, rawItems = [], []
possessions = [] 

# funcs ==========
def updateItem(idx, mon, p1):
  math = (lambda l, r: l + r) if mon['op'] == '+' else (lambda l, r: l * r)
  func = lambda n: math(n, n if mon['right'] == 'old' else int(mon['right']))
  if p1:
    rawItems[idx] = func(rawItems[idx]) // 3
  else:
    for k, v in items[idx].items():
      items[idx][k] = func(v) % k

def testItem(idx, mon, p1): 
  return (rawItems[idx] % mon['mod'] if p1 else items[idx][mon['mod']]) == 0

def doTurn(p1):
  for mIdx, monItems in enumerate(possessions):
    monkey = monkeys[mIdx]
    for item in  monItems:
      updateItem(item, monkey, p1)
      possessions[monkey['choices'][testItem(item, monkey, p1)]].append(item)
      monkey['inspections'] += 1
    possessions[mIdx] = []

#grok data ==========
lines = sys.stdin.readlines()
mods = [int(i) for i in re.findall('divisible by (\d+)', ''.join(lines))]
monkeyData = [lines[i-7:i-1] for i in range(7, len(lines) + 2, 7)]

def init():
  monkeys.clear()
  possessions.clear()
  items.clear()
  rawItems.clear()
  for m in monkeyData:
    sym = re.search("new = old (\S) (\S+)", m[2])
    nums = [int(i) for i in re.findall('\d+', m[3] + m[4] + m[5])]
    monkeys.append({
      'op':sym[1],
      'mod': nums[0],
      'right': sym[2],
      'choices': [nums[2], nums[1]],
      'inspections': 0
    })
    possessions.append([])
    for item in [int(i) for i in re.findall('\d+', m[1])]:
      items.append({ mod: item % mod for mod in mods })
      rawItems.append(item)
      possessions[len(monkeys) - 1].append(len(items) - 1)


#main ==========
init()
for _ in range(20): doTurn(True)
print(reduce(lambda a,b: a*b, sorted(m['inspections'] for m in monkeys)[-2:]))
init()
for _ in range(10000): doTurn(False)
print(reduce(lambda a,b: a*b, sorted(m['inspections'] for m in monkeys)[-2:]))