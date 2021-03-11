package main

import (
	"bufio"
	"fmt"
	"math"
	"os"
)

var(
	r = bufio.NewReader(os.Stdin)
	w = bufio.NewWriter(os.Stdout)
	num int
	minr, ming, minb [1001]int
	rcost, gcost, bcost int
)

func main() {
	defer w.Flush()
	fmt.Fscanf(r, "%d ", &num)
	//init
	fmt.Fscanf(r,"%d %d %d ", &rcost, &gcost, &bcost)
	minr[1] = rcost
	ming[1] = gcost
	minb[1] = bcost
	//loop
	for i := 2; i < num+1; i++ {
		fmt.Fscanf(r,"%d %d %d ", &rcost, &gcost, &bcost)
		minr[i] = rcost + int(math.Min(float64(ming[i-1]),float64(minb[i-1])))
		ming[i] = gcost + int(math.Min(float64(minr[i-1]),float64(minb[i-1])))
		minb[i] = bcost + int(math.Min(float64(minr[i-1]),float64(ming[i-1])))

	}
	fmt.Fprintln(w,math.Min(float64(minr[num]),math.Min(float64(ming[num]),float64(minb[num]))))



}
