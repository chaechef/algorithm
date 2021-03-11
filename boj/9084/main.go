package main

import (
	"bufio"
	"fmt"
	"os"
)

var (
	r = bufio.NewReader(os.Stdin)
	w = bufio.NewWriter(os.Stdout)
	tc, n, m int
	cache [][]int
	coins []int
)

func main() {
	defer w.Flush()
	fmt.Fscanf(r, "%d ", &tc)
	for t := 0; t < tc; t++ {
		fmt.Fscanf(r, "%d ", &n)
		coins = make([]int, n)
		for i := 0; i < n; i++ {
			fmt.Fscanf(r, "%d ", &coins[i])
		}
		fmt.Fscanf(r, "%d ", &m)
		cache = make([][]int, n)
		for i := 0; i < n; i++ {
			cache[i] = make([]int, m+1)
		}

		for i := 1; i < m+1; i++ {
			if i % coins[0] == 0 {
				cache[0][i] = 1
			}
		}
		for i := 1; i < n; i++ {
			currCoin := coins[i]
			for j := 1; j < m+1; j++ {
				if j < currCoin {
					cache[i][j] = cache[i-1][j]
				}else if j == currCoin {
					cache[i][j] = cache[i-1][j] + 1
				}else {
					cache[i][j] = cache[i-1][j] + cache[i][j-currCoin]
				}
			}
		}
		fmt.Fprintln(w, cache[n-1][m])
	}
}
