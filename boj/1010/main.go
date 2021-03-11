package main

import (
	"bufio"
	"fmt"
	"os"
)

var (
	r = bufio.NewReader(os.Stdin)
	w = bufio.NewWriter(os.Stdout)
	tc int
	n,m int64
)

func main() {
	defer w.Flush()
	fmt.Fscanf(r,"%d ", &tc)
	for t := 0; t < tc; t++ {
		fmt.Fscanf(r, "%d %d ", &n, &m)

		//mCn combination ex> 6C3 6 5 4 / 3 2 1
		var res int64
		res = 1
		var i int64
		for i = 0; i < n; i++ {
			res *= m-i
			res /= i+1
		}

		fmt.Fprintln(w, res)

	}

}
