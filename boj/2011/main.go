package main

import (
	"bufio"
	"fmt"
	"os"
	"strconv"
)

var (
	r =bufio.NewReader(os.Stdin)
	w = bufio.NewWriter(os.Stdout)
	str string
	l int
	cache [][]int
	num1, num int
)

func main() {
	defer w.Flush()
	fmt.Fscanf(r, "%s ", &str)
	l = len(str)
	cache = make([][]int, l)
	for i := 0; i < l; i++ {
		cache[i] = make([]int,27)
	}

	num, _ = strconv.Atoi(string(str[0]))
	if num != 0 {
		cache[0][num] = 1

	}
	if l > 1 {
		num1, _ = strconv.Atoi(str[:2])

		if num1 > 9 && num1 < 27 {
			cache[1][num1] = 1
		}
	}

	for i := 1; i < l; i++ {
		num, _  = strconv.Atoi(string(str[i]))
		var sum int
		for j := 1; j < 27; j++ {
			sum += cache[i-1][j]
		}
		if num != 0 {
			cache[i][num] = (cache[i][num] + sum) % 1000000
		}
		if i+2 <= l {
			num1, _ = strconv.Atoi(str[i:i+2])
			if num1 > 9 &&num1 < 27 {
				cache[i+1][num1] = sum
			}
		}

	}
	fmt.Fprintln(w, sum(cache[l-1]))

}

func sum(arr []int) int {
	var sum int
	for i := 0; i < len(arr); i++ {
		sum = (sum + arr[i]) % 1000000
	}
	return sum
}
