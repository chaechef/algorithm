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

type quad struct {
	rx, ry, bx, by int
}
var (
	r= bufio.NewReader(os.Stdin)
	w = bufio.NewWriter(os.Stdout)
	n, m int
	graph []string
	visited [10][10][10][10]bool
	dx = [4]int{1,0,-1,0}
	dy = [4]int{0,1,0,-1}
	cord quad
)

func main() {
	defer w.Flush()
	fmt.Fscan(r, &n, &m)
	graph = make([]string, n)
	for i := 0; i < n; i++ {
		fmt.Fscan(r, &graph[i])
		for j := 0; j < m; j++ {
			if graph[i][j] == 'R' {
				cord.rx = i
				cord.ry = j
			}
			if graph[i][j] == 'B'{
				cord.bx = i
				cord.by = j
			}
		}
	}
	recursion(cord,0)
}

func recursion(start quad, count int)  {
	if visited[start.rx][start.ry][start.bx][start.by] == true {
		return
	}
	visited[cord.rx][cord.ry][cord.bx][cord.by] = true
	fmt.Fprintln(w, start)
	//button right, up, left
	for i := 0; i < 4; i++ {
		var checkRed, checkBlue bool
		crx, cry, cbx, cby := start.rx, start.ry, start.bx, start.by
		nrx, nry, nbx, nby := crx + dx[i], cry + dy[i], cbx + dx[i], cby + dy[i]
		for inRange(nrx, nry) && graph[nrx][nry] != '#' {
			crx, cry = nrx, nry
			if graph[crx][cry] == 'O'{
				checkRed = true
				break
			}
			nrx, nry = crx + dx[i], cry + dy[i]
		}
		for inRange(nbx, nby) && graph[nbx][nby] != '#' {
			cbx, cby = nbx, nby
			if graph[cbx][cby] == 'O'{
				checkBlue = true
				break
			}
			nbx, nby = cbx + dx[i], cby + dy[i]
		}
		if checkRed && !checkBlue {
			fmt.Fprintln(w, count)

		}

	}



}



func inRange(x int, y int) bool {
	if x >=0 && y >= 0 && x < n && y < n {
		return true
	}else {
		return false
	}
}