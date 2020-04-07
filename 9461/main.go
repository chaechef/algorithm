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
	n int
	num [101]int
)

func main() {
	defer w.Flush()
	fmt.Fscanf(r, "%d ", &tc)
	//init
	num[1] = 1
	num[2] = 1
	num[3] = 1
	for i := 4; i < 101; i++ {
		num[i] = num[i-3] + num[i-2]
	}

	for i := 0; i < tc; i++ {
		fmt.Fscanf(r, "%d ", &n)
		fmt.Fprintln(w, num[n])
	}
}
