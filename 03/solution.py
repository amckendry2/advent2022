import sys

def getDupe(f, s): return f[next(i for i in range(len(f)) if f[i] in s)]
def getBadge(f, s, t): return f[next(i for i in range(len(f)) if f[i] in s and f[i] in t)]
def charScore(c): return (s - 38) if (s := ord(c)) < 97 else s - 96

lines = sys.stdin.readlines()
groups = [lines[i:i+3] for i in range(0, len(lines), 3)]
p1 = sum([charScore(getDupe(l[:(half := len(l)//2)],l[half:])) for l in lines])
p2 = sum([charScore(getBadge(*g)) for g in groups])

print(f'Part 1: {p1}')
print(f'Part 2: {p2}')
