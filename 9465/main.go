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
	stiker [][]int
	cache [][]int
	n int
)

func main() {
	defer w.Flush()
	fmt.Fscanf(r, "%d ", &tc)
	for i := 0; i < tc; i++ {
		//init
		fmt.Fscanf(r, "%d ", &n)
		stiker = make([][]int, 2)
		cache = make([][]int, 2)
		for j := 0; j < 2 ; j++{
			stiker[j] = make([]int, n)
			cache[j] = make([]int, n)
		}
		for j := 0; j< 2; j++ {
			for k := 0; k < n; k++ {
				fmt.Fscanf(r,"%d ", &stiker[j][k])
				cache[j][k] = -1
			}
		}
		//recursion
		res := max(recursion(0,n-1), recursion(1,n-1))

		fmt.Fprintln(w, res)
	}
}
func max(a int, b int) int {
	if a > b {
		return a
	}else {
		return b
	}
}
func recursion(position int ,num int) int {
	if num < 0 {
		return 0
	}
	if num == 0 {
		return stiker[position][num]
	}

	if cache[position][num] != -1 {
		return cache[position][num]
	}
	nextposition := (position + 1 ) % 2
	res := stiker[position][num] + max(recursion(nextposition, num-1),recursion(nextposition,num-2))
	cache[position][num] = res
	return res
}
