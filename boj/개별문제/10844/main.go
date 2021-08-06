package main

import (
	"bufio"
	"fmt"
	"os"
)

var (
	w = bufio.NewWriter(os.Stdout)
	r = bufio.NewReader(os.Stdin)
	dp [][]int
	n int
)

func main() {
	defer w.Flush()
	fmt.Fscanf(r,"%d ", &n)
	dp = make([][]int, n + 1)
	for i := 0; i < n + 1; i++ {
		dp[i] = make([]int, 10)
	}
	for i := 1; i < 10; i++ {
		dp[1][i] = 1
	}
	for i := 2; i < n+1; i++ {
		for j := 0; j < 10; j++ {
			if j == 0 {
				dp[i][j] = dp[i-1][1]
			}else if j == 9 {
				dp[i][j] = dp[i-1][8]
			}else {
				dp[i][j] = (dp[i-1][j-1] + dp[i-1][j+1]) % 1000000000
			}
		}
	}
	fmt.Fprintln(w, sum(dp[n]))

}

func sum(arr []int) int {
	var res = 0
	for i := 0; i < len(arr); i++ {
		res = (res + arr[i]) % 1000000000
	}
	return res
}