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
	stair []int
	dp []int
)

func main() {
	defer w.Flush()

	fmt.Fscanf(r, "%d ", &n)
	stair = make([]int, n)
	dp = make([]int, n)

	for i := 0; i < n; i++ {
		fmt.Fscanf(r, "%d ", &stair[i])
	}

	dp[0] = stair[0]
	if n > 1 {
		dp[1] = stair[0] + stair[1]
	}
	if n > 2 {
		dp[2] =	max(stair[0] + stair[2], stair[1] + stair[2])
	}
	for i := 3; i < n; i++ {
		temp1 := dp[i-2] + stair[i]
		temp2 := dp[i-3] + stair[i-1] + stair[i]
		dp[i] = max(temp1, temp2)
	}
	fmt.Fprintln(w, dp[n-1])
}

func max(a int, b int) int {
	if a > b {
		return a
	}else {
		return b
	}
}