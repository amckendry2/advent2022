import sys
import re
from functools import reduce

jungle = []

class Item:
  def __init__(self, val, mods):
    self.mods = {m: val % m for m in mods}
    self.basicVal = val
  def updateMods(self, func):
    self.mods = {k: (func(v) % k) for k,v in self.mods.items()}
    self.basicVal = func(self.basicVal) // 3

class Monkey:
  def __init__(self, items, op, right, testMod, choices):
    self.items = items
    self.op = op
    self.right = right
    self.testMod = testMod
    self.choices = choices
    self.inspections = 0

  def doTurn(self, isPart1):
    for i in self.items:
      i.updateMods(lambda v: self.op(v, v if self.right == 'old' else int(self.right)))
      testVal = i.basicVal % self.testMod if isPart1 else i.mods[self.testMod]
      jungle[self.choices[testVal == 0]].items.append(i)
      self.inspections += 1
    self.items = []
  
lines = sys.stdin.readlines()
monkeys = [lines[i-7:i-1] for i in range(7, len(lines) + 2, 7)]
mods = [int(i) for i in re.findall('divisible by (\d+)', ''.join(lines))]

def resetJungle():
  jungle.clear()
  for m in monkeys:
    items = [Item(int(val), mods) for val in re.findall('\d+', m[1])]
    sym = re.search("new = old (\S) (\S+)", m[2]) 
    nums = [int(i) for i in re.findall('\d+', m[3] + m[4] + m[5])]
    op = (lambda l, r: l + r) if sym[1] == '+' else (lambda l, r: l * r)
    jungle.append(Monkey(items, op, sym[2], nums[0], [nums[2], nums[1]]))

resetJungle()
for i in range(20): for m in jungle:  m.doTurn(True)
print(reduce(lambda a, b: a * b, sorted(m.inspections for m in jungle)[-2:]))
resetJungle()
for i in range(10000):
  for m in jungle:
    m.doTurn(False)
print(reduce(lambda a, b: a * b, sorted(m.inspections for m in jungle)[-2:]))
