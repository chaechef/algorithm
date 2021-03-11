package main

import (
	"bufio"
	"fmt"
	"os"
)

var (
	r = bufio.NewReader(os.Stdin)
	w = bufio.NewWriter(os.Stdout)
	n, k int
	cache [][]int
)

func main() {
	defer w.Flush()
	fmt.Fscanf(r, "%d %d ", &n, &k)
	cache = make([][]int, n+1)
	for i := 0; i < n+1; i++ {
		cache[i] = make([]int, n+1)
	}

	res := recursion(n,k)
	fmt.Fprintln(w, res)

}

func recursion(tn int, tk int) int {
	if tn == tk {
		return 1
	}
	if tn == 0 || tk == 0 {
		return 1
	}
	if cache[tn][tk] != 0 {
		return cache[tn][tk]
	}

	cache[tn][tk] = (recursion(tn-1,tk) + recursion(tn-1,tk-1)) % 10007
	return cache[tn][tk]
}
