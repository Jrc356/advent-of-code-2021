#!/bin/python3

lines = []
with open('input.txt') as f:
  lines += [l.replace('\n', '') for l in f.readlines()]

outputs = [l.split(' | ')[1] for l in lines]

uniques = 0

for output in outputs:
  split = output.split(' ')
  for s in split:
    l = len(s)
        # 1       # 4        # 7       # 8
    if l == 2 or l == 4 or l == 3 or l == 7:
      uniques+=1

print(uniques)