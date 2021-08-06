package main

import (
	"bufio"
	"fmt"
	"os"
)

var	(
	r = bufio.NewReader(os.Stdin)
	w = bufio.NewWriter(os.Stdout)
	n int
	cache [1001]int
)

func main() {
	defer w.Flush()
	fmt.Fscanf(r,"%d ", &n)
	res := recursion(n)
	fmt.Fprintln(w, res)
}

func recursion(num int) int {
	if num == 1 || num == 2{
		return num
	}
	if cache[num] != 0 {
		return cache[num]
	}
	res := recursion(num - 1) + recursion(num - 2)
	cache[num] = res % 10007
	return cache[num]
}
