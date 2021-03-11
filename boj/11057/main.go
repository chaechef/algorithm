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
	cache [10][1001]int
)

func main() {
	defer w.Flush()
	fmt.Fscanf(r, "%d ", &n)

	for i := 0; i < 10; i++ {
		cache[i][1] = 1
	}
	for i:=1; i <= n ; i++ {
		for j := 0; j < 10; j++ {
			for k:=0 ; k<=j; k++  {
				cache[j][i] = (cache[j][i] + cache[k][i-1]) % 10007
			}
		}
	}

	sum := 0
	for i := 0; i < 10; i++ {
		sum = (sum + cache[i][n]) % 10007
	}
	fmt.Fprintln(w, sum)
}

