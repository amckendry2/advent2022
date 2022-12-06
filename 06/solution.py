import sys

def func(n, s): return next(i for i in range(n, len(s)) if len(set(s[i-n:i])) == n)
print(f'Part 1: {func(4, line := sys.stdin.readline())}')
print(f'Part 2: {func(14, line)}')