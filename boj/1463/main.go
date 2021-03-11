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
	dp [1000001]int
)

func main() {
	defer w.Flush()

	fmt.Fscanf(r,"%d ", &n)
	for i := 1; i < n+1; i++ {
		dp[i] = i-1
	}
	for i := 2; i < n+1; i++ {
		if i % 2 == 0 {
			if dp[i/2] + 1 < dp[i] {
				dp[i] = dp[i/2] + 1
			}
		}
		if i % 3 == 0 {
			if dp[i/3] + 1 < dp[i] {
				dp[i] = dp[i/3] + 1
			}
		}
		if dp[i-1] + 1 < dp[i] {
			dp[i] = dp[i-1] + 1
		}
	}
	fmt.Fprintln(w, dp[n])
}
