package main

import (
	"bufio"
	"fmt"
	"os"
)

type pair struct {
	first int
	second int
}

var (
	 r = bufio.NewReader(os.Stdin)
	 w = bufio.NewWriter(os.Stdout)
	 n, m int
	 graph [][]int
	 dx = [4]int{1,0,-1,0}
	 dy = [4]int{0,1,0,-1}
	 res int
	 visited []bool
)

func main() {
	defer w.Flush()
	fmt.Fscan(r, &n, &m)
	graph = make([][]int, n+1)
	visited = make([]bool, n + 1)
	for i := 0; i < n+1; i++ {
		graph[i] = make([]int, n+1)
	}
	for i := 0; i < m; i++ {
		var t1,t2 int
		fmt.Fscan(r, &t1, &t2)
		graph[t1][t2] = 1
		graph[t2][t1] = 1
	}
	for i := 0; i < n+1; i++ {
		for j := 0; j < n+1; j++ {
			if graph[i][j] == 1 {
				bfs(i, j)
				res++
			}
		}
	}
	for i := 1; i < n+1; i++ {
		if visited[i] == false {
			res++
		}
	}
	fmt.Fprintln(w, res)
}

func bfs(x int, y int)  {
	var queue []int
	queue = append(queue, x)
	queue = append(queue, y)
	visited[x] = true
	visited[y] = true
	graph[x][y] = 0
	graph[y][x] = 0
	for len(queue) > 0 {
		curr := queue[0]
		queue = queue[1:]
		for i := 0; i < n+1; i++ {
			if graph[curr][i] == 1 {
				queue = append(queue, i)
				graph[curr][i] = 0
				graph[i][curr] = 0
				visited[i] = true
			}
		}
	}
}
