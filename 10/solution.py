import sys

acc, cycles = 1, []

for cmd in [(c[:4], int(c[5:] or 0)) for c in sys.stdin.readlines()]:
  cycles.append(acc)
  if cmd[0] == 'addx':
    cycles.append(acc)
    acc += cmd[1]

screen = ['#' if abs(cycles[i] - i % 40) < 2 else ' ' for i in range(240)]

print(f'Part 1: {sum(cycles[i - 1] * i for i in range(20, 221, 40))}')

print('Part 2:')
print('//=======================================\\\\')
for row in range(0, 201, 40): print('||',*screen[row:row+39]+['||'], sep='')
print('\\\\=======================================//')
