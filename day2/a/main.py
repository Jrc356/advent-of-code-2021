#!/bin/python3

horizontal = 0
depth = 0

with open('input.txt') as f:
  commands = f.read().strip().split('\n')

for command in commands:
  split = command.split(' ')
  c = split[0]
  amt = int(split[1])

  if c == 'forward':
    horizontal += amt
  elif c == 'up':
    depth -= amt
  elif c == 'down':
    depth += amt
  else:
    print('PANIC')
    print(c)
    exit(1)

print(horizontal * depth)