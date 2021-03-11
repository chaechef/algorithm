package main

import (
	"bufio"
	"fmt"
	"os"
)

var max = -1
var n, m int

func pick(arr []int, idx int ,topick int, sum int)  {

	if topick == 0 && sum <= m {
		if sum > max {
			max = sum
		}
	}
	if idx >= n || topick < 0 || sum > m {
		return

	}

	pick(arr, idx+1, topick -1 ,sum + arr[idx])
	pick(arr, idx+1, topick ,sum)

}

func main() {
	r := bufio.NewReader(os.Stdin)
	w := bufio.NewWriter(os.Stdout)
	defer w.Flush()

	fmt.Fscanln(r, &n, &m)
	arr := make([]int, n)

	for i := 0; i < n; i++{
		fmt.Fscanf(r,"%d", &arr[i])
	}
	pick(arr,0,3,0)
	fmt.Fprintln(w, max)
}
