package main

import (
	"bufio"
	"fmt"
	"os"
)

var r = bufio.NewReader(os.Stdin)
var w = bufio.NewWriter(os.Stdout)
var board [9][9]int
var xblank []int
var yblank []int
var finish = false

func main()  {
	defer w.Flush()
	for i := 0; i < 9; i++ {
		for j := 0; j < 9; j++ {
			fmt.Fscan(r, &board[i][j])
			if board[i][j] == 0 {
				xblank = append(xblank, i)
				yblank = append(yblank, j)
			}
		}
	}
	fill(0)
}

func fill(curr int)  {
	if finish == true {
		return
	}

	if curr == len(xblank) {
		//print
		for i := 0; i < 9; i++ {
			for j := 0; j < 9; j++ {
				fmt.Fprint(w,board[i][j]," ")
			}
			fmt.Fprintln(w)
		}
		finish = true
		return
	}
	var x, y = xblank[curr], yblank[curr]
	available := check( x, y)

	for i := 0; i < len(available); i++ {
		available = check( x, y)

		board[x][y] = available[i]
		fill(curr + 1)
		board[x][y] = 0
	}
}

func check(x int, y int) []int {
	var nums [10]bool
	for i := 0; i < 9; i++ {
		nums[board[x][i]] = true
		nums[board[i][y]] = true
	}
	xsection := x / 3
	ysection := y / 3

	for i:=xsection*3; i < xsection*3+3 ; i++ {
		for j:=ysection*3; j< ysection*3+3; j++	{
			nums[board[i][j]] = true
		}
	}
	var ret []int
	for i := 1; i < 10; i++	{
		if nums[i] == false {
			ret = append(ret, i)
		}
	}
	return ret

}