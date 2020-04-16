package main

import (
	"bufio"
	"fmt"
	"os"
)

var (
	r = bufio.NewReader(os.Stdin)
	w = bufio.NewWriter(os.Stdout)
	n, s, m int
	volumns []int
	cache [][]bool
	res int
	)

func main() {
	defer w.Flush()
	fmt.Fscanf(r, "%d %d %d ", &n, &s, &m)
	volumns = make([]int, n)
	for i := 0; i < n; i++ {
		fmt.Fscanf(r, "%d ", &volumns[i])
	}
	cache = make([][]bool, n+1)
	for i := 0; i < n+1; i++ {
		cache[i] = make([]bool, m+1)
	}
	cache[0][s] = true
	for i := 0; i < n; i++ {
		for j := 0; j < m+1; j++ {
			if cache[i][j] == true {
				if j + volumns[i] < m + 1{
					cache[i+1][j+volumns[i]] = true
				}
				if j - volumns[i] >= 0 {
					cache[i+1][j-volumns[i]] = true
				}
			}
		}
	}

	check := false
	for i := m; i >= 0; i-- {
		if cache[n][i] == true {
			res = i
			check = true
			break
		}
	}
	if check == false {
		res = -1
	}
	fmt.Fprintln(w, res)
}
