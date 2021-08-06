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
	cache [68]int64
)

func main()  {
	defer w.Flush()
	fmt.Fscanf(r, "%d ", &tc)
	cache[0] = 1
	cache[1] = 1
	cache[2] = 2
	cache[3] = 4
	for i := 4; i < 68; i++ {
		cache[i] = cache[i-1] + cache[i-2] + cache[i-3] + cache[i-4]
	}

	for i := 0; i < tc; i++ {
		var n int
		fmt.Fscanf(r, "%d ", &n)
		fmt.Fprintln(w, cache[n])
	}

}