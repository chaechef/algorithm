package main

import (
	"bufio"
	"fmt"
	"os"
)

var (
	r = bufio.NewReader(os.Stdin)
	w = bufio.NewWriter(os.Stdout)
	n ,m, k int
	arr [][]int
	cache [][]int
)

func main() {
	defer w.Flush()
	fmt.Fscanf(r, "%d %d %d ", &n, &m, &k)
	arr = make([][]int, n)
	cache = make([][]int, n)
	for i := 0; i < n; i++ {
		arr[i] = make([]int, m)
		cache[i] = make([]int, m)
		for j := 0; j < m; j++ {
			cache[i][j] = 0
		}
	}
	start := 1
	for i := 0; i < n; i++ {
		for j := 0; j < m; j++ {
			arr[i][j] = start
			start++
		}
	}
	cache[0][0] = 1
	for i := 0; i < n; i++ {
		for j := 0; j < m; j++ {
			if i -1 >= 0 {
				cache[i][j] += cache[i-1][j]
			}
			if j -1 >=0 {
				cache[i][j] += cache[i][j-1]
			}
		}
	}
	var tx, ty int
	for i := 0; i < n; i++ {
		for j := 0; j<m; j++ {
			if arr[i][j] == k {
				tx = i
				ty = j
			}
		}
	}
	if k ==0 {
		fmt.Fprintln(w, cache[n-1][m-1])
	}else {
		fmt.Fprintln(w, cache[tx][ty] * cache[n-tx-1][m-ty-1])
	}
}
