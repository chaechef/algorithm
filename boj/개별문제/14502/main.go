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
	walls []pair
	virus []pair
	dx = [4]int{1,0,-1,0}
	dy = [4]int{0,1,0,-1}
	max int
)

func main() {
	defer w.Flush()
	fmt.Fscan(r, &n, &m)
	graph = make([][]int, n)
	for i := 0; i < n; i++ {
		graph[i] = make([]int, m)
	}
	for i := 0; i < n; i++ {
		for j := 0; j < m; j++ {
			fmt.Fscan(r, &graph[i][j])
			if graph[i][j] == 0 {
				walls = append(walls, pair{i,j})
			}
			if graph[i][j] == 2 {
				virus = append(virus, pair{i,j})
			}
		}
	}
	var p []int
	putwall(p,0)
	fmt.Fprintln(w, max)
}

func inRnage(x int, y int) bool {
	if x >=0 && y>= 0 && x < n && y < m {
		return true
	}else {
		return false
	}
}
func bfs(gcopy [][]int) int {
	var queue []pair
	for i := 0; i < len(virus); i++ {
		queue = append(queue, virus[i])
	}

	for len(queue) > 0 {
		cx, cy := queue[0].first, queue[0].second
		queue = queue[1:]
		for i := 0; i < 4; i++ {
			nx, ny := cx + dx[i], cy + dy[i]
			if inRnage(nx, ny) && gcopy[nx][ny] == 0 {
				gcopy[nx][ny] = 2
				queue = append(queue, pair{nx,ny})
			}
		}
	}
	var cnt int
	for i := 0; i < n; i++ {
		for j := 0; j < m; j++ {
			if gcopy[i][j] == 0 {
				cnt++
			}
		}
	}
	return cnt
}

func putwall(picked []int ,count int)  {
	if count == 3 {
		var gcopy = make([][]int, n)
		for i := 0; i < n; i++ {
			gcopy[i] = make([]int, m)
			copy(gcopy[i],graph[i])

		}
		for i := 0; i < 3; i++ {
			gcopy[walls[picked[i]].first][walls[picked[i]].second] = 1
		}
		res := bfs(gcopy)
		if max < res {
			max = res
		}
		return
	}
	var smallest int
	if len(picked) == 0 {
		smallest = 0
	}else {
		smallest = picked[len(picked)-1] + 1
	}

	for i := smallest; i < len(walls) ; i++ {
		picked = append(picked, i)
		putwall(picked, count+1)
		picked = picked[:len(picked)-1]
	}

}

