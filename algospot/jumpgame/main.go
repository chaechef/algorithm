package main

import (
	"bufio"
	"fmt"
	"os"
)

var (
	r = bufio.NewReader(os.Stdin)
	w = bufio.NewWriter(os.Stdout)
	tc int
	n int
	board [][]int
	cache [][]int
)

func main() {
	defer w.Flush()
	fmt.Fscanf(r,"%d ", &tc)
	for t := 0; t < tc; t++ {
		fmt.Fscanf(r,"%d ", &n)
		board = makeSlice(board,n)
		cache = makeSlice(cache,n)
		cache = memset(cache, -1)
		for i := 0; i < n; i++ {
			for j := 0; j < n; j++ {
				fmt.Fscanf(r,"%d ", &board[i][j])
			}
		}
		res := recursion(n-1,n-1)
		if res == 0 {
			fmt.Fprintln(w,"NO")
		}else {
			fmt.Fprintln(w, "YES")
		}
	}
}


func recursion(x int, y int) int {
	if !isRange(x,y){
		return 0
	}
	if x == 0 && y == 0 {
		return 1
	}
	if cache[x][y] != -1 {
		return cache[x][y]
	}
	var res int
	for i := x-1; i >= 0; i-- {
		if isRange(i,y) && board[i][y] + i == x {
			res += recursion(i,y)
		}
	}
	for i := y - 1; i >= 0; i-- {
		if isRange(x,i) && board[x][i] + i == y {
			res +=recursion(x,i)
		}
	}
	cache[x][y] = res
	return cache[x][y]

}

func isRange(x int, y int) bool {
	if x < 0 || y < 0 || x >= n || y >= n {
		return false
	}else {
		return true
	}
}

func memset (arr [][]int, n int)  [][]int {
	for i := 0; i < len(arr); i++ {
		for j := 0; j < len(arr[0]); j++ {
			arr[i][j] = n
		}
	}
	return arr
}


func makeSlice(arr [][]int, n int ) [][]int {
	arr = make([][]int, n)
	for i := 0; i < n; i++ {
		arr[i] = make([]int, n)
	}
	return arr
}