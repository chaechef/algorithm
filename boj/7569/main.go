package main

import (
	"bufio"
	"fmt"
	"os"
)

var (
	r = bufio.NewReader(os.Stdin)
	w = bufio.NewWriter(os.Stdout)
	n, m ,z int
	graph [][][]int
	dx = [6]int{1,0,-1,0,0,0}
	dy = [6]int{0,1,0,-1,0,0}
	dz = [6]int{0,0,0,0,1,-1}
	check bool
	queue []tuple
	max = 0
)
type tuple struct {
	first int
	second int
	third int
}
func main() {
	defer w.Flush()
	fmt.Fscanf(r, "%d %d %d ", &m, &n, &z)
	graph = make([][][]int, z)

	for i := 0; i < z; i++ {
		graph[i] = make([][]int, n)
		for j := 0; j < n; j++ {
			graph[i][j] = make([]int, m)
		}
	}
	for i := 0; i < z; i++ {
		for j := 0; j < n; j++ {
			for k := 0; k < m; k++ {
				fmt.Fscanf(r, "%d ", &graph[i][j][k])
				if graph[i][j][k] == 0 {
					check = true
				}
				if graph[i][j][k] == 1 {
					queue = append(queue, tuple{i,j, k})
				}
			}
		}
	}

	if check == false {
		fmt.Fprintln(w, 0)
		return
	}
	bfs()

	for i := 0; i < z; i++ {
		for j := 0; j < n; j++ {
			for k := 0; k < m; k++ {
				if graph[i][j][k] == 0 {
					fmt.Fprintln(w, -1)
					return
				}
				if graph[i][j][k] > max {
					max = graph[i][j][k]
				}
			}
		}
	}
	fmt.Fprintln(w, max-1)
}

func bfs()  {
	for len(queue) > 0 {
		cx, cy, cz := queue[0].first, queue[0].second, queue[0].third
		queue = queue[1:]
		for i := 0; i < 6; i++ {
			nx, ny, nz := cx + dx[i], cy + dy[i], cz + dz[i]
			if isRange(nx,ny,nz) && graph[nx][ny][nz] == 0 {
				graph[nx][ny][nz] = graph[cx][cy][cz] + 1
				queue = append(queue,tuple{nx,ny, nz})
			}
		}
	}
}

func isRange(x int, y int, t int) bool {
	if x >=0 && y >= 0 && x < z && y < n && t >= 0 && t < m{
		return true
	}else{
		return false
	}
}
