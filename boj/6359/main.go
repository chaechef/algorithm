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
	cache []int
)

func main() {
	defer w.Flush()
	fmt.Fscanf(r, "%d ", &tc)

	for t := 0; t < tc; t++ {
		fmt.Fscanf(r, "%d ",&n)
		cache = make([]int, n+1)
		for i := 1; i < n+1; i++ {
			for j := 1; i*j < n+1; j++ {
				cache[i*j]++
			}
		}

		res := 0
		for _,v := range cache{
			if v % 2 == 1 {
				res++
			}
		}
		fmt.Fprintln(w,res)

	}
}
