package main

import (
	"bufio"
	"fmt"
	"os"
)

var r = bufio.NewReader(os.Stdin)
var w = bufio.NewWriter(os.Stdout)

func backtracking(picked []int, num int, topick int)  {
	if topick == 0 {
		//print
		for i := 0; i < len(picked); i++ {
			fmt.Fprint(w, picked[i], " ")
		}
		fmt.Fprint(w, "\n")
		return
	}

	for i := 1; i <= num; i++ {
			picked = append(picked, i)
			backtracking(picked, num, topick-1)
			picked = picked[:len(picked)-1]
	}
}
func main() {

	defer w.Flush()
	var n, m int
	var arr []int
	fmt.Fscanln(r, &n, &m)
	backtracking( arr, n, m )
}
