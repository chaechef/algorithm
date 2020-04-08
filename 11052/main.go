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
	card []int
	cache []int
)

func main() {
	defer w.Flush()
	fmt.Fscanf(r,"%d ", &n)
	card = make([]int, n+1)
	cache = make([]int, n+1)
	for i:=1; i<n+1; i++ {
		fmt.Fscanf(r,"%d ", &card[i])
	}
	res := recursion(n)
	fmt.Fprintln(w, res)
}

func recursion(num int) int {
	if num == 0 {
		return 0
	}
	if num == 1 {
		return card[1]
	}
	if cache[num] != 0{
		return cache[num]
	}

 	max := 0
	for i := num; i > 0; i-- {
		temp := recursion(num - i) + card[i]
		if temp > max {
			max = temp
		}
	}
	cache[num]= max
	return cache[num]
}
