package main

import "fmt"

func main() {
	arr := make([]bool , 10001)

	for i := 1; i < 10001; i++ {
		selfNum := i
		for j := i; j > 0; j = j/10 {
			selfNum += j%10
		}
		if selfNum < 10001{
			arr[selfNum] = true

		}
	}
	for i := 1; i < 10001; i++ {
		if arr[i] == false{
			fmt.Println(i)

		}
	}
}
