package main

import (
	"fmt"
)

func areFriends (n int, m int) [][]int {
	arr := make([][]int, n)
	for j := 0; j < n; j++{
		arr[j] = make([]int, n)
	}
	for j := 0; j < m; j++{
		var p1, p2 int
		fmt.Scanf("%d %d", &p1, &p2)
		arr[p1][p2] = 1
		arr[p2][p1] = 1
	}
	return arr
}

func PrintFriends ( arr [][]int) {
	for i := 0; i < len(arr); i++{
		for j := 0; j < len(arr[0]); j++ {
			fmt.Printf("%d ", arr[i][j])
		}
		fmt.Println()
	}
}

func makePair (arr [][]int, friends []int) int {
	first := -1
	for i := 0; i< len(friends); i++ {
		if friends[i] == 0 {
			first = i
			break
		}
	}
	if first == -1 {
		return 1
	}
	res := 0
	for i := first+1; i < len(friends); i++ {
		if friends[first] == 0 && friends[i] == 0 && arr[first][i] == 1 {
			friends[first] = 1
			friends[i] = 1
			arr[first][i] = 0
			arr[i][first] = 0
			res += makePair(arr, friends)
			friends[first] = 0
			friends[i] = 0
			arr[first][i] = 1
			arr[i][first] = 1
		}
	}
	return res
}

func main() {
	testcase := 0
	fmt.Scanf("%d", &testcase)
	for i := 0; i < testcase; i++ {
		var n, m int
		fmt.Scanf("%d %d", &n, &m)
		arr := areFriends(n,m)
		//PrintFriends(arr)
		friends := make( []int, n)
		res := makePair(arr, friends)
		fmt.Println(res)

	}
}
