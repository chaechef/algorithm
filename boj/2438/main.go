package main

import (
	"bufio"
	"fmt"
	"os"
)

var	(
	r = bufio.NewReader(os.Stdin)
	w = bufio.NewWriter(os.Stdout)
	n int
)

func main() {
	defer w.Flush()
	fmt.Fscan(r, &n)
	for i := 1; i < n+1; i++ {
		for j := 0; j < i; j++ {
			fmt.Fprint(w, "*")
		}
		fmt.Fprintln(w)
	}
}
