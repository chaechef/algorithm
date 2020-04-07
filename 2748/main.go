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
	arr [91]int64
)

func main() {
	defer w.Flush()
	fmt.Fscanf(r,"%d ", &n)
	arr[0] = 0
	arr[1] = 1
	for i := 2; i < n + 1; i++ {
		arr[i] = arr[i-1] + arr[i-2]
	}

	fmt.Fprintln(w,arr[n])
}
