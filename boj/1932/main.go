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
	triangle [][]int
	dp [][]int
)

func main() {
	defer w.Flush()
	fmt.Fscanf(r,"%d ", &n)
	//init
	triangle = make([][]int, n)
	dp = make([][]int, n)

	for i:=0; i < n ;i++  {
		triangle[i] = make([]int, n)
		dp[i] = make([]int, n)

	}

	for i := 0; i < n; i++{
		for j := 0; j < i + 1; j++ {
			fmt.Fscanf(r,"%d ", &triangle[i][j])
		}
	}

	dp[0][0] = triangle[0][0]

	for i := 1; i < n; i++ {
		for j := 0; j < i + 1; j++ {
			var temp1, temp2 int
			if j - 1 >= 0 {
				temp1 = dp[i-1][j-1]
			}
			if j <= i - 1 {
				temp2 = dp[i-1][j]
			}
			res := min(temp1, temp2)
			dp[i][j] = triangle[i][j] + res
		}
	}
	fmt.Fprintln(w, maxArray(dp[n-1]))
}
func maxArray(arr []int) int {
	max := -1
	for i := 0; i < len(arr); i++ {
		if arr[i] > max {
			max = arr[i]
		}
	}
	return max
}

func min(a int, b int) int {
	if a > b {
		return a
	}else{
		return b
	}

}