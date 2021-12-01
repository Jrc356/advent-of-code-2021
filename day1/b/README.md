# How to run
## Option 1
```shell
$ go run main.go -s <session>
```

To get the `session` value: 
1. Login to [advent of code](https://adventofcode.com/)
2. Go to the [day 1 input](https://adventofcode.com/2021/day/1/input)
3. Open the network tab and find the request to the input url
4. Look for the the header `Cookie: session=<some garbled nonsense>`
5. copy `<some garbled nonsense>`
This is your session

## Option 2
The other option is to copy the input directly into a new file called `depths.txt`

# Problem Statement
--- Part Two ---

Considering every single measurement isn't as useful as you expected: there's just too much noise in the data.

Instead, consider sums of a three-measurement sliding window. Again considering the above example:

199  A      
200  A B    
208  A B C  
210    B C D
200  E   C D
207  E F   D
240  E F G  
269    F G H
260      G H
263        H

Start by comparing the first and second three-measurement windows. The measurements in the first window are marked A (199, 200, 208); their sum is 199 + 200 + 208 = 607. The second window is marked B (200, 208, 210); its sum is 618. The sum of measurements in the second window is larger than the sum of the first, so this first comparison increased.

Your goal now is to count the number of times the sum of measurements in this sliding window increases from the previous sum. So, compare A with B, then compare B with C, then C with D, and so on. Stop when there aren't enough measurements left to create a new three-measurement sum.

In the above example, the sum of each three-measurement window is as follows:

A: 607 (N/A - no previous sum)
B: 618 (increased)
C: 618 (no change)
D: 617 (decreased)
E: 647 (increased)
F: 716 (increased)
G: 769 (increased)
H: 792 (increased)

In this example, there are 5 sums that are larger than the previous sum.

Consider sums of a three-measurement sliding window. How many sums are larger than the previous sum?

Although it hasn't changed, [you can still get your puzzle input](https://adventofcode.com/2021/day/1/input).