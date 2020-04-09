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
	arr [][]int
	cache [][]int
	dx = [4]int {1,0,-1,0}
	dy = [4]int {0,-1,0,1}
)

func main() {
	defer w.Flush()
	fmt.Fscanf(r,"%d ", &n)
	arr = make([][]int, n)
	cache = make([][]int, n)
	for i := 0; i < n; i++ {
		arr[i] = make([]int, n)
		cache[i] = make([]int, n)
	}
	for i := 0; i < n; i++ {
		for j := 0; j < n; j++ {
			fmt.Fscanf(r,"%d ", &arr[i][j])
			cache[i][j] = -1
		}
	}
	max :=0
	for i := 0; i < n; i++ {
		for j := 0; j < n; j++ {
			temp := recursion(i,j)
			if temp > max {
				max= temp
			}
		}
	}

	fmt.Fprintln(w, max)

}

func recursion(x int, y int) int {
	if isRange(x,y) == false {
		return 0
	}

	if cache[x][y] != -1 {
		return cache[x][y]
	}

	res := 0
	for i := 0; i < 4; i++ {
		nx := dx[i] + x
		ny := dy[i] + y
		if isRange(nx, ny) == true {
			if arr[x][y] < arr[nx][ny] {
				temp := recursion(nx,ny)
				if temp > res {
					res = temp
				}
			}

		}
	}

	cache[x][y] = res + 1
	return cache[x][y]
}

func isRange(x int, y int) bool {
	if x >= 0 && y >= 0 && x < n && y < n {
		return true
	}else {
		return false
	}
}