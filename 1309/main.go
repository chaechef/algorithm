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
	cache [][]int
)

func main() {
	defer w.Flush()
	fmt.Fscanf(r, "%d ", &n)
	cache = make([][]int, n+1)
	for i := 0; i < n+1; i++ {
		cache[i] = make([]int, 3)
	}
	cache[0][0] = 1
	cache[0][1] = 1
	cache[0][2] = 1

	for i := 1; i < n+1; i++ {
		cache[i][0] = (cache[i-1][0] + cache[i-1][1] + cache[i-1][2]) % 9901
		cache[i][1] = (cache[i-1][0] + cache[i-1][2]) % 9901
		cache[i][2] = (cache[i-1][0] + cache[i-1][1]) % 9901
	}
	fmt.Fprintln(w, cache[n][0])
}
