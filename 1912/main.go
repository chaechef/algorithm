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
		fmt.Fscanf(r, "%d ", &arr[i])
	}

	dp[0] = arr[0]

	for i := 1; i < n; i++ {
		if dp[i-1] + arr[i] < arr[i] {
			dp[i] = arr[i]
		}else {
			dp[i] = dp[i-1] + arr[i]
		}
	}
	fmt.Fprintln(w,max(dp))

}

func max(arr []int) int {
	res := -1001
	for i:=0; i<len(arr); i++ {
		if res < arr[i] {
			res = arr[i]
		}
	}
	return res
}
