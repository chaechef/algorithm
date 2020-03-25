package main

import (
	"fmt"
)

func main() {
	//array definition
	arr := []int{1, 2, 3, 4, 5}
	PrintArray(arr)

	//array by make
	arr1 := make([]int, 5)
	for i := 0; i < 5; i++ {
		arr1[i] = i * 10
	}
	PrintArray(arr1)

	//array push
	for i := 0; i < 5; i++ {
		arr1 = append(arr1, i+1)
	}
	PrintArray(arr1)

	//array slice
	arr2 := arr1[4:10]
	PrintArray(arr2)

}

func PrintArray(array []int) {
	for i := 0; i < len(array); i++ {
		fmt.Println(array[i])
	}
	fmt.Println()
}
