#!/bin/bash

nums=($(cat input.txt))

bits=()

for num in "${nums[@]}"; do
  for (( i=0; i<${#num}; i++ )); do
    bit="${num:$i:1}"
    if [[ $bit == 1 ]]; then
      bits[$i]=$((bits[$i] + 1))
    else
      bits[$i]=$((bits[$i] - 1))
    fi
  done
done

gamma=""
epsilon=""

for bit in "${bits[@]}"; do
  if [[ $bit < 0 ]]; then
    # most common bit is 0
    gamma="${gamma}0"
    epsilon="${epsilon}1"
  else
    # most common bit is 1
    gamma="${gamma}1"
    epsilon="${epsilon}0"
  fi
done

echo "Binary:"
echo "Gamma: $gamma"
echo "Epsil: $epsilon"

echo "Decimal:"
gamma_dec=$((2#$gamma))
epsil_dec=$((2#$epsilon))
echo "Gamma: $gamma_dec"
echo "Epsil: $epsil_dec"

echo "Power:"
echo $(($gamma_dec * $epsil_dec))
