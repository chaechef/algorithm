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

func main() {
	defer w.Flush()
	fmt.Fscanf(r, "%d ", &n)
	cache = make([]int, n+1)

	for i := 1; i < n+1; i++ {
		if cache[i] == 0 {
			cache[i] = i
		}
		if i * i < n + 1 {
			cache[i*i] = 1
		}
	}

	for i := 1; i < n+1; i++ {
		min := cache[i]
		for j := 1; j <= i / 2 ; j++ {
			temp := cache[j] + cache[i-j]
			if temp < min {
				min = temp
			}
		}
		cache[i] = min
	}
	fmt.Fprintln(w, cache[n])


}
