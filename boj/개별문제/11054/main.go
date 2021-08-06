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
	dp1 []int
	dp2 []int
)

func main() {
	defer w.Flush()
	fmt.Fscanf(r,"%d ", &n)
	arr = make([]int, n)
	dp1 = make([]int, n)
	dp2 = make([]int, n)
	for i := 0; i < n; i++ {
		fmt.Fscanf(r,"%d ", &arr[i])
	}

	//to right
	for i := 0; i < n; i++ {
		dp1[i] = 1
		for j := 0; j < i; j++ {
			if arr[i] > arr[j] && dp1[j] + 1 > dp1[i]{
				dp1[i] = dp1[j] + 1
			}
		}
	}

	//to reft
	for i := n - 1; i >= 0; i-- {
		dp2[i] = 1
		for j := n-1; j > i ; j--  {
			if arr[j] < arr[i] && dp2[i] < dp2[j] + 1 {
				dp2[i] = dp2[j] + 1
			}
		}
	}
	res := 0
	for i := 0; i < n; i++ {
		if res < dp1[i] + dp2[i]{
			res = dp1[i] + dp2[i]
		}
	}

	fmt.Fprintln(w, res-1)

}
