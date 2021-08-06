package main

import (
	"bufio"
	"fmt"
	"os"
)

const INIT = -2000000000

var (
	r = bufio.NewReader(os.Stdin)
	w = bufio.NewWriter(os.Stdout)
	n, m int
	graph [][]int
	cache [3][][]int
	visited [][]bool
	dx = [3]int{0,0,1}
	dy = [3]int{1,-1,0} //down right left
)

func main()  {
	defer w.Flush()
	fmt.Fscan(r, &n, &m)
	graph = make([][]int, n)
	visited = make([][]bool, n)
	for i := 0; i < n; i++ {
		graph[i] = make([]int, m)
		visited[i] = make([]bool,m)
	}
	for i := 0; i < 3; i++ {
		cache[i] = make([][]int, n)
		for j := 0; j < n; j++ {
			cache[i][j] = make([]int, m)
			for k := 0; k < m; k++ {
				cache[i][j][k] = INIT
			}
		}
	}
	for i := 0; i < n; i++ {
		for j := 0; j < m; j++ {
			fmt.Fscan(r, &graph[i][j])
		}
	}

	res := recursion(0,0,0)
	fmt.Fprintln(w, res)
	//for i := 0; i < 3; i++ {
	//	for j := 0; j < n; j++ {
	//		fmt.Fprintln(w, cache[i][j])
	//	}
	//	fmt.Fprintln(w)
	//}
}

func recursion(direction int, x int, y int) int {
	if cache[direction][x][y] != INIT {
		return cache[direction][x][y]
	}
	if x == n-1 && y == m -1 {
		cache[direction][x][y] = graph[x][y]
		return cache[direction][x][y]
	}
	visited[x][y] = true
	var c1, c2, c3 = INIT, INIT, INIT

	if y - 1 >= 0 && visited[x][y-1] == false {
		c1 = recursion(0,x,y-1)
	}
	if y + 1 < m && visited[x][y+1] == false {
		c2 = recursion(1,x,y+1)
	}
	if x + 1  < n && visited[x+1][y] == false {
		c3 = recursion(2,x+1,y)
	}
	visited[x][y] = false
	cache[direction][x][y] = maxint(maxint(c1,c2),c3) + graph[x][y]
	return cache[direction][x][y]
}
func maxint(a int, b int) int {
	if a > b {
		return a
	}else {
		return b
	}
}

func inRange(x int, y int) bool {
	if x >= 0 && y >= 0 && x < n && y < m {
		return true
	}else {
		return false
	}
}