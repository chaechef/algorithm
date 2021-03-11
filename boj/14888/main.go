package main

import (
	"bufio"
	"fmt"
	"os"
)

var r = bufio.NewReader(os.Stdin)
var w = bufio.NewWriter(os.Stdout)
var (
	n int
	operatorNums [4]int
	nums []int
	min = 1000000000
	max = -1000000000
)

func main() {
	defer w.Flush()

	fmt.Fscanln(r, &n)
	nums = make([]int, n)
	var operators []int

	for i := 0; i < n; i++ {
		fmt.Fscanf(r,"%d ", &nums[i])
	}

	for i := 0; i < 4; i++ {
		fmt.Fscanf(r,"%d ", &operatorNums[i])
	}
	setOperator(operators,0)
	fmt.Fprintln(w, max)
	fmt.Fprintln(w, min)
}

func setOperator( operators []int ,curr int)  {
	if curr == n -1 {
		var res int
		res= nums[0]

		for i := 0; i < n -1 ; i++ {
			switch operators[i] {
			case 0:
				res = res + nums[i+1]
			case 1:
				res = res - nums[i+1]
			case 2:
				res = res * nums[i+1]
			case 3:
				res = int(res) / int(nums[i+1])
			}
		}

		if res > max {
			max = res
		}
		if res < min {
			min = res
		}
		return
	}
	for i := 0; i < 4; i++ {
		if operatorNums[i] > 0 {
			operatorNums[i]--
			operators = append(operators, i)
			setOperator(operators, curr+1)
			operatorNums[i]++
			operators = operators[:len(operators)-1]
		}
	}
}