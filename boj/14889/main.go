package main

import (
	"bufio"
	"fmt"
	"math"
	"os"
)

var r = bufio.NewReader(os.Stdin)
var w = bufio.NewWriter(os.Stdout)

var (
	n int
	arr [][]int
	check []bool
	min = 1000000000
)
func main() {

	defer w.Flush()

	fmt.Fscanf(r, "%d ", &n)
	arr = make([][]int, n)
	check = make([]bool, n)
	for i := 0; i < n ; i++ {
		arr[i] = make([]int, n)
	}
	for i := 0; i < n; i++ {
		for j := 0; j < n; j++ {
			fmt.Fscanf(r,"%d ", &arr[i][j])
		}
	}
	maketeam(make([]int, 0),0)
	fmt.Fprintln(w, min)
}

func score(picked []int) int {
	var res int
	for i := 0; i< len(picked); i++  {
		for j := 0; j < len(picked); j++ {
			if i != j {
				res += arr[picked[i]][picked[j]]
			}
		}
	}

	return res
}
func maketeam(picked []int ,num int)  {
	if num == n / 2 {
		var another []int
		for i := 0; i < n; i++ {
			if check[i] == false {
				another = append(another, i)
			}
		}
		scoreA := score(picked)
		scoreB := score(another)

		diff := math.Abs(float64(scoreA-scoreB))
		if min > int(diff) {
			min = int(diff)
		}
	}

	var smallest = 0
	if len(picked) > 0 {
		smallest = picked[len(picked)-1] + 1
	}

	for i := smallest; i < n ; i++ {
		picked = append(picked, i)
		check[i] = true
		maketeam(picked, num +1)
		picked = picked[:len(picked)-1]
		check[i] = false
	}
}