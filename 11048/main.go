package main

import (
	"bufio"
	"fmt"
	"os"
)

var (
	r = bufio.NewReader(os.Stdin)
	w = bufio.NewWriter(os.Stdout)
	n, m int
	arr [][]int
	cache [][]int
)

func main() {
	defer w.Flush()
	fmt.Fscanf(r, "%d %d ", &n, &m )
	arr = make([][]int, n)
	cache = make([][]int, n)
	for i := 0; i < n; i++ {
		arr[i] = make([]int, m)
		cache[i] = make([]int, m)
		for j := 0; j < m; j++ {
			cache[i][j] = 0
		}
	}

	for i := 0; i < n; i++ {
		for j := 0; j < m; j++ {
			fmt.Fscanf(r, "%d ", &arr[i][j])
		}
	}

	for i := 0; i < n; i++ {
		for j := 0; j < m; j++ {
			var t1,t2,t3 int
			if j -1 >= 0 {
				t1 = cache[i][j-1]
			}
			if i -1 >= 0 {
				t2 = cache[i-1][j]
			}
			if i-1 >=0 && j-1 >=0 {
				t3 = cache[i-1][j-1]
			}
			res := maxInt(t1,maxInt(t2,t3)) + arr[i][j]
			cache[i][j] = res
		}
	}
	fmt.Fprintln(w, cache[n-1][m-1])
}

func maxInt(a int, b int) int {
	if a > b {
		return a
	}else {
		return b
	}
}
