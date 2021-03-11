package main

import (
	"bufio"
	"fmt"
	"os"
)

var(
	r = bufio.NewReader(os.Stdin)
	w = bufio.NewWriter(os.Stdout)
	arr [1000001]int
	n int
)

func main() {
	defer w.Flush()

	fmt.Fscanf(r, "%d ", &n)
	arr[1] = 1  // 1
	arr[2] = 2 // 11 00
	for i := 3; i <= n; i++ {
		arr[i] = ((arr[i-2] % 15746) + (arr[i-1] % 15746) )% 15746
	}
	fmt.Fprintln(w,arr[n])

}