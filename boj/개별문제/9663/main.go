package main

import (
	"bufio"
	"fmt"
	"math"
	"os"
)

var r = bufio.NewReader(os.Stdin)
var w = bufio.NewWriter(os.Stdout)
var board [15]int
var res, n int

func main() {
	defer w.Flush()
	fmt.Fscanln(r, &n)
	nqueen(0)
	fmt.Fprintln(w, res)
}

func nqueen(curr int)  {
	if curr == n {
		res++
		return
	}

	for i := 0; i < n; i++ {
		check := true
		for j := 0; j < curr; j++ {
			if board[j] == i || math.Abs(float64(curr-j)) == math.Abs(float64(board[j] - i)) {
				check= false
				break
			}
		}
		if check {
			board[curr] = i
			nqueen(curr +1)
		}
	}

}