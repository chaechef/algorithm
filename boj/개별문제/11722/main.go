package main

import (
	"bufio"
	"fmt"
	"os"
)

var	(
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
		cache[i] = -1
	}
	recursion(n-1)
	fmt.Fprintln(w, maxint(cache))
}
func maxint	(a []int) int {
	max := 0
	for i := 0; i < len(a); i++ {
		if a[i] > max {
			max = a[i]
		}
	}
	return max
}

func recursion(num int) int {
	if num == 0 {
		cache[num] = 1
		return cache[num]
	}

	if cache[num] != -1 {
		return cache[num]
	}
	max := 1
	for i := 0; i < num; i++ {
		var temp int
		temp = recursion(i)
		if arr[i] > arr[num] {
			temp++
			if temp > max {
				max = temp
			}
		}else {
			continue
		}


	}
	cache[num] = max

	return cache[num]
}