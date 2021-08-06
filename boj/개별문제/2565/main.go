package main

import (
	"bufio"
	"fmt"
	"os"
)

var	(
	r = bufio.NewReader(os.Stdin)
	w = bufio.NewWriter(os.Stdout)
	n int
	arrA []int
	arrB []int
	cache []int
)

func main() {
	defer w.Flush()
	fmt.Fscanf(r, "%d ", &n)
	arrA = make([]int, n)
	arrB = make([]int, n)
	cache = make([]int, n)
	//init
	for i := 0; i < n; i++ {
		fmt.Fscanf(r, "%d %d ", &arrA[i], &arrB[i])
	}
	mysort(arrA,arrB)


	for i := 0; i < n; i++ {
		cache[i] = 1
		for j := 0; j < i; j++ {
			if arrB[j] < arrB[i] && cache[i] < cache[j] + 1 {
				cache[i] = cache[j] + 1
			}
		}
	}

	fmt.Fprintln(w,n-max(cache))

}
func max(arr []int) int {
	max := 0
	for i := 0; i < len(arr); i++ {
		if max < arr[i] {
			max = arr[i]
		}
	}
	return max
}
//bubble sort
func mysort(arrA []int, arrB []int)  {
	for i := 0; i < len(arrA); i++ {
		for j := i; j < len(arrA); j++ {
			if arrA[i] > arrA[j] {
				temp := arrA[i]
				arrA[i] = arrA[j]
				arrA[j] = temp
				temp1 := arrB[i]
				arrB[i] = arrB[j]
				arrB[j] = temp1
			}
		}
	}

}