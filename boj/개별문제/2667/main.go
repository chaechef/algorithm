package main

import (
	"bufio"
	"fmt"
	"os"
	"sort"
)

var (
	r = bufio.NewReader(os.Stdin)
	w = bufio.NewWriter(os.Stdout)
	n int
	graph [][]int
	danji int
	houses []int
	dx = [4]int{1,0,-1,0}
	dy = [4]int{0,1,0,-1}
)

func main() {
	defer w.Flush()
	fmt.Fscanf(r, "%d ",&n)
	graph = make([][]int, n)
	for i := 0; i < n; i++ {
		graph[i] = make([]int, n)
	}
	for i := 0; i < n; i++ {
		for j := 0; j < n; j++ {
			fmt.Fscanf(r, "%1d", &graph[i][j])
		}
		fmt.Fscanf(r,"\n")
	}
	for i := 0; i < n; i++ {
		for j := 0; j < n; j++ {
			if graph[i][j] == 1 {
				danji++
				res := bfs(i,j)
				houses = append(houses,res)
			}
		}
	}
	fmt.Fprintln(w, danji)
	sort.Ints(houses)
	for i := 0; i< len(houses); i++  {
		fmt.Fprintln(w, houses[i])
	}
}

func isRange(x int, y int) bool {
	if x >=0 && y>=0 && x < n && y <n {
		return true
	}else {
		return false
	}
}
func bfs(x int, y int) int {
	graph[x][y] = 0
	var queueX []int
	var queueY []int
	queueX = append(queueX, x)
	queueY = append(queueY, y)
	var num = 1
	for len(queueX) > 0 {
		cx := queueX[0]
		cy := queueY[0]
		queueX = queueX[1:]
		queueY = queueY[1:]
		for i := 0; i < 4; i++ {
			nx := cx + dx[i]
			ny := cy + dy[i]
			if isRange(nx,ny) && graph[nx][ny] == 1{
				queueX = append(queueX,nx)
				queueY = append(queueY,ny)
				graph[nx][ny] = 0
				num++
			}
		}
	}

	return num
}