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
		cache[i] = arr[i]
		for j := 0; j < i; j++ {
			if arr[j] < arr[i] {
				if cache[i] < cache[j] + arr[i]{
					cache[i] = cache[j] + arr[i]
				}
			}
		}
	}
	fmt.Fprintln(w, maxint(cache))


}

func maxint(a []int) int {
	res := 0
	for i:=0; i<len(a); i++ {
		if a[i] > res {
			res = a[i]
		}
	}
	return res
}
