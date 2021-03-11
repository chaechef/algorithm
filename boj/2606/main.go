package main

import (
	"bufio"
	"fmt"
	"os"
)

var (
	r = bufio.NewReader(os.Stdin)
	w = bufio.NewWriter(os.Stdout)
	graph [][]int
	visited []bool
	queue []int
	n,m int
	res int
)

func main() {
	defer w.Flush()
	fmt.Fscanf(r, "%d ", &n)
	graph = make([][]int, n+1)
	visited = make([]bool, n+1)
	for i := 0; i < n+1; i++ {
		graph[i] = make([]int, n+1)
	}
	fmt.Fscanf(r, "%d ", &m)
	for i := 0; i < m; i++ {
		var t1,t2 int
		fmt.Fscanf(r, "%d %d ", &t1, &t2)
		graph[t1][t2] = 1
		graph[t2][t1] = 1
	}

	bfs(1)
	fmt.Fprintln(w, res)
}

func bfs(start int)  {
	queue = append(queue, start)
	visited[start] = true

	for len(queue) > 0 {
		curr := queue[0]
		queue = queue[1:]
		for i := 0; i< len(graph[curr]); i++ {
			if graph[curr][i] == 1 && visited[i] == false {
				queue = append(queue,i)
				visited[i] = true
				res++
			}
		}
	}
}
