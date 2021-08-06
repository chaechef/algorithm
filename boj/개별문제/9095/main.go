package main

import (
	"bufio"
	"fmt"
	"os"
)

var (
	r = bufio.NewReader(os.Stdin)
	w = bufio.NewWriter(os.Stdout)
	tc int
	cache []int
	n int
)

func main() {
	defer w.Flush()
	fmt.Fscanf(r,"%d ",&tc)
	cache = make([]int, 12)
	for i := 0; i < tc; i++ {
		fmt.Fscanf(r, "%d ", &n)
		res := recursion(n)
		fmt.Fprintln(w,res)
	}
}

func recursion(num int) int {
	if num == 1 {
		return 1
	}
	if num == 2 {
		return 2
	}
	if num == 3 {
		return 4
	}
	if cache[num] != 0 {
		return cache[num]
	}
	tmp1 := recursion(num - 1)
	tmp2 := recursion(num - 2)
	tmp3 := recursion(num - 3)
	sum := tmp1 + tmp2 + tmp3
	cache[num] = sum
	return sum
}
