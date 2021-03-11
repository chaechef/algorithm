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
	arr []int
	cache [][]int
	right int
)

func main() {
	defer w.Flush()
	fmt.Fscanf(r, "%d ", &n)
	arr = make([]int, n)
	cache = make([][]int, n)
	for i := 0; i < n; i++ {
		cache[i] = make([]int,21)
	}
	for i := 0; i < n; i++ {
		fmt.Fscanf(r, "%d ", &arr[i])
	}
	cache[0][arr[0]] = 1
	for i := 1; i < n-1; i++ {
		for j := 0; j < 21; j++ {
			if cache[i-1][j] != 0 {
				temp1 := j + arr[i]
				if temp1 >= 0 && temp1 < 21 {
					cache[i][temp1] += cache[i-1][j]
				}
				temp2 := j - arr[i]
				if temp2 >=0 && temp2 < 21 {
					cache[i][temp2] += cache[i-1][j]
				}
			}
		}
	}
	fmt.Fprintln(w, cache[n-2][arr[n-1]])
}
