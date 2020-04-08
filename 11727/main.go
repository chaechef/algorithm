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
	cache [1001]int
)

func main() {
	defer w.Flush()
	fmt.Fscanf(r, "%d ", &n )
	res := recursion(n)
	fmt.Fprintln(w, res)
}
func recursion(num int) int {
	if num == 1 {
		return 1
	}
	if num == 2 {
		return 3
	}
	if cache[num] != 0 {
		return cache[num]
	}
	res := recursion(num-2)*2 + recursion(num-1)
	cache[num] = res % 10007
	return cache[num]
}