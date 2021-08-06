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
	cache []int
)

func main ()  {
	defer w.Flush()
	fmt.Fscanf(r, "%d ", &n)
	cache = make([]int, n+1)
	if n > 1 {
		cache[2] = 3
	}
	for i := 4; i < n+1; i = i+2 {
		cache[i] = cache[i-2] * 3
		for j := 2; j <= i-4; j = j+2 {
			cache[i] += cache[j] * 2
		}
		cache[i] += 2
	}
	fmt.Fprintln(w, cache[n])
}
