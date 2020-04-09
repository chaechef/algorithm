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
	input [3]int
	minprevcache [3]int
	maxprevcache [3]int
	mincurrcache [3]int
	maxcurrcache [3]int
)

func main() {
	defer w.Flush()
	fmt.Fscanf(r,"%d ",&n)
	for i := 0; i < n; i++ {
		fmt.Fscanf(r, "%d %d %d ", &input[0], &input[1], &input[2])
		mincurrcache[0] = minint(minprevcache[0], minprevcache[1]) + input[0]
		mincurrcache[1] = minint(minint(minprevcache[0],minprevcache[1]),minprevcache[2]) + input[1]
		mincurrcache[2] = minint(minprevcache[1],minprevcache[2]) + input[2]
		maxcurrcache[0] = maxint(maxprevcache[0], maxprevcache[1]) + input[0]
		maxcurrcache[1] = maxint(maxint(maxprevcache[0],maxprevcache[1]),maxprevcache[2]) + input[1]
		maxcurrcache[2] = maxint(maxprevcache[1],maxprevcache[2]) + input[2]
		minprevcache = copycache(minprevcache,mincurrcache)
		maxprevcache = copycache(maxprevcache,maxcurrcache)
	}
	fmt.Fprint(w, maxint(maxint(maxcurrcache[0],maxcurrcache[1]),maxcurrcache[2]),minint(minint(mincurrcache[0],mincurrcache[1]),mincurrcache[2]))

}


func copycache(arr1 [3]int, arr2 [3]int) [3]int {
	for i := 0; i < len(arr2); i++ {
		arr1[i] = arr2[i]
	}
	return arr1
}

func minint(a int, b int) int {
	if a > b {
		return  b
	}else {
		return a
	}
}

func maxint (a int, b int) int {
	if a > b {
		return a
	}else {
		return b
	}
}