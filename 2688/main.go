package main

import (
	"bufio"
	"fmt"
	"os"
)

var (
	r = bufio.NewReader(os.Stdin)
	w = bufio.NewWriter(os.Stdout)
	tc, n int
	cache [10][65]int
)

func main()  {
	defer w.Flush()
	fmt.Fscanf(r,"%d ", &tc)
	for i := 0; i < 10; i++ {
		cache[i][1] = 1
	}
	for i := 2; i < 65; i++ {
		for j := 0; j < 10; j++ {
			for k := 0; k <= j; k++ {
				cache[j][i] += cache[k][i-1]
			}
		}
	}

	for t := 0; t < tc; t++ {
		fmt.Fscanf(r, "%d ",&n)
		res:=0
		for i := 0; i < 10; i++ {
			res += cache[i][n]
		}
		fmt.Fprintln(w, res)
	}
}
