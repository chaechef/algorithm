package main

import (
	"bufio"
	"fmt"
	"os"
)

var r = bufio.NewReader(os.Stdin)
var w = bufio.NewWriter(os.Stdout)
var n int
var res = 0

func main() {
	defer w.Flush()
	fmt.Fscan(r, &n)
	board := make([][]int, n)
	for i := 0; i < n; i++ {
		board[i] = make([]int, n)
	}
	nqueen(board, 0, n)
	fmt.Fprintln(w, res)
}

func printboard(board [][]int)  {
	for i := 0; i < len(board); i++ {
		for j := 0; j < len(board[0]); j++ {
			fmt.Fprint(w, board[i][j], " ")
		}
		fmt.Fprintln(w)
	}
	fmt.Fprintln(w)

}
func nqueen( board [][]int, curr int , topick int )  {
	if curr >= n && topick != 0 {
		return
	}
	if topick == 0 {
		res++
		return
	}

	for i := 0; i < n; i++{
		if board[curr][i] == 0 {
			//copy
			cpy := make([][]int, n)
			for j := 0; j < n; j++ {
				cpy[j] = make([]int, n)
				copy(cpy[j], board[j])
			}

			checkOn(cpy,curr,i)
			//printboard(cpy)
			nqueen(cpy,curr+1, topick-1)
		}
	}
}

func checkOn(board [][]int , x int, y int) {
	board[x][y] = 2
	for i := x + 1; i < n; i++ {
		board[i][y] = 1
		if y + i -x < n {
			board[i][y+i-x] = 1

		}
		if y + x - i >= 0  {
			board[i][y+x-i] = 1
		}
	}
}