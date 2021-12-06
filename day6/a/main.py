#!/bin/python3

with open('input.txt', 'r') as f:
  inp = f.readline()

fish = [int(f) for f in inp.split(',')]

day = 0
for i in range(80):
  day += 1
  for f in range(len(fish)):
    if fish[f] == 0:
      fish[f] = 6
      fish.append(8)
    else:
      fish[f] -= 1

print(len(fish))