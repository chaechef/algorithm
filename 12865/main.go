package main

import (
	"bufio"
	"fmt"
	"os"
)

var (
	r = bufio.NewReader(os.Stdin)
	w = bufio.NewWriter(os.Stdout)
	n, maxweight int
	weights, values []int
	dp [][]int
)

func main()  {
	defer w.Flush()
	fmt.Fscanf(r,"%d %d ", &n, &maxweight)
	//init
	weights = make([]int, n)
	values = make([]int, n)
	dp = make([][]int, n)
	for i := 0; i < n; i++ {
		dp[i] = make([]int, maxweight+1)
	}
	for i := 0; i < n; i++ {
		fmt.Fscanf(r,"%d %d ",&weights[i],&values[i])
	}
	res := allsearch(0,maxweight)
	fmt.Fprintln(w, res)
}

func allsearch(index int, max int) int {
	//finish condition
	if index == n {
		return 0
	}
	//init
	currW := weights[index]
	currV := values[index]
	var res int

	//check memo
	res = dp[index][max]
	if res > 0 {
		return res
	}

	if currW > max {
		res = allsearch(index+1, max)
		dp[index][max] = res
	} else {
		temp1 := allsearch(index+1, max)
		temp2 := allsearch(index+1, max-currW) + currV
		res = maxInt(temp1,temp2)
		dp[index][max] = res

	}
	return res
}

func maxInt(a int, b int) int {
	if a > b {
		return a
	}else {
		return b
	}
}