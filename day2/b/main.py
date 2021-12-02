#!/bin/python3

horizontal = 0
depth = 0
aim = 0

with open('input.txt') as f:
  commands = f.read().strip().split('\n')

for command in commands:
  split = command.split(' ')
  c = split[0]
  amt = int(split[1])

  if c == 'forward':
    horizontal += amt
    depth += (amt * aim)
  elif c == 'up':
    aim -= amt
  elif c == 'down':
    aim += amt
  else:
    print('PANIC')
    print(c)
    exit(1)

print(horizontal * depth)