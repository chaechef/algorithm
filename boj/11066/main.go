package main

import (
	"bufio"
	"fmt"
	"os"
)

const IMAX = 2147483647

var	(
	r = bufio.NewReader(os.Stdin)
	w = bufio.NewWriter(os.Stdout)
	tc, n int
	arr []int
	cache [][]int
	sum []int
)

func main() {
	defer w.Flush()
	fmt.Fscanf(r, "%d ", &tc)
	for t := 0; t < tc; t++ {
		//init
		fmt.Fscanf(r, "%d ", &n)
		arr = make([]int,n)
		cache = make([][]int, n)
		sum = make([]int, n)

		for i := 0; i < n; i++ {
			cache[i] = make([]int, n)
			for j := 0; j < n; j++ {
				cache[i][j] = IMAX
			}
		}

		//input
		for i := 0; i < n; i++ {
			fmt.Fscanf(r, "%d ", &arr[i])
			if i != 0 {
				sum[i] = sum[i-1] + arr[i]
			}else{
				sum[i] = arr[i]
			}
		}

		//dp
		res := recursion(0,n-1)

		//output
		fmt.Fprintln(w, res)

	}
}

func recursion(l int, r int) int {
	if l == r {
		cache[l][r] = 0
		return cache[l][r]
	}
	if l + 1 == r {
		cache[l][r] = arr[l] + arr[r]
		return cache[l][r]
	}
	if cache[l][r] != IMAX {
		return cache[l][r]
	}

	for i := 0; l+i+1 <= r ; i++ {
		var temp int
		temp += recursion(l,l+i)
		temp += recursion(l+i+1,r)
		if l -1 >= 0 {
			temp += sum[r] - sum[l-1]

		}else{
			temp += sum[r]
		}
		if temp < cache[l][r] {
			cache[l][r] = temp
		}
	}

	return cache[l][r]

}