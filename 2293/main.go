package main

import (
	"bufio"
	"fmt"
	"os"
)

var	(
	r = bufio.NewReader(os.Stdin)
	w = bufio.NewWriter(os.Stdout)
	n, k int
	coins []int
	cache []int
)

func main() {
	//init
	defer w.Flush()
	fmt.Fscanf(r, "%d %d ", &n, &k)
	coins = make([]int, n+1)
	cache = make([]int, k+1)
	//input
	for i := 1; i < n+1; i++ {
		fmt.Fscanf(r, "%d ", &coins[i])
	}

	//output
	for i := 1; i < k+1; i++ {
		if i % coins[1] == 0 {
			cache[i] = 1
		}
	}
	for i := 2; i < n+1; i++ {
		for j := 1; j < k+1; j++ {
			if j - coins[i] == 0 {
				cache[j] = cache[j] + 1
			}else if j - coins[i] > 0 {
				cache[j] = cache[j-coins[i]] + cache[j]
			}else{
				cache[j] = cache[j]
			}
		}
	}
	fmt.Fprintln(w, cache[k])

}
