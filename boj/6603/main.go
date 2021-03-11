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
	arr []int
)

func main() {
	defer w.Flush()
	fmt.Fscan(r, &n)
	for n != 0 {
		arr = make([]int, n)
		for i := 0; i < n; i++ {
			fmt.Fscan(r, &arr[i])
		}
		var temp []int
		recursion(temp, 0, 0)
		fmt.Fprintln(w)
		fmt.Fscan(r, &n)
	}
}

func recursion(picked []int, idx int, count int)  {
	if count == 6 {
		for i := 0; i < len(picked); i++ {
			fmt.Fprint(w, picked[i], " ")
		}
		fmt.Fprintln(w)
		return
	}

	for i := idx; i < n; i++ {
		picked = append(picked, arr[i])
		recursion(picked, i+1, count + 1)
		picked = picked[:len(picked)-1]
	}


}