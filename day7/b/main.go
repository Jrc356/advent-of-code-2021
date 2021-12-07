package main

import (
	"fmt"
	"io/ioutil"
	"log"
	"math"
	"sort"
	"strconv"
	"strings"
)

const FILE_NAME = "input.txt"

func main() {
	body, err := ioutil.ReadFile(FILE_NAME)
	if err != nil {
		log.Fatal(err)
	}

	input := string(body)
	positions_s := strings.Split(input, ",")
	var positions_i [1000]int
	max_p := 0
	for i := range positions_s {
		position, _ := strconv.Atoi(positions_s[i])
		positions_i[i] = position
		if position > max_p {
			max_p = position
		}
	}

	positions := make(map[int]int)
	for i := 0; i < max_p; i++ {
		for j := range positions_i {
			diff := int(math.Abs(float64(positions_i[j] - i)))
			for k := diff; k > 0; k-- {
				positions[i] += k
			}
		}
	}

	keys := make([]int, 0, len(positions_i))
	for k := range positions {
		keys = append(keys, k)
	}

	sort.Ints(keys)

	least_fuel := 1000000000000000000

	for _, k := range keys {
		fmt.Println(k, ":", positions[k])
		if positions[k] < least_fuel {
			least_fuel = positions[k]
		}
	}

	fmt.Println("Least fuel: ", least_fuel)

}
