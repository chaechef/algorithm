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
		fmt.Fscanf(r, "%d ", &arr[i])
	}

	for i := 0; i < n; i++ {
		cache[i] = 1
		for j := 0; j < i; j++ {
			if arr[i] > arr[j] && cache[i] < cache[j] + 1 {
				cache[i] = cache[j] + 1
			}
		}
	}
	fmt.Fprintln(w, maxint(cache))

}

func maxint(arr []int) int {
	max := 0

	for i := 0; i < len(arr); i++ {
		if arr[i] > max {
			max = arr[i]
		}
	}
	return max
}