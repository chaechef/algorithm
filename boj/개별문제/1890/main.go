package main

import (
	"bufio"
	"fmt"
	"os"
)

var (
	r = bufio.NewReader(os.Stdin)
	w = bufio.NewWriter(os.Stdout)
	n int64
	arr [][]int64
	cache [][]int64
	i, j int64
)

func main() {
	defer w.Flush()
	fmt.Fscanf(r, "%d ", &n)
	arr = make([][]int64, n)
	cache = make([][]int64, n)
	for i = 0; i < n; i++ {
		arr[i] = make([]int64, n)
		cache[i] = make([]int64, n)
		for j = 0; j < n; j++ {
			cache[i][j] = -1
		}
	}

	for i = 0; i < n; i++ {
		for j = 0; j < n; j++ {
			fmt.Fscanf(r, "%d ",&arr[i][j])
		}
	}
	res := recursion(0,0)
	fmt.Fprintln(w,res)
}

func recursion(x int64, y int64) int64 {
	if x == n-1 && y ==n-1 {
		return 1
	}
	if x >= n || y >= n {
		return 0
	}
	if cache[x][y] != -1 {
		return cache[x][y]
	}

	jump := arr[x][y]
	if jump == 0 {
		return  0
	}
	var res int64
	if x + jump < n {
		res += recursion(x+jump,y)
	}
	if y + jump < n {
		res += recursion(x,y+jump)
	}
	cache[x][y] = res
	return cache[x][y]
}
