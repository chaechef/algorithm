package main

import (
	"bufio"
	"fmt"
	"os"
)

var (
	r = bufio.NewReader(os.Stdin)
	w = bufio.NewWriter(os.Stdout)
	n,m int
	arr [][]int
	cache [][]int
	max int
)

func main() {
	defer w.Flush()
	fmt.Fscanf(r, "%d %d ", &n, &m)
	arr = make([][]int, n)
	cache = make([][]int, n)
	for i := 0; i < n; i++ {
		arr[i] = make([]int, m)
		cache[i] = make([]int, m)
	}

	for i := 0; i < n; i++ {
		for j := 0; j < m; j++ {
			fmt.Fscanf(r,"%1d", &arr[i][j])
			if isRange(i,j-1) && arr[i][j] == 1 {
				cache[i][j] = cache[i][j-1] + 1
			}else {
				cache[i][j] = arr[i][j]
			}
		}
		fmt.Fscanf(r," ")
	}
	for i := 0; i < m; i++ {
		for j := 0; j < n; j++ {
			if cache[j][i] > max  && check(j,i,cache[j][i]) {
				max = cache[j][i]
			}
		}
	}
	fmt.Fprintln(w, max*max)
}

func check(x int, y int, size int) bool {
	var count int
	for i := x+1; i < n; i++ {
		if cache[i][y] >= size {
			count++
		}else {
			break
		}
	}
	for i := x - 1; i >= 0; i-- {
		if cache[i][y] >= size {
			count++
		}else{
			break
		}
	}
	if count + 1 >= size {
		return true
	}
	return false
}

func isRange(x int, y int) bool {
	if x >=0 && y >= 0 && x < n && y < m {
		return true
	}else {
		return false
	}
}
