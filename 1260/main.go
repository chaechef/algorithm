package main

import (
	"bufio"
	"fmt"
	"os"
)

var (
	r = bufio.NewReader(os.Stdin)
	w = bufio.NewWriter(os.Stdout)
	n,m,v int
	graph [][]int
	dx = [4]int{1,0,-1,0}
	dy = [4]int{0,-1,0,1}
	visited []bool
	cities []int
)

func main() {
	defer w.Flush()
	fmt.Fscanf(r, "%d %d %d ", &n, &m, &v)
	graph = make([][]int, n+1)
	visited = make([]bool,n+1)
	for i := 0; i < n+1; i++ {
		graph[i] = make([]int, n+1)
	}
	for i := 0; i < m; i++ {
		var t1,t2 int
		fmt.Fscanf(r, "%d %d ", &t1, &t2)
		graph[t1][t2] = 1
		graph[t2][t1] = 1
	}
	dfs(v)
	fmt.Fprintln(w)
	visited = make([]bool,n+1)
	bfs(v)

}

func dfs(start int)  {
	visited[start] = true
	fmt.Fprint(w, start," ")

	for i := 0; i < len(graph[start]); i++ {
		if graph[start][i] == 1 && visited[i] == false {
			dfs(i)
		}
	}
}

func bfs(start int)  {
	cities = append(cities, start)
	visited[start] = true
	for len(cities) > 0 {
		curr := cities[0]
		cities = cities[1:]
		fmt.Fprint(w, curr, " ")
		for i := 0; i< len(graph[curr]); i++  {
			if visited[i] == false && graph[curr][i] == 1 {
				cities = append(cities, i )
				visited[i] = true

			}
		}
	}
	fmt.Fprintln(w)
}
