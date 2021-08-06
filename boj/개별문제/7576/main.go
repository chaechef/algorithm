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
	graph [][]int
	dx = [4]int{1,0,-1,0}
	dy = [4]int{0,1,0,-1}
	check bool
	queue []pair
	max = 0
)
type pair struct {
	first int
	second int
}
func main() {
	defer w.Flush()
	fmt.Fscanf(r, "%d %d ", &m, &n)
	graph = make([][]int, n)
	for i := 0; i < n; i++ {
		graph[i] = make([]int, m)
	}

	for i := 0; i < n; i++ {
		for j := 0; j < m; j++ {
			fmt.Fscanf(r, "%d ", &graph[i][j])
			if graph[i][j] == 0 {
				check = true
			}
			if graph[i][j] == 1 {
				queue = append(queue, pair{i,j})
			}
		}
	}
	if check == false {
		fmt.Fprintln(w, 0)
		return
	}
	
	bfs()
	for i := 0; i < n; i++ {
		for j := 0; j < m; j++ {
			if graph[i][j] == 0 {
				fmt.Fprintln(w, -1)
				return
			}
			if graph[i][j] > max {
				max = graph[i][j]
			}
		}
	}
	fmt.Fprintln(w, max-1)
}

func bfs()  {
	for len(queue) > 0 {
		cx, cy := queue[0].first, queue[0].second
		queue = queue[1:]
		for i := 0; i < 4; i++ {
			nx, ny := cx + dx[i], cy + dy[i]
			if isRange(nx,ny) && graph[nx][ny] == 0 {
				graph[nx][ny] = graph[cx][cy] + 1
				queue = append(queue,pair{nx,ny})
			}
		}
	}
}

func isRange(x int, y int) bool {
	if x >=0 && y >= 0 && x < n && y < m {
		return true
	}else{
		return false
	}
}
