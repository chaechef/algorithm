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
	dp []int
	quantity []int
)

func main() {
	defer w.Flush()

	fmt.Fscanf(r,"%d ", &n)
	quantity = make([]int, n)
	dp = make([]int, n)
	for i := 0; i < n; i++ {
		fmt.Fscanf(r,"%d ", &quantity[i])
	}

	dp[0] = quantity[0]
	if n > 1 {
		dp[1] = quantity[0] + quantity[1]
	}

	if n > 2 {
		dp[2] = max(max(quantity[0] + quantity[2], quantity[1] + quantity[2]),quantity[0]+quantity[1])
	}
	for i := 3; i < n; i++ {
		temp1 := quantity[i] + dp[i-2]
		temp2 := quantity[i] + quantity[i-1] + dp[i-3]
		dp[i] = max(max(temp1,temp2),dp[i-1])
	}
	if n > 1{
		fmt.Fprintln(w,max(dp[n-1],dp[n-2]))
	}else {
		fmt.Fprintln(w,dp[n-1])

	}

}

func max(a int, b int) int {
	if a > b {
		return a
	}else {
		return  b
	}
}