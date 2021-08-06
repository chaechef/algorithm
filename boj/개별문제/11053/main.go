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
	dp []int
)

func main() {
	defer w.Flush()

	fmt.Fscanf(r,"%d ", &n)
	arr = make([]int, n)
	dp = make([]int, n)
	for i := 0; i < n; i++ {
		fmt.Fscanf(r,"%d ", &arr[i])
	}
	dp[0] = 1
	for i := 1; i < n; i++ {
		dp[i] = 1
		for j := i-1; j >= 0; j-- {
			if arr[i] > arr[j] && dp[i] < dp[j] + 1{
				dp[i] = dp[j] + 1
			}
		}
	}
	fmt.Fprintln(w, max(dp))
}

func max( a []int ) int {
	max := 0
	for i := 0; i < len(a); i++ {
		if a[i] > max {
			max = a[i]
		}
	}
	return max
}