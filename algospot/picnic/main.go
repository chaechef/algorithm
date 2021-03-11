package main

import (
	"bufio"
	"fmt"
	"os"
)

var (
	r = bufio.NewReader(os.Stdin)
	w = bufio.NewWriter(os.Stdout)
	tc, n, m int
	t1, t2 int
	students []int
	arefriends [][]bool
)

func main() {
	defer w.Flush()
	fmt.Fscan(r, &tc)
	for t := 0; t < tc; t++ {
		fmt.Fscan(r, &n, &m )
		students = make([]int, n)
		for i := 0; i < n; i++ {
			students[i] = -1
		}
		arefriends = make([][]bool, n)
		for i := 0; i < n; i++ {
			arefriends[i] = make([]bool, n)
		}
		for i := 0; i < m; i++ {
			fmt.Fscan(r, &t1, &t2)
			arefriends[t1][t2] = true
			arefriends[t2][t1] = true
		}
		res := makepair(students, 1)
		fmt.Fprintln(w, res)
	}
}

func makepair(s []int, f int) int {
	if f == n /2 {
		return 1
	}

	var curr, res int
	for i := 0; i < n; i++ {
		if s[i] != -1 {
			curr = i
			break
		}
	}

	for i := curr + 1; i < n; i++ {
		if arefriends[curr][i] == true {
			s[curr] = f
			s[i]= f
			res += makepair(s, f+1)
			s[curr] = -1
			s[i]= -1
		}
	}
	return res

}