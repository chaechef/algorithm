package main

import (
	"bufio"
	"fmt"
	"os"
)

var (
	r = bufio.NewReader(os.Stdin)
	w = bufio.NewWriter(os.Stdout)
	n, k int
	graph [100001]int
)

func main() {
	defer w.Flush()
	fmt.Fscanf(r, "%d %d ", &n, &k)
	if n > k {
		fmt.Fprintln(w, n-k)
		return
	}
	bfs(n)
	fmt.Fprintln(w, graph[k])
}

func bfs(n int)  {
	var queue []int
	queue = append(queue, n)

	for len(queue) > 0 {
		curr := queue[0]
		queue = queue[1:]
		n1, n2, n3 := curr+1, curr-1, curr*2
		if curr == k {
			break
		}
		if isRange(n1) && graph[n1] == 0 {
			graph[n1] = graph[curr]+1
			queue = append(queue, n1)
		}
		if isRange(n2) && graph[n2] == 0{
			graph[n2] = graph[curr]+1
			queue = append(queue, n2)

		}
		if isRange(n3) && graph[n3] == 0{
			graph[n3] = graph[curr]+1
			queue = append(queue, n3)
		}
	}
}

func isRange(n int) bool {
	if n >=0 && n < 100001 {
		return true
	}else {
		return false
	}
}