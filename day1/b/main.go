package main

import (
	"bufio"
	"errors"
	"flag"
	"fmt"
	"io/ioutil"
	"log"
	"net/http"
	"os"
	"strconv"
	"strings"
	"time"
)

// These could be defined as a cmd arg instead
const INPUT = "https://adventofcode.com/2021/day/1/input"
const OUTPUT_FILE = "./depths.txt"

// Kinda unnecessary with 1 arg but can be useful if there's more
type Args struct {
	session string
}

// Get and parse cmd line args
func get_args() Args {
	args := Args{}
	flag.StringVar(&args.session, "s", "NA", "Specify advent of code session")
	flag.Parse()

	if args.session == "NA" {
		log.Fatal("Advent of code session not provided")
	}
	return args
}

// Create a new request with the Cookie header set
func create_request(session string) *http.Request {
	req, err := http.NewRequest("GET", INPUT, nil)
	if err != nil {
		log.Fatal(err)
	}

	req.Header.Set("Cookie", fmt.Sprintf("session=%s", session))
	return req
}

// Create a new http client with a 3 second timeout
func new_client() http.Client {
	return http.Client{
		Timeout: time.Second * 3,
	}
}

// Calculates sum of an array of numbers (as strings)
func get_sum(nums []string) int {
	sum := 0
	for _, num := range nums {
		print(num, "\n")
		n, _ := strconv.Atoi(num)
		sum += n
	}
	print("****\n")
	return sum
}

// Count the number of depth increases
func count_depth_increases(depths []string) int {
	increases := 0
	for i := range depths {
		if i < 3 {
			continue
		}

		sum1 := get_sum(depths[i-3 : i])
		sum2 := get_sum(depths[i-2 : i+1])
		if sum1 < sum2 {
			increases++
		}
	}
	return increases
}

// Write s to the OUTPUT_FILE
func write_to_file(s string) {
	file, err := os.Create(OUTPUT_FILE)
	if err != nil {
		log.Fatal(err)
	}

	writer := bufio.NewWriter(file)
	_, err = writer.WriteString(s)
	if err != nil {
		log.Fatal(err)
	}
	writer.Flush()
}

// Check if a file exists
func file_exists(path string) bool {
	_, err := os.Stat(path)
	return !errors.Is(err, os.ErrNotExist)
}

/*
	If input from advent of code is not already stored local in a file
		get the input from advent of code website and store to a file else
		read it from the file
*/
func get_input() string {
	if !file_exists(OUTPUT_FILE) {
		// Get the input
		args := get_args()
		client := new_client()
		request := create_request(args.session)

		resp, err := client.Do(request)
		if err != nil {
			log.Fatal(err)
		}

		defer resp.Body.Close()

		body, err := ioutil.ReadAll(resp.Body)
		if err != nil {
			log.Fatal(err)
		}

		write_to_file(string(body))
		return string(body)
	} else {
		// Read the input
		body, err := ioutil.ReadFile(OUTPUT_FILE)
		if err != nil {
			log.Fatal(err)
		}
		return string(body)
	}
}

func main() {
	input := get_input()
	depths := strings.Split(input, "\n")
	increases := count_depth_increases(depths)
	fmt.Printf("Increases: %d\n", increases)
}
