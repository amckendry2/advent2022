from concurrent.futures import process
import sys
import re

def leftIn(a, b): return b[0] <= a[0] <= b[1]
def rightIn(a, b): return b[0] <= a[1] <= b[1]
def aInsideB(a, b): return leftIn(a, b) and rightIn(a, b)
def aOverlapB(a, b): return leftIn(a, b) or rightIn(a, b)
def inside(a, b): return aInsideB(a, b) or aInsideB(b, a)
def overlap(a, b): return aOverlapB(a, b) or aOverlapB(b, a) 

def extract(pair): return [int(s) for s in re.split('(\d+)-(\d+)', pair)[1:3]]
def processLine(line): return [extract(pair) for pair in line]

lines = [processLine(l.strip().split(',')) for l in sys.stdin.readlines()]
print(f'Part 1: {len([l for l in lines if inside(*l)])}')
print(f'Part 2: {len([l for l in lines if overlap(*l)])}')
