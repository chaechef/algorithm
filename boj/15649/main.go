package main

import (
	"bufio"
	"fmt"
	"os"
)

var r = bufio.NewReader(os.Stdin)
var w = bufio.NewWriter(os.Stdout)

func backtracking(checks []bool ,picked []int, num int, topick int)  {
	if topick == 0 {
		//print
		for i := 0; i < len(picked); i++ {
			fmt.Fprint(w, picked[i], " ")
		}
		fmt.Fprint(w, "\n")
		return
	}

	for i := 1; i <= num; i++ {
		if checks[i] == false {
			picked = append(picked, i)
			checks[i] = true
			backtracking(checks ,picked, num, topick-1)
			checks[i] = false
			picked = picked[:len(picked)-1]
		}
	}
}
func main() {

	defer w.Flush()
	var n, m int
	var arr []int
	fmt.Fscanln(r, &n, &m)
	checks := make([]bool, n+1)

	backtracking( checks, arr, n, m )
}
