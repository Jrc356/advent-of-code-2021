#!/bin/python3

with open('input.txt', 'r') as f:
  inp = f.readline()

fish = {}
for i in range(9):
  fish[i] = 0

for f in inp.split(','):
  fish[int(f)] += 1

day = 0
for i in range(256):
  day += 1
  print('Day: ', day)
  print(fish)
  print()
  
  # fish giving birth
  zero = fish[0]
  
  # move everyone down one
  for i in range(8):
    fish[i] = fish[i+1]
  
  # give birth
  fish[8] = zero
  # reset ones that gave birth
  fish[6] += zero

totalFish = 0
for f in fish:
  totalFish += fish[f]

print('Day: ', day)
print('Total fish: ', totalFish)