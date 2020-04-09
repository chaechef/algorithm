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
	question int
	left, right int
	cache [][]int
)

func main() {
	defer w.Flush()
	fmt.Fscanf(r, "%d ", &n)
	arr = make([]int, n+1)
	cache = make([][]int, n+1)
	for i := 0; i < n+1; i++ {
		cache[i] = make([]int, n+1)
		for j := 0; j < n+1; j++ {
			cache[i][j] = -1
		}
	}
	for i := 1; i < n+1; i++ {
		fmt.Fscanf(r, "%d ", &arr[i])
	}
	fmt.Fscanf(r,"%d ", &question)
	for i := 0; i < question; i++ {
		fmt.Fscanf(r, "%d %d ",&left, &right)
		res := recursion(left,right)
		fmt.Fprintln(w, res)
	}
}

func recursion(left int, right int) int {
	if left == right {
		return 1
	}
	if left +1 == right {
		if arr[left] == arr[right] {
			return 1
		} else {
			return 0
		}
	}
	if cache[left][right] != -1 {
		return cache[left][right]
	}

	if arr[left] == arr[right] && recursion(left+1,right-1) == 1 {
		cache[left][right] = 1
	}else {
		cache[left][right] = 0
	}

	return cache[left][right]

}
