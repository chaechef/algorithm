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
	mmap [][]int
	cache [][]int
	dx = []int{1,0,-1,0}
	dy = []int{0,-1,0,1}
)


func main() {
	defer w.Flush()
	fmt.Fscanf(r, "%d %d ", &n, &m)
	mmap = make([][]int, n)
	cache = make([][]int, n)
	for i := 0; i < n; i++ {
		mmap[i] = make([]int, m)
		cache[i] = make([]int, m)
	}
	for i := 0; i < n; i++ {
		for j := 0; j < m; j++ {
			fmt.Fscanf(r, "%d ", &mmap[i][j])
			cache[i][j] = -1
		}
	}
	var res int
	res += recursion(n-1,m-1)
	fmt.Fprintln(w, res)
}

func recursion(x int, y int) int {
	if x == 0 && y == 0 {
		return 1
	}
	if cache[x][y] != -1 {
		return cache[x][y]
	}

	cache[x][y] = 0
	for i := 0; i < 4; i++ {
		nx := dx[i] + x
		ny := dy[i] + y
		if isrange(nx,ny) == true {
			if mmap[nx][ny] > mmap[x][y] {
				cache[x][y] += recursion(nx,ny)
			}
		}
	}
	return cache[x][y]

}

func isrange(x int , y int) bool {
	if x < 0 || y < 0 || x >= n || y >= m {
		return false
	}else{
		return true
	}
}