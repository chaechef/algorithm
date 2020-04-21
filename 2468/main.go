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
	 n int
	 graph [][]int
	 arr [101]bool
	 cp [][]bool
	 dx = [4]int{1,0,-1,0}
	 dy = [4]int{0,1,0,-1}
	 max = 1
	 maxheight int
)

func main() {
	defer w.Flush()
	fmt.Fscan(r, &n)
	graph = make([][]int, n)
	for i := 0; i < n; i++ {
		graph[i] = make([]int, n)
	}
	for i := 0; i < n; i++ {
		for j := 0; j < n; j++ {
			fmt.Fscan(r, &graph[i][j])
			if maxheight < graph[i][j] {
				maxheight = graph[i][j]
			}
		}
	}

	for k := 1; k < maxheight; k++ {
			cp = make([][]bool, n)
			for i := 0; i < n; i++ {
				cp[i] = make([]bool, n)
				for j := 0; j < n; j++ {
					if graph[i][j] <= k {
						cp[i][j] = true
					}else {
						cp[i][j] = false
					}
				}
			}
			var res int
			for i := 0; i < n; i++ {
				for j := 0; j < n; j++ {
					if cp[i][j] == false{
						bfs(i,j)
						res++
					}
				}
			}
			if max < res {
				max = res
			}
	}
	fmt.Fprintln(w, max)
}

func bfs(x int, y int) {
	var queue []pair
	cp[x][y] = true
	queue = append(queue, pair{x,y})

	for len(queue) > 0 {
		cx, cy := queue[0].first, queue[0].second
		queue = queue[1:]
		for i := 0; i < 4; i++ {
			nx, ny := cx +dx[i], cy+dy[i]
			if inRange(nx,ny) && cp[nx][ny] == false {
				queue = append(queue, pair{nx,ny})
				cp[nx][ny] = true
			}
		}
	}
}

func inRange(x int, y int) bool {
	if x >=0 && y>=0 && x <n && y <n {
		return true
	}else {
		return false
	}
}