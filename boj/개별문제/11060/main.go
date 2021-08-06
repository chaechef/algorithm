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
	arr []int
	cache []int
)

func main() {
	defer w.Flush()
	fmt.Fscanf(r, "%d ", &n)
	arr = make([]int, n)
	cache = make([]int, n)
	for i := 0; i < n; i++ {
		cache[i] = -1
	}
	for i := 0; i < n; i++ {
		fmt.Fscanf(r, "%d ", &arr[i])
	}
	cache[0] = 0
	for i := 0; i < n -1; i++ {
		jump := arr[i]
		for j := 1; j < jump+1; j++ {
			if i + j < n  && cache[i] != -1{
				if cache[i+j] == -1 {
					cache[i+j] = cache[i] + 1
				}else {
					if cache[i+j] > cache[i] + 1{
						cache[i+j] = cache[i] + 1
					}
				}
			}
		}
	}

	fmt.Fprintln(w, cache[n-1])
}
