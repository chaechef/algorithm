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
	dx = [4]int{1,0,-1,0}
	dy = [4]int{0,1,0,-1}
	graph [][]int
	visited [][]int
)
type pair struct {
	first int
	second int
}
func main() {
	defer w.Flush()
	fmt.Fscanf(r, "%d %d ", &n, &m )
	graph = make([][]int, n)
	visited = make([][]int, n)

	for i := 0; i < n; i++ {
		graph[i] = make([]int, m)
		visited[i] = make([]int, m)
	}

	for i := 0; i < n; i++ {
		for j:=0;j<m; j++  {
			fmt.Fscanf(r, "%1d", &graph[i][j])
			visited[i][j] = graph[i][j]
		}
		fmt.Fscanf(r,"\n")
	}
	bfs(0,0)
	fmt.Fprintln(w, graph[n-1][m-1])
}

func isRange(x int, y int) bool {
	if x >= 0 && y >= 0 && x < n && y < m {
		return true
	}else {
		return false
	}
}

func bfs(x int, y int)  {
	visited[x][y] = 0
	var queue []pair
	queue = append(queue, pair{x,y})
	for len(queue) > 0 {
		cx, cy := queue[0].first, queue[0].second
		queue = queue[1:]
		for i := 0; i < 4; i++ {
			nx, ny := cx+dx[i], cy + dy[i]
			if isRange(nx, ny) && visited[nx][ny] == 1 {
				queue = append(queue, pair{nx,ny})
				visited[nx][ny] = 0
				graph[nx][ny] = graph[cx][cy] + 1
			}
		}
	}

}


