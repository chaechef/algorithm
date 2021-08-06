package main

import (
	"bufio"
	"fmt"
	"os"
)

var (
	r = bufio.NewReader(os.Stdin)
	w = bufio.NewWriter(os.Stdout)
	n , k int
	cache [][]int
)

func main() {
	defer w.Flush()
	fmt.Fscanf(r,"%d %d ",&n ,&k)
	cache = make([][]int, k+1)
	for i := 0; i < k+1; i++ {
		cache[i] = make([]int, n+1)
	}
	res := recursion(n,k)
	fmt.Fprintln(w, res )
}

func recursion(num int, topick int) int {

	if topick == 1 {
		return 1
	}

	if cache[topick][num] != 0 {
		return cache[topick][num]
	}

	var res int
	for i := 0; i < num+1; i++ {
		res = (res + recursion(num-i, topick-1)) % 1000000000
	}
	cache[topick][num] = res
	return cache[topick][num]
}
