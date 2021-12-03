#!/bin/bash
most_common() {
  arr=("$@")
  common=()
  for n in "${arr[@]}"; do
    for (( i=0; i<${#n}; i++ )); do
      bit="${n:$i:1}"
      if [[ $bit == 1 ]]; then
        common[$i]=$((common[$i] + 1))
      else
        common[$i]=$((common[$i] - 1))
      fi
    done
  done
  echo "${common[@]}"
}

rating() {
  metric=$1
  bit_pos=$2
  args=("$@")
  arr=("${args[@]:2}")

  if [[ ${#arr[@]} == 0 ]]; then
    echo $bit_pos
    echo "${arr[@]}"
    echo "PANIC"
    exit 1
  fi

  if [[ ${#arr[@]} == 1 ]]; then
    echo "${arr[0]}"
    return 0
  fi

  common=($(most_common "${arr[@]}"))
  new_arr=()
  bit=${common[$bit_pos]}
  if ([[ $metric == "oxygen" ]] && [ $bit -ge 0 ]) || ([[ $metric != "oxygen" ]] && [ $bit -lt 0 ]); then
    for num in "${arr[@]}"; do
      if [[ ${num:$bit_pos:1} == "1" ]]; then
        new_arr+=($num)
      fi
    done

  else
    for num in "${arr[@]}"; do
      if [[ ${num:$bit_pos:1} == "0" ]]; then
        new_arr+=($num)
      fi
    done
  fi
  rating $metric $(($bit_pos+1)) "${new_arr[@]}"
}

nums=($(cat input.txt))

bits_arr=()

# Oxygen rating
oxygen_rating=$(rating "oxygen" 0 "${nums[@]}")

# CO2 scrubber
co2_rating=$(rating "scrubber" 0 "${nums[@]}")

echo "Binary:"
echo "oxygen: $oxygen_rating"
echo "scrubs: $co2_rating"


echo "Decimal:"
oxy_dec=$((2#$oxygen_rating))
co2_dec=$((2#$co2_rating))
echo "oxygen: $oxy_dec"
echo "scrubs: $co2_dec"

echo "Life Support:"
echo $(($oxy_dec * $co2_dec))