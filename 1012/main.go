package main

import (
	"bufio"
	"fmt"
	"os"
)

var (
	r = bufio.NewReader(os.Stdin)
	w = bufio.NewWriter(os.Stdout)
	tc int
	n, m, num int
	t1, t2 int
	graph [][]int
	dx = [4]int{1,0,-1,0}
	dy = [4]int{0,1,0,-1}
)

type pair struct {
	first int
	second int
}

func main() {
	defer w.Flush()
	fmt.Fscanf(r, "%d ", &tc)
	for t := 0; t < tc; t++ {
		var res int
		fmt.Fscanf(r, "%d %d %d ", &n, &m, &num)
		graph = make([][]int, n)
		for i := 0; i < n; i++ {
			graph[i] = make([]int, m)
		}
		for i := 0; i < num; i++ {
			fmt.Fscanf(r, "%d %d ",&t1, &t2)
			graph[t1][t2] = 1
		}

		for i := 0; i < n; i++ {
			for j := 0; j < m; j++ {
				if graph[i][j] == 1 {
					res++
					bfs(i,j)
				}
			}
		}
		fmt.Fprintln(w, res)
	}
}

func isRange(x int, y int) bool {
	if x >=0 && y>=0 && x< n && y< m {
		return true
	}else {
		return false
	}
}

func bfs(x int, y int)  {
	var queue []pair
	var a = pair{x,y}
	queue = append(queue, a)
	graph[x][y] = 0

	for len(queue) > 0 {
		cx := queue[0].first
		cy := queue[0].second
		queue = queue[1:]
		for i := 0; i < 4; i++ {
			nx := cx + dx[i]
			ny := cy + dy[i]
			if isRange(nx,ny) && graph[nx][ny] == 1 {
				queue = append(queue, pair{nx,ny})
				graph[nx][ny] = 0
			}
		}
	}

}