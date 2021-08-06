package main

import (
	"bufio"
	"fmt"
	"os"
)

var	(
	r = bufio.NewReader(os.Stdin)
	w = bufio.NewWriter(os.Stdout)
	n,m, tc int
	arr [][]int
	cache [][]int
)

func main() {
	defer w.Flush()
	fmt.Fscanf(r, "%d %d ", &n, &m)
	arr = make([][]int, n+1)
	cache = make([][]int, n+1)
	for i := 0; i < n+1; i++ {
		arr[i] = make([]int, m+1)
		cache[i] = make([]int, m+1)
	}

	for i :=1; i < n+1; i++ {
		for j := 1; j < m+1; j++ {
			fmt.Fscanf(r, "%d ", &arr[i][j])
		}
	}
	for i := 1; i < n+1; i++ {
		for j := 1; j < m+1; j++ {
			cache[i][j] += arr[i][j]
			if i - 1 > 0 {
				cache[i][j] += cache[i-1][j]
			}
			if j - 1 > 0 {
				cache[i][j] += cache[i][j-1]
			}
			if i -1 > 0 && j -1 > 0 {
				cache[i][j] -= cache[i-1][j-1]
			}
		}
	}
	fmt.Fscanf(r, "%d ", &tc)
	for i := 0; i < tc; i++ {
		var x1,x2,y1,y2,res int
		fmt.Fscanf(r, "%d %d %d %d ", &x1, &y1, &x2, &y2)
		res += cache[x2][y2]
		res -= cache[x2][y1-1]
		res -= cache[x1-1][y2]
		res += cache[x1-1][y1-1]
		fmt.Fprintln(w, res)
	}

}
