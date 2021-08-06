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
	matrix [][]int
	cache [][]int
)

func main() {
	defer w.Flush()
	fmt.Fscanf(r, "%d ", &n)
	matrix = make([][]int, 2)
	cache = make([][]int, n)
	for i := 0; i < 2; i++ {
		matrix[i] = make([]int,n)
	}
	for i := 0; i < n; i++ {
		cache[i] = make([]int, n)
		for j := 0; j < n; j++ {
			cache[i][j] = 2147483647
		}
	}
	for i := 0; i < n; i++ {
		fmt.Fscanf(r, "%d %d ", &matrix[0][i], &matrix[1][i] )
	}
	res := recursion(0,n-1)
	fmt.Fprintln(w, res)
}

func recursion(l int, r int) int {
	if l == r {
		cache[l][r] = 0
		return cache[l][r]
	}
	if l+1 == r {
		cache[l][r] = matrix[0][l] * matrix[1][l] * matrix[1][r]
		return cache[l][r]
	}
	if cache[l][r] != 2147483647 {
		return cache[l][r]
	}
	for i := 0; l + i + 1 <= r; i++ {
		var temp int
		temp += recursion(l,l+i)
		temp += recursion(l+i+1,r)
		temp += matrix[0][l] * matrix[1][l+i] * matrix[1][r]
		if cache[l][r] > temp {
			cache[l][r] = temp
		}
	}
	return cache[l][r]
}
