package main

import (
	"fmt"
)

func main() {
	arr := []int{1, 2, 3, 4, 5}
	PrintArray(arr)

	arr1 := make([]int, 5)
	for i := 0; i < 5; i++ {
		arr1[i] = i * 10
	}
	PrintArray(arr1)

	for i := 0; i < 5; i++ {
		arr1 = append(arr1, i+1)
	}
	//push element
	PrintArray(arr1)

	arr2 := arr1[4:10]
	//slice array
	PrintArray(arr2)

}

func PrintArray(array []int) {
	for i := 0; i < len(array); i++ {
		fmt.Println(array[i])
	}
	fmt.Println()
}
