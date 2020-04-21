package main

import (
	"bufio"
	"fmt"
	"os"
)

var (
	r =bufio.NewReader(os.Stdin)
	w = bufio.NewWriter(os.Stdout)
	n, res1, res2 int
	graph1 [][]int
	graph2 [][]int
	str string
	dx = [4]int{1,0,-1,0}
	dy = [4]int{0,1,0,-1}
)

type pair struct {
	first int
	second int
}

func main() {
	defer w.Flush()
	fmt.Fscan(r, &n)
	graph1 = make([][]int, n)
	graph2 = make([][]int, n)
	for i := 0; i < n; i++ {
		fmt.Fscan(r, &str)
		graph1[i] = make([]int, n)
		graph2[i] = make([]int, n)
		for j := 0; j < n; j++ {
			if str[j] == 'R' {
				graph1[i][j] = 1
				graph2[i][j] = 1
			} else if str[j] == 'G' {
				graph1[i][j] = 2
				graph2[i][j] = 1
			} else {
				graph1[i][j] = 3
				graph2[i][j] = 3
			}
		}
	}
	for i := 0; i < n; i++ {
		for j := 0; j < n; j++ {
			if graph1[i][j] == 1 || graph1[i][j] == 2 || graph1[i][j] == 3 {
				bfs(i,j,graph1[i][j])
				res1++
			}
		}
	}
	for i := 0; i < n; i++ {
		for j := 0; j < n; j++ {
			if graph2[i][j] == 1 || graph2[i][j] == 2 || graph2[i][j] == 3 {
				bfs2(i,j,graph2[i][j])
				res2++
			}
		}
	}
	fmt.Fprintln(w, res1, res2)

}
func bfs2(x int, y int, sign int) {
	var queue []pair
	queue = append(queue, pair{x,y})
	graph2[x][y] = 0

	for len(queue) > 0 {
		cx, cy := queue[0].first, queue[0].second
		queue = queue[1:]
		for i := 0; i < 4; i++ {
			nx, ny := cx + dx[i], cy + dy[i]
			if inRange(nx,ny) && graph2[nx][ny] == sign {
				queue = append(queue,pair{nx,ny})
				graph2[nx][ny] = 0
			}
		}
	}
}
func bfs(x int, y int, sign int) {
	var queue []pair
	queue = append(queue, pair{x,y})
	graph1[x][y] = 0

	for len(queue) > 0 {
		cx, cy := queue[0].first, queue[0].second
		queue = queue[1:]
		for i := 0; i < 4; i++ {
			nx, ny := cx + dx[i], cy + dy[i]
			if inRange(nx,ny) && graph1[nx][ny] == sign {
				queue = append(queue,pair{nx,ny})
				graph1[nx][ny] = 0
			}
		}
	}
}

func inRange(x int, y int) bool {
	if x >=0 && y>= 0 && x <n && y< n {
		return true
	}else {
		return false
	}
}