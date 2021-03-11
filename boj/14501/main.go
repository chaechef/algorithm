package main

import (
	"bufio"
	"fmt"
	"os"
)

var (
	r = bufio.NewReader(os.Stdin)
	w = bufio.NewWriter(os.Stdout)
	n int
	table [][]int
	cache []int
)

func main() {
	defer w.Flush()
	fmt.Fscanf(r,"%d ", &n)
	table = make([][]int, 2)
	for i := 0; i < 2; i++ {
		table[i] = make([]int, n+1)
	}
	cache = make([]int, n+1)
	for i := 1; i < n+1; i++ {
		fmt.Fscanf(r,"%d %d ", &table[0][i], &table[1][i])
	}

	res := recursion(n)
	fmt.Fprintln(w, res)
}

func recursion(num int) int {
	if num == 0 {
		return 0
	}
	if cache[num] != 0 {
		return cache[num]
	}

	max := 0
	for i := num; i > 0; i-- {
		var temp int
		if table[0][i] + i <= num + 1 {
			temp = table[1][i] + recursion(i-1)
		}
		if temp > max {
			max = temp
		}
	}
	cache[num] = max
	return cache[num]
}