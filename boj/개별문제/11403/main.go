package main

import (
	"bufio"
	"fmt"
	"os"
)

var (
	r = bufio.NewReader(os.Stdin)
	w = bufio.NewWriter(os.Stdout)
	n int
	graph [][]int
	graph1 [][]int
	visited []bool
)

func main() {
	defer w.Flush()
	fmt.Fscan(r, &n)
	graph = make([][]int,n)
	graph1 = make([][]int, n)
	for i := 0; i < n; i++ {
		graph[i] = make([]int, n)
		graph1[i] = make([]int, n)
	}
	for i := 0; i < n; i++ {
		for j := 0; j < n; j++ {
			fmt.Fscan(r, &graph[i][j])
		}
	}
	for i := 0; i < n; i++ {
		visited = make([]bool ,n)
		bfs(i)
	}

	for i := 0; i < n; i++ {
		for j := 0; j < n; j++ {
			fmt.Fprint(w, graph1[i][j], " ")
		}
		fmt.Fprintln(w)
	}
}

func bfs(start int)  {
	var queue []int

	for i := 0; i < n; i++ {
		if graph[start][i] == 1 {
			queue = append(queue, i)
			graph1[start][i] = 1
		}
	}
	for len(queue) > 0 {
		curr := queue[0]
		visited[curr] = true
		queue = queue[1:]
		for i := 0; i < n; i++ {
			if graph[curr][i] == 1 && visited[i] == false {
				queue = append(queue, i)
				graph1[start][i] = 1
			}
		}
	}

}
